from asyncio import sleep
import queue
from threading import Lock, Timer
import threading
import time
from typing import Any, Callable, Dict, List
import uuid

from modelmetry.observability.event import Event
from modelmetry.observability.finding import Finding
from modelmetry.observability.ingest import build_ingest_batch_from_traces
from modelmetry.observability.trace import Trace
import sys

from modelmetry.openapi.api.default_api import DefaultApi
from modelmetry.openapi.models.create_event_params import CreateEventParams
from modelmetry.openapi.models.create_finding_params import CreateFindingParams
from modelmetry.openapi.models.create_session_params import CreateSessionParams
from modelmetry.openapi.models.create_span_params import CreateSpanParams
from modelmetry.openapi.models.create_trace_params import CreateTraceParams
from modelmetry.openapi.models.ingest_signals_v1_request_body import (
    IngestSignalsV1RequestBody,
)
from modelmetry.openapi.models.span import Span


class FlushManager:
    def __init__(
        self, api: DefaultApi, on_failure: Callable[[List[List[Trace]]], None]
    ):
        self.api = api
        self._running = True
        self.queue = queue.Queue()
        self.on_failure = on_failure
        self.worker_thread = threading.Thread(target=self._worker, daemon=True)
        self.worker_thread.start()

    def process(self, list_of_traces: List[Trace]):
        self.queue.put(list_of_traces)

    def _worker(self):
        while self._running or not self.queue.empty():
            try:
                list_of_traces = self.queue.get(timeout=1)  # Wait for 1 second
                batch = build_ingest_batch_from_traces(list_of_traces)
                self._send_batch(batch)
                self.queue.task_done()

            except queue.Empty:
                continue  # If queue is empty, continue the loop

            except Exception as e:
                print(f"Error sending traces: {e}")
                self.on_failure(list_of_traces)
                self.queue.task_done()

    def _send_batch(self, batch: IngestSignalsV1RequestBody):
        print("FlushManager._send_batch")
        self.api.ingest_signals_v1(batch)

    def shutdown(self):
        self._running = False

        if self.queue.empty():
            print("FlushManager.shutdown queue is empty, returning")
            return

        self.worker_thread.join(timeout=2)

        if self.worker_thread.is_alive():
            print("Warning: Worker thread did not exit cleanly")


class ObservabilityClient:
    tenant_id: str = None
    backend: DefaultApi = None

    traces: List[Trace] = []
    in_transit: Dict[str, Trace] = {}

    traces_lock: Lock = None
    flush_manager: FlushManager = None
    flush_interval: int = None
    flush_timer: Timer = None
    max_size_kb: int = 5

    def __init__(
        self,
        backend: DefaultApi,
        tenant_id: str,
        max_size_kb: int = None,
        flush_interval: int = None,
    ) -> None:
        self.tenant_id = tenant_id
        self.backend = backend
        self.traces = []

        self.traces_lock = threading.Lock()
        self.task_manager = FlushManager(api=backend, on_failure=self._on_batch_failure)
        self.max_size_kb = max_size_kb
        self.flush_interval = flush_interval
        self.flush_timer = threading.Timer(self.flush_interval, self._timed_flush)
        self.flush_timer.start()

    def flush_batch(self, traces_to_flush: List[Trace]):
        batch = []
        with self.traces_lock:
            # select the traces that have ended to transit
            ready_traces = [
                t
                for t in traces_to_flush
                if t.has_ended() and not self.in_transit.get(t.xid)
            ]

            # add the traces to the batch, if they have ended and are not currently in transit
            for trace in ready_traces:
                batch.append(trace)

            # remove them from the list of traces to be flushed
            for trace in ready_traces:
                self.traces.remove(trace)

            # add them to the in-transit list
            self.mark_as_transiting(traces_to_flush)

        if batch:
            self.task_manager.process(batch)

    def _timed_flush(self):
        print("_timed_flush")
        if self.traces:
            self.flush_batch(self.traces)
        self.flush_timer = threading.Timer(self.flush_interval, self._timed_flush)
        self.flush_timer.start()

    def _on_batch_failure(self, failed_traces: List[Trace]):
        print("_on_batch_failure")
        # with self.traces_lock:
        self.traces.extend(failed_traces)

    def flush_all(self):
        self.flush_batch(self.traces)

    def flush_sync(self):
        self.flush_all()
        self.task_manager.queue.join()

    def shutdown(self):
        self.flush_timer.cancel()
        self.flush_all()
        self.task_manager.shutdown()
        self.traces_lock = None
        print("shutdown completed successfully")

    def get_traces(self) -> List[Trace]:
        return self.traces

    def get_in_transit(self) -> Dict[str, Trace]:
        return self.in_transit

    def trace(self, name: str, attributes: Dict[str, Any] = None) -> Trace:
        trace = Trace(name=name, tenant_id=self.tenant_id, attributes=attributes)
        self.traces.append(trace)
        return trace

    def get_queued_traces(self) -> List[Trace]:
        return [
            t for t in self.traces if t.has_ended() and not self.in_transit.get(t.xid)
        ]

    def mark_as_transiting(self, traces: List[Trace]) -> None:
        for trace in traces:
            self.in_transit[trace.xid] = trace

    def unmark_as_transiting(self, traces: List[Trace]) -> None:
        for trace in traces:
            del self.in_transit[trace.xid]

    def calculate_kilobyte_size(self, anything: Any) -> int:
        return sys.getsizeof(anything) // 1024

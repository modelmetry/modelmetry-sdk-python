import asyncio
from threading import Timer
from typing import Any, Callable, Dict, List
import uuid

from modelmetry.observability.trace import Trace
import sys

from modelmetry.openapi.models.ingest_signals_v1_request_body import IngestSignalsV1RequestBody


class ObservabilityClient:
    traces: List[Trace] = []
    max_size_kb: int = 5
    max_batch_len: int = 5
    interval_ms: int = 1000

    timer: Timer = None

    # in transit
    flights: Dict[str, Any] = {}  # Any is normally a promise
    in_transit: Dict[str, Trace] = {}
    on_flushed: Callable[[List[Trace]], None] = lambda traces: None

    def __init__(
        self,
        tenant_id: str,
        max_size_kb: int = None,
        max_batch_len: int = None,
        interval_ms: int = None,
    ) -> None:
        self.tenant_id = tenant_id
        self.traces = []

        self.interval_ms = interval_ms or None
        self.max_size_kb = max_size_kb or self.max_size_kb
        self.max_batch_len = max_batch_len or self.max_batch_len

        self.start_timer()

    # async flushBatch(traces: Trace[]): Promise<void> {
    #   const batchId = Math.random().toString(36).substring(7);

    #   // a. select the traces that have ended to transit
    #   // b. and remove them from the list of traces to be flushed
    #   // c. add them to the in-transit list
    #   const tracesToTransit = traces.filter((t) => {
    #     // if the trace has not ended, bail early
    #     if (!t.hasEnded()) return false;

    #     // if the trace is already in transit, bail early
    #     if (this.inTransit[t.getXid()]) return false;

    #     // ok
    #     return true;
    #   });

    #   // mark them as in transit
    #   this.markAsTransiting(tracesToTransit);

    #   // remove the traces to transit from the list of traces to be flushed
    #   const idsOfTracesToTransit = tracesToTransit.map((t) => t.getXid());
    #   this.traces = this.traces.filter((t) => !idsOfTracesToTransit.includes(t.getXid()));

    #   // bail early if there's nothing to flush
    #   if (tracesToTransit.length === 0) {
    #     return;
    #   }

    #   try {

    #     // build the batch
    #     const batch = buildIngestBatchFromTraces(tracesToTransit);

    #     // store the promise
    #     const flight = this.client.POST("/signals/ingest/v1", { body: { ...batch } });
    #     this.flights[batchId] = flight;
    #     flight.finally(() => { delete this.flights[batchId] });

    #     // send the batch
    #     const { error } = await flight;

    #     // handle errors
    #     if (error) throw new APIError(error);

    #     // callback
    #     this.onFlushed(tracesToTransit);

    #   } catch (error) {

    #     // restore the traces that failed to flush
    #     this.traces.push(...tracesToTransit);

    #     // handle errors
    #     if (error instanceof APIError) {
    #       console.error("Failed to flush traces (api error)", error.errorModel);
    #       return;
    #     }

    #     // handle other errors
    #     console.error("Failed to flush traces (unknown)", error);

    #   } finally {
    #     // mark them as not in transit
    #     this.unmarkAsTransiting(tracesToTransit);
    #   }

    #   console.log(`Flushed ${tracesToTransit.length} traces`);
    #   return;
    # }

    async def flush_batch(self, traces: List[Trace]) -> None:
        batch_id = uuid.uuid4()

        #  a. select the traces that have ended to transit
        traces_to_transit = [
            t for t in traces if t.has_ended() and not self.in_transit.get(t.xid)
        ]

        #  b. and remove them from the list of traces to be flushed
        for trace in traces_to_transit:
            self.traces.remove(trace)

        #  c. add them to the in-transit list
        self.mark_as_transiting(traces_to_transit)

        # remove the traces to transit from the list of traces to be flushed
        ids_of_traces_to_transit = [t.xid for t in traces_to_transit]

        # bail early if there's nothing to flush
        if not traces_to_transit:
            return

        try:
            # build the batch
            batch = buildIngestBatchFromTraces(traces_to_transit)

            # store the promise
            flight = self.client.POST("/signals/ingest/v1", body={**batch})
            self.flights[batch_id] = flight
            flight.finally(lambda: self.flights.pop(batch_id))
    
            # send the batch
            error = await flight

            # handle errors
            if error:
                raise APIError(error)
            
            # callback
            self.on_flushed(traces_to_transit)

        except Exception as error:
            # restore the traces that failed to flush
            self.traces.extend(traces_to_transit)
                               
            # handle errors
            if isinstance(error, APIError):
                print("Failed to flush traces (api error)", error.error_model)
                return
            
            # handle other errors
            print("Failed to flush traces (unknown)", error)

        finally:
            
            # mark them as not in transit
            self.unmark_as_transiting(traces_to_transit)

        # try {

        #   // build the batch
        #   const batch = buildIngestBatchFromTraces(tracesToTransit);

        #   // store the promise
        #   const flight = this.client.POST("/signals/ingest/v1", { body: { ...batch } });
        #   this.flights[batchId] = flight;
        #   flight.finally(() => { delete this.flights[batchId] });

        #   // send the batch
        #   const { error } = await flight;

        #   // handle errors
        #   if (error) throw new APIError(error);

        #   // callback
        #   this.onFlushed(tracesToTransit);

        # } catch (error) {

        #   // restore the traces that failed to flush
        #   this.traces.push(...tracesToTransit);

        #   // handle errors
        #   if (error instanceof APIError) {
        #     console.error("Failed to flush traces (api error)", error.errorModel);
        #     return;
        #   }

        #   // handle other errors
        #   console.error("Failed to flush traces (unknown)", error);

        # } finally {
        #   // mark them as not in transit
        #   this.unmarkAsTransiting(tracesToTransit);
        # }

    async def flush_if_conditions_fulfilled(self):
        queue = self.get_queued_traces()
        if len(queue) >= self.max_batch_len:
            return await self.flush_batch(queue)

        size = self.calculate_kilobyte_size(queue)
        if size >= self.max_size_kb:
            return await self.flush_batch(queue)

        return

    async def flush_all(self) -> None:
        return await self.flush_batch(self.traces)

    async def shutdown(self) -> None:
        self.stop_timer()

        try:
            # flush all traces
            await self.flush_all()

            # if there are no more flights, bail early
            if not self.flights:
                return

            # wait for all flights to land
            await asyncio.gather(*self.flights.values(), return_exceptions=True)

            # flush one more time in case some traces were added during the wait
            await self.flush_all()

        except Exception as error:
            print("Error whilst shutting down the observability client", error)

    async def handle_timer_execution(self):
        if not self.timer:
            return

        self.stop_timer()
        await self.flush_if_conditions_fulfilled()
        self.start_timer()

    def start_timer(self):
        if not self.timer:
            return
        if not self.interval_ms or self.interval_ms <= 0:
            return
        self.timer = Timer(self.interval_ms, self.handle_timer_execution)

    def stop_timer(self):
        if self.timer:
            self.timer.cancel()
            self.timer = None

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


def buildIngestBatchFromTraces(traces: List[Trace]) -> IngestSignalsV1RequestBody:
    pass
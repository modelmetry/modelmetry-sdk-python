import sys
import unittest
from unittest.mock import MagicMock
from modelmetry.openapi.api.default_api import DefaultApi
from modelmetry.observability.client import ObservabilityClient
from modelmetry.observability.trace import Trace


class TestClientFlushing(unittest.TestCase):
    def setUp(self):
        self.api = DefaultApi()
        self.client = ObservabilityClient(self.api, "ten_test")

    def tearDown(self):
        self.client.shutdown()
        return super().tearDown()

    # def test_flush_batch(self):
    #     traces = [
    #         Trace(name="trace1", tenant_id="ten_test"),
    #         Trace(name="trace2", tenant_id="ten_test"),
    #     ]
    #     self.client.traces = traces
    #     self.client.task_manager.process = MagicMock()
    #     self.client.flush_batch(traces)
    #     self.assertEqual(self.client.traces, [])
    #     self.client.task_manager.process.assert_called_once_with(traces)

    # def test_timed_flush(self):
    #     traces = [
    #         Trace(name="trace1", tenant_id="ten_test"),
    #         Trace(name="trace2", tenant_id="ten_test"),
    #     ]
    #     self.client.traces = traces
    #     self.client.flush_batch = MagicMock()
    #     self.client._timed_flush()
    #     self.assertEqual(self.client.traces, [])
    #     self.client.flush_batch.assert_called_once_with(traces)

    # def test_on_batch_failure(self):
    #     traces = [
    #         Trace(name="trace1", tenant_id="ten_test"),
    #         Trace(name="trace2", tenant_id="ten_test"),
    #     ]
    #     self.client.traces = []
    #     self.client._on_batch_failure(traces)
    #     self.assertEqual(self.client.traces, traces)

    # def test_flush_all(self):
    #     traces = [
    #         Trace(name="trace1", tenant_id="ten_test"),
    #         Trace(name="trace2", tenant_id="ten_test"),
    #     ]
    #     self.client.traces = traces
    #     self.client.flush_batch = MagicMock()
    #     self.client.flush_all()
    #     self.assertEqual(self.client.traces, [])
    #     self.client.flush_batch.assert_called_once_with(traces)

    # def test_flush_sync(self):
    #     traces = [
    #         Trace(name="trace1", tenant_id="ten_test"),
    #         Trace(name="trace2", tenant_id="ten_test"),
    #     ]
    #     self.client.traces = traces
    #     self.client.flush_all = MagicMock()
    #     self.client.task_manager.queue.join = MagicMock()
    #     self.client.flush_sync()
    #     self.assertEqual(self.client.traces, [])
    #     self.client.flush_all.assert_called_once()
    #     self.client.task_manager.queue.join.assert_called_once()

    # def test_get_traces(self):
    #     traces = [
    #         Trace(name="trace1", tenant_id="ten_test"),
    #         Trace(name="trace2", tenant_id="ten_test"),
    #     ]
    #     self.client.traces = traces
    #     self.assertEqual(self.client.get_traces(), traces)

    # def test_get_in_transit(self):
    #     self.assertEqual(self.client.get_in_transit(), self.client.in_transit)

    def test_trace(self):
        trace = self.client.trace("trace1")
        trace.end()
        self.assertEqual(trace.name, "trace1")
        self.assertEqual(trace.tenant_id, "ten_test")
        self.assertIn(trace, self.client.traces)

    # def test_get_queued_traces(self):
    #     t1 = self.client.trace("trace1").end()
    #     t2 = self.client.trace("trace2").end()
    #     t3 = self.client.trace("trace3").end()
    #     self.client.in_transit = {
    #         t1.xid: t1,
    #     }
    #     self.assertEqual(self.client.get_queued_traces(), [t2, t3])

    # def test_mark_as_transiting(self):
    #     t1 = self.client.trace("trace1").end()
    #     t2 = self.client.trace("trace2").end()
    #     traces = [t1, t2]
    #     self.client.mark_as_transiting(traces)
    #     self.assertEqual(self.client.in_transit, {trace.xid: trace for trace in traces})

    # def test_unmark_as_transiting(self):
    #     traces = [
    #         Trace(name="trace1", tenant_id="ten_test"),
    #         Trace(name="trace2", tenant_id="ten_test"),
    #     ]
    #     self.client.in_transit = {trace.xid: trace for trace in traces}
    #     self.client.unmark_as_transiting(traces)
    #     self.assertEqual(self.client.in_transit, {})

    # def test_calculate_kilobyte_size(self):
    #     size = self.client.calculate_kilobyte_size("test")
    #     self.assertEqual(size, 0)  # sys.getsizeof("test") returns 52, so 52 // 1024 = 0

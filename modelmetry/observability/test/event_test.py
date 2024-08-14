import unittest

import unittest
from datetime import datetime
from modelmetry.observability.event import Event

class TestEvent(unittest.TestCase):
  def test_constructor(self):
    name = "test_event"
    trace_id = "12345"
    span_id = "67890"
    at = datetime.now()
    attributes = {"key1": "value1", "key2": "value2"}

    event = Event(name, trace_id, span_id, at, attributes)

    self.assertEqual(event.name, name)
    self.assertEqual(event.trace_id, trace_id)
    self.assertEqual(event.span_id, span_id)
    self.assertEqual(event.at, at)
    self.assertEqual(event.attributes, attributes)

  def test_set_attribute(self):
    event = Event("test_event")
    key = "key"
    value = "value"

    event.set_attribute(key, value)

    self.assertEqual(event.attributes[key], value)

  def test_merge_attributes(self):
    event = Event("test_event")
    attributes = {"key1": "value1", "key2": "value2"}

    event.merge_attributes(attributes)

    self.assertEqual(event.attributes, attributes)

  def test_put_attributes(self):
    event = Event("test_event")
    attributes = {"key1": "value1", "key2": "value2"}

    event.put_attributes(attributes)

    self.assertEqual(event.attributes, attributes)

  def test_to_ingest_params(self):
    name = "test_event"
    trace_id = "12345"
    span_id = "67890"
    at = datetime.now()
    attributes = {"key1": "value1", "key2": "value2"}

    event = Event(name, trace_id, span_id, at, attributes)
    ingest_params = event.to_ingest_params()

    self.assertEqual(ingest_params.xid, event.xid)
    self.assertEqual(ingest_params.name, event.name)
    self.assertEqual(ingest_params.at, event.at)
    self.assertEqual(ingest_params.attributes, event.attributes)
    self.assertEqual(ingest_params.trace_id, event.trace_id)
    self.assertEqual(ingest_params.span_id, event.span_id)
    self.assertIsNone(ingest_params.entry_id)
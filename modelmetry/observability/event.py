import sys
sys.path.append('.')

import uuid

from typing import Dict, Optional
from datetime import datetime
from modelmetry.openapi import CreateEventParams

class Event:
  def __init__(
    self,
    name: str,
    trace_id: Optional[str] = None,
    span_id: Optional[str] = None,
    at: Optional[datetime] = None,
    attributes: Optional[Dict[str, str]] = None,
  ) -> None:
    self.xid = str(uuid.uuid4())
    self.name = name
    self.trace_id = trace_id
    self.span_id = span_id
    self.at = at or datetime.now()
    self.attributes = attributes or {}

  def set_attribute(self, key: str, value: str) -> "Event":
    self.attributes[key] = value
    return self

  def merge_attributes(self, attributes: Dict[str, str]) -> "Event":
    self.attributes.update(attributes)
    return self

  def put_attributes(self, attributes: Dict[str, str]) -> "Event":
    self.attributes = attributes
    return self

  @staticmethod
  def from_span(span: "Span", name: str) -> "Event":
    return Event(
      name=name,
      trace_id=span.get_trace_id(),
      span_id=span.get_xid(),
    )

  def to_ingest_params(self) -> CreateEventParams:
    return CreateEventParams(
      xid=self.xid,
      name=self.name,
      at=self.at,
      attributes=self.attributes,
      trace_id=self.trace_id,
      span_id=self.span_id,
      entry_id=None,
    )
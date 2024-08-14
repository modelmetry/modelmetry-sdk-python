from typing import Any, Optional, Union
from datetime import datetime
import uuid

from typing import Dict, Optional
from datetime import datetime
from modelmetry.openapi import CreateFindingParams, CreateFindingParamsValue

class Finding:
  def __init__(
    self,
    name: str,
    value: Union[int, bool, str],
    trace_id: Optional[str] = None,
    span_id: Optional[str] = None,
    description: Optional[str] = None,
    source: Optional[str] = "api",
    comment: Optional[str] = None,
    metadata: Optional[Dict[str, Any]] = None,
    at: Optional[datetime] = None,
  ) -> None:
    self.xid: str = str(uuid.uuid4())
    self.name: str = name
    self.value: Union[int, bool, str] = value
    self.trace_id: Optional[str] = trace_id
    self.span_id: Optional[str] = span_id
    self.description: Optional[str] = description
    self.source: str = source or "api"
    self.comment: Optional[str] = comment
    self.metadata = metadata or {}
    self.at: datetime = at or datetime.now()

  def set_value(self, value: Union[int, bool, str]) -> "Finding":
    self.value = value
    return self

  def to_ingest_params(self) -> CreateFindingParams:
    return CreateFindingParams(
      xid = self.xid,
      name = self.name,
      value = CreateFindingParamsValue(actual_instance=self.value),
      comment = self.comment,
      description = self.description,
      source = self.source or "api",
      at = self.at.isoformat(),
      metadata = self.metadata,
      trace_id = self.trace_id,
      span_id = self.span_id,
      entry_id = None,
    )

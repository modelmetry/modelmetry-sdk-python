# coding: utf-8

"""
    Modelmetry API

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)

    The version of the OpenAPI document: 1.0.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


from __future__ import annotations
import pprint
import re  # noqa: F401
import json

from pydantic import BaseModel, ConfigDict, Field, StrictFloat, StrictInt, StrictStr
from typing import Any, ClassVar, Dict, List, Optional, Union
from modelmetry.openapi.models.simplified_finding import SimplifiedFinding
from typing import Optional, Set
from typing_extensions import Self

class SummarisedEntry(BaseModel):
    """
    SummarisedEntry
    """ # noqa: E501
    check_id: Optional[StrictStr] = Field(alias="CheckID")
    duration_ms: StrictInt = Field(alias="DurationMs")
    evaluator_id: StrictStr = Field(alias="EvaluatorID")
    findings: List[SimplifiedFinding] = Field(alias="Findings")
    id: StrictStr = Field(alias="ID")
    instance_id: Optional[StrictStr] = Field(alias="InstanceID")
    message: StrictStr = Field(alias="Message")
    outcome: StrictStr = Field(alias="Outcome")
    score: Optional[Union[StrictFloat, StrictInt]] = Field(alias="Score")
    skip: StrictStr = Field(alias="Skip")
    span_id: Optional[StrictStr] = Field(alias="SpanID")
    tenant_id: StrictStr = Field(alias="TenantID")
    trace_id: Optional[StrictStr] = Field(alias="TraceID")
    __properties: ClassVar[List[str]] = ["CheckID", "DurationMs", "EvaluatorID", "Findings", "ID", "InstanceID", "Message", "Outcome", "Score", "Skip", "SpanID", "TenantID", "TraceID"]

    model_config = ConfigDict(
        populate_by_name=True,
        validate_assignment=True,
        protected_namespaces=(),
    )


    def to_str(self) -> str:
        """Returns the string representation of the model using alias"""
        return pprint.pformat(self.model_dump(by_alias=True))

    def to_json(self) -> str:
        """Returns the JSON representation of the model using alias"""
        # TODO: pydantic v2: use .model_dump_json(by_alias=True, exclude_unset=True) instead
        return json.dumps(self.to_dict())

    @classmethod
    def from_json(cls, json_str: str) -> Optional[Self]:
        """Create an instance of SummarisedEntry from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self) -> Dict[str, Any]:
        """Return the dictionary representation of the model using alias.

        This has the following differences from calling pydantic's
        `self.model_dump(by_alias=True)`:

        * `None` is only added to the output dict for nullable fields that
          were set at model initialization. Other fields with value `None`
          are ignored.
        """
        excluded_fields: Set[str] = set([
        ])

        _dict = self.model_dump(
            by_alias=True,
            exclude=excluded_fields,
            exclude_none=True,
        )
        # override the default output from pydantic by calling `to_dict()` of each item in findings (list)
        _items = []
        if self.findings:
            for _item in self.findings:
                if _item:
                    _items.append(_item.to_dict())
            _dict['Findings'] = _items
        # set to None if check_id (nullable) is None
        # and model_fields_set contains the field
        if self.check_id is None and "check_id" in self.model_fields_set:
            _dict['CheckID'] = None

        # set to None if instance_id (nullable) is None
        # and model_fields_set contains the field
        if self.instance_id is None and "instance_id" in self.model_fields_set:
            _dict['InstanceID'] = None

        # set to None if score (nullable) is None
        # and model_fields_set contains the field
        if self.score is None and "score" in self.model_fields_set:
            _dict['Score'] = None

        # set to None if span_id (nullable) is None
        # and model_fields_set contains the field
        if self.span_id is None and "span_id" in self.model_fields_set:
            _dict['SpanID'] = None

        # set to None if trace_id (nullable) is None
        # and model_fields_set contains the field
        if self.trace_id is None and "trace_id" in self.model_fields_set:
            _dict['TraceID'] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of SummarisedEntry from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "CheckID": obj.get("CheckID"),
            "DurationMs": obj.get("DurationMs"),
            "EvaluatorID": obj.get("EvaluatorID"),
            "Findings": [SimplifiedFinding.from_dict(_item) for _item in obj["Findings"]] if obj.get("Findings") is not None else None,
            "ID": obj.get("ID"),
            "InstanceID": obj.get("InstanceID"),
            "Message": obj.get("Message"),
            "Outcome": obj.get("Outcome"),
            "Score": obj.get("Score"),
            "Skip": obj.get("Skip"),
            "SpanID": obj.get("SpanID"),
            "TenantID": obj.get("TenantID"),
            "TraceID": obj.get("TraceID")
        })
        return _obj



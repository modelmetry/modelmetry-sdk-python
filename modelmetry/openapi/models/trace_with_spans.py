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

from datetime import datetime
from pydantic import BaseModel, ConfigDict, Field, StrictStr
from typing import Any, ClassVar, Dict, List, Optional
from modelmetry.openapi.models.span import Span
from typing import Optional, Set
from typing_extensions import Self

class TraceWithSpans(BaseModel):
    """
    TraceWithSpans
    """ # noqa: E501
    var_schema: Optional[StrictStr] = Field(default=None, description="A URL to the JSON Schema for this object.", alias="$schema")
    attributes: Dict[str, Any] = Field(alias="Attributes")
    created_at: datetime = Field(alias="CreatedAt")
    end: datetime = Field(alias="End")
    id: StrictStr = Field(alias="ID")
    name: StrictStr = Field(alias="Name")
    session_id: StrictStr = Field(alias="SessionID")
    spans: List[Span] = Field(alias="Spans")
    start: datetime = Field(alias="Start")
    tenant_id: StrictStr = Field(alias="TenantID")
    updated_at: datetime = Field(alias="UpdatedAt")
    xid: StrictStr = Field(alias="XID")
    additional_properties: Dict[str, Any] = {}
    __properties: ClassVar[List[str]] = ["$schema", "Attributes", "CreatedAt", "End", "ID", "Name", "SessionID", "Spans", "Start", "TenantID", "UpdatedAt", "XID"]

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
        """Create an instance of TraceWithSpans from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self) -> Dict[str, Any]:
        """Return the dictionary representation of the model using alias.

        This has the following differences from calling pydantic's
        `self.model_dump(by_alias=True)`:

        * `None` is only added to the output dict for nullable fields that
          were set at model initialization. Other fields with value `None`
          are ignored.
        * OpenAPI `readOnly` fields are excluded.
        * Fields in `self.additional_properties` are added to the output dict.
        """
        excluded_fields: Set[str] = set([
            "var_schema",
            "additional_properties",
        ])

        _dict = self.model_dump(
            by_alias=True,
            exclude=excluded_fields,
            exclude_none=True,
        )
        # override the default output from pydantic by calling `to_dict()` of each item in spans (list)
        _items = []
        if self.spans:
            for _item in self.spans:
                if _item:
                    _items.append(_item.to_dict())
            _dict['Spans'] = _items
        # puts key-value pairs in additional_properties in the top level
        if self.additional_properties is not None:
            for _key, _value in self.additional_properties.items():
                _dict[_key] = _value

        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of TraceWithSpans from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "$schema": obj.get("$schema"),
            "Attributes": obj.get("Attributes"),
            "CreatedAt": obj.get("CreatedAt"),
            "End": obj.get("End"),
            "ID": obj.get("ID"),
            "Name": obj.get("Name"),
            "SessionID": obj.get("SessionID"),
            "Spans": [Span.from_dict(_item) for _item in obj["Spans"]] if obj.get("Spans") is not None else None,
            "Start": obj.get("Start"),
            "TenantID": obj.get("TenantID"),
            "UpdatedAt": obj.get("UpdatedAt"),
            "XID": obj.get("XID")
        })
        # store additional fields in additional_properties
        for _key in obj.keys():
            if _key not in cls.__properties:
                _obj.additional_properties[_key] = obj.get(_key)

        return _obj


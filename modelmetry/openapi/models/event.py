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
from typing import Any, ClassVar, Dict, List
from typing import Optional, Set
from typing_extensions import Self

class Event(BaseModel):
    """
    Event
    """ # noqa: E501
    created_at: datetime = Field(alias="CreatedAt")
    entry_id: StrictStr = Field(alias="EntryID")
    id: StrictStr = Field(alias="ID")
    metadata: Dict[str, Any] = Field(alias="Metadata")
    name: StrictStr = Field(alias="Name")
    span_id: StrictStr = Field(alias="SpanID")
    tenant_id: StrictStr = Field(alias="TenantID")
    trace_id: StrictStr = Field(alias="TraceID")
    updated_at: datetime = Field(alias="UpdatedAt")
    xid: StrictStr = Field(alias="XID")
    additional_properties: Dict[str, Any] = {}
    __properties: ClassVar[List[str]] = ["CreatedAt", "EntryID", "ID", "Metadata", "Name", "SpanID", "TenantID", "TraceID", "UpdatedAt", "XID"]

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
        """Create an instance of Event from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self) -> Dict[str, Any]:
        """Return the dictionary representation of the model using alias.

        This has the following differences from calling pydantic's
        `self.model_dump(by_alias=True)`:

        * `None` is only added to the output dict for nullable fields that
          were set at model initialization. Other fields with value `None`
          are ignored.
        * Fields in `self.additional_properties` are added to the output dict.
        """
        excluded_fields: Set[str] = set([
            "additional_properties",
        ])

        _dict = self.model_dump(
            by_alias=True,
            exclude=excluded_fields,
            exclude_none=True,
        )
        # puts key-value pairs in additional_properties in the top level
        if self.additional_properties is not None:
            for _key, _value in self.additional_properties.items():
                _dict[_key] = _value

        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of Event from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "CreatedAt": obj.get("CreatedAt"),
            "EntryID": obj.get("EntryID"),
            "ID": obj.get("ID"),
            "Metadata": obj.get("Metadata"),
            "Name": obj.get("Name"),
            "SpanID": obj.get("SpanID"),
            "TenantID": obj.get("TenantID"),
            "TraceID": obj.get("TraceID"),
            "UpdatedAt": obj.get("UpdatedAt"),
            "XID": obj.get("XID")
        })
        # store additional fields in additional_properties
        for _key in obj.keys():
            if _key not in cls.__properties:
                _obj.additional_properties[_key] = obj.get(_key)

        return _obj



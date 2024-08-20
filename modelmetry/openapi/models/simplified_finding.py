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
from pydantic import BaseModel, ConfigDict, Field, StrictStr, field_validator
from typing import Any, ClassVar, Dict, List
from modelmetry.openapi.models.create_finding_params_value import CreateFindingParamsValue
from typing import Optional, Set
from typing_extensions import Self

class SimplifiedFinding(BaseModel):
    """
    SimplifiedFinding
    """ # noqa: E501
    at: datetime = Field(alias="At")
    comment: StrictStr = Field(alias="Comment")
    evaluator_id: StrictStr = Field(alias="EvaluatorID")
    metadata: Dict[str, Any] = Field(alias="Metadata")
    name: StrictStr = Field(alias="Name")
    source: StrictStr = Field(alias="Source")
    value: CreateFindingParamsValue = Field(alias="Value")
    additional_properties: Dict[str, Any] = {}
    __properties: ClassVar[List[str]] = ["At", "Comment", "EvaluatorID", "Metadata", "Name", "Source", "Value"]

    @field_validator('source')
    def source_validate_enum(cls, value):
        """Validates the enum"""
        if value not in set(['annotation', 'evaluator', 'sdk']):
            raise ValueError("must be one of enum values ('annotation', 'evaluator', 'sdk')")
        return value

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
        """Create an instance of SimplifiedFinding from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of value
        if self.value:
            _dict['Value'] = self.value.to_dict()
        # puts key-value pairs in additional_properties in the top level
        if self.additional_properties is not None:
            for _key, _value in self.additional_properties.items():
                _dict[_key] = _value

        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of SimplifiedFinding from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "At": obj.get("At"),
            "Comment": obj.get("Comment"),
            "EvaluatorID": obj.get("EvaluatorID"),
            "Metadata": obj.get("Metadata"),
            "Name": obj.get("Name"),
            "Source": obj.get("Source") if obj.get("Source") is not None else 'annotation',
            "Value": CreateFindingParamsValue.from_dict(obj["Value"]) if obj.get("Value") is not None else None
        })
        # store additional fields in additional_properties
        for _key in obj.keys():
            if _key not in cls.__properties:
                _obj.additional_properties[_key] = obj.get(_key)

        return _obj



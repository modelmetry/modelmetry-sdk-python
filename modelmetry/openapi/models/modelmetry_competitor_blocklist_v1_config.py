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

from pydantic import BaseModel, ConfigDict, Field, StrictStr, field_validator
from typing import Any, ClassVar, Dict, List
from typing_extensions import Annotated
from typing import Optional, Set
from typing_extensions import Self

class ModelmetryCompetitorBlocklistV1Config(BaseModel):
    """
    ModelmetryCompetitorBlocklistV1Config
    """ # noqa: E501
    case_sensitivity: StrictStr = Field(description="Whether to consider the word's case when matching strings", alias="CaseSensitivity")
    competitors: Annotated[List[StrictStr], Field(min_length=1)] = Field(description="List of competitors to search for", alias="Competitors")
    look_in: StrictStr = Field(description="Where to search for competitor mentions", alias="LookIn")
    additional_properties: Dict[str, Any] = {}
    __properties: ClassVar[List[str]] = ["CaseSensitivity", "Competitors", "LookIn"]

    @field_validator('case_sensitivity')
    def case_sensitivity_validate_enum(cls, value):
        """Validates the enum"""
        if value not in set(['case_sensitive', 'case_insensitive']):
            raise ValueError("must be one of enum values ('case_sensitive', 'case_insensitive')")
        return value

    @field_validator('look_in')
    def look_in_validate_enum(cls, value):
        """Validates the enum"""
        if value not in set(['user', 'assistant', '*']):
            raise ValueError("must be one of enum values ('user', 'assistant', '*')")
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
        """Create an instance of ModelmetryCompetitorBlocklistV1Config from a JSON string"""
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
        """Create an instance of ModelmetryCompetitorBlocklistV1Config from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "CaseSensitivity": obj.get("CaseSensitivity") if obj.get("CaseSensitivity") is not None else 'sensitive',
            "Competitors": obj.get("Competitors"),
            "LookIn": obj.get("LookIn") if obj.get("LookIn") is not None else '*'
        })
        # store additional fields in additional_properties
        for _key in obj.keys():
            if _key not in cls.__properties:
                _obj.additional_properties[_key] = obj.get(_key)

        return _obj



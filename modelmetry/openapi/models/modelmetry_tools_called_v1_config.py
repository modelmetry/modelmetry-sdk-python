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

from pydantic import BaseModel, ConfigDict, Field
from typing import Any, ClassVar, Dict, List, Optional
from modelmetry.openapi.models.modelmetry_tools_called_v1_expectation import ModelmetryToolsCalledV1Expectation
from typing import Optional, Set
from typing_extensions import Self

class ModelmetryToolsCalledV1Config(BaseModel):
    """
    ModelmetryToolsCalledV1Config
    """ # noqa: E501
    expectations: Optional[Any] = Field(default=None, alias="Expectations")
    expections: List[ModelmetryToolsCalledV1Expectation] = Field(description="The expected JSON schema to validate against", alias="Expections")
    additional_properties: Dict[str, Any] = {}
    __properties: ClassVar[List[str]] = ["Expectations", "Expections"]

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
        """Create an instance of ModelmetryToolsCalledV1Config from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of each item in expections (list)
        _items = []
        if self.expections:
            for _item in self.expections:
                if _item:
                    _items.append(_item.to_dict())
            _dict['Expections'] = _items
        # puts key-value pairs in additional_properties in the top level
        if self.additional_properties is not None:
            for _key, _value in self.additional_properties.items():
                _dict[_key] = _value

        # set to None if expectations (nullable) is None
        # and model_fields_set contains the field
        if self.expectations is None and "expectations" in self.model_fields_set:
            _dict['Expectations'] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of ModelmetryToolsCalledV1Config from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "Expectations": obj.get("Expectations"),
            "Expections": [ModelmetryToolsCalledV1Expectation.from_dict(_item) for _item in obj["Expections"]] if obj.get("Expections") is not None else None
        })
        # store additional fields in additional_properties
        for _key in obj.keys():
            if _key not in cls.__properties:
                _obj.additional_properties[_key] = obj.get(_key)

        return _obj



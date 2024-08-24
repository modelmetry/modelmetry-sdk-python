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

from pydantic import BaseModel, ConfigDict, Field, StrictBool, StrictFloat, StrictInt, StrictStr
from typing import Any, ClassVar, Dict, List, Optional, Union
from typing_extensions import Annotated
from modelmetry.openapi.models.tool import Tool
from typing import Optional, Set
from typing_extensions import Self

class Options(BaseModel):
    """
    Options
    """ # noqa: E501
    api_key: Optional[StrictStr] = Field(default=None, alias="APIKey")
    api_version: Optional[StrictStr] = Field(default=None, alias="APIVersion")
    base_url: Optional[StrictStr] = Field(default=None, alias="BaseURL")
    deployment_id: Optional[StrictStr] = Field(default=None, alias="DeploymentID")
    frequency_penalty: Optional[Union[StrictFloat, StrictInt]] = Field(default=None, alias="FrequencyPenalty")
    function_call: Optional[StrictStr] = Field(default=None, alias="FunctionCall")
    functions: Optional[List[StrictStr]] = Field(default=None, alias="Functions")
    logit_bias: Optional[Dict[str, Any]] = Field(default=None, alias="LogitBias")
    logprobs: Optional[StrictBool] = Field(default=None, alias="Logprobs")
    max_tokens: Optional[StrictInt] = Field(default=None, alias="MaxTokens")
    model: Optional[StrictStr] = Field(default=None, alias="Model")
    model_list: Optional[List[StrictStr]] = Field(default=None, alias="ModelList")
    n: Optional[StrictInt] = Field(default=None, alias="N")
    presence_penalty: Optional[Union[StrictFloat, StrictInt]] = Field(default=None, alias="PresencePenalty")
    provider: Optional[StrictStr] = Field(default=None, alias="Provider")
    response_format: Optional[Dict[str, Any]] = Field(default=None, alias="ResponseFormat")
    seed: Optional[StrictInt] = Field(default=None, alias="Seed")
    stop: Optional[Dict[str, Any]] = Field(default=None, alias="Stop")
    stream: Optional[StrictBool] = Field(default=None, alias="Stream")
    temperature: Optional[Union[Annotated[float, Field(le=1, strict=True, ge=0)], Annotated[int, Field(le=1, strict=True, ge=0)]]] = Field(default=None, alias="Temperature")
    timeout: Optional[Union[Annotated[float, Field(strict=True, ge=0)], Annotated[int, Field(strict=True, ge=0)]]] = Field(default=None, alias="Timeout")
    tool_choice: Optional[StrictStr] = Field(default=None, alias="ToolChoice")
    tools: Optional[List[Tool]] = Field(default=None, alias="Tools")
    top_logprobs: Optional[StrictInt] = Field(default=None, alias="TopLogprobs")
    top_p: Optional[Union[Annotated[float, Field(le=1, strict=True, ge=0)], Annotated[int, Field(le=1, strict=True, ge=0)]]] = Field(default=None, alias="TopP")
    user: Optional[StrictStr] = Field(default=None, alias="User")
    additional_properties: Dict[str, Any] = {}
    __properties: ClassVar[List[str]] = ["APIKey", "APIVersion", "BaseURL", "DeploymentID", "FrequencyPenalty", "FunctionCall", "Functions", "LogitBias", "Logprobs", "MaxTokens", "Model", "ModelList", "N", "PresencePenalty", "Provider", "ResponseFormat", "Seed", "Stop", "Stream", "Temperature", "Timeout", "ToolChoice", "Tools", "TopLogprobs", "TopP", "User"]

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
        """Create an instance of Options from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of each item in tools (list)
        _items = []
        if self.tools:
            for _item in self.tools:
                if _item:
                    _items.append(_item.to_dict())
            _dict['Tools'] = _items
        # puts key-value pairs in additional_properties in the top level
        if self.additional_properties is not None:
            for _key, _value in self.additional_properties.items():
                _dict[_key] = _value

        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of Options from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "APIKey": obj.get("APIKey"),
            "APIVersion": obj.get("APIVersion"),
            "BaseURL": obj.get("BaseURL"),
            "DeploymentID": obj.get("DeploymentID"),
            "FrequencyPenalty": obj.get("FrequencyPenalty"),
            "FunctionCall": obj.get("FunctionCall"),
            "Functions": obj.get("Functions"),
            "LogitBias": obj.get("LogitBias"),
            "Logprobs": obj.get("Logprobs"),
            "MaxTokens": obj.get("MaxTokens"),
            "Model": obj.get("Model"),
            "ModelList": obj.get("ModelList"),
            "N": obj.get("N"),
            "PresencePenalty": obj.get("PresencePenalty"),
            "Provider": obj.get("Provider"),
            "ResponseFormat": obj.get("ResponseFormat"),
            "Seed": obj.get("Seed"),
            "Stop": obj.get("Stop"),
            "Stream": obj.get("Stream"),
            "Temperature": obj.get("Temperature"),
            "Timeout": obj.get("Timeout"),
            "ToolChoice": obj.get("ToolChoice"),
            "Tools": [Tool.from_dict(_item) for _item in obj["Tools"]] if obj.get("Tools") is not None else None,
            "TopLogprobs": obj.get("TopLogprobs"),
            "TopP": obj.get("TopP"),
            "User": obj.get("User")
        })
        # store additional fields in additional_properties
        for _key in obj.keys():
            if _key not in cls.__properties:
                _obj.additional_properties[_key] = obj.get(_key)

        return _obj



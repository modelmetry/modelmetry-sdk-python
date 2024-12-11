from typing import Any, Dict, List, Union

from devtools import pprint

from modelmetry import openapi
from modelmetry.guardrails.response import GuardrailCheckResponse
from modelmetry.openapi.api.default_api import DefaultApi
from modelmetry.openapi.models import (
    CheckPayloadRequestBody,
    Payload,
    CompletionPayload,
    SystemMessage,
    UserMessage,
    AssistantMessage,
    ToolMessage,
)
from modelmetry.openapi.models.completion_family_data_messages_inner import (
    CompletionFamilyDataMessagesInner,
)

# create a Message type that's a union of the above four message types
Message = Union[SystemMessage, UserMessage, AssistantMessage, ToolMessage]


class GuardrailsClient:
    backend: DefaultApi = None
    tenant_id: str | None = None

    def __init__(
        self,
        # backend
        api_key: str,
        tenant_id: str | None = None,
        host="https://api.modelmetry.com",
        # opts
    ):
        if not api_key:
            raise ValueError("api_key is required to instantiate GuardrailsClient")

        self.tenant_id = tenant_id or None
        self.api_key = api_key
        self.client = openapi.ApiClient(
            openapi.Configuration(host, api_key={"apikeyAuth": api_key})
        )
        self.backend = openapi.DefaultApi(self.client)

    def check_text(self, text: str, params: Dict[str, Any]) -> GuardrailCheckResponse:
        role = params.get("role", "user")
        if role == "user":
            # {"Role": "user", "Contents": [{"Text": text}]}
            obj = dict()
            obj["Role"] = "user"
            obj["Contents"] = [{"Text": text}]
            message = UserMessage.from_dict(obj)
        elif role == "system":
            message = SystemMessage(Role=role, Text=text)
        elif role == "assistant":
            message = AssistantMessage(Role=role, Text=text)
        elif role == "tool":
            message = ToolMessage(Role=role, Text=text)
        else:
            raise ValueError(f"Invalid role: {role}")
        return self.check_message(message, params)

    def check_message(
        self, message: Message, params: Dict[str, Any]
    ) -> GuardrailCheckResponse:
        return self.check_messages([message], params)

    def check_messages(
        self, messages: List[Message], params: Dict[str, Any]
    ) -> GuardrailCheckResponse:

        body = CheckPayloadRequestBody(
            TenantID=self.tenant_id or None,
            GuardrailID=params["guardrail_id"] or "-",
            Payload=Payload(
                Completion=CompletionPayload(
                    Messages=[
                        CompletionFamilyDataMessagesInner.from_dict(message.to_dict())
                        for message in messages
                    ],
                    Options={},
                )
            ),
        )

        try:
            data = self.backend.check_payload(body)
            pprint(data)
            output = GuardrailCheckResponse(check=data)
            output.check = data
            return output
        except openapi.ApiException as e:
            pprint(e.body)
            output = GuardrailCheckResponse(error=e)
            return output

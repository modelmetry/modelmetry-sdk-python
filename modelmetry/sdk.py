"""
This module defines a Client class for interacting with an API using the OpenAPI-generated client library.

Classes:
    Client: This class provides methods to interact with the API.

Usage:
    To use the Client class, you need to instantiate it with your API key, tenant ID, and optionally the host URL.
    Once instantiated, you can call the `call_guardrail` method with a `CallGuardrailRequestBody` object to perform
    the desired operation.

Example:
    >>> from openapi.models.call_guardrail_request_body import CallGuardrailRequestBody
    >>> api_key = "your_api_key"
    >>> tenant_id = "your_tenant_id"
    >>> client = Client(api_key, tenant_id)
    >>> body = CallGuardrailRequestBody(...)
    >>> response = client.call_guardrail(body)
"""

from typing import List

from modelmetry import openapi
from modelmetry.openapi.models import CallGuardrailRequestBody, Call
from modelmetry.observability.client import ObservabilityClient
from modelmetry.openapi.models.chat_input import ChatInput
from modelmetry.openapi.models.text_input import TextInput


class GuardrailCallOutput:
    """
    Represents an object with ID and Passed fields.
    """

    def __init__(self, call: Call):
        """
        Initializes the GuardrailCallOutput with ID and Passed fields.

        Parameters:
            call (Call): The Call object in its entirety from the response.
        """
        self.Call = call
        self.Passed = True if call.outcome == "pass" else False
        self.Failed = True if call.outcome == "fail" else False
        self.Errored = True if call.outcome == "error" else False

    def __str__(self):
        return f"GuardrailCallOutput(ID={self.Call.id}, Passed={self.Passed} Failed={self.Failed} Errored={self.Errored})"

    def __repr__(self):
        return f"GuardrailCallOutput(ID={self.Call.id}, Passed={self.Passed} Failed={self.Failed} Errored={self.Errored})"


class Client:
    """
    A client for interacting with an API.

    Attributes:
        configuration (openapi.Configuration): The configuration for the OpenAPI client.
        tenant_id (str): The tenant ID for the API.
        client (openapi.ApiClient): The API client instance.
        api_instance (openapi.DefaultApi): The API instance for making calls.

    Methods:
        __init__(self, api_key: str, tenant_id: str, host: str): Initializes the Client with API key, tenant ID, and host.
        call_guardrail(self, body: CallGuardrailRequestBody): Calls the guardrail endpoint with the provided body.
    """

    _observability: ObservabilityClient = None

    def __init__(self, api_key: str, tenant_id: str, host="https://api.modelmetry.com"):
        """
        Initializes the Client with the necessary configuration.

        Parameters:
            api_key (str): The API key for authentication.
            tenant_id (str): The tenant ID for the API.
            host (str, optional): The host URL of the API. Defaults to "https://api.modelmetry.com".
        """
        self.configuration = openapi.Configuration(
            host,
            api_key={"apikeyAuth": api_key},
        )
        self.tenant_id = tenant_id
        self.api_key = api_key
        self.client = openapi.ApiClient(self.configuration)
        self.api_instance = openapi.DefaultApi(self.client)

        self._observability = ObservabilityClient(
            tenant_id=tenant_id,
            backend=self.api_instance,
        )

    def observability(self) -> ObservabilityClient:
        return self._observability

    def shutdown(self):
        self._observability.shutdown()

    def check(
        self,
        guardrail_id: str,
        input_text: str = None,
        input_chat: openapi.ChatInput = None,
        output_text: str = None,
        output_chat: List[openapi.ChatInputMessagesInner] = None,
    ) -> GuardrailCallOutput:

        input: openapi.CompletionPayloadInput | None = None
        output: openapi.Output | None = None

        if input_text:
            input = openapi.CompletionPayloadInput(TextInput(Text=input_text))

        if input_chat:
            input = openapi.CompletionPayloadInput(input_chat)

        if output_chat:
            output = openapi.Output(Messages=output_chat)

        if output_text and len(output_text) > 0:
            output = openapi.Output(Text=output_text)

        body = CallGuardrailRequestBody(
            TenantID=self.tenant_id,
            GuardrailID=guardrail_id,
            Payload=openapi.Payload(Input=input, Output=output),
        )

        res = self.api_instance.call_guardrail_with_http_info(body)
        output = GuardrailCallOutput(res.data)
        return output

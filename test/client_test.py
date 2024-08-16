import sys

sys.path.append(".")

from modelmetry.openapi.api_response import ApiResponse
from unittest.mock import MagicMock, patch
from datetime import date

from modelmetry.sdk import Client, GuardrailCallOutput
from modelmetry.openapi.models import Call, Output


def test_client_api_key_and_tenant_id():
    client = Client(api_key="test_api_key", tenant_id="test_tenant_id")
    assert client.api_key == "test_api_key" and client.tenant_id == "test_tenant_id"


def test_client_check():
    # Mock response
    mock_response = ApiResponse(
        status_code=200,
        raw_data=b"",
        data=Call(
            id="call_123",
            tenant_id="test_tenant_id",
            guardrail_id="test_guardrail_id",
            outcome="pass",
            duration_ms=1000,
            payload={},
            summarised_entries=[],
            metadata={},
            created_at=date.today(),
            updated_at=date.today(),
            created_by="test_user",
            updated_by="test_user",
        ),
    )

    # Prepare
    client = Client(api_key="test_api_key", tenant_id="test_tenant_id")
    guardrail_id = "test_guardrail_id"
    output_text = "Test output"

    # Call the method
    client.api_instance.call_guardrail_with_http_info = MagicMock(
        return_value=mock_response
    )

    result = client.check(guardrail_id=guardrail_id, output_text=output_text)

    # Assertions
    assert isinstance(result, GuardrailCallOutput)
    assert result.Call.id == "call_123"
    assert result.Passed
    assert not result.Failed
    assert not result.Errored

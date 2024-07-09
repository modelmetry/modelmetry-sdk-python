import sys 
sys.path.append('.')

from unittest.mock import patch
from datetime import date

from modelmetry.sdk import Client, GuardrailCallOutput
from modelmetry.openapi.models import Call, TextOutput

def test_client_api_key_and_tenant_id():
    client = Client(api_key="test_api_key", tenant_id="test_tenant_id")
    assert client.api_key == "test_api_key" and client.tenant_id == "test_tenant_id"

@patch('modelmetry.openapi.api.default_api.DefaultApi.call_guardrail_with_http_info')
def test_client_check(mock_call_guardrail):
    # Mock response
    mock_response = Call(
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
    )
    mock_call_guardrail.return_value = (mock_response, 200, {})

    # Prepare
    client = Client(api_key="test_api_key", tenant_id="test_tenant_id")
    guardrail_id = "test_guardrail_id"
    text_output = TextOutput(text="Test output")

    # Call the method
    result = client.check(guardrail_id=guardrail_id, text_output=text_output)

    # Assertions
    assert isinstance(result, GuardrailCallOutput)
    assert result.Call.id == "call_123"
    assert result.Passed
    assert not result.Failed
    assert not result.Errored
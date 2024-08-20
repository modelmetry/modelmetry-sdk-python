import sys

sys.path.append(".")

from modelmetry.openapi.api_response import ApiResponse
from unittest.mock import MagicMock, patch
from datetime import date

from modelmetry.sdk import Client, GuardrailCheckOutput
from modelmetry.openapi.models import GuardrailCheck, Output


def test_client_api_key_and_tenant_id():
    client = Client(api_key="test_api_key", tenant_id="test_tenant_id")
    assert client.api_key == "test_api_key" and client.tenant_id == "test_tenant_id"

import sys

sys.path.append(".")

from modelmetry.sdk import Client


def test_client_api_key_and_tenant_id():
    client = Client(api_key="test_api_key", tenant_id="test_tenant_id")
    assert client.api_key == "test_api_key" and client.tenant_id == "test_tenant_id"

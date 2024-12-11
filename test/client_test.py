import sys

sys.path.append(".")

from modelmetry.sdk import Client


def test_client_api_key_and_tenant_id():
    client = Client(
        api_key="test_api_key", tenant_id="test_tenant_id", host="test_host"
    )
    assert (
        client._configuration.api_key == "test_api_key"
        and client._configuration.tenant_id == "test_tenant_id"
        and client._configuration.host == "test_host"
    )

# CheckPayloadRequestBody


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**var_schema** | **str** | A URL to the JSON Schema for this object. | [optional] [readonly] 
**guardrail_id** | **str** |  | 
**payload** | [**Payload**](Payload.md) |  | 
**tenant_id** | **str** |  | [optional] 

## Example

```python
from modelmetry.openapi.models.check_payload_request_body import CheckPayloadRequestBody

# TODO update the JSON string below
json = "{}"
# create an instance of CheckPayloadRequestBody from a JSON string
check_payload_request_body_instance = CheckPayloadRequestBody.from_json(json)
# print the JSON string representation of the object
print(CheckPayloadRequestBody.to_json())

# convert the object into a dict
check_payload_request_body_dict = check_payload_request_body_instance.to_dict()
# create an instance of CheckPayloadRequestBody from a dict
check_payload_request_body_from_dict = CheckPayloadRequestBody.from_dict(check_payload_request_body_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



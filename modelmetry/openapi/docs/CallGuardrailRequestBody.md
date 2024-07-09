# CallGuardrailRequestBody


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**var_schema** | **str** | A URL to the JSON Schema for this object. | [optional] [readonly] 
**guardrail_id** | **str** |  | 
**payload** | [**Payload**](Payload.md) |  | 
**tenant_id** | **str** |  | 

## Example

```python
from modelmetry.openapi.models.call_guardrail_request_body import CallGuardrailRequestBody

# TODO update the JSON string below
json = "{}"
# create an instance of CallGuardrailRequestBody from a JSON string
call_guardrail_request_body_instance = CallGuardrailRequestBody.from_json(json)
# print the JSON string representation of the object
print(CallGuardrailRequestBody.to_json())

# convert the object into a dict
call_guardrail_request_body_dict = call_guardrail_request_body_instance.to_dict()
# create an instance of CallGuardrailRequestBody from a dict
call_guardrail_request_body_from_dict = CallGuardrailRequestBody.from_dict(call_guardrail_request_body_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



# EvaluateRequestBody


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**var_schema** | **str** | A URL to the JSON Schema for this object. | [optional] [readonly] 
**by_config** | [**EvaluateRequestByConfig**](EvaluateRequestByConfig.md) |  | [optional] 
**by_entry** | [**EvaluateRequestByEntry**](EvaluateRequestByEntry.md) |  | [optional] 
**by_instance** | [**EvaluateRequestByInstance**](EvaluateRequestByInstance.md) |  | [optional] 
**persist** | **bool** |  | [optional] 
**tenant_id** | **str** |  | 

## Example

```python
from modelmetry.openapi.models.evaluate_request_body import EvaluateRequestBody

# TODO update the JSON string below
json = "{}"
# create an instance of EvaluateRequestBody from a JSON string
evaluate_request_body_instance = EvaluateRequestBody.from_json(json)
# print the JSON string representation of the object
print(EvaluateRequestBody.to_json())

# convert the object into a dict
evaluate_request_body_dict = evaluate_request_body_instance.to_dict()
# create an instance of EvaluateRequestBody from a dict
evaluate_request_body_from_dict = EvaluateRequestBody.from_dict(evaluate_request_body_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



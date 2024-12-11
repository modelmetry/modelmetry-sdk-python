# EvaluateRequestByInstance


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**instance_id** | **str** |  | 
**payload** | [**Payload**](Payload.md) |  | 

## Example

```python
from modelmetry.openapi.models.evaluate_request_by_instance import EvaluateRequestByInstance

# TODO update the JSON string below
json = "{}"
# create an instance of EvaluateRequestByInstance from a JSON string
evaluate_request_by_instance_instance = EvaluateRequestByInstance.from_json(json)
# print the JSON string representation of the object
print(EvaluateRequestByInstance.to_json())

# convert the object into a dict
evaluate_request_by_instance_dict = evaluate_request_by_instance_instance.to_dict()
# create an instance of EvaluateRequestByInstance from a dict
evaluate_request_by_instance_from_dict = EvaluateRequestByInstance.from_dict(evaluate_request_by_instance_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



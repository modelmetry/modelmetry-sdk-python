# EvaluateRequestByConfig


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**config** | **object** |  | 
**evaluator_id** | **str** |  | 
**grading** | [**GradingConfiguration**](GradingConfiguration.md) |  | [optional] 
**payload** | [**Payload**](Payload.md) |  | 
**secrets** | **List[str]** |  | [optional] 

## Example

```python
from modelmetry.openapi.models.evaluate_request_by_config import EvaluateRequestByConfig

# TODO update the JSON string below
json = "{}"
# create an instance of EvaluateRequestByConfig from a JSON string
evaluate_request_by_config_instance = EvaluateRequestByConfig.from_json(json)
# print the JSON string representation of the object
print(EvaluateRequestByConfig.to_json())

# convert the object into a dict
evaluate_request_by_config_dict = evaluate_request_by_config_instance.to_dict()
# create an instance of EvaluateRequestByConfig from a dict
evaluate_request_by_config_from_dict = EvaluateRequestByConfig.from_dict(evaluate_request_by_config_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



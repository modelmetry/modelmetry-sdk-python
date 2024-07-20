# SimplifiedFinding


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**at** | **datetime** |  | 
**comment** | **str** |  | 
**evaluator_id** | **str** |  | 
**metadata** | **object** |  | 
**name** | **str** |  | 
**source** | **str** |  | 
**value** | [**CreateFindingParamsValue**](CreateFindingParamsValue.md) |  | 

## Example

```python
from modelmetry.openapi.models.simplified_finding import SimplifiedFinding

# TODO update the JSON string below
json = "{}"
# create an instance of SimplifiedFinding from a JSON string
simplified_finding_instance = SimplifiedFinding.from_json(json)
# print the JSON string representation of the object
print(SimplifiedFinding.to_json())

# convert the object into a dict
simplified_finding_dict = simplified_finding_instance.to_dict()
# create an instance of SimplifiedFinding from a dict
simplified_finding_from_dict = SimplifiedFinding.from_dict(simplified_finding_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



# CreateFindingParams


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**at** | **datetime** |  | [optional] 
**comment** | **str** |  | [optional] 
**description** | **str** |  | [optional] 
**entry_id** | **str** |  | [optional] 
**metadata** | **object** |  | [optional] 
**name** | **str** |  | 
**source** | **str** |  | [optional] 
**span_id** | **str** |  | [optional] 
**trace_id** | **str** |  | [optional] 
**value** | [**CreateFindingParamsValue**](CreateFindingParamsValue.md) |  | 
**xid** | **str** |  | 

## Example

```python
from modelmetry.openapi.models.create_finding_params import CreateFindingParams

# TODO update the JSON string below
json = "{}"
# create an instance of CreateFindingParams from a JSON string
create_finding_params_instance = CreateFindingParams.from_json(json)
# print the JSON string representation of the object
print(CreateFindingParams.to_json())

# convert the object into a dict
create_finding_params_dict = create_finding_params_instance.to_dict()
# create an instance of CreateFindingParams from a dict
create_finding_params_from_dict = CreateFindingParams.from_dict(create_finding_params_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



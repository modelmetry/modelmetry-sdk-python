# Finding


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**at** | **datetime** |  | 
**comment** | **str** |  | 
**created_at** | **datetime** |  | 
**entry_id** | **str** |  | 
**evaluator_id** | **str** |  | 
**id** | **str** |  | 
**metadata** | **object** |  | 
**name** | **str** |  | 
**source** | **str** |  | 
**span_id** | **str** |  | 
**tenant_id** | **str** |  | 
**trace_id** | **str** |  | 
**updated_at** | **datetime** |  | 
**value** | [**CreateFindingParamsValue**](CreateFindingParamsValue.md) |  | 
**xid** | **str** |  | 

## Example

```python
from modelmetry.openapi.models.finding import Finding

# TODO update the JSON string below
json = "{}"
# create an instance of Finding from a JSON string
finding_instance = Finding.from_json(json)
# print the JSON string representation of the object
print(Finding.to_json())

# convert the object into a dict
finding_dict = finding_instance.to_dict()
# create an instance of Finding from a dict
finding_from_dict = Finding.from_dict(finding_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



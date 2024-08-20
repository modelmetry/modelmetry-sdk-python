# SummarisedEntry


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**check_id** | **str** |  | 
**duration_ms** | **int** |  | 
**evaluator_id** | **str** |  | 
**findings** | [**List[SimplifiedFinding]**](SimplifiedFinding.md) |  | 
**id** | **str** |  | 
**instance_id** | **str** |  | 
**message** | **str** |  | 
**outcome** | **str** |  | 
**score** | **float** |  | 
**skip** | **str** |  | 
**tenant_id** | **str** |  | 

## Example

```python
from modelmetry.openapi.models.summarised_entry import SummarisedEntry

# TODO update the JSON string below
json = "{}"
# create an instance of SummarisedEntry from a JSON string
summarised_entry_instance = SummarisedEntry.from_json(json)
# print the JSON string representation of the object
print(SummarisedEntry.to_json())

# convert the object into a dict
summarised_entry_dict = summarised_entry_instance.to_dict()
# create an instance of SummarisedEntry from a dict
summarised_entry_from_dict = SummarisedEntry.from_dict(summarised_entry_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



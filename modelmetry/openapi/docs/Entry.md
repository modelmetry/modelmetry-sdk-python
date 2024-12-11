# Entry


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**var_schema** | **str** | A URL to the JSON Schema for this object. | [optional] [readonly] 
**check_id** | **str** |  | 
**config** | **object** |  | 
**created_at** | **datetime** |  | 
**created_by** | **str** |  | 
**duration_ms** | **int** |  | 
**evaluator_id** | **str** |  | 
**findings** | [**List[Finding]**](Finding.md) |  | 
**finished_at** | **datetime** |  | 
**grading** | [**GradingConfiguration**](GradingConfiguration.md) |  | 
**id** | **str** |  | 
**instance_id** | **str** |  | 
**message** | **str** |  | 
**metadata** | **object** |  | 
**outcome** | **str** | The status of the entry. | [default to 'na']
**payload** | [**Payload**](Payload.md) |  | 
**skip** | **str** |  | 
**span_id** | **str** |  | 
**started_at** | **datetime** |  | 
**tenant_id** | **str** |  | 
**trace_id** | **str** |  | 
**updated_at** | **datetime** |  | 
**updated_by** | **str** |  | 

## Example

```python
from modelmetry.openapi.models.entry import Entry

# TODO update the JSON string below
json = "{}"
# create an instance of Entry from a JSON string
entry_instance = Entry.from_json(json)
# print the JSON string representation of the object
print(Entry.to_json())

# convert the object into a dict
entry_dict = entry_instance.to_dict()
# create an instance of Entry from a dict
entry_from_dict = Entry.from_dict(entry_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



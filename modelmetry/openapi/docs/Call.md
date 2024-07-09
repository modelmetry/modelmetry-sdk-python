# Call


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**var_schema** | **str** | A URL to the JSON Schema for this object. | [optional] [readonly] 
**created_at** | **datetime** |  | 
**created_by** | **str** |  | 
**duration_ms** | **int** |  | 
**guardrail_id** | **str** |  | 
**id** | **str** |  | 
**metadata** | **object** |  | 
**outcome** | **str** |  | 
**payload** | [**Payload**](Payload.md) |  | 
**summarised_entries** | [**List[SummarisedEntry]**](SummarisedEntry.md) |  | 
**tenant_id** | **str** |  | 
**updated_at** | **datetime** |  | 
**updated_by** | **str** |  | 

## Example

```python
from modelmetry.openapi.models.call import Call

# TODO update the JSON string below
json = "{}"
# create an instance of Call from a JSON string
call_instance = Call.from_json(json)
# print the JSON string representation of the object
print(Call.to_json())

# convert the object into a dict
call_dict = call_instance.to_dict()
# create an instance of Call from a dict
call_from_dict = Call.from_dict(call_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



# Check


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
from modelmetry.openapi.models.check import Check

# TODO update the JSON string below
json = "{}"
# create an instance of Check from a JSON string
check_instance = Check.from_json(json)
# print the JSON string representation of the object
print(Check.to_json())

# convert the object into a dict
check_dict = check_instance.to_dict()
# create an instance of Check from a dict
check_from_dict = Check.from_dict(check_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



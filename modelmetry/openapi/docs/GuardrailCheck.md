# GuardrailCheck


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
**outcome** | **str** | The status of the entry. | [default to na]
**payload** | [**Payload**](Payload.md) |  | 
**summarised_entries** | [**List[SummarisedEntry]**](SummarisedEntry.md) |  | 
**tenant_id** | **str** |  | 
**updated_at** | **datetime** |  | 
**updated_by** | **str** |  | 

## Example

```python
from modelmetry.openapi.models.guardrail_check import GuardrailCheck

# TODO update the JSON string below
json = "{}"
# create an instance of GuardrailCheck from a JSON string
guardrail_check_instance = GuardrailCheck.from_json(json)
# print the JSON string representation of the object
print(GuardrailCheck.to_json())

# convert the object into a dict
guardrail_check_dict = guardrail_check_instance.to_dict()
# create an instance of GuardrailCheck from a dict
guardrail_check_from_dict = GuardrailCheck.from_dict(guardrail_check_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



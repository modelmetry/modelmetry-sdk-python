# CreateSpanParams


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**attributes** | **object** |  | [optional] 
**end** | **datetime** |  | 
**family** | **str** |  | [optional] 
**family_data** | **object** |  | [optional] 
**message** | **str** |  | [optional] 
**name** | **str** |  | 
**parent_id** | **str** |  | [optional] 
**severity** | **str** |  | [optional] 
**start** | **datetime** |  | 
**trace_id** | **str** |  | 
**xid** | **str** |  | 

## Example

```python
from modelmetry.openapi.models.create_span_params import CreateSpanParams

# TODO update the JSON string below
json = "{}"
# create an instance of CreateSpanParams from a JSON string
create_span_params_instance = CreateSpanParams.from_json(json)
# print the JSON string representation of the object
print(CreateSpanParams.to_json())

# convert the object into a dict
create_span_params_dict = create_span_params_instance.to_dict()
# create an instance of CreateSpanParams from a dict
create_span_params_from_dict = CreateSpanParams.from_dict(create_span_params_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



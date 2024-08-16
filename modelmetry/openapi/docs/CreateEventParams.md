# CreateEventParams


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**at** | **datetime** |  | [optional] 
**entry_id** | **str** |  | [optional] 
**metadata** | **object** |  | [optional] 
**name** | **str** |  | 
**span_id** | **str** |  | [optional] 
**trace_id** | **str** |  | [optional] 
**xid** | **str** |  | 

## Example

```python
from modelmetry.openapi.models.create_event_params import CreateEventParams

# TODO update the JSON string below
json = "{}"
# create an instance of CreateEventParams from a JSON string
create_event_params_instance = CreateEventParams.from_json(json)
# print the JSON string representation of the object
print(CreateEventParams.to_json())

# convert the object into a dict
create_event_params_dict = create_event_params_instance.to_dict()
# create an instance of CreateEventParams from a dict
create_event_params_from_dict = CreateEventParams.from_dict(create_event_params_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



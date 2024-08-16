# CreateTraceParams


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**end** | **datetime** |  | [optional] 
**metadata** | **object** |  | [optional] 
**name** | **str** |  | [optional] 
**session_id** | **str** |  | [optional] 
**start** | **datetime** |  | 
**xid** | **str** |  | 

## Example

```python
from modelmetry.openapi.models.create_trace_params import CreateTraceParams

# TODO update the JSON string below
json = "{}"
# create an instance of CreateTraceParams from a JSON string
create_trace_params_instance = CreateTraceParams.from_json(json)
# print the JSON string representation of the object
print(CreateTraceParams.to_json())

# convert the object into a dict
create_trace_params_dict = create_trace_params_instance.to_dict()
# create an instance of CreateTraceParams from a dict
create_trace_params_from_dict = CreateTraceParams.from_dict(create_trace_params_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



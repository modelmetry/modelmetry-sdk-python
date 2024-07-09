# SimpleMessage


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**contents** | [**List[SimplePart]**](SimplePart.md) |  | 
**name** | **str** |  | [optional] 
**role** | **str** |  | 
**tool_call_id** | **str** |  | [optional] 
**tool_calls** | [**List[ToolCall]**](ToolCall.md) |  | [optional] 

## Example

```python
from modelmetry.openapi.models.simple_message import SimpleMessage

# TODO update the JSON string below
json = "{}"
# create an instance of SimpleMessage from a JSON string
simple_message_instance = SimpleMessage.from_json(json)
# print the JSON string representation of the object
print(SimpleMessage.to_json())

# convert the object into a dict
simple_message_dict = simple_message_instance.to_dict()
# create an instance of SimpleMessage from a dict
simple_message_from_dict = SimpleMessage.from_dict(simple_message_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



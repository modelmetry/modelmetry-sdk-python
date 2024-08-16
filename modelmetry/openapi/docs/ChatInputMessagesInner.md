# ChatInputMessagesInner

Represents a completion message.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**contents** | [**List[AssistantMessageContentsInner]**](AssistantMessageContentsInner.md) |  | 
**name** | **str** |  | [optional] 
**role** | **str** |  | 
**tool_calls** | [**List[ToolCall]**](ToolCall.md) |  | [optional] 
**tool_call_id** | **str** |  | 

## Example

```python
from modelmetry.openapi.models.chat_input_messages_inner import ChatInputMessagesInner

# TODO update the JSON string below
json = "{}"
# create an instance of ChatInputMessagesInner from a JSON string
chat_input_messages_inner_instance = ChatInputMessagesInner.from_json(json)
# print the JSON string representation of the object
print(ChatInputMessagesInner.to_json())

# convert the object into a dict
chat_input_messages_inner_dict = chat_input_messages_inner_instance.to_dict()
# create an instance of ChatInputMessagesInner from a dict
chat_input_messages_inner_from_dict = ChatInputMessagesInner.from_dict(chat_input_messages_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



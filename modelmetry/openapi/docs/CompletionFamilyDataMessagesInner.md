# CompletionFamilyDataMessagesInner

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
from modelmetry.openapi.models.completion_family_data_messages_inner import CompletionFamilyDataMessagesInner

# TODO update the JSON string below
json = "{}"
# create an instance of CompletionFamilyDataMessagesInner from a JSON string
completion_family_data_messages_inner_instance = CompletionFamilyDataMessagesInner.from_json(json)
# print the JSON string representation of the object
print(CompletionFamilyDataMessagesInner.to_json())

# convert the object into a dict
completion_family_data_messages_inner_dict = completion_family_data_messages_inner_instance.to_dict()
# create an instance of CompletionFamilyDataMessagesInner from a dict
completion_family_data_messages_inner_from_dict = CompletionFamilyDataMessagesInner.from_dict(completion_family_data_messages_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



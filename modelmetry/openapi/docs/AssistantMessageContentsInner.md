# AssistantMessageContentsInner

Represents a part of a completion message.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**text** | **str** |  | 
**data** | **str** |  | 
**detail** | **str** |  | [optional] 
**mime_type** | **str** |  | 

## Example

```python
from modelmetry.openapi.models.assistant_message_contents_inner import AssistantMessageContentsInner

# TODO update the JSON string below
json = "{}"
# create an instance of AssistantMessageContentsInner from a JSON string
assistant_message_contents_inner_instance = AssistantMessageContentsInner.from_json(json)
# print the JSON string representation of the object
print(AssistantMessageContentsInner.to_json())

# convert the object into a dict
assistant_message_contents_inner_dict = assistant_message_contents_inner_instance.to_dict()
# create an instance of AssistantMessageContentsInner from a dict
assistant_message_contents_inner_from_dict = AssistantMessageContentsInner.from_dict(assistant_message_contents_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



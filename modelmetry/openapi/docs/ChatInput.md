# ChatInput


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**messages** | [**List[SimpleMessage]**](SimpleMessage.md) |  | [optional] 
**settings** | [**SimpleOptions**](SimpleOptions.md) |  | 

## Example

```python
from modelmetry.openapi.models.chat_input import ChatInput

# TODO update the JSON string below
json = "{}"
# create an instance of ChatInput from a JSON string
chat_input_instance = ChatInput.from_json(json)
# print the JSON string representation of the object
print(ChatInput.to_json())

# convert the object into a dict
chat_input_dict = chat_input_instance.to_dict()
# create an instance of ChatInput from a dict
chat_input_from_dict = ChatInput.from_dict(chat_input_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



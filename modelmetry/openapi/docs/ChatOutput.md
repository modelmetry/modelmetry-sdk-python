# ChatOutput


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**messages** | [**List[SimpleMessage]**](SimpleMessage.md) |  | 
**settings** | [**SimpleOptions**](SimpleOptions.md) |  | 

## Example

```python
from modelmetry.openapi.models.chat_output import ChatOutput

# TODO update the JSON string below
json = "{}"
# create an instance of ChatOutput from a JSON string
chat_output_instance = ChatOutput.from_json(json)
# print the JSON string representation of the object
print(ChatOutput.to_json())

# convert the object into a dict
chat_output_dict = chat_output_instance.to_dict()
# create an instance of ChatOutput from a dict
chat_output_from_dict = ChatOutput.from_dict(chat_output_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



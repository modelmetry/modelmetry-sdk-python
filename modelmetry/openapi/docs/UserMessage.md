# UserMessage


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**contents** | [**List[AssistantMessageContentsInner]**](AssistantMessageContentsInner.md) |  | 
**name** | **str** |  | [optional] 
**role** | **str** |  | 

## Example

```python
from modelmetry.openapi.models.user_message import UserMessage

# TODO update the JSON string below
json = "{}"
# create an instance of UserMessage from a JSON string
user_message_instance = UserMessage.from_json(json)
# print the JSON string representation of the object
print(UserMessage.to_json())

# convert the object into a dict
user_message_dict = user_message_instance.to_dict()
# create an instance of UserMessage from a dict
user_message_from_dict = UserMessage.from_dict(user_message_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



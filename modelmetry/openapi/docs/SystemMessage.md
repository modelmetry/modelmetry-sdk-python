# SystemMessage


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**contents** | [**List[AssistantMessageContentsInner]**](AssistantMessageContentsInner.md) |  | 
**name** | **str** |  | [optional] 
**role** | **str** |  | 

## Example

```python
from modelmetry.openapi.models.system_message import SystemMessage

# TODO update the JSON string below
json = "{}"
# create an instance of SystemMessage from a JSON string
system_message_instance = SystemMessage.from_json(json)
# print the JSON string representation of the object
print(SystemMessage.to_json())

# convert the object into a dict
system_message_dict = system_message_instance.to_dict()
# create an instance of SystemMessage from a dict
system_message_from_dict = SystemMessage.from_dict(system_message_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



# CompletionPayloadInput

Input for completion

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**text** | **str** |  | 
**messages** | [**List[ChatInputMessagesInner]**](ChatInputMessagesInner.md) |  | 
**options** | [**Options**](Options.md) |  | [optional] 

## Example

```python
from modelmetry.openapi.models.completion_payload_input import CompletionPayloadInput

# TODO update the JSON string below
json = "{}"
# create an instance of CompletionPayloadInput from a JSON string
completion_payload_input_instance = CompletionPayloadInput.from_json(json)
# print the JSON string representation of the object
print(CompletionPayloadInput.to_json())

# convert the object into a dict
completion_payload_input_dict = completion_payload_input_instance.to_dict()
# create an instance of CompletionPayloadInput from a dict
completion_payload_input_from_dict = CompletionPayloadInput.from_dict(completion_payload_input_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



# CompletionPayload


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**context** | [**CompletionPayloadContext**](CompletionPayloadContext.md) |  | [optional] 
**input** | [**Input**](Input.md) |  | [optional] 
**model** | **str** |  | 
**options** | [**SimpleOptions**](SimpleOptions.md) |  | 
**output** | [**Output**](Output.md) |  | [optional] 

## Example

```python
from modelmetry.openapi.models.completion_payload import CompletionPayload

# TODO update the JSON string below
json = "{}"
# create an instance of CompletionPayload from a JSON string
completion_payload_instance = CompletionPayload.from_json(json)
# print the JSON string representation of the object
print(CompletionPayload.to_json())

# convert the object into a dict
completion_payload_dict = completion_payload_instance.to_dict()
# create an instance of CompletionPayload from a dict
completion_payload_from_dict = CompletionPayload.from_dict(completion_payload_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



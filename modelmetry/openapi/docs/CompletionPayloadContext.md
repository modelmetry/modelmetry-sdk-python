# CompletionPayloadContext


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**parsed_system** | **str** |  | 
**retrieved_items** | [**List[RetrievedItem]**](RetrievedItem.md) |  | 

## Example

```python
from modelmetry.openapi.models.completion_payload_context import CompletionPayloadContext

# TODO update the JSON string below
json = "{}"
# create an instance of CompletionPayloadContext from a JSON string
completion_payload_context_instance = CompletionPayloadContext.from_json(json)
# print the JSON string representation of the object
print(CompletionPayloadContext.to_json())

# convert the object into a dict
completion_payload_context_dict = completion_payload_context_instance.to_dict()
# create an instance of CompletionPayloadContext from a dict
completion_payload_context_from_dict = CompletionPayloadContext.from_dict(completion_payload_context_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



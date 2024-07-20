# EmbeddingsPayload


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**inputs** | **List[str]** |  | 
**options** | [**SimpleOptions**](SimpleOptions.md) |  | 

## Example

```python
from modelmetry.openapi.models.embeddings_payload import EmbeddingsPayload

# TODO update the JSON string below
json = "{}"
# create an instance of EmbeddingsPayload from a JSON string
embeddings_payload_instance = EmbeddingsPayload.from_json(json)
# print the JSON string representation of the object
print(EmbeddingsPayload.to_json())

# convert the object into a dict
embeddings_payload_dict = embeddings_payload_instance.to_dict()
# create an instance of EmbeddingsPayload from a dict
embeddings_payload_from_dict = EmbeddingsPayload.from_dict(embeddings_payload_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



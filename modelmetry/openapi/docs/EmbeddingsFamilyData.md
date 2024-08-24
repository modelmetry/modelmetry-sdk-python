# EmbeddingsFamilyData


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**inputs** | **List[str]** |  | 
**options** | [**Options**](Options.md) |  | 

## Example

```python
from modelmetry.openapi.models.embeddings_family_data import EmbeddingsFamilyData

# TODO update the JSON string below
json = "{}"
# create an instance of EmbeddingsFamilyData from a JSON string
embeddings_family_data_instance = EmbeddingsFamilyData.from_json(json)
# print the JSON string representation of the object
print(EmbeddingsFamilyData.to_json())

# convert the object into a dict
embeddings_family_data_dict = embeddings_family_data_instance.to_dict()
# create an instance of EmbeddingsFamilyData from a dict
embeddings_family_data_from_dict = EmbeddingsFamilyData.from_dict(embeddings_family_data_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



# ModelmetryEmbeddingsSimilarityV1Config


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**extraction_method** | **str** | The method to use for extracting text strings. | 
**model** | **str** | The model to use for encoding text to embeddings (only OpenAI models at this stage). | 
**reference_text** | **str** | The reference text to compare against. Be as detailed or as general as you like. | 
**strategy** | **str** | The strategy to use for computing similarity. | 

## Example

```python
from modelmetry.openapi.models.modelmetry_embeddings_similarity_v1_config import ModelmetryEmbeddingsSimilarityV1Config

# TODO update the JSON string below
json = "{}"
# create an instance of ModelmetryEmbeddingsSimilarityV1Config from a JSON string
modelmetry_embeddings_similarity_v1_config_instance = ModelmetryEmbeddingsSimilarityV1Config.from_json(json)
# print the JSON string representation of the object
print(ModelmetryEmbeddingsSimilarityV1Config.to_json())

# convert the object into a dict
modelmetry_embeddings_similarity_v1_config_dict = modelmetry_embeddings_similarity_v1_config_instance.to_dict()
# create an instance of ModelmetryEmbeddingsSimilarityV1Config from a dict
modelmetry_embeddings_similarity_v1_config_from_dict = ModelmetryEmbeddingsSimilarityV1Config.from_dict(modelmetry_embeddings_similarity_v1_config_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



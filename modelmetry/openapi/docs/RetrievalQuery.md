# RetrievalQuery


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**embeddings** | **List[float]** |  | [optional] 
**text_representation** | **str** |  | 

## Example

```python
from modelmetry.openapi.models.retrieval_query import RetrievalQuery

# TODO update the JSON string below
json = "{}"
# create an instance of RetrievalQuery from a JSON string
retrieval_query_instance = RetrievalQuery.from_json(json)
# print the JSON string representation of the object
print(RetrievalQuery.to_json())

# convert the object into a dict
retrieval_query_dict = retrieval_query_instance.to_dict()
# create an instance of RetrievalQuery from a dict
retrieval_query_from_dict = RetrievalQuery.from_dict(retrieval_query_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



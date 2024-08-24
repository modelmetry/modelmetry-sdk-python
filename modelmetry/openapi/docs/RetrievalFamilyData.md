# RetrievalFamilyData


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**documents** | [**List[Document]**](Document.md) |  | 
**queries** | [**List[RetrievalQuery]**](RetrievalQuery.md) |  | 

## Example

```python
from modelmetry.openapi.models.retrieval_family_data import RetrievalFamilyData

# TODO update the JSON string below
json = "{}"
# create an instance of RetrievalFamilyData from a JSON string
retrieval_family_data_instance = RetrievalFamilyData.from_json(json)
# print the JSON string representation of the object
print(RetrievalFamilyData.to_json())

# convert the object into a dict
retrieval_family_data_dict = retrieval_family_data_instance.to_dict()
# create an instance of RetrievalFamilyData from a dict
retrieval_family_data_from_dict = RetrievalFamilyData.from_dict(retrieval_family_data_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



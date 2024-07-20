# RetrievalPayload


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**queries** | [**List[RetrievalQuery]**](RetrievalQuery.md) |  | 
**retrieved** | [**List[RetrievedItem]**](RetrievedItem.md) |  | 

## Example

```python
from modelmetry.openapi.models.retrieval_payload import RetrievalPayload

# TODO update the JSON string below
json = "{}"
# create an instance of RetrievalPayload from a JSON string
retrieval_payload_instance = RetrievalPayload.from_json(json)
# print the JSON string representation of the object
print(RetrievalPayload.to_json())

# convert the object into a dict
retrieval_payload_dict = retrieval_payload_instance.to_dict()
# create an instance of RetrievalPayload from a dict
retrieval_payload_from_dict = RetrievalPayload.from_dict(retrieval_payload_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



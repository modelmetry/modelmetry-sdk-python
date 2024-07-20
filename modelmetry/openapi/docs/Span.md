# Span


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**attributes** | **object** |  | 
**completion** | [**CompletionPayload**](CompletionPayload.md) |  | 
**created_at** | **datetime** |  | 
**embeddings** | [**EmbeddingsPayload**](EmbeddingsPayload.md) |  | 
**end** | **datetime** |  | 
**events** | [**List[Event]**](Event.md) |  | 
**family** | **str** |  | 
**findings** | [**List[Finding]**](Finding.md) |  | 
**id** | **str** |  | 
**message** | **str** |  | 
**name** | **str** |  | 
**other** | **object** |  | 
**parent_id** | **str** |  | 
**retrieval** | [**RetrievalPayload**](RetrievalPayload.md) |  | 
**severity** | **str** |  | 
**start** | **datetime** |  | 
**tenant_id** | **str** |  | 
**trace_id** | **str** |  | 
**updated_at** | **datetime** |  | 
**xid** | **str** |  | 

## Example

```python
from modelmetry.openapi.models.span import Span

# TODO update the JSON string below
json = "{}"
# create an instance of Span from a JSON string
span_instance = Span.from_json(json)
# print the JSON string representation of the object
print(Span.to_json())

# convert the object into a dict
span_dict = span_instance.to_dict()
# create an instance of Span from a dict
span_from_dict = Span.from_dict(span_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



# TraceWithSpans


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**created_at** | **datetime** |  | 
**end** | **datetime** |  | 
**id** | **str** |  | 
**metadata** | **Dict[str, object]** |  | 
**name** | **str** |  | 
**session_id** | **str** |  | [optional] 
**spans** | [**List[Span]**](Span.md) |  | 
**start** | **datetime** |  | 
**tenant_id** | **str** |  | 
**updated_at** | **datetime** |  | 
**xid** | **str** |  | 

## Example

```python
from modelmetry.openapi.models.trace_with_spans import TraceWithSpans

# TODO update the JSON string below
json = "{}"
# create an instance of TraceWithSpans from a JSON string
trace_with_spans_instance = TraceWithSpans.from_json(json)
# print the JSON string representation of the object
print(TraceWithSpans.to_json())

# convert the object into a dict
trace_with_spans_dict = trace_with_spans_instance.to_dict()
# create an instance of TraceWithSpans from a dict
trace_with_spans_from_dict = TraceWithSpans.from_dict(trace_with_spans_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



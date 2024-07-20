# IngestSignalsV1RequestBody


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**var_schema** | **str** | A URL to the JSON Schema for this object. | [optional] [readonly] 
**events** | [**List[CreateEventParams]**](CreateEventParams.md) |  | [optional] 
**findings** | [**List[CreateFindingParams]**](CreateFindingParams.md) |  | [optional] 
**sessions** | [**List[CreateSessionParams]**](CreateSessionParams.md) |  | [optional] 
**spans** | [**List[CreateSpanParams]**](CreateSpanParams.md) |  | [optional] 
**traces** | [**List[CreateTraceParams]**](CreateTraceParams.md) |  | [optional] 

## Example

```python
from modelmetry.openapi.models.ingest_signals_v1_request_body import IngestSignalsV1RequestBody

# TODO update the JSON string below
json = "{}"
# create an instance of IngestSignalsV1RequestBody from a JSON string
ingest_signals_v1_request_body_instance = IngestSignalsV1RequestBody.from_json(json)
# print the JSON string representation of the object
print(IngestSignalsV1RequestBody.to_json())

# convert the object into a dict
ingest_signals_v1_request_body_dict = ingest_signals_v1_request_body_instance.to_dict()
# create an instance of IngestSignalsV1RequestBody from a dict
ingest_signals_v1_request_body_from_dict = IngestSignalsV1RequestBody.from_dict(ingest_signals_v1_request_body_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



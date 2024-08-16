# IngestSignalsV1ResponseBody


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**var_schema** | **str** | A URL to the JSON Schema for this object. | [optional] [readonly] 

## Example

```python
from modelmetry.openapi.models.ingest_signals_v1_response_body import IngestSignalsV1ResponseBody

# TODO update the JSON string below
json = "{}"
# create an instance of IngestSignalsV1ResponseBody from a JSON string
ingest_signals_v1_response_body_instance = IngestSignalsV1ResponseBody.from_json(json)
# print the JSON string representation of the object
print(IngestSignalsV1ResponseBody.to_json())

# convert the object into a dict
ingest_signals_v1_response_body_dict = ingest_signals_v1_response_body_instance.to_dict()
# create an instance of IngestSignalsV1ResponseBody from a dict
ingest_signals_v1_response_body_from_dict = IngestSignalsV1ResponseBody.from_dict(ingest_signals_v1_response_body_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



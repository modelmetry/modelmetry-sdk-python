# ModelmetryHTTPRequestV1Config


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**findings_json_path** | **str** | The JSON path to the findings in the response body. | [optional] 
**headers** | **Dict[str, str]** | A map of headers to include in the request. | 
**message_json_path** | **str** | The JSON path to the message in the response body. | [optional] 
**method** | **str** | The HTTP method to use for the request. | [default to 'POST']
**outcome_json_path** | **str** | The JSON path to the outcome in the response body. | [optional] 
**url** | **str** | The URL to send the HTTP request to. | 

## Example

```python
from modelmetry.openapi.models.modelmetry_http_request_v1_config import ModelmetryHTTPRequestV1Config

# TODO update the JSON string below
json = "{}"
# create an instance of ModelmetryHTTPRequestV1Config from a JSON string
modelmetry_http_request_v1_config_instance = ModelmetryHTTPRequestV1Config.from_json(json)
# print the JSON string representation of the object
print(ModelmetryHTTPRequestV1Config.to_json())

# convert the object into a dict
modelmetry_http_request_v1_config_dict = modelmetry_http_request_v1_config_instance.to_dict()
# create an instance of ModelmetryHTTPRequestV1Config from a dict
modelmetry_http_request_v1_config_from_dict = ModelmetryHTTPRequestV1Config.from_dict(modelmetry_http_request_v1_config_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



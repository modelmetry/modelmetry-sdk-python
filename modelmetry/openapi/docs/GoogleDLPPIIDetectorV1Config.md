# GoogleDLPPIIDetectorV1Config


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**info_types** | **List[str]** | Info types to detect as per Google Cloud DLP&#39;s documentation | 
**minimum_likelihood** | **str** | Threshold for detection | [default to 'LIKELY']

## Example

```python
from modelmetry.openapi.models.google_dlppii_detector_v1_config import GoogleDLPPIIDetectorV1Config

# TODO update the JSON string below
json = "{}"
# create an instance of GoogleDLPPIIDetectorV1Config from a JSON string
google_dlppii_detector_v1_config_instance = GoogleDLPPIIDetectorV1Config.from_json(json)
# print the JSON string representation of the object
print(GoogleDLPPIIDetectorV1Config.to_json())

# convert the object into a dict
google_dlppii_detector_v1_config_dict = google_dlppii_detector_v1_config_instance.to_dict()
# create an instance of GoogleDLPPIIDetectorV1Config from a dict
google_dlppii_detector_v1_config_from_dict = GoogleDLPPIIDetectorV1Config.from_dict(google_dlppii_detector_v1_config_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



# ModelmetrySecretDetectorV1Config


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**custom_patterns** | **Dict[str, str]** | Custom regex patterns to detect secrets | [optional] 

## Example

```python
from modelmetry.openapi.models.modelmetry_secret_detector_v1_config import ModelmetrySecretDetectorV1Config

# TODO update the JSON string below
json = "{}"
# create an instance of ModelmetrySecretDetectorV1Config from a JSON string
modelmetry_secret_detector_v1_config_instance = ModelmetrySecretDetectorV1Config.from_json(json)
# print the JSON string representation of the object
print(ModelmetrySecretDetectorV1Config.to_json())

# convert the object into a dict
modelmetry_secret_detector_v1_config_dict = modelmetry_secret_detector_v1_config_instance.to_dict()
# create an instance of ModelmetrySecretDetectorV1Config from a dict
modelmetry_secret_detector_v1_config_from_dict = ModelmetrySecretDetectorV1Config.from_dict(modelmetry_secret_detector_v1_config_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



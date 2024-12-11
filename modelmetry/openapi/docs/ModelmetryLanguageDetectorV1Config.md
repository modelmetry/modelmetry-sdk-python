# ModelmetryLanguageDetectorV1Config


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**confidence_threshold** | **float** | Minimum confidence threshold for the language detection. If the confidence is lower than this, the evaluation will be skipped. | [default to 0.2]
**word_count_threshold** | **int** | Minimum number of words to check, as the language detection can be unreliable for very short texts. Texts shorter than the minimum will be skipped. | [default to 2]

## Example

```python
from modelmetry.openapi.models.modelmetry_language_detector_v1_config import ModelmetryLanguageDetectorV1Config

# TODO update the JSON string below
json = "{}"
# create an instance of ModelmetryLanguageDetectorV1Config from a JSON string
modelmetry_language_detector_v1_config_instance = ModelmetryLanguageDetectorV1Config.from_json(json)
# print the JSON string representation of the object
print(ModelmetryLanguageDetectorV1Config.to_json())

# convert the object into a dict
modelmetry_language_detector_v1_config_dict = modelmetry_language_detector_v1_config_instance.to_dict()
# create an instance of ModelmetryLanguageDetectorV1Config from a dict
modelmetry_language_detector_v1_config_from_dict = ModelmetryLanguageDetectorV1Config.from_dict(modelmetry_language_detector_v1_config_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



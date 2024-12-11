# ModelmetryJSONValidatorV1Config


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**expected_json_schema** | **str** | The expected JSON schema to validate against | [optional] 

## Example

```python
from modelmetry.openapi.models.modelmetry_json_validator_v1_config import ModelmetryJSONValidatorV1Config

# TODO update the JSON string below
json = "{}"
# create an instance of ModelmetryJSONValidatorV1Config from a JSON string
modelmetry_json_validator_v1_config_instance = ModelmetryJSONValidatorV1Config.from_json(json)
# print the JSON string representation of the object
print(ModelmetryJSONValidatorV1Config.to_json())

# convert the object into a dict
modelmetry_json_validator_v1_config_dict = modelmetry_json_validator_v1_config_instance.to_dict()
# create an instance of ModelmetryJSONValidatorV1Config from a dict
modelmetry_json_validator_v1_config_from_dict = ModelmetryJSONValidatorV1Config.from_dict(modelmetry_json_validator_v1_config_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



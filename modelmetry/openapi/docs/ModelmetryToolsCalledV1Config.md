# ModelmetryToolsCalledV1Config


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**expectations** | **object** |  | [optional] 
**expections** | [**List[ModelmetryToolsCalledV1Expectation]**](ModelmetryToolsCalledV1Expectation.md) | The expected JSON schema to validate against | 

## Example

```python
from modelmetry.openapi.models.modelmetry_tools_called_v1_config import ModelmetryToolsCalledV1Config

# TODO update the JSON string below
json = "{}"
# create an instance of ModelmetryToolsCalledV1Config from a JSON string
modelmetry_tools_called_v1_config_instance = ModelmetryToolsCalledV1Config.from_json(json)
# print the JSON string representation of the object
print(ModelmetryToolsCalledV1Config.to_json())

# convert the object into a dict
modelmetry_tools_called_v1_config_dict = modelmetry_tools_called_v1_config_instance.to_dict()
# create an instance of ModelmetryToolsCalledV1Config from a dict
modelmetry_tools_called_v1_config_from_dict = ModelmetryToolsCalledV1Config.from_dict(modelmetry_tools_called_v1_config_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



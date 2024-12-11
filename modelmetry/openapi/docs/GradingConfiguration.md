# GradingConfiguration


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**assessments** | [**List[Assessment]**](Assessment.md) |  | 

## Example

```python
from modelmetry.openapi.models.grading_configuration import GradingConfiguration

# TODO update the JSON string below
json = "{}"
# create an instance of GradingConfiguration from a JSON string
grading_configuration_instance = GradingConfiguration.from_json(json)
# print the JSON string representation of the object
print(GradingConfiguration.to_json())

# convert the object into a dict
grading_configuration_dict = grading_configuration_instance.to_dict()
# create an instance of GradingConfiguration from a dict
grading_configuration_from_dict = GradingConfiguration.from_dict(grading_configuration_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



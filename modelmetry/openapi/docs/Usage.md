# Usage


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**input** | [**UsageValue**](UsageValue.md) |  | [optional] 
**output** | [**UsageValue**](UsageValue.md) |  | [optional] 
**total** | [**UsageValue**](UsageValue.md) |  | [optional] 

## Example

```python
from modelmetry.openapi.models.usage import Usage

# TODO update the JSON string below
json = "{}"
# create an instance of Usage from a JSON string
usage_instance = Usage.from_json(json)
# print the JSON string representation of the object
print(Usage.to_json())

# convert the object into a dict
usage_dict = usage_instance.to_dict()
# create an instance of Usage from a dict
usage_from_dict = Usage.from_dict(usage_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


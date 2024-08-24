# UsageValue


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**amount** | **float** |  | 
**unit** | **str** |  | [default to 'tokens']

## Example

```python
from modelmetry.openapi.models.usage_value import UsageValue

# TODO update the JSON string below
json = "{}"
# create an instance of UsageValue from a JSON string
usage_value_instance = UsageValue.from_json(json)
# print the JSON string representation of the object
print(UsageValue.to_json())

# convert the object into a dict
usage_value_dict = usage_value_instance.to_dict()
# create an instance of UsageValue from a dict
usage_value_from_dict = UsageValue.from_dict(usage_value_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



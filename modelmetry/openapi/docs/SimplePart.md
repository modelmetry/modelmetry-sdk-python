# SimplePart


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**detail** | **str** |  | [optional] 
**mime_type** | **str** |  | [optional] 
**text** | **str** |  | 
**uri** | **str** |  | [optional] 

## Example

```python
from modelmetry.openapi.models.simple_part import SimplePart

# TODO update the JSON string below
json = "{}"
# create an instance of SimplePart from a JSON string
simple_part_instance = SimplePart.from_json(json)
# print the JSON string representation of the object
print(SimplePart.to_json())

# convert the object into a dict
simple_part_dict = simple_part_instance.to_dict()
# create an instance of SimplePart from a dict
simple_part_from_dict = SimplePart.from_dict(simple_part_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



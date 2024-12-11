# DataPart


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | **str** |  | 
**detail** | **str** |  | [optional] 
**mime_type** | **str** |  | 

## Example

```python
from modelmetry.openapi.models.data_part import DataPart

# TODO update the JSON string below
json = "{}"
# create an instance of DataPart from a JSON string
data_part_instance = DataPart.from_json(json)
# print the JSON string representation of the object
print(DataPart.to_json())

# convert the object into a dict
data_part_dict = data_part_instance.to_dict()
# create an instance of DataPart from a dict
data_part_from_dict = DataPart.from_dict(data_part_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



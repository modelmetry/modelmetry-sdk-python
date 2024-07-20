# RetrievedItem


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**content** | **object** |  | 
**content_type** | **str** |  | 
**identifier** | **str** |  | 
**metadata** | **object** |  | 

## Example

```python
from modelmetry.openapi.models.retrieved_item import RetrievedItem

# TODO update the JSON string below
json = "{}"
# create an instance of RetrievedItem from a JSON string
retrieved_item_instance = RetrievedItem.from_json(json)
# print the JSON string representation of the object
print(RetrievedItem.to_json())

# convert the object into a dict
retrieved_item_dict = retrieved_item_instance.to_dict()
# create an instance of RetrievedItem from a dict
retrieved_item_from_dict = RetrievedItem.from_dict(retrieved_item_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



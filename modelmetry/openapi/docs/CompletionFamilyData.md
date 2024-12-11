# CompletionFamilyData


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**cost** | [**Cost**](Cost.md) |  | [optional] 
**documents** | [**List[Document]**](Document.md) |  | [optional] 
**messages** | [**List[CompletionFamilyDataMessagesInner]**](CompletionFamilyDataMessagesInner.md) |  | [optional] 
**options** | [**Options**](Options.md) |  | [optional] 
**usage** | [**Usage**](Usage.md) |  | [optional] 

## Example

```python
from modelmetry.openapi.models.completion_family_data import CompletionFamilyData

# TODO update the JSON string below
json = "{}"
# create an instance of CompletionFamilyData from a JSON string
completion_family_data_instance = CompletionFamilyData.from_json(json)
# print the JSON string representation of the object
print(CompletionFamilyData.to_json())

# convert the object into a dict
completion_family_data_dict = completion_family_data_instance.to_dict()
# create an instance of CompletionFamilyData from a dict
completion_family_data_from_dict = CompletionFamilyData.from_dict(completion_family_data_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



# CompletionFamilyDataInput

Input for completion

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**text** | **str** |  | 
**messages** | [**List[ChatInputMessagesInner]**](ChatInputMessagesInner.md) |  | 

## Example

```python
from modelmetry.openapi.models.completion_family_data_input import CompletionFamilyDataInput

# TODO update the JSON string below
json = "{}"
# create an instance of CompletionFamilyDataInput from a JSON string
completion_family_data_input_instance = CompletionFamilyDataInput.from_json(json)
# print the JSON string representation of the object
print(CompletionFamilyDataInput.to_json())

# convert the object into a dict
completion_family_data_input_dict = completion_family_data_input_instance.to_dict()
# create an instance of CompletionFamilyDataInput from a dict
completion_family_data_input_from_dict = CompletionFamilyDataInput.from_dict(completion_family_data_input_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



# SimpleOptions


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**frequency_penalty** | **float** |  | [optional] 
**logprobs** | **bool** |  | [optional] 
**max_tokens** | **int** |  | [optional] 
**n** | **int** |  | [optional] 
**presence_penalty** | **float** |  | [optional] 
**seed** | **int** |  | [optional] 
**stream** | **bool** |  | [optional] 
**temperature** | **float** |  | [optional] 
**timeout** | **float** |  | [optional] 
**tool_choice** | **str** |  | [optional] 
**tools** | [**List[Tool]**](Tool.md) |  | [optional] 
**top_logprobs** | **int** |  | [optional] 
**top_p** | **float** |  | [optional] 
**user** | **str** |  | [optional] 

## Example

```python
from modelmetry.openapi.models.simple_options import SimpleOptions

# TODO update the JSON string below
json = "{}"
# create an instance of SimpleOptions from a JSON string
simple_options_instance = SimpleOptions.from_json(json)
# print the JSON string representation of the object
print(SimpleOptions.to_json())

# convert the object into a dict
simple_options_dict = simple_options_instance.to_dict()
# create an instance of SimpleOptions from a dict
simple_options_from_dict = SimpleOptions.from_dict(simple_options_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



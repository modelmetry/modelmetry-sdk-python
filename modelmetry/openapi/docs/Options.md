# Options


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**api_key** | **str** |  | [optional] 
**api_version** | **str** |  | [optional] 
**base_url** | **str** |  | [optional] 
**deployment_id** | **str** |  | [optional] 
**frequency_penalty** | **float** |  | [optional] 
**function_call** | **str** |  | [optional] 
**functions** | **List[str]** |  | [optional] 
**logit_bias** | **object** |  | [optional] 
**logprobs** | **bool** |  | [optional] 
**max_tokens** | **int** |  | [optional] 
**model** | **str** |  | [optional] 
**model_list** | **List[str]** |  | [optional] 
**n** | **int** |  | [optional] 
**presence_penalty** | **float** |  | [optional] 
**provider** | **str** |  | [optional] 
**response_format** | **object** |  | [optional] 
**seed** | **int** |  | [optional] 
**stop** | **object** |  | [optional] 
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
from modelmetry.openapi.models.options import Options

# TODO update the JSON string below
json = "{}"
# create an instance of Options from a JSON string
options_instance = Options.from_json(json)
# print the JSON string representation of the object
print(Options.to_json())

# convert the object into a dict
options_dict = options_instance.to_dict()
# create an instance of Options from a dict
options_from_dict = Options.from_dict(options_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



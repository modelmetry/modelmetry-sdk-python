# AzurePromptShieldsV1Config


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**endpoint** | **str** | The endpoint of the Azure Prompt Shields API. | 

## Example

```python
from modelmetry.openapi.models.azure_prompt_shields_v1_config import AzurePromptShieldsV1Config

# TODO update the JSON string below
json = "{}"
# create an instance of AzurePromptShieldsV1Config from a JSON string
azure_prompt_shields_v1_config_instance = AzurePromptShieldsV1Config.from_json(json)
# print the JSON string representation of the object
print(AzurePromptShieldsV1Config.to_json())

# convert the object into a dict
azure_prompt_shields_v1_config_dict = azure_prompt_shields_v1_config_instance.to_dict()
# create an instance of AzurePromptShieldsV1Config from a dict
azure_prompt_shields_v1_config_from_dict = AzurePromptShieldsV1Config.from_dict(azure_prompt_shields_v1_config_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



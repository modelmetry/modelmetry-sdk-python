# ModelmetryBooleanLLMAsJudgeV1Config


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**finding_name** | **str** | The name of the finding to use for this evaluator&#39;s boolean output (e.g., is_threatening, is_about_hotels). | 
**instructions** | **str** | You are an LLM evaluator. We need the guarantee that the output answers what is being asked on the input, please evaluate as False if it doesn&#39;t. | 
**max_tokens** | **int** | The limit on the number of tokens the entire prompt can be. | [default to 8192]
**model** | **str** | The model to use. | [default to 'openai/gpt-4o-mini']

## Example

```python
from modelmetry.openapi.models.modelmetry_boolean_llmas_judge_v1_config import ModelmetryBooleanLLMAsJudgeV1Config

# TODO update the JSON string below
json = "{}"
# create an instance of ModelmetryBooleanLLMAsJudgeV1Config from a JSON string
modelmetry_boolean_llmas_judge_v1_config_instance = ModelmetryBooleanLLMAsJudgeV1Config.from_json(json)
# print the JSON string representation of the object
print(ModelmetryBooleanLLMAsJudgeV1Config.to_json())

# convert the object into a dict
modelmetry_boolean_llmas_judge_v1_config_dict = modelmetry_boolean_llmas_judge_v1_config_instance.to_dict()
# create an instance of ModelmetryBooleanLLMAsJudgeV1Config from a dict
modelmetry_boolean_llmas_judge_v1_config_from_dict = ModelmetryBooleanLLMAsJudgeV1Config.from_dict(modelmetry_boolean_llmas_judge_v1_config_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



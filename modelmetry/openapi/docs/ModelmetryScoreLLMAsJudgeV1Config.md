# ModelmetryScoreLLMAsJudgeV1Config


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**finding_name** | **str** | The name of the finding to use for the result (e.g., threatening_level, about_hotel_score). | 
**instructions** | **str** | You are an LLM evaluator. Please score from 0.0 to 1.0 how likely the user is to be satisfied with this answer, from 0.0 being not satisfied at all to 1.0 being completely satisfied. | 
**max_tokens** | **int** | The limit on the number of tokens the entire prompt can be. | [default to 8192]
**model** | **str** | The model to use. | [default to 'openai/gpt-4o-mini']

## Example

```python
from modelmetry.openapi.models.modelmetry_score_llmas_judge_v1_config import ModelmetryScoreLLMAsJudgeV1Config

# TODO update the JSON string below
json = "{}"
# create an instance of ModelmetryScoreLLMAsJudgeV1Config from a JSON string
modelmetry_score_llmas_judge_v1_config_instance = ModelmetryScoreLLMAsJudgeV1Config.from_json(json)
# print the JSON string representation of the object
print(ModelmetryScoreLLMAsJudgeV1Config.to_json())

# convert the object into a dict
modelmetry_score_llmas_judge_v1_config_dict = modelmetry_score_llmas_judge_v1_config_instance.to_dict()
# create an instance of ModelmetryScoreLLMAsJudgeV1Config from a dict
modelmetry_score_llmas_judge_v1_config_from_dict = ModelmetryScoreLLMAsJudgeV1Config.from_dict(modelmetry_score_llmas_judge_v1_config_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



# ModelmetrySentimentAnalysisV1Config


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**model** | **str** | The model to use. | [default to 'openai/gpt-4o-mini']
**scope** | **str** |  | 

## Example

```python
from modelmetry.openapi.models.modelmetry_sentiment_analysis_v1_config import ModelmetrySentimentAnalysisV1Config

# TODO update the JSON string below
json = "{}"
# create an instance of ModelmetrySentimentAnalysisV1Config from a JSON string
modelmetry_sentiment_analysis_v1_config_instance = ModelmetrySentimentAnalysisV1Config.from_json(json)
# print the JSON string representation of the object
print(ModelmetrySentimentAnalysisV1Config.to_json())

# convert the object into a dict
modelmetry_sentiment_analysis_v1_config_dict = modelmetry_sentiment_analysis_v1_config_instance.to_dict()
# create an instance of ModelmetrySentimentAnalysisV1Config from a dict
modelmetry_sentiment_analysis_v1_config_from_dict = ModelmetrySentimentAnalysisV1Config.from_dict(modelmetry_sentiment_analysis_v1_config_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



# ModelmetryCompetitorBlocklistV1Config


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**case_sensitivity** | **str** | Whether to consider the word&#39;s case when matching strings | [default to 'sensitive']
**competitors** | **List[str]** | List of competitors to search for | 
**look_in** | **str** | Where to search for competitor mentions | [default to '*']

## Example

```python
from modelmetry.openapi.models.modelmetry_competitor_blocklist_v1_config import ModelmetryCompetitorBlocklistV1Config

# TODO update the JSON string below
json = "{}"
# create an instance of ModelmetryCompetitorBlocklistV1Config from a JSON string
modelmetry_competitor_blocklist_v1_config_instance = ModelmetryCompetitorBlocklistV1Config.from_json(json)
# print the JSON string representation of the object
print(ModelmetryCompetitorBlocklistV1Config.to_json())

# convert the object into a dict
modelmetry_competitor_blocklist_v1_config_dict = modelmetry_competitor_blocklist_v1_config_instance.to_dict()
# create an instance of ModelmetryCompetitorBlocklistV1Config from a dict
modelmetry_competitor_blocklist_v1_config_from_dict = ModelmetryCompetitorBlocklistV1Config.from_dict(modelmetry_competitor_blocklist_v1_config_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



# GoogleTextModerationV1Config


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**attributes** | **List[str]** | The attributes to check for. An empty list will check for all attributes. | [default to []]

## Example

```python
from modelmetry.openapi.models.google_text_moderation_v1_config import GoogleTextModerationV1Config

# TODO update the JSON string below
json = "{}"
# create an instance of GoogleTextModerationV1Config from a JSON string
google_text_moderation_v1_config_instance = GoogleTextModerationV1Config.from_json(json)
# print the JSON string representation of the object
print(GoogleTextModerationV1Config.to_json())

# convert the object into a dict
google_text_moderation_v1_config_dict = google_text_moderation_v1_config_instance.to_dict()
# create an instance of GoogleTextModerationV1Config from a dict
google_text_moderation_v1_config_from_dict = GoogleTextModerationV1Config.from_dict(google_text_moderation_v1_config_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



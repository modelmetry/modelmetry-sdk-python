# CreateSessionParams


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**attributes** | **object** |  | [optional] 
**name** | **str** |  | [optional] 
**xid** | **str** |  | 

## Example

```python
from modelmetry.openapi.models.create_session_params import CreateSessionParams

# TODO update the JSON string below
json = "{}"
# create an instance of CreateSessionParams from a JSON string
create_session_params_instance = CreateSessionParams.from_json(json)
# print the JSON string representation of the object
print(CreateSessionParams.to_json())

# convert the object into a dict
create_session_params_dict = create_session_params_instance.to_dict()
# create an instance of CreateSessionParams from a dict
create_session_params_from_dict = CreateSessionParams.from_dict(create_session_params_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



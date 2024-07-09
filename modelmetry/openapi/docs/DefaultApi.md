# modelmetry.openapi.DefaultApi

All URIs are relative to *http://api.modelmetry.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**call_guardrail**](DefaultApi.md#call_guardrail) | **POST** /calls | CallGuardrail


# **call_guardrail**
> Call call_guardrail(call_guardrail_request_body, dryrun=dryrun)

CallGuardrail

### Example

* Api Key Authentication (apikeyAuth):

```python
import modelmetry.openapi
from modelmetry.openapi.models.call import Call
from modelmetry.openapi.models.call_guardrail_request_body import CallGuardrailRequestBody
from modelmetry.openapi.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://api.modelmetry.com
# See configuration.py for a list of all supported configuration parameters.
configuration = modelmetry.openapi.Configuration(
    host = "http://api.modelmetry.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: apikeyAuth
configuration.api_key['apikeyAuth'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['apikeyAuth'] = 'Bearer'

# Enter a context with an instance of the API client
with modelmetry.openapi.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = modelmetry.openapi.DefaultApi(api_client)
    call_guardrail_request_body = modelmetry.openapi.CallGuardrailRequestBody() # CallGuardrailRequestBody | 
    dryrun = True # bool |  (optional)

    try:
        # CallGuardrail
        api_response = api_instance.call_guardrail(call_guardrail_request_body, dryrun=dryrun)
        print("The response of DefaultApi->call_guardrail:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DefaultApi->call_guardrail: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **call_guardrail_request_body** | [**CallGuardrailRequestBody**](CallGuardrailRequestBody.md)|  | 
 **dryrun** | **bool**|  | [optional] 

### Return type

[**Call**](Call.md)

### Authorization

[apikeyAuth](../README.md#apikeyAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json, application/problem+json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**0** | Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)


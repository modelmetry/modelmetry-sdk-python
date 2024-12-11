# modelmetry.openapi.DefaultApi

All URIs are relative to *http://api.modelmetry.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**check_payload**](DefaultApi.md#check_payload) | **POST** /checks | Check payload
[**evaluate**](DefaultApi.md#evaluate) | **POST** /evaluations | Evaluate
[**ingest_signals_v1**](DefaultApi.md#ingest_signals_v1) | **POST** /signals/ingest/v1 | Ingest signals v1


# **check_payload**
> GuardrailCheck check_payload(check_payload_request_body, dryrun=dryrun)

Check payload

### Example

* Api Key Authentication (apikeyAuth):

```python
import modelmetry.openapi
from modelmetry.openapi.models.check_payload_request_body import CheckPayloadRequestBody
from modelmetry.openapi.models.guardrail_check import GuardrailCheck
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
    check_payload_request_body = modelmetry.openapi.CheckPayloadRequestBody() # CheckPayloadRequestBody | 
    dryrun = True # bool |  (optional)

    try:
        # Check payload
        api_response = api_instance.check_payload(check_payload_request_body, dryrun=dryrun)
        print("The response of DefaultApi->check_payload:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DefaultApi->check_payload: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **check_payload_request_body** | [**CheckPayloadRequestBody**](CheckPayloadRequestBody.md)|  | 
 **dryrun** | **bool**|  | [optional] 

### Return type

[**GuardrailCheck**](GuardrailCheck.md)

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

# **evaluate**
> Entry evaluate(evaluate_request_body)

Evaluate

### Example

* Api Key Authentication (apikeyAuth):

```python
import modelmetry.openapi
from modelmetry.openapi.models.entry import Entry
from modelmetry.openapi.models.evaluate_request_body import EvaluateRequestBody
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
    evaluate_request_body = modelmetry.openapi.EvaluateRequestBody() # EvaluateRequestBody | 

    try:
        # Evaluate
        api_response = api_instance.evaluate(evaluate_request_body)
        print("The response of DefaultApi->evaluate:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DefaultApi->evaluate: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **evaluate_request_body** | [**EvaluateRequestBody**](EvaluateRequestBody.md)|  | 

### Return type

[**Entry**](Entry.md)

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

# **ingest_signals_v1**
> IngestSignalsV1ResponseBody ingest_signals_v1(ingest_signals_v1_request_body)

Ingest signals v1

### Example

* Api Key Authentication (apikeyAuth):

```python
import modelmetry.openapi
from modelmetry.openapi.models.ingest_signals_v1_request_body import IngestSignalsV1RequestBody
from modelmetry.openapi.models.ingest_signals_v1_response_body import IngestSignalsV1ResponseBody
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
    ingest_signals_v1_request_body = modelmetry.openapi.IngestSignalsV1RequestBody() # IngestSignalsV1RequestBody | 

    try:
        # Ingest signals v1
        api_response = api_instance.ingest_signals_v1(ingest_signals_v1_request_body)
        print("The response of DefaultApi->ingest_signals_v1:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DefaultApi->ingest_signals_v1: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **ingest_signals_v1_request_body** | [**IngestSignalsV1RequestBody**](IngestSignalsV1RequestBody.md)|  | 

### Return type

[**IngestSignalsV1ResponseBody**](IngestSignalsV1ResponseBody.md)

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


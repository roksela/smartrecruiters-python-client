# smartrecruiters_python_client.OffersApi

All URIs are relative to *https://api.smartrecruiters.com/*

Method | HTTP request | Description
------------- | ------------- | -------------
[**candidates_offers_all**](OffersApi.md#candidates_offers_all) | **GET** /candidates/{id}/jobs/{jobId}/offers | Get candidate&#39;s offers
[**candidates_offers_find**](OffersApi.md#candidates_offers_find) | **GET** /offers | Search offers
[**candidates_offers_get**](OffersApi.md#candidates_offers_get) | **GET** /candidates/{id}/jobs/{jobId}/offers/{offerId} | Get candidate&#39;s offer


# **candidates_offers_all**
> Offers candidates_offers_all(id, job_id)

Get candidate's offers

### Example 
```python
from __future__ import print_statement
import time
import smartrecruiters_python_client
from smartrecruiters_python_client.rest import ApiException
from pprint import pprint

# Configure API key authorization: key
smartrecruiters_python_client.configuration.api_key['x-smarttoken'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# smartrecruiters_python_client.configuration.api_key_prefix['x-smarttoken'] = 'Bearer'

# create an instance of the API class
api_instance = smartrecruiters_python_client.OffersApi()
id = 'id_example' # str | Identifier of a Candidate
job_id = 'job_id_example' # str | Identifier of a Job

try: 
    # Get candidate's offers
    api_response = api_instance.candidates_offers_all(id, job_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling OffersApi->candidates_offers_all: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Identifier of a Candidate | 
 **job_id** | **str**| Identifier of a Job | 

### Return type

[**Offers**](Offers.md)

### Authorization

[key](../README.md#key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json; charset=utf-8

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **candidates_offers_find**
> Offers candidates_offers_find(limit=limit, offset=offset, created_after=created_after, created_before=created_before, age=age, status=status)

Search offers

### Example 
```python
from __future__ import print_statement
import time
import smartrecruiters_python_client
from smartrecruiters_python_client.rest import ApiException
from pprint import pprint

# Configure API key authorization: key
smartrecruiters_python_client.configuration.api_key['x-smarttoken'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# smartrecruiters_python_client.configuration.api_key_prefix['x-smarttoken'] = 'Bearer'

# create an instance of the API class
api_instance = smartrecruiters_python_client.OffersApi()
limit = 10 # int | number of elements to return. max value is 100 (optional) (default to 10)
offset = 0 # int | number of elements to skip while processing result (optional) (default to 0)
created_after = '2013-10-20T19:20:30+01:00' # datetime | ISO8601-formatted time boundaries for the offer creation time, Format: yyyy-MM-ddTHH:mm:ss.SSSZZ (optional)
created_before = '2013-10-20T19:20:30+01:00' # datetime | ISO8601-formatted time boundaries for the offer creation time, Format: yyyy-MM-ddTHH:mm:ss.SSSZZ (optional)
age = 'age_example' # str | word-based offer age; when age is specified createdAfter and createdBefore are ignored, Examples: 10 days, 7 hours, 1 week, etc. (optional)
status = ['status_example'] # list[str] | offer states that need to be included in the results; by default all states are included (optional)

try: 
    # Search offers
    api_response = api_instance.candidates_offers_find(limit=limit, offset=offset, created_after=created_after, created_before=created_before, age=age, status=status)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling OffersApi->candidates_offers_find: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **limit** | **int**| number of elements to return. max value is 100 | [optional] [default to 10]
 **offset** | **int**| number of elements to skip while processing result | [optional] [default to 0]
 **created_after** | **datetime**| ISO8601-formatted time boundaries for the offer creation time, Format: yyyy-MM-ddTHH:mm:ss.SSSZZ | [optional] 
 **created_before** | **datetime**| ISO8601-formatted time boundaries for the offer creation time, Format: yyyy-MM-ddTHH:mm:ss.SSSZZ | [optional] 
 **age** | **str**| word-based offer age; when age is specified createdAfter and createdBefore are ignored, Examples: 10 days, 7 hours, 1 week, etc. | [optional] 
 **status** | [**list[str]**](str.md)| offer states that need to be included in the results; by default all states are included | [optional] 

### Return type

[**Offers**](Offers.md)

### Authorization

[key](../README.md#key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json; charset=utf-8

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **candidates_offers_get**
> Offer candidates_offers_get(id, job_id, offer_id)

Get candidate's offer

### Example 
```python
from __future__ import print_statement
import time
import smartrecruiters_python_client
from smartrecruiters_python_client.rest import ApiException
from pprint import pprint

# Configure API key authorization: key
smartrecruiters_python_client.configuration.api_key['x-smarttoken'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# smartrecruiters_python_client.configuration.api_key_prefix['x-smarttoken'] = 'Bearer'

# create an instance of the API class
api_instance = smartrecruiters_python_client.OffersApi()
id = 'id_example' # str | Identifier of a Candidate
job_id = 'job_id_example' # str | Identifier of a Job
offer_id = 'offer_id_example' # str | Identifier of a Offer

try: 
    # Get candidate's offer
    api_response = api_instance.candidates_offers_get(id, job_id, offer_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling OffersApi->candidates_offers_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Identifier of a Candidate | 
 **job_id** | **str**| Identifier of a Job | 
 **offer_id** | **str**| Identifier of a Offer | 

### Return type

[**Offer**](Offer.md)

### Authorization

[key](../README.md#key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json; charset=utf-8

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)


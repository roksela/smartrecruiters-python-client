# smartrecruiters_python_client.AnalyticsApi

All URIs are relative to *https://api.smartrecruiters.com/*

Method | HTTP request | Description
------------- | ------------- | -------------
[**analytics_applications**](AnalyticsApi.md#analytics_applications) | **GET** /analytics/applications | Get the list of applications.
[**analytics_hiring_team**](AnalyticsApi.md#analytics_hiring_team) | **GET** /analytics/hiring-team | Get the list of hiring team members.
[**analytics_interviews**](AnalyticsApi.md#analytics_interviews) | **GET** /analytics/interviews | Get the list of interviews.
[**analytics_job_fields**](AnalyticsApi.md#analytics_job_fields) | **GET** /analytics/job-fields | Get the list of job fields.
[**analytics_jobs**](AnalyticsApi.md#analytics_jobs) | **GET** /analytics/jobs | Get the list of jobs.
[**analytics_positions**](AnalyticsApi.md#analytics_positions) | **GET** /analytics/positions | Get the list of job positions.


# **analytics_applications**
> ApplicationsReport analytics_applications(date_format=date_format)

Get the list of applications.

Get the list of applications. Fore more comprehensive description see [Analytics API](https://dev.smartrecruiters.com/customer-api/analytics-api/) and [Applications Data Service](https://dev.smartrecruiters.com/customer-api/analytics-api/applications-data-service/). 

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
api_instance = smartrecruiters_python_client.AnalyticsApi()
date_format = 'yyyy-MM-dd'T'HH:mm:ss' # str | Defines response date format (optional) (default to yyyy-MM-dd'T'HH:mm:ss)

try: 
    # Get the list of applications.
    api_response = api_instance.analytics_applications(date_format=date_format)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AnalyticsApi->analytics_applications: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **date_format** | **str**| Defines response date format | [optional] [default to yyyy-MM-dd&#39;T&#39;HH:mm:ss]

### Return type

[**ApplicationsReport**](ApplicationsReport.md)

### Authorization

[key](../README.md#key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json; charset=utf-8, text/csv

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **analytics_hiring_team**
> HiringTeamReport analytics_hiring_team()

Get the list of hiring team members.

Get the list of hiring team members. Fore more comprehensive description see [Analytics API](https://dev.smartrecruiters.com/customer-api/analytics-api/) and [Hiring Team Data Service](https://dev.smartrecruiters.com/customer-api/analytics-api/hiring-team-data-service/). 

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
api_instance = smartrecruiters_python_client.AnalyticsApi()

try: 
    # Get the list of hiring team members.
    api_response = api_instance.analytics_hiring_team()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AnalyticsApi->analytics_hiring_team: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**HiringTeamReport**](HiringTeamReport.md)

### Authorization

[key](../README.md#key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json; charset=utf-8, text/csv

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **analytics_interviews**
> InterviewsReport analytics_interviews(date_format=date_format)

Get the list of interviews.

Get the list of interviews. Fore more comprehensive description see [Analytics API](https://dev.smartrecruiters.com/customer-api/analytics-api/) and [Interviews Data Service](https://dev.smartrecruiters.com/customer-api/analytics-api/interviews-data-service/). 

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
api_instance = smartrecruiters_python_client.AnalyticsApi()
date_format = 'yyyy-MM-dd'T'HH:mm:ss' # str | Defines response date format (optional) (default to yyyy-MM-dd'T'HH:mm:ss)

try: 
    # Get the list of interviews.
    api_response = api_instance.analytics_interviews(date_format=date_format)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AnalyticsApi->analytics_interviews: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **date_format** | **str**| Defines response date format | [optional] [default to yyyy-MM-dd&#39;T&#39;HH:mm:ss]

### Return type

[**InterviewsReport**](InterviewsReport.md)

### Authorization

[key](../README.md#key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json; charset=utf-8, text/csv

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **analytics_job_fields**
> JobFieldsReport analytics_job_fields()

Get the list of job fields.

Get the list of job fields. Fore more comprehensive description see [Analytics API](https://dev.smartrecruiters.com/customer-api/analytics-api/) and [Job Fields Data Service](https://dev.smartrecruiters.com/customer-api/analytics-api/job-fields-data-service/). 

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
api_instance = smartrecruiters_python_client.AnalyticsApi()

try: 
    # Get the list of job fields.
    api_response = api_instance.analytics_job_fields()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AnalyticsApi->analytics_job_fields: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**JobFieldsReport**](JobFieldsReport.md)

### Authorization

[key](../README.md#key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json; charset=utf-8, text/csv

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **analytics_jobs**
> JobsReport analytics_jobs(date_format=date_format)

Get the list of jobs.

Get the list of jobs. Fore more comprehensive description see [Analytics API](https://dev.smartrecruiters.com/customer-api/analytics-api/) and [Jobs Data Service](https://dev.smartrecruiters.com/customer-api/analytics-api/jobs-data-service/). 

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
api_instance = smartrecruiters_python_client.AnalyticsApi()
date_format = 'yyyy-MM-dd'T'HH:mm:ss' # str | Defines response date format (optional) (default to yyyy-MM-dd'T'HH:mm:ss)

try: 
    # Get the list of jobs.
    api_response = api_instance.analytics_jobs(date_format=date_format)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AnalyticsApi->analytics_jobs: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **date_format** | **str**| Defines response date format | [optional] [default to yyyy-MM-dd&#39;T&#39;HH:mm:ss]

### Return type

[**JobsReport**](JobsReport.md)

### Authorization

[key](../README.md#key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json; charset=utf-8, text/csv

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **analytics_positions**
> PositionsReport analytics_positions(date_format=date_format)

Get the list of job positions.

Get the list of job positions. Fore more comprehensive description see [Analytics API](https://dev.smartrecruiters.com/customer-api/analytics-api/) and [Positions Data Service](https://dev.smartrecruiters.com/customer-api/analytics-api/positions/). 

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
api_instance = smartrecruiters_python_client.AnalyticsApi()
date_format = 'yyyy-MM-dd'T'HH:mm:ss' # str | Defines response date format (optional) (default to yyyy-MM-dd'T'HH:mm:ss)

try: 
    # Get the list of job positions.
    api_response = api_instance.analytics_positions(date_format=date_format)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AnalyticsApi->analytics_positions: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **date_format** | **str**| Defines response date format | [optional] [default to yyyy-MM-dd&#39;T&#39;HH:mm:ss]

### Return type

[**PositionsReport**](PositionsReport.md)

### Authorization

[key](../README.md#key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json; charset=utf-8, text/csv

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)


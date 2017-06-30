# smartrecruiters_python_client.PostingsApi

All URIs are relative to *https://api.smartrecruiters.com/*

Method | HTTP request | Description
------------- | ------------- | -------------
[**v1_get_posting**](PostingsApi.md#v1_get_posting) | **GET** /v1/companies/{companyIdentifier}/postings/{postingId} | Get posting by posting id for given company
[**v1_list_departments**](PostingsApi.md#v1_list_departments) | **GET** /v1/companies/{companyIdentifier}/departments | List departments for given company
[**v1_list_postings**](PostingsApi.md#v1_list_postings) | **GET** /v1/companies/{companyIdentifier}/postings | Lists active postings published by given company


# **v1_get_posting**
> Posting v1_get_posting(company_identifier, posting_id, source_type_id=source_type_id, source_id=source_id)

Get posting by posting id for given company

Note: In order to update content of a job posting available via the Posting API, you need to re-post the job in SmartRecruiters application.

### Example 
```python
from __future__ import print_statement
import time
import smartrecruiters_python_client
from smartrecruiters_python_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = smartrecruiters_python_client.PostingsApi()
company_identifier = 'company_identifier_example' # str | Identifier of a company
posting_id = 'posting_id_example' # str | Posting identifier
source_type_id = 'source_type_id_example' # str | sourceTypeId can be retrieved using [get /configuration/sources](https://dev.smartrecruiters.com/customer-api/live-docs/#!/configuration/configuration_getSourceTypes) endpoint. Used together with **sourceId** to add source tracking parameter to **applyUrl**. (optional)
source_id = 'source_id_example' # str | sourceId can be retrieved using [get /configuration/sources/{sourceType}/values](https://dev.smartrecruiters.com/customer-api/live-docs/#!/configuration/configuration_getSources) endpoint. Used together with **sourceTypeId** to add source tracking parameter to **applyUrl**. (optional)

try: 
    # Get posting by posting id for given company
    api_response = api_instance.v1_get_posting(company_identifier, posting_id, source_type_id=source_type_id, source_id=source_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PostingsApi->v1_get_posting: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **company_identifier** | **str**| Identifier of a company | 
 **posting_id** | **str**| Posting identifier | 
 **source_type_id** | **str**| sourceTypeId can be retrieved using [get /configuration/sources](https://dev.smartrecruiters.com/customer-api/live-docs/#!/configuration/configuration_getSourceTypes) endpoint. Used together with **sourceId** to add source tracking parameter to **applyUrl**. | [optional] 
 **source_id** | **str**| sourceId can be retrieved using [get /configuration/sources/{sourceType}/values](https://dev.smartrecruiters.com/customer-api/live-docs/#!/configuration/configuration_getSources) endpoint. Used together with **sourceTypeId** to add source tracking parameter to **applyUrl**. | [optional] 

### Return type

[**Posting**](Posting.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json; charset=utf-8

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **v1_list_departments**
> Departments v1_list_departments(company_identifier)

List departments for given company

List departments for given company.

### Example 
```python
from __future__ import print_statement
import time
import smartrecruiters_python_client
from smartrecruiters_python_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = smartrecruiters_python_client.PostingsApi()
company_identifier = 'company_identifier_example' # str | Identifier of a company

try: 
    # List departments for given company
    api_response = api_instance.v1_list_departments(company_identifier)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PostingsApi->v1_list_departments: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **company_identifier** | **str**| Identifier of a company | 

### Return type

[**Departments**](Departments.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json; charset=utf-8

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **v1_list_postings**
> PostingList v1_list_postings(company_identifier, q=q, limit=limit, offset=offset, destination=destination, country=country, region=region, city=city, department=department, language=language)

Lists active postings published by given company

Lists active postings published by given company. Return PostingList

### Example 
```python
from __future__ import print_statement
import time
import smartrecruiters_python_client
from smartrecruiters_python_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = smartrecruiters_python_client.PostingsApi()
company_identifier = 'company_identifier_example' # str | Identifier of a company
q = 'q_example' # str | full-text search query based on a job title, location (optional)
limit = 56 # int | number of elements to return. max value is 100 (optional)
offset = 56 # int | number of elements to skip while processing result (optional)
destination = 'destination_example' # str | Filter indicating which postings to return: * **PUBLIC**: response will include ONLY public postings * **INTERNAL**: response will include ONLY internal postings * **INTERNAL_OR_PUBLIC**: response will include internal postings or public postings, but not both for a single job. If a job has both types of postings, only internal postings will be returned  (optional)
country = 'country_example' # str | country code filter (part of the location object) (optional)
region = 'region_example' # str | region filter (part of the location object) (optional)
city = 'city_example' # str | city filter (part of the location object) (optional)
department = 'department_example' # str | department filter (department id) (optional)
language = ['language_example'] # list[str] | Exceptions to the language code ISO format: * \"en-GB\" - \"English - English (UK)\" * \"fr-CA\" - \"French - français (Canada)\" * \"pt-BR\" - \"Portugal - português (Brasil)\" * \"pt-PT\" - \"Portugal - português (Portugal)\" * \"zh-HK\" - \"Chinese (Traditional) - 中文 (香港)\" * \"zh-CN\" - \"Chinese (Simplified) - 中文 (简体)\"  (optional)

try: 
    # Lists active postings published by given company
    api_response = api_instance.v1_list_postings(company_identifier, q=q, limit=limit, offset=offset, destination=destination, country=country, region=region, city=city, department=department, language=language)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PostingsApi->v1_list_postings: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **company_identifier** | **str**| Identifier of a company | 
 **q** | **str**| full-text search query based on a job title, location | [optional] 
 **limit** | **int**| number of elements to return. max value is 100 | [optional] 
 **offset** | **int**| number of elements to skip while processing result | [optional] 
 **destination** | **str**| Filter indicating which postings to return: * **PUBLIC**: response will include ONLY public postings * **INTERNAL**: response will include ONLY internal postings * **INTERNAL_OR_PUBLIC**: response will include internal postings or public postings, but not both for a single job. If a job has both types of postings, only internal postings will be returned  | [optional] 
 **country** | **str**| country code filter (part of the location object) | [optional] 
 **region** | **str**| region filter (part of the location object) | [optional] 
 **city** | **str**| city filter (part of the location object) | [optional] 
 **department** | **str**| department filter (department id) | [optional] 
 **language** | [**list[str]**](str.md)| Exceptions to the language code ISO format: * \&quot;en-GB\&quot; - \&quot;English - English (UK)\&quot; * \&quot;fr-CA\&quot; - \&quot;French - français (Canada)\&quot; * \&quot;pt-BR\&quot; - \&quot;Portugal - português (Brasil)\&quot; * \&quot;pt-PT\&quot; - \&quot;Portugal - português (Portugal)\&quot; * \&quot;zh-HK\&quot; - \&quot;Chinese (Traditional) - 中文 (香港)\&quot; * \&quot;zh-CN\&quot; - \&quot;Chinese (Simplified) - 中文 (简体)\&quot;  | [optional] 

### Return type

[**PostingList**](PostingList.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json; charset=utf-8

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)


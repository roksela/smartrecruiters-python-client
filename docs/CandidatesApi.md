# smartrecruiters_python_client.CandidatesApi

All URIs are relative to *https://api.smartrecruiters.com/*

Method | HTTP request | Description
------------- | ------------- | -------------
[**candidates_add**](CandidatesApi.md#candidates_add) | **POST** /candidates | Create a new candidate and assign to a Talent Pool
[**candidates_add_to_job**](CandidatesApi.md#candidates_add_to_job) | **POST** /jobs/{jobId}/candidates | Create a new candidate and assign to a job
[**candidates_all**](CandidatesApi.md#candidates_all) | **GET** /candidates | Search candidates
[**candidates_attachments_add**](CandidatesApi.md#candidates_attachments_add) | **POST** /candidates/{id}/attachments | Attach files to a candidate.
[**candidates_attachments_get**](CandidatesApi.md#candidates_attachments_get) | **GET** /candidates/{id}/attachments/{attachmentId} | Get a candidate&#39;s attachment.
[**candidates_attachments_list**](CandidatesApi.md#candidates_attachments_list) | **GET** /candidates/{id}/attachments | Get list candidate&#39;s attachments.
[**candidates_delete**](CandidatesApi.md#candidates_delete) | **DELETE** /candidates/{id} | Delete Candidate
[**candidates_get**](CandidatesApi.md#candidates_get) | **GET** /candidates/{id} | Get details of a candidate
[**candidates_onboarding_get**](CandidatesApi.md#candidates_onboarding_get) | **GET** /candidates/{id}/onboardingStatus | Get Onboarding Status for a candidate
[**candidates_onboarding_get_for_job**](CandidatesApi.md#candidates_onboarding_get_for_job) | **GET** /candidates/{id}/jobs/{jobId}/onboardingStatus | Get Onboarding Status for a candidate associated with given job
[**candidates_onboarding_update**](CandidatesApi.md#candidates_onboarding_update) | **PUT** /candidates/{id}/onboardingStatus | Set Onboarding Status for a candidate
[**candidates_onboarding_update_for_job**](CandidatesApi.md#candidates_onboarding_update_for_job) | **PUT** /candidates/{id}/jobs/{jobId}/onboardingStatus | Sets Onboarding Status for a candidate associated with given job
[**candidates_properties_get**](CandidatesApi.md#candidates_properties_get) | **GET** /candidates/{id}/properties | Get candidate property values for a candidate
[**candidates_properties_get_for_job**](CandidatesApi.md#candidates_properties_get_for_job) | **GET** /candidates/{id}/jobs/{jobId}/properties | Get candidate property values for a candidate&#39;s job
[**candidates_properties_values_update**](CandidatesApi.md#candidates_properties_values_update) | **PUT** /candidates/{id}/properties/{propertyId} | Add/update candidate property value
[**candidates_properties_values_update_for_job**](CandidatesApi.md#candidates_properties_values_update_for_job) | **PUT** /candidates/{id}/jobs/{jobId}/properties/{propertyId} | Add/update candidate property value
[**candidates_resume_add**](CandidatesApi.md#candidates_resume_add) | **POST** /candidates/cv | Parse a resume, create a candidate and assign to a Talent Pool.
[**candidates_resume_add_to_job**](CandidatesApi.md#candidates_resume_add_to_job) | **POST** /jobs/{jobId}/candidates/cv | Parse a resume, create a candidate and assign to a job.
[**candidates_screening_answers_get**](CandidatesApi.md#candidates_screening_answers_get) | **GET** /candidates/{id}/jobs/{jobId}/screening-answers | Get candidate screening answers for a candidate&#39;s job
[**candidates_source_update**](CandidatesApi.md#candidates_source_update) | **PUT** /candidates/{id}/jobs/{jobId}/source | Update a candidate&#39;s source
[**candidates_status_history_get**](CandidatesApi.md#candidates_status_history_get) | **GET** /candidates/{id}/status/history | Get candidate&#39;s status history
[**candidates_status_update**](CandidatesApi.md#candidates_status_update) | **PUT** /candidates/{id}/jobs/{jobId}/status | Update a candidate&#39;s status
[**candidates_status_update_primary**](CandidatesApi.md#candidates_status_update_primary) | **PUT** /candidates/{id}/status | Update a candidate&#39;s status on primary assignment
[**candidates_tags_add**](CandidatesApi.md#candidates_tags_add) | **POST** /candidates/{id}/tags | Add tags to a candidate
[**candidates_tags_delete**](CandidatesApi.md#candidates_tags_delete) | **DELETE** /candidates/{id}/tags | Delete tags for a candidate
[**candidates_tags_get**](CandidatesApi.md#candidates_tags_get) | **GET** /candidates/{id}/tags | Get tags for a candidate
[**candidates_tags_replace**](CandidatesApi.md#candidates_tags_replace) | **PUT** /candidates/{id}/tags | Update tags for a candidate
[**candidates_update**](CandidatesApi.md#candidates_update) | **PATCH** /candidates/{id} | Update candidate personal information


# **candidates_add**
> CandidateDetails candidates_add(candidate)

Create a new candidate and assign to a Talent Pool

Create a new candidate and assign to a Talent Pool.  **Tracking candidate source**  When adding a new candidate, it's very important you track its source appropriately. In order to associate a source with your app/integration, add below object to a candidate body object for this endpoint: ``` {   \"sourceDetails\": {     \"sourceTypeId\": \"string\",     \"sourceSubTypeId\": \"string\",     \"sourceId\": \"string\"   } } ``` **sourceTypeId** - it's a Source Type - available values can be found using [get /configuration/sources](https://dev.smartrecruiters.com/customer-api/live-docs/#!/configuration/configuration_getSourceTypes) endpoint  **sourceSubTypeId** - it's a Source Subtype, an optional parameter - available values can be found using [get /configuration/sources](https://dev.smartrecruiters.com/customer-api/live-docs/#!/configuration/configuration_getSourceTypes) endpoint  **sourceId** - it's a Source Id - available values for a given sourceTypeId can be found using [get /configuration/sources/:sourceTypeId/values](https://dev.smartrecruiters.com/customer-api/live-docs/#!/configuration/configuration_getSources) endpoint  NOTE: Not defining the source will default to **API** source.  NOTE II: In case you can't find an appropriate source to track against you can: * Create a custom source for each customer account separately on [this admin page](https://www.smartrecruiters.com/settings/configuration/custom-sources\\) (you need to be logged in as an admin to the customer account in order to view this page) * Request to [partners@smartrecruiters.com](mailto:partners@smartrecruiters.com) adding a standard source that will be available for all customers if your app/integration is productised (available to all SmartRecruiters customers) 

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
api_instance = smartrecruiters_python_client.CandidatesApi()
candidate = smartrecruiters_python_client.CandidateInput() # CandidateInput | Candidate object that needs to be created.

try: 
    # Create a new candidate and assign to a Talent Pool
    api_response = api_instance.candidates_add(candidate)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CandidatesApi->candidates_add: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **candidate** | [**CandidateInput**](CandidateInput.md)| Candidate object that needs to be created. | 

### Return type

[**CandidateDetails**](CandidateDetails.md)

### Authorization

[key](../README.md#key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json; charset=utf-8

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **candidates_add_to_job**
> CandidateDetails candidates_add_to_job(candidate, job_id)

Create a new candidate and assign to a job

Create a new candidate and assign to a job.  **Tracking candidate source**  When adding a new candidate, it's very important you track its source appropriately. In order to associate a source with your app / integration, add the below object to a candidate body object for this endpoint: ``` {   \"sourceDetails\": {     \"sourceTypeId\": \"string\",     \"sourceSubTypeId\": \"string\",     \"sourceId\": \"string\"   } } ``` **sourceTypeId** - it's a Source Type - available values can be found using [get /configuration/sources](https://dev.smartrecruiters.com/customer-api/live-docs/#!/configuration/configuration_getSourceTypes) endpoint  **sourceSubTypeId** - it's a Source Subtype, an optional parameter - available values can be found using [get /configuration/sources](https://dev.smartrecruiters.com/customer-api/live-docs/#!/configuration/configuration_getSourceTypes) endpoint  **sourceId** - it's a Source Id - available values for a given sourceTypeId can be found using [get /configuration/sources/:sourceTypeId/values](https://dev.smartrecruiters.com/customer-api/live-docs/#!/configuration/configuration_getSources) endpoint  NOTE: Not defining the source will default to **API** source.  NOTE II: In case you can't find an appropriate source to track against you can: * Create a custom source for each customer account separately on [this admin page](https://www.smartrecruiters.com/settings/configuration/custom-sources\\) (you need to be logged in as an admin to the customer account in order to view this page) * Request to [partners@smartrecruiters.com](mailto:partners@smartrecruiters.com) adding a standard source that will be available for all customers if your app / integration is productised (available to all SmartRecruiters customers) 

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
api_instance = smartrecruiters_python_client.CandidatesApi()
candidate = smartrecruiters_python_client.CandidateInput() # CandidateInput | Candidate object that needs to be created.
job_id = 'job_id_example' # str | job identifier

try: 
    # Create a new candidate and assign to a job
    api_response = api_instance.candidates_add_to_job(candidate, job_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CandidatesApi->candidates_add_to_job: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **candidate** | [**CandidateInput**](CandidateInput.md)| Candidate object that needs to be created. | 
 **job_id** | **str**| job identifier | 

### Return type

[**CandidateDetails**](CandidateDetails.md)

### Authorization

[key](../README.md#key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json; charset=utf-8

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **candidates_all**
> Candidates candidates_all(q=q, limit=limit, offset=offset, job_id=job_id, location=location, average_rating=average_rating, status=status, sub_status=sub_status, tag=tag, updated_after=updated_after, onboarding_status=onboarding_status, property_id=property_id, property_value_id=property_value_id)

Search candidates

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
api_instance = smartrecruiters_python_client.CandidatesApi()
q = 'q_example' # str | keyword search on all candidate fields; case insensitive; e.g. java developer (optional)
limit = 10 # int | number of elements to return. max value is 100 (optional) (default to 10)
offset = 0 # int | number of elements to skip while processing result (optional) (default to 0)
job_id = ['job_id_example'] # list[str] | job filter to display candidates who applied for a job [id]; can be used repeatedly; (optional)
location = ['location_example'] # list[str] | location keyword search which looks up a string in a candidate’s location data; can be used repeatedly; case insensitive; e.g. Krakow (optional)
average_rating = [56] # list[int] | average rating filter to display candidates with a specific average rating (integer); can be used repeatedly; e.g. 4 (optional)
status = ['status_example'] # list[str] | candidate’s status filter in a context of a job; can be used repeatedly (optional)
sub_status = 'sub_status_example' # str | candidate’s sub-status filter in a context of a job. Works only in a correlation with a set value for the \"status\" field. (optional)
tag = ['tag_example'] # list[str] | tag assigned to a candidate; can be used repeatedly; case insensitive; e.g. fluent english (optional)
updated_after = '2013-10-20T19:20:30+01:00' # datetime | ISO8601-formatted time boundaries for the candidate update time, Format: yyyy-MM-ddTHH:mm:ss.SSSZZ (optional)
onboarding_status = 'onboarding_status_example' # str | candidate's onboarding status (optional)
property_id = ['property_id_example'] # list[str] | candidate's property id (1-N) (optional)
property_value_id = ['property_value_id_example'] # list[str] | candidate's property value id (1-N) (optional)

try: 
    # Search candidates
    api_response = api_instance.candidates_all(q=q, limit=limit, offset=offset, job_id=job_id, location=location, average_rating=average_rating, status=status, sub_status=sub_status, tag=tag, updated_after=updated_after, onboarding_status=onboarding_status, property_id=property_id, property_value_id=property_value_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CandidatesApi->candidates_all: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **q** | **str**| keyword search on all candidate fields; case insensitive; e.g. java developer | [optional] 
 **limit** | **int**| number of elements to return. max value is 100 | [optional] [default to 10]
 **offset** | **int**| number of elements to skip while processing result | [optional] [default to 0]
 **job_id** | [**list[str]**](str.md)| job filter to display candidates who applied for a job [id]; can be used repeatedly; | [optional] 
 **location** | [**list[str]**](str.md)| location keyword search which looks up a string in a candidate’s location data; can be used repeatedly; case insensitive; e.g. Krakow | [optional] 
 **average_rating** | [**list[int]**](int.md)| average rating filter to display candidates with a specific average rating (integer); can be used repeatedly; e.g. 4 | [optional] 
 **status** | [**list[str]**](str.md)| candidate’s status filter in a context of a job; can be used repeatedly | [optional] 
 **sub_status** | **str**| candidate’s sub-status filter in a context of a job. Works only in a correlation with a set value for the \&quot;status\&quot; field. | [optional] 
 **tag** | [**list[str]**](str.md)| tag assigned to a candidate; can be used repeatedly; case insensitive; e.g. fluent english | [optional] 
 **updated_after** | **datetime**| ISO8601-formatted time boundaries for the candidate update time, Format: yyyy-MM-ddTHH:mm:ss.SSSZZ | [optional] 
 **onboarding_status** | **str**| candidate&#39;s onboarding status | [optional] 
 **property_id** | [**list[str]**](str.md)| candidate&#39;s property id (1-N) | [optional] 
 **property_value_id** | [**list[str]**](str.md)| candidate&#39;s property value id (1-N) | [optional] 

### Return type

[**Candidates**](Candidates.md)

### Authorization

[key](../README.md#key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json; charset=utf-8

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **candidates_attachments_add**
> Attachment candidates_attachments_add(id, attachment_type, file)

Attach files to a candidate.

Attach files to a candidate.

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
api_instance = smartrecruiters_python_client.CandidatesApi()
id = 'id_example' # str | Identifier of a candidate
attachment_type = 'GENERIC_FILE' # str | Type of attachment you want to upload. (default to GENERIC_FILE)
file = '/path/to/file.txt' # file | The file to upload.

try: 
    # Attach files to a candidate.
    api_response = api_instance.candidates_attachments_add(id, attachment_type, file)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CandidatesApi->candidates_attachments_add: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Identifier of a candidate | 
 **attachment_type** | **str**| Type of attachment you want to upload. | [default to GENERIC_FILE]
 **file** | **file**| The file to upload. | 

### Return type

[**Attachment**](Attachment.md)

### Authorization

[key](../README.md#key)

### HTTP request headers

 - **Content-Type**: multipart/form-data
 - **Accept**: application/json; charset=utf-8

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **candidates_attachments_get**
> candidates_attachments_get(id, attachment_id)

Get a candidate's attachment.

Get a candidate's attachment.

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
api_instance = smartrecruiters_python_client.CandidatesApi()
id = 'id_example' # str | Identifier of a candidate
attachment_id = 'attachment_id_example' # str | Identifier of an attachment

try: 
    # Get a candidate's attachment.
    api_instance.candidates_attachments_get(id, attachment_id)
except ApiException as e:
    print("Exception when calling CandidatesApi->candidates_attachments_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Identifier of a candidate | 
 **attachment_id** | **str**| Identifier of an attachment | 

### Return type

void (empty response body)

### Authorization

[key](../README.md#key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json; charset=utf-8

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **candidates_attachments_list**
> Attachments candidates_attachments_list(id)

Get list candidate's attachments.

Get list of candidate's attachments.

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
api_instance = smartrecruiters_python_client.CandidatesApi()
id = 'id_example' # str | Identifier of a candidate

try: 
    # Get list candidate's attachments.
    api_response = api_instance.candidates_attachments_list(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CandidatesApi->candidates_attachments_list: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Identifier of a candidate | 

### Return type

[**Attachments**](Attachments.md)

### Authorization

[key](../README.md#key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json; charset=utf-8

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **candidates_delete**
> candidates_delete(id)

Delete Candidate

Delete candidate

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
api_instance = smartrecruiters_python_client.CandidatesApi()
id = 'id_example' # str | Identifier of a Candidate

try: 
    # Delete Candidate
    api_instance.candidates_delete(id)
except ApiException as e:
    print("Exception when calling CandidatesApi->candidates_delete: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Identifier of a Candidate | 

### Return type

void (empty response body)

### Authorization

[key](../README.md#key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json; charset=utf-8

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **candidates_get**
> CandidateDetails candidates_get(id)

Get details of a candidate

Get details of a candidate

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
api_instance = smartrecruiters_python_client.CandidatesApi()
id = 'id_example' # str | Identifier of a Candidate

try: 
    # Get details of a candidate
    api_response = api_instance.candidates_get(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CandidatesApi->candidates_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Identifier of a Candidate | 

### Return type

[**CandidateDetails**](CandidateDetails.md)

### Authorization

[key](../README.md#key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json; charset=utf-8

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **candidates_onboarding_get**
> OnboardingStatus candidates_onboarding_get(id)

Get Onboarding Status for a candidate

Get Onboarding Status for a candidate.

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
api_instance = smartrecruiters_python_client.CandidatesApi()
id = 'id_example' # str | Identifier of a candidate

try: 
    # Get Onboarding Status for a candidate
    api_response = api_instance.candidates_onboarding_get(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CandidatesApi->candidates_onboarding_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Identifier of a candidate | 

### Return type

[**OnboardingStatus**](OnboardingStatus.md)

### Authorization

[key](../README.md#key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json; charset=utf-8

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **candidates_onboarding_get_for_job**
> OnboardingStatus candidates_onboarding_get_for_job(id, job_id)

Get Onboarding Status for a candidate associated with given job

Get Onboarding Status for a candidate associated with given job.

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
api_instance = smartrecruiters_python_client.CandidatesApi()
id = 'id_example' # str | Identifier of a candidate
job_id = 'job_id_example' # str | Identifier of a job

try: 
    # Get Onboarding Status for a candidate associated with given job
    api_response = api_instance.candidates_onboarding_get_for_job(id, job_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CandidatesApi->candidates_onboarding_get_for_job: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Identifier of a candidate | 
 **job_id** | **str**| Identifier of a job | 

### Return type

[**OnboardingStatus**](OnboardingStatus.md)

### Authorization

[key](../README.md#key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json; charset=utf-8

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **candidates_onboarding_update**
> candidates_onboarding_update(id, onboarding_status)

Set Onboarding Status for a candidate

Set Onboarding Status for a candidate.

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
api_instance = smartrecruiters_python_client.CandidatesApi()
id = 'id_example' # str | Identifier of a candidate
onboarding_status = smartrecruiters_python_client.OnboardingStatus() # OnboardingStatus | Onboarding status.

try: 
    # Set Onboarding Status for a candidate
    api_instance.candidates_onboarding_update(id, onboarding_status)
except ApiException as e:
    print("Exception when calling CandidatesApi->candidates_onboarding_update: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Identifier of a candidate | 
 **onboarding_status** | [**OnboardingStatus**](OnboardingStatus.md)| Onboarding status. | 

### Return type

void (empty response body)

### Authorization

[key](../README.md#key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json; charset=utf-8

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **candidates_onboarding_update_for_job**
> candidates_onboarding_update_for_job(id, job_id, onboarding_status)

Sets Onboarding Status for a candidate associated with given job

Sets Onboarding Status for a candidate associated with given job.

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
api_instance = smartrecruiters_python_client.CandidatesApi()
id = 'id_example' # str | Identifier of a candidate
job_id = 'job_id_example' # str | Identifier of a job
onboarding_status = smartrecruiters_python_client.OnboardingStatus() # OnboardingStatus | Onboarding status.

try: 
    # Sets Onboarding Status for a candidate associated with given job
    api_instance.candidates_onboarding_update_for_job(id, job_id, onboarding_status)
except ApiException as e:
    print("Exception when calling CandidatesApi->candidates_onboarding_update_for_job: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Identifier of a candidate | 
 **job_id** | **str**| Identifier of a job | 
 **onboarding_status** | [**OnboardingStatus**](OnboardingStatus.md)| Onboarding status. | 

### Return type

void (empty response body)

### Authorization

[key](../README.md#key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json; charset=utf-8

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **candidates_properties_get**
> CandidateProperties candidates_properties_get(id, context=context)

Get candidate property values for a candidate

Returns ``` {} ``` when there is no value set for a candidate property. 

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
api_instance = smartrecruiters_python_client.CandidatesApi()
id = 'id_example' # str | candidate identifier
context = 'context_example' # str | context for candidate properties to display (optional)

try: 
    # Get candidate property values for a candidate
    api_response = api_instance.candidates_properties_get(id, context=context)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CandidatesApi->candidates_properties_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| candidate identifier | 
 **context** | **str**| context for candidate properties to display | [optional] 

### Return type

[**CandidateProperties**](CandidateProperties.md)

### Authorization

[key](../README.md#key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json; charset=utf-8

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **candidates_properties_get_for_job**
> CandidateProperties candidates_properties_get_for_job(id, job_id, context=context)

Get candidate property values for a candidate's job

Returns ``` {} ``` when there is no value set for a candidate property. 

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
api_instance = smartrecruiters_python_client.CandidatesApi()
id = 'id_example' # str | Identifier of a Candidate
job_id = 'job_id_example' # str | Identifier of a Job
context = 'context_example' # str | context for candidate properties to display (optional)

try: 
    # Get candidate property values for a candidate's job
    api_response = api_instance.candidates_properties_get_for_job(id, job_id, context=context)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CandidatesApi->candidates_properties_get_for_job: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Identifier of a Candidate | 
 **job_id** | **str**| Identifier of a Job | 
 **context** | **str**| context for candidate properties to display | [optional] 

### Return type

[**CandidateProperties**](CandidateProperties.md)

### Authorization

[key](../README.md#key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json; charset=utf-8

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **candidates_properties_values_update**
> candidates_properties_values_update(id, property_id, candidate_property_input_value=candidate_property_input_value)

Add/update candidate property value

Set a candidate property value for the candidate. Below you can find a list of value examples, dependent on different candidate property types. * **BOOLEAN** ``` { \"value\": true } ``` Value has to be `true` or `false`. * **COUNTRY** ``` { \"value\": \"us\" } ``` Value has to be lowercase string in ISO 3166-1 alpha-2 format. * **CURRENCY** ``` {   \"value\": {     \"code\": \"GBP\",     \"value\": 23232   } } ``` Code of value is a currency code in ISO 4217 format. * **DATE** ``` { \"value\": \"2015-11-17T23:00:00.000Z\" } ``` * **NUMBER, PERCENT** ``` { \"value\": 42 } ``` * **REGION** ``` { \"value\": \"us-wa\" } ``` Value has to be lowercase string in ISO 3166-2 compatible format. * **SINGLE_SELECT** ``` { \"value\": \"f6fe768f-b5e6-4794-9938-c2f42ab0a572\" } ``` Value has to be an id of candidate property value (provided by GET /configuration/candidate-properties/{propertyId}/values). * **TEXT** ``` { \"value\": \"Example text\" } ``` * **USER** ``` { \"value\": \"50fe861de4b00265edec6775\" } ``` Value has to be a valid user id  To reset a value for any of the above types, please pass ``` {} ``` 

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
api_instance = smartrecruiters_python_client.CandidatesApi()
id = 'id_example' # str | Identifier of a Candidate
property_id = 'property_id_example' # str | Identifier of a Candidate Property
candidate_property_input_value = smartrecruiters_python_client.CandidatePropertyInputValue() # CandidatePropertyInputValue | Input value of the candidate property. (optional)

try: 
    # Add/update candidate property value
    api_instance.candidates_properties_values_update(id, property_id, candidate_property_input_value=candidate_property_input_value)
except ApiException as e:
    print("Exception when calling CandidatesApi->candidates_properties_values_update: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Identifier of a Candidate | 
 **property_id** | **str**| Identifier of a Candidate Property | 
 **candidate_property_input_value** | [**CandidatePropertyInputValue**](CandidatePropertyInputValue.md)| Input value of the candidate property. | [optional] 

### Return type

void (empty response body)

### Authorization

[key](../README.md#key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json; charset=utf-8

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **candidates_properties_values_update_for_job**
> candidates_properties_values_update_for_job(id, job_id, property_id, candidate_property_input_value=candidate_property_input_value)

Add/update candidate property value

Set a candidate property value for the candidate. Below you can find a list of value examples, dependent on different candidate property types. * **BOOLEAN** ``` { \"value\": true } ``` Value has to be `true` or `false`. * **COUNTRY** ``` { \"value\": \"us\" } ``` Value has to be lowercase string in ISO 3166-1 alpha-2 format. * **CURRENCY** ``` {   \"value\": {     \"code\": \"GBP\",     \"value\": 23232   } } ``` Code of value is a currency code in ISO 4217 format. * **DATE** ``` { \"value\": \"2015-11-17T23:00:00.000Z\" } ``` * **NUMBER, PERCENT** ``` { \"value\": 42 } ``` * **REGION** ``` { \"value\": \"us-wa\" } ``` Value has to be lowercase string in ISO 3166-2 compatible format. * **SINGLE_SELECT** ``` { \"value\": \"f6fe768f-b5e6-4794-9938-c2f42ab0a572\" } ``` Value has to be an id of candidate property value (provided by GET /configuration/candidate-properties/{propertyId}/values). * **TEXT** ``` { \"value\": \"Example text\" } ``` * **USER** ``` { \"value\": \"50fe861de4b00265edec6775\" } ``` Value has to be a valid user id  To reset a value for any of the above types, please pass ``` {} ``` 

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
api_instance = smartrecruiters_python_client.CandidatesApi()
id = 'id_example' # str | Identifier of a Candidate
job_id = 'job_id_example' # str | Identifier of a Job
property_id = 'property_id_example' # str | Identifier of a Candidate Property
candidate_property_input_value = smartrecruiters_python_client.CandidatePropertyInputValue() # CandidatePropertyInputValue | Input value of the candidate property. (optional)

try: 
    # Add/update candidate property value
    api_instance.candidates_properties_values_update_for_job(id, job_id, property_id, candidate_property_input_value=candidate_property_input_value)
except ApiException as e:
    print("Exception when calling CandidatesApi->candidates_properties_values_update_for_job: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Identifier of a Candidate | 
 **job_id** | **str**| Identifier of a Job | 
 **property_id** | **str**| Identifier of a Candidate Property | 
 **candidate_property_input_value** | [**CandidatePropertyInputValue**](CandidatePropertyInputValue.md)| Input value of the candidate property. | [optional] 

### Return type

void (empty response body)

### Authorization

[key](../README.md#key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json; charset=utf-8

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **candidates_resume_add**
> CandidateDetails candidates_resume_add(file, source_type_id=source_type_id, source_sub_type_id=source_sub_type_id, source_id=source_id, internal=internal)

Parse a resume, create a candidate and assign to a Talent Pool.

Parse a resume, create a candidate and assign to a Talent Pool.

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
api_instance = smartrecruiters_python_client.CandidatesApi()
file = '/path/to/file.txt' # file | The resume file to parse.
source_type_id = 'source_type_id_example' # str | Candidate Source type id (optional)
source_sub_type_id = 'source_sub_type_id_example' # str | Candidate Source subtype id (optional)
source_id = 'source_id_example' # str | Candidate Source id (optional)
internal = true # bool | Mark as company employee (optional)

try: 
    # Parse a resume, create a candidate and assign to a Talent Pool.
    api_response = api_instance.candidates_resume_add(file, source_type_id=source_type_id, source_sub_type_id=source_sub_type_id, source_id=source_id, internal=internal)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CandidatesApi->candidates_resume_add: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **file** | **file**| The resume file to parse. | 
 **source_type_id** | **str**| Candidate Source type id | [optional] 
 **source_sub_type_id** | **str**| Candidate Source subtype id | [optional] 
 **source_id** | **str**| Candidate Source id | [optional] 
 **internal** | **bool**| Mark as company employee | [optional] 

### Return type

[**CandidateDetails**](CandidateDetails.md)

### Authorization

[key](../README.md#key)

### HTTP request headers

 - **Content-Type**: multipart/form-data
 - **Accept**: application/json; charset=utf-8

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **candidates_resume_add_to_job**
> CandidateDetails candidates_resume_add_to_job(file, job_id, source_type_id=source_type_id, source_sub_type_id=source_sub_type_id, source_id=source_id, internal=internal)

Parse a resume, create a candidate and assign to a job.

Parse a resume, create a candidate and assign to a job.

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
api_instance = smartrecruiters_python_client.CandidatesApi()
file = '/path/to/file.txt' # file | The resume file to parse.
job_id = 'job_id_example' # str | Identifier of a Job
source_type_id = 'source_type_id_example' # str | Candidate Source type id (optional)
source_sub_type_id = 'source_sub_type_id_example' # str | Candidate Source subtype id (optional)
source_id = 'source_id_example' # str | Candidate Source id (optional)
internal = true # bool | Mark as company employee (optional)

try: 
    # Parse a resume, create a candidate and assign to a job.
    api_response = api_instance.candidates_resume_add_to_job(file, job_id, source_type_id=source_type_id, source_sub_type_id=source_sub_type_id, source_id=source_id, internal=internal)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CandidatesApi->candidates_resume_add_to_job: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **file** | **file**| The resume file to parse. | 
 **job_id** | **str**| Identifier of a Job | 
 **source_type_id** | **str**| Candidate Source type id | [optional] 
 **source_sub_type_id** | **str**| Candidate Source subtype id | [optional] 
 **source_id** | **str**| Candidate Source id | [optional] 
 **internal** | **bool**| Mark as company employee | [optional] 

### Return type

[**CandidateDetails**](CandidateDetails.md)

### Authorization

[key](../README.md#key)

### HTTP request headers

 - **Content-Type**: multipart/form-data
 - **Accept**: application/json; charset=utf-8

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **candidates_screening_answers_get**
> ScreeningAnswers candidates_screening_answers_get(id, job_id)

Get candidate screening answers for a candidate's job

Returns candidate screening question answers for a candidate's job. Returns an empty array when there is no screening answers for given candidate's job.  UUID in question category indicates custom question. Other value indicates predefined library question.  In order to create human readable format of answers please use label properties. Ignore labels for answers with single field. Based on labels from included example you can get following text:  ```text Do you have a current driver's license?  - No  Free text question  - Long text answer for free text questions  Checkbox question  - Confirmed  Legacy acknowledgment question - replaced by checkbox  - Confirmed  Gender, Race and Ethnicity [(definitions)](https://smartrecruiters.com/oneclick/static/html/en/eeoGeneral.html)  - Gender: Male  - Race/Ethnicity: Prefer not to answer  Currency question  - 1234  Multiple choice dropdown  - third value, second value, first value  Languages  1)  - Language: English  - Proficiency level: Advanced  2)  - Language: Spanish  - Proficiency level: Beginner  3)  - Language: French  - Proficiency level: Intermediate  What are your preferred work shifts? 1)  - Day: Weekdays  - From: 08:00 AM  - To: 04:00 PM 2)  - Day: Weekdays  - From: 10:00 AM  - To: 02:00 PM  Your Name  - John ``` 

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
api_instance = smartrecruiters_python_client.CandidatesApi()
id = 'id_example' # str | Identifier of a Candidate
job_id = 'job_id_example' # str | Identifier of a Job

try: 
    # Get candidate screening answers for a candidate's job
    api_response = api_instance.candidates_screening_answers_get(id, job_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CandidatesApi->candidates_screening_answers_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Identifier of a Candidate | 
 **job_id** | **str**| Identifier of a Job | 

### Return type

[**ScreeningAnswers**](ScreeningAnswers.md)

### Authorization

[key](../README.md#key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json; charset=utf-8

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **candidates_source_update**
> candidates_source_update(id, job_id, candidate_source)

Update a candidate's source

Update a candidate's source

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
api_instance = smartrecruiters_python_client.CandidatesApi()
id = 'id_example' # str | Identifier of a Candidate
job_id = 'job_id_example' # str | Identifier of a Job
candidate_source = smartrecruiters_python_client.CandidateSource() # CandidateSource | Candidate source to be set

try: 
    # Update a candidate's source
    api_instance.candidates_source_update(id, job_id, candidate_source)
except ApiException as e:
    print("Exception when calling CandidatesApi->candidates_source_update: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Identifier of a Candidate | 
 **job_id** | **str**| Identifier of a Job | 
 **candidate_source** | [**CandidateSource**](CandidateSource.md)| Candidate source to be set | 

### Return type

void (empty response body)

### Authorization

[key](../README.md#key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json; charset=utf-8

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **candidates_status_history_get**
> CandidateStatusHistoryList candidates_status_history_get(id)

Get candidate's status history

Get candidate's status history

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
api_instance = smartrecruiters_python_client.CandidatesApi()
id = 'id_example' # str | Identifier of a Candidate

try: 
    # Get candidate's status history
    api_response = api_instance.candidates_status_history_get(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CandidatesApi->candidates_status_history_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Identifier of a Candidate | 

### Return type

[**CandidateStatusHistoryList**](CandidateStatusHistoryList.md)

### Authorization

[key](../README.md#key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json; charset=utf-8

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **candidates_status_update**
> candidates_status_update(id, job_id, candidate_status=candidate_status)

Update a candidate's status

Update a candidate's status

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
api_instance = smartrecruiters_python_client.CandidatesApi()
id = 'id_example' # str | Identifier of a Candidate
job_id = 'job_id_example' # str | Identifier of a Job
candidate_status = smartrecruiters_python_client.CandidateStatus() # CandidateStatus | Candidate Status to be set (optional)

try: 
    # Update a candidate's status
    api_instance.candidates_status_update(id, job_id, candidate_status=candidate_status)
except ApiException as e:
    print("Exception when calling CandidatesApi->candidates_status_update: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Identifier of a Candidate | 
 **job_id** | **str**| Identifier of a Job | 
 **candidate_status** | [**CandidateStatus**](CandidateStatus.md)| Candidate Status to be set | [optional] 

### Return type

void (empty response body)

### Authorization

[key](../README.md#key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json; charset=utf-8

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **candidates_status_update_primary**
> candidates_status_update_primary(id, candidate_status=candidate_status)

Update a candidate's status on primary assignment

Update a candidate's status on primary assignment

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
api_instance = smartrecruiters_python_client.CandidatesApi()
id = 'id_example' # str | Identifier of a Candidate
candidate_status = smartrecruiters_python_client.CandidateStatus() # CandidateStatus | Candidate Status to be set (optional)

try: 
    # Update a candidate's status on primary assignment
    api_instance.candidates_status_update_primary(id, candidate_status=candidate_status)
except ApiException as e:
    print("Exception when calling CandidatesApi->candidates_status_update_primary: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Identifier of a Candidate | 
 **candidate_status** | [**CandidateStatus**](CandidateStatus.md)| Candidate Status to be set | [optional] 

### Return type

void (empty response body)

### Authorization

[key](../README.md#key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json; charset=utf-8

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **candidates_tags_add**
> CandidateTags candidates_tags_add(id, candidate_tags)

Add tags to a candidate

Add new tags to a given candidate. It doesn't replace existing tags.

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
api_instance = smartrecruiters_python_client.CandidatesApi()
id = 'id_example' # str | Identifier of a Candidate
candidate_tags = smartrecruiters_python_client.CandidateTags() # CandidateTags | Tags to be added.

try: 
    # Add tags to a candidate
    api_response = api_instance.candidates_tags_add(id, candidate_tags)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CandidatesApi->candidates_tags_add: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Identifier of a Candidate | 
 **candidate_tags** | [**CandidateTags**](CandidateTags.md)| Tags to be added. | 

### Return type

[**CandidateTags**](CandidateTags.md)

### Authorization

[key](../README.md#key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json; charset=utf-8

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **candidates_tags_delete**
> candidates_tags_delete(id)

Delete tags for a candidate

Delete tags for a given candidate. All tags associated with a candidate are removed.

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
api_instance = smartrecruiters_python_client.CandidatesApi()
id = 'id_example' # str | Identifier of a Candidate

try: 
    # Delete tags for a candidate
    api_instance.candidates_tags_delete(id)
except ApiException as e:
    print("Exception when calling CandidatesApi->candidates_tags_delete: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Identifier of a Candidate | 

### Return type

void (empty response body)

### Authorization

[key](../README.md#key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json; charset=utf-8

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **candidates_tags_get**
> CandidateTags candidates_tags_get(id)

Get tags for a candidate

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
api_instance = smartrecruiters_python_client.CandidatesApi()
id = 'id_example' # str | Identifier of a Candidate

try: 
    # Get tags for a candidate
    api_response = api_instance.candidates_tags_get(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CandidatesApi->candidates_tags_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Identifier of a Candidate | 

### Return type

[**CandidateTags**](CandidateTags.md)

### Authorization

[key](../README.md#key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json; charset=utf-8

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **candidates_tags_replace**
> CandidateTags candidates_tags_replace(id, candidate_tags)

Update tags for a candidate

Update tags for a given candidate. It replaces all existing tags with the new array provided.

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
api_instance = smartrecruiters_python_client.CandidatesApi()
id = 'id_example' # str | Identifier of a Candidate
candidate_tags = smartrecruiters_python_client.CandidateTags() # CandidateTags | Tags to be set.

try: 
    # Update tags for a candidate
    api_response = api_instance.candidates_tags_replace(id, candidate_tags)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CandidatesApi->candidates_tags_replace: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Identifier of a Candidate | 
 **candidate_tags** | [**CandidateTags**](CandidateTags.md)| Tags to be set. | 

### Return type

[**CandidateTags**](CandidateTags.md)

### Authorization

[key](../README.md#key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json; charset=utf-8

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **candidates_update**
> CandidateDetails candidates_update(id, personal_details=personal_details)

Update candidate personal information

Update candidate details

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
api_instance = smartrecruiters_python_client.CandidatesApi()
id = 'id_example' # str | Identifier of a candidate
personal_details = smartrecruiters_python_client.PersonalDetails() # PersonalDetails | Candidate personal information (optional)

try: 
    # Update candidate personal information
    api_response = api_instance.candidates_update(id, personal_details=personal_details)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CandidatesApi->candidates_update: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Identifier of a candidate | 
 **personal_details** | [**PersonalDetails**](PersonalDetails.md)| Candidate personal information | [optional] 

### Return type

[**CandidateDetails**](CandidateDetails.md)

### Authorization

[key](../README.md#key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json; charset=utf-8

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)


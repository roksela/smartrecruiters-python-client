# smartrecruiters_python_client.JobsApi

All URIs are relative to *https://api.smartrecruiters.com/*

Method | HTTP request | Description
------------- | ------------- | -------------
[**jobs_all**](JobsApi.md#jobs_all) | **GET** /jobs | Search jobs
[**jobs_create**](JobsApi.md#jobs_create) | **POST** /jobs | Create a new job
[**jobs_get**](JobsApi.md#jobs_get) | **GET** /jobs/{id} | Get content of a job with a given id.
[**jobs_hiring_team_add**](JobsApi.md#jobs_hiring_team_add) | **POST** /jobs/{id}/hiring-team | Add hiring team member of a job with a given id.
[**jobs_hiring_team_get**](JobsApi.md#jobs_hiring_team_get) | **GET** /jobs/{id}/hiring-team | Get hiring team of a job with a given id.
[**jobs_hiring_team_remove**](JobsApi.md#jobs_hiring_team_remove) | **DELETE** /jobs/{id}/hiring-team/{userId} | Removes hiring team member of a job with a given id.
[**jobs_jobads_all**](JobsApi.md#jobs_jobads_all) | **GET** /jobs/{id}/jobads | Find and list job ads for a given job
[**jobs_jobads_create**](JobsApi.md#jobs_jobads_create) | **POST** /jobs/{id}/jobads | Create a new job ad
[**jobs_jobads_get**](JobsApi.md#jobs_jobads_get) | **GET** /jobs/{id}/jobads/{jobadId} | Get a job ad
[**jobs_jobads_postings_all**](JobsApi.md#jobs_jobads_postings_all) | **GET** /jobs/{id}/jobads/{jobadId}/postings | List publications for a job ad
[**jobs_jobads_postings_create**](JobsApi.md#jobs_jobads_postings_create) | **POST** /jobs/{id}/jobads/{jobadId}/postings | Publishes a job ad
[**jobs_jobads_postings_unpublish**](JobsApi.md#jobs_jobads_postings_unpublish) | **DELETE** /jobs/{id}/jobads/{jobadId}/postings | Unpublish a job ad
[**jobs_jobads_update**](JobsApi.md#jobs_jobads_update) | **PUT** /jobs/{id}/jobads/{jobadId} | Update a job ad
[**jobs_notes_get**](JobsApi.md#jobs_notes_get) | **GET** /jobs/{id}/note | Get note of a job.
[**jobs_notes_update**](JobsApi.md#jobs_notes_update) | **PUT** /jobs/{id}/note | Update note of a job.
[**jobs_patch**](JobsApi.md#jobs_patch) | **PATCH** /jobs/{id} | Update a job
[**jobs_positions_all**](JobsApi.md#jobs_positions_all) | **GET** /jobs/{id}/positions | Positions for a job
[**jobs_positions_create**](JobsApi.md#jobs_positions_create) | **POST** /jobs/{id}/positions | Create a new position for a job
[**jobs_positions_get**](JobsApi.md#jobs_positions_get) | **GET** /jobs/{id}/positions/{positionId} | Get a single position
[**jobs_positions_remove**](JobsApi.md#jobs_positions_remove) | **DELETE** /jobs/{id}/positions/{positionId} | Delete position
[**jobs_positions_update**](JobsApi.md#jobs_positions_update) | **PUT** /jobs/{id}/positions/{positionId} | Update position
[**jobs_publication_all**](JobsApi.md#jobs_publication_all) | **GET** /jobs/{id}/publication | Find and list publications for a job
[**jobs_publication_create**](JobsApi.md#jobs_publication_create) | **POST** /jobs/{id}/publication | Publishes a default job ad
[**jobs_publication_unpublish**](JobsApi.md#jobs_publication_unpublish) | **DELETE** /jobs/{id}/publication | Unpublishes a job from all sources
[**jobs_status_history_get**](JobsApi.md#jobs_status_history_get) | **GET** /jobs/{id}/status/history | Job status history
[**jobs_status_update**](JobsApi.md#jobs_status_update) | **PUT** /jobs/{id}/status | Updates job status
[**jobs_update**](JobsApi.md#jobs_update) | **PUT** /jobs/{id} | Updates job


# **jobs_all**
> Jobs jobs_all(q=q, limit=limit, offset=offset, city=city, department=department, updated_after=updated_after, last_activity_after=last_activity_after, language=language, posting_status=posting_status)

Search jobs

Search jobs by params

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
api_instance = smartrecruiters_python_client.JobsApi()
q = 'q_example' # str | full-text search query based on a job title, location; case insensitive; e.g. java developer (optional)
limit = 10 # int | number of elements to return. max value is 100 (optional) (default to 10)
offset = 0 # int | number of elements to skip while processing result (optional) (default to 0)
city = ['city_example'] # list[str] | city filter (part of the location object); can be used repeatedly; case insensitive; e.g. San Francisco (optional)
department = ['department_example'] # list[str] | department filter (by department label); can be used repeatedly; case insensitive; e.g. “Marketing” (optional)
updated_after = '2013-10-20T19:20:30+01:00' # datetime | ISO8601-formatted time boundaries for the job update time, Format: yyyy-MM-ddTHH:mm:ss.SSSZZ (optional)
last_activity_after = '2013-10-20T19:20:30+01:00' # datetime | ISO8601-formatted time boundaries for the job lastActivityOn time, Format: yyyy-MM-ddTHH:mm:ss.SSSZZ. lastActivityOn is updated when job is edited, new candidates apply or job is published.  (optional)
language = 'language_example' # str | Exceptions to the language code ISO format: * \"en-GB\" - \"English - English (UK)\" * \"fr-CA\" - \"French - français (Canada)\" * \"pt-BR\" - \"Portugal - português (Brasil)\" * \"pt-PT\" - \"Portugal - português (Portugal)\" * \"zh-HK\" - \"Chinese (Traditional) - 中文 (香港)\" * \"zh-CN\" - \"Chinese (Simplified) - 中文 (简体)\"  (optional)
posting_status = 'posting_status_example' # str | Posting status of a job  (optional)

try: 
    # Search jobs
    api_response = api_instance.jobs_all(q=q, limit=limit, offset=offset, city=city, department=department, updated_after=updated_after, last_activity_after=last_activity_after, language=language, posting_status=posting_status)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling JobsApi->jobs_all: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **q** | **str**| full-text search query based on a job title, location; case insensitive; e.g. java developer | [optional] 
 **limit** | **int**| number of elements to return. max value is 100 | [optional] [default to 10]
 **offset** | **int**| number of elements to skip while processing result | [optional] [default to 0]
 **city** | [**list[str]**](str.md)| city filter (part of the location object); can be used repeatedly; case insensitive; e.g. San Francisco | [optional] 
 **department** | [**list[str]**](str.md)| department filter (by department label); can be used repeatedly; case insensitive; e.g. “Marketing” | [optional] 
 **updated_after** | **datetime**| ISO8601-formatted time boundaries for the job update time, Format: yyyy-MM-ddTHH:mm:ss.SSSZZ | [optional] 
 **last_activity_after** | **datetime**| ISO8601-formatted time boundaries for the job lastActivityOn time, Format: yyyy-MM-ddTHH:mm:ss.SSSZZ. lastActivityOn is updated when job is edited, new candidates apply or job is published.  | [optional] 
 **language** | **str**| Exceptions to the language code ISO format: * \&quot;en-GB\&quot; - \&quot;English - English (UK)\&quot; * \&quot;fr-CA\&quot; - \&quot;French - français (Canada)\&quot; * \&quot;pt-BR\&quot; - \&quot;Portugal - português (Brasil)\&quot; * \&quot;pt-PT\&quot; - \&quot;Portugal - português (Portugal)\&quot; * \&quot;zh-HK\&quot; - \&quot;Chinese (Traditional) - 中文 (香港)\&quot; * \&quot;zh-CN\&quot; - \&quot;Chinese (Simplified) - 中文 (简体)\&quot;  | [optional] 
 **posting_status** | **str**| Posting status of a job  | [optional] 

### Return type

[**Jobs**](Jobs.md)

### Authorization

[key](../README.md#key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json; charset=utf-8

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **jobs_create**
> JobDetails jobs_create(job=job)

Create a new job

Create a new job. Ignores all nonexistent job properties and job properties values.

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
api_instance = smartrecruiters_python_client.JobsApi()
job = smartrecruiters_python_client.JobInput() # JobInput | Job object that needs to be created (optional)

try: 
    # Create a new job
    api_response = api_instance.jobs_create(job=job)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling JobsApi->jobs_create: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **job** | [**JobInput**](JobInput.md)| Job object that needs to be created | [optional] 

### Return type

[**JobDetails**](JobDetails.md)

### Authorization

[key](../README.md#key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json; charset=utf-8

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **jobs_get**
> JobDetails jobs_get(id)

Get content of a job with a given id.

Get content of a job with a given id.

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
api_instance = smartrecruiters_python_client.JobsApi()
id = 'id_example' # str | identifier of a job

try: 
    # Get content of a job with a given id.
    api_response = api_instance.jobs_get(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling JobsApi->jobs_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| identifier of a job | 

### Return type

[**JobDetails**](JobDetails.md)

### Authorization

[key](../README.md#key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json; charset=utf-8

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **jobs_hiring_team_add**
> HiringTeamMemberResponse jobs_hiring_team_add(id, hiring_team_member=hiring_team_member)

Add hiring team member of a job with a given id.

Add hiring team member of a job with a given id

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
api_instance = smartrecruiters_python_client.JobsApi()
id = 'id_example' # str | identifier of a job
hiring_team_member = smartrecruiters_python_client.HiringTeamMember() # HiringTeamMember | HiringTeamMember object (optional)

try: 
    # Add hiring team member of a job with a given id.
    api_response = api_instance.jobs_hiring_team_add(id, hiring_team_member=hiring_team_member)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling JobsApi->jobs_hiring_team_add: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| identifier of a job | 
 **hiring_team_member** | [**HiringTeamMember**](HiringTeamMember.md)| HiringTeamMember object | [optional] 

### Return type

[**HiringTeamMemberResponse**](HiringTeamMemberResponse.md)

### Authorization

[key](../README.md#key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json; charset=utf-8

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **jobs_hiring_team_get**
> HiringTeamMembers jobs_hiring_team_get(id)

Get hiring team of a job with a given id.

Get hiring team of a job with a given id.

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
api_instance = smartrecruiters_python_client.JobsApi()
id = 'id_example' # str | identifier of a job

try: 
    # Get hiring team of a job with a given id.
    api_response = api_instance.jobs_hiring_team_get(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling JobsApi->jobs_hiring_team_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| identifier of a job | 

### Return type

[**HiringTeamMembers**](HiringTeamMembers.md)

### Authorization

[key](../README.md#key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json; charset=utf-8

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **jobs_hiring_team_remove**
> jobs_hiring_team_remove(id, user_id)

Removes hiring team member of a job with a given id.

Removes hiring team member of a job with a given id.

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
api_instance = smartrecruiters_python_client.JobsApi()
id = 'id_example' # str | identifier of a job
user_id = 'user_id_example' # str | identifier of an user

try: 
    # Removes hiring team member of a job with a given id.
    api_instance.jobs_hiring_team_remove(id, user_id)
except ApiException as e:
    print("Exception when calling JobsApi->jobs_hiring_team_remove: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| identifier of a job | 
 **user_id** | **str**| identifier of an user | 

### Return type

void (empty response body)

### Authorization

[key](../README.md#key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json; charset=utf-8

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **jobs_jobads_all**
> JobAds jobs_jobads_all(id)

Find and list job ads for a given job

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
api_instance = smartrecruiters_python_client.JobsApi()
id = 'id_example' # str | identifier of a job

try: 
    # Find and list job ads for a given job
    api_response = api_instance.jobs_jobads_all(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling JobsApi->jobs_jobads_all: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| identifier of a job | 

### Return type

[**JobAds**](JobAds.md)

### Authorization

[key](../README.md#key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json; charset=utf-8

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **jobs_jobads_create**
> JobAdItem jobs_jobads_create(id, job_ad)

Create a new job ad

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
api_instance = smartrecruiters_python_client.JobsApi()
id = 'id_example' # str | identifier of a job
job_ad = smartrecruiters_python_client.JobAdContent() # JobAdContent | job ad

try: 
    # Create a new job ad
    api_response = api_instance.jobs_jobads_create(id, job_ad)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling JobsApi->jobs_jobads_create: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| identifier of a job | 
 **job_ad** | [**JobAdContent**](JobAdContent.md)| job ad | 

### Return type

[**JobAdItem**](JobAdItem.md)

### Authorization

[key](../README.md#key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json; charset=utf-8

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **jobs_jobads_get**
> JobAdItem jobs_jobads_get(id, jobad_id)

Get a job ad

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
api_instance = smartrecruiters_python_client.JobsApi()
id = 'id_example' # str | identifier of a job
jobad_id = 'jobad_id_example' # str | identifier of a job ad

try: 
    # Get a job ad
    api_response = api_instance.jobs_jobads_get(id, jobad_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling JobsApi->jobs_jobads_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| identifier of a job | 
 **jobad_id** | **str**| identifier of a job ad | 

### Return type

[**JobAdItem**](JobAdItem.md)

### Authorization

[key](../README.md#key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json; charset=utf-8

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **jobs_jobads_postings_all**
> PublicationList jobs_jobads_postings_all(id, jobad_id, active_only=active_only)

List publications for a job ad

List publications for a job ad

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
api_instance = smartrecruiters_python_client.JobsApi()
id = 'id_example' # str | identifier of a job
jobad_id = 'jobad_id_example' # str | job ad identifier
active_only = true # bool | publication status filter; when omitted, defaults to 'true' (only active publications are returned); 'false' returns active and inactive publications (optional) (default to true)

try: 
    # List publications for a job ad
    api_response = api_instance.jobs_jobads_postings_all(id, jobad_id, active_only=active_only)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling JobsApi->jobs_jobads_postings_all: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| identifier of a job | 
 **jobad_id** | **str**| job ad identifier | 
 **active_only** | **bool**| publication status filter; when omitted, defaults to &#39;true&#39; (only active publications are returned); &#39;false&#39; returns active and inactive publications | [optional] [default to true]

### Return type

[**PublicationList**](PublicationList.md)

### Authorization

[key](../README.md#key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json; charset=utf-8

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **jobs_jobads_postings_create**
> JobAdPublicationScheduled jobs_jobads_postings_create(id, jobad_id, publication=publication)

Publishes a job ad

Publishes a job ad to internal sources (Career Pages, Job Widget, Facebook App, WordPress Plugin, Posting API) and optionally to all free job aggregators.  By default it's set to publish to job aggregators  It reflects a Publish action available in the SmartRecruiters UI.  Note: Internal sources depend on a company's payment plan. 

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
api_instance = smartrecruiters_python_client.JobsApi()
id = 'id_example' # str | identifier of a job
jobad_id = 'jobad_id_example' # str | job ad identifier
publication = smartrecruiters_python_client.Publication() # Publication | Publication object (optional)

try: 
    # Publishes a job ad
    api_response = api_instance.jobs_jobads_postings_create(id, jobad_id, publication=publication)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling JobsApi->jobs_jobads_postings_create: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| identifier of a job | 
 **jobad_id** | **str**| job ad identifier | 
 **publication** | [**Publication**](Publication.md)| Publication object | [optional] 

### Return type

[**JobAdPublicationScheduled**](JobAdPublicationScheduled.md)

### Authorization

[key](../README.md#key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json; charset=utf-8

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **jobs_jobads_postings_unpublish**
> JobAdUnpublishScheduled jobs_jobads_postings_unpublish(id, jobad_id)

Unpublish a job ad

Unpublishes a job ad from all sources.  **Unpublishing a default job ad will unpublish all other job ads within that job.** 

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
api_instance = smartrecruiters_python_client.JobsApi()
id = 'id_example' # str | identifier of a job
jobad_id = 'jobad_id_example' # str | job ad identifier

try: 
    # Unpublish a job ad
    api_response = api_instance.jobs_jobads_postings_unpublish(id, jobad_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling JobsApi->jobs_jobads_postings_unpublish: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| identifier of a job | 
 **jobad_id** | **str**| job ad identifier | 

### Return type

[**JobAdUnpublishScheduled**](JobAdUnpublishScheduled.md)

### Authorization

[key](../README.md#key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json; charset=utf-8

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **jobs_jobads_update**
> JobAdItem jobs_jobads_update(id, jobad_id, job_ad)

Update a job ad

Enables you to update an existing job ad. NOTE: In order for a job ad changes to be reflected on internal sources (Career Sites, Job Widgets etc.) and Job Aggregators, you need to Publish the job ad after making an update. 

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
api_instance = smartrecruiters_python_client.JobsApi()
id = 'id_example' # str | identifier of a job
jobad_id = 'jobad_id_example' # str | job ad identifier
job_ad = smartrecruiters_python_client.JobAdContent() # JobAdContent | job ad

try: 
    # Update a job ad
    api_response = api_instance.jobs_jobads_update(id, jobad_id, job_ad)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling JobsApi->jobs_jobads_update: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| identifier of a job | 
 **jobad_id** | **str**| job ad identifier | 
 **job_ad** | [**JobAdContent**](JobAdContent.md)| job ad | 

### Return type

[**JobAdItem**](JobAdItem.md)

### Authorization

[key](../README.md#key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json; charset=utf-8

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **jobs_notes_get**
> JobNote jobs_notes_get(id)

Get note of a job.

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
api_instance = smartrecruiters_python_client.JobsApi()
id = 'id_example' # str | identifier of a job

try: 
    # Get note of a job.
    api_response = api_instance.jobs_notes_get(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling JobsApi->jobs_notes_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| identifier of a job | 

### Return type

[**JobNote**](JobNote.md)

### Authorization

[key](../README.md#key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json; charset=utf-8

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **jobs_notes_update**
> JobNote jobs_notes_update(id, job_note)

Update note of a job.

Update note of a job.

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
api_instance = smartrecruiters_python_client.JobsApi()
id = 'id_example' # str | identifier of a job
job_note = smartrecruiters_python_client.JobNote() # JobNote | 

try: 
    # Update note of a job.
    api_response = api_instance.jobs_notes_update(id, job_note)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling JobsApi->jobs_notes_update: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| identifier of a job | 
 **job_note** | [**JobNote**](JobNote.md)|  | 

### Return type

[**JobNote**](JobNote.md)

### Authorization

[key](../README.md#key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json; charset=utf-8

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **jobs_patch**
> JobDetails jobs_patch(id, json_patch=json_patch)

Update a job

Update a job. All attributes that are used when creating a job can be used. Ignores all nonexistent job properties and job properties values.

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
api_instance = smartrecruiters_python_client.JobsApi()
id = 'id_example' # str | Identifier of a job
json_patch = smartrecruiters_python_client.JSONPatch() # JSONPatch | patch request (optional)

try: 
    # Update a job
    api_response = api_instance.jobs_patch(id, json_patch=json_patch)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling JobsApi->jobs_patch: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Identifier of a job | 
 **json_patch** | [**JSONPatch**](JSONPatch.md)| patch request | [optional] 

### Return type

[**JobDetails**](JobDetails.md)

### Authorization

[key](../README.md#key)

### HTTP request headers

 - **Content-Type**: application/json-patch+json
 - **Accept**: application/json; charset=utf-8

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **jobs_positions_all**
> JobPositions jobs_positions_all(id)

Positions for a job

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
api_instance = smartrecruiters_python_client.JobsApi()
id = 'id_example' # str | identifier of a job

try: 
    # Positions for a job
    api_response = api_instance.jobs_positions_all(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling JobsApi->jobs_positions_all: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| identifier of a job | 

### Return type

[**JobPositions**](JobPositions.md)

### Authorization

[key](../README.md#key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json; charset=utf-8

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **jobs_positions_create**
> JobPosition jobs_positions_create(id, job_position)

Create a new position for a job

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
api_instance = smartrecruiters_python_client.JobsApi()
id = 'id_example' # str | identifier of a job
job_position = smartrecruiters_python_client.JobPositionInput() # JobPositionInput | Position body object

try: 
    # Create a new position for a job
    api_response = api_instance.jobs_positions_create(id, job_position)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling JobsApi->jobs_positions_create: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| identifier of a job | 
 **job_position** | [**JobPositionInput**](JobPositionInput.md)| Position body object | 

### Return type

[**JobPosition**](JobPosition.md)

### Authorization

[key](../README.md#key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json; charset=utf-8

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **jobs_positions_get**
> JobPosition jobs_positions_get(id, position_id)

Get a single position

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
api_instance = smartrecruiters_python_client.JobsApi()
id = 'id_example' # str | identifier of a job
position_id = 'position_id_example' # str | identifier of a position

try: 
    # Get a single position
    api_response = api_instance.jobs_positions_get(id, position_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling JobsApi->jobs_positions_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| identifier of a job | 
 **position_id** | **str**| identifier of a position | 

### Return type

[**JobPosition**](JobPosition.md)

### Authorization

[key](../README.md#key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json; charset=utf-8

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **jobs_positions_remove**
> jobs_positions_remove(id, position_id)

Delete position

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
api_instance = smartrecruiters_python_client.JobsApi()
id = 'id_example' # str | identifier of a job
position_id = 'position_id_example' # str | identifier of a position

try: 
    # Delete position
    api_instance.jobs_positions_remove(id, position_id)
except ApiException as e:
    print("Exception when calling JobsApi->jobs_positions_remove: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| identifier of a job | 
 **position_id** | **str**| identifier of a position | 

### Return type

void (empty response body)

### Authorization

[key](../README.md#key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json; charset=utf-8

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **jobs_positions_update**
> JobPosition jobs_positions_update(id, job_position, position_id)

Update position

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
api_instance = smartrecruiters_python_client.JobsApi()
id = 'id_example' # str | identifier of a job
job_position = smartrecruiters_python_client.JobPositionInput() # JobPositionInput | Position body object
position_id = 'position_id_example' # str | identifier of a position

try: 
    # Update position
    api_response = api_instance.jobs_positions_update(id, job_position, position_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling JobsApi->jobs_positions_update: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| identifier of a job | 
 **job_position** | [**JobPositionInput**](JobPositionInput.md)| Position body object | 
 **position_id** | **str**| identifier of a position | 

### Return type

[**JobPosition**](JobPosition.md)

### Authorization

[key](../README.md#key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json; charset=utf-8

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **jobs_publication_all**
> PublicationList jobs_publication_all(id, active_only=active_only)

Find and list publications for a job

Find and list publications for a job

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
api_instance = smartrecruiters_python_client.JobsApi()
id = 'id_example' # str | identifier of a job
active_only = true # bool | publication status filter; defaults to 'true' (only active publications are returned); 'false' returns active and inactive publications (optional) (default to true)

try: 
    # Find and list publications for a job
    api_response = api_instance.jobs_publication_all(id, active_only=active_only)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling JobsApi->jobs_publication_all: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| identifier of a job | 
 **active_only** | **bool**| publication status filter; defaults to &#39;true&#39; (only active publications are returned); &#39;false&#39; returns active and inactive publications | [optional] [default to true]

### Return type

[**PublicationList**](PublicationList.md)

### Authorization

[key](../README.md#key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json; charset=utf-8

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **jobs_publication_create**
> jobs_publication_create(id, publication=publication)

Publishes a default job ad

Publishes default job ad to internal sources and to free job aggregators.  It reflects a Publish action available in the SmartRecruiters UI.  Note:   Internal sources: Career Pages, Job Widget, Facebook App, WordPress Plugin, Posting API depend on a company's payment plan. 

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
api_instance = smartrecruiters_python_client.JobsApi()
id = 'id_example' # str | Identifier of a job
publication = smartrecruiters_python_client.Publication() # Publication | Publication object (optional)

try: 
    # Publishes a default job ad
    api_instance.jobs_publication_create(id, publication=publication)
except ApiException as e:
    print("Exception when calling JobsApi->jobs_publication_create: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Identifier of a job | 
 **publication** | [**Publication**](Publication.md)| Publication object | [optional] 

### Return type

void (empty response body)

### Authorization

[key](../README.md#key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json; charset=utf-8

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **jobs_publication_unpublish**
> jobs_publication_unpublish(id)

Unpublishes a job from all sources

Unpublishes a job from all sources

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
api_instance = smartrecruiters_python_client.JobsApi()
id = 'id_example' # str | identifier of a job

try: 
    # Unpublishes a job from all sources
    api_instance.jobs_publication_unpublish(id)
except ApiException as e:
    print("Exception when calling JobsApi->jobs_publication_unpublish: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| identifier of a job | 

### Return type

void (empty response body)

### Authorization

[key](../README.md#key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json; charset=utf-8

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **jobs_status_history_get**
> JobStatusHistory jobs_status_history_get(id)

Job status history

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
api_instance = smartrecruiters_python_client.JobsApi()
id = 'id_example' # str | identifier of a job

try: 
    # Job status history
    api_response = api_instance.jobs_status_history_get(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling JobsApi->jobs_status_history_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| identifier of a job | 

### Return type

[**JobStatusHistory**](JobStatusHistory.md)

### Authorization

[key](../README.md#key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json; charset=utf-8

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **jobs_status_update**
> JobStatusUpdate jobs_status_update(job_status, id)

Updates job status

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
api_instance = smartrecruiters_python_client.JobsApi()
job_status = smartrecruiters_python_client.JobStatusUpdate() # JobStatusUpdate | 
id = 'id_example' # str | Identifier of a job

try: 
    # Updates job status
    api_response = api_instance.jobs_status_update(job_status, id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling JobsApi->jobs_status_update: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **job_status** | [**JobStatusUpdate**](JobStatusUpdate.md)|  | 
 **id** | **str**| Identifier of a job | 

### Return type

[**JobStatusUpdate**](JobStatusUpdate.md)

### Authorization

[key](../README.md#key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json; charset=utf-8

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **jobs_update**
> JobDetails jobs_update(id, job=job)

Updates job

Enables you to update job. This operation requires passing an instance of the Job object as part of the PUT request. Ignores all nonexistent job properties and job properties values. Returns an updated job.

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
api_instance = smartrecruiters_python_client.JobsApi()
id = 'id_example' # str | Identifier of a job
job = smartrecruiters_python_client.JobInput() # JobInput | Job object that needs to be updated (optional)

try: 
    # Updates job
    api_response = api_instance.jobs_update(id, job=job)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling JobsApi->jobs_update: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Identifier of a job | 
 **job** | [**JobInput**](JobInput.md)| Job object that needs to be updated | [optional] 

### Return type

[**JobDetails**](JobDetails.md)

### Authorization

[key](../README.md#key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json; charset=utf-8

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)


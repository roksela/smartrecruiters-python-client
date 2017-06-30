# smartrecruiters_python_client.ConfigurationApi

All URIs are relative to *https://api.smartrecruiters.com/*

Method | HTTP request | Description
------------- | ------------- | -------------
[**configuration_candidate_properties_all**](ConfigurationApi.md#configuration_candidate_properties_all) | **GET** /configuration/candidate-properties | Get a list of available candidate properties
[**configuration_candidate_properties_get**](ConfigurationApi.md#configuration_candidate_properties_get) | **GET** /configuration/candidate-properties/{id} | Get candidate property by id
[**configuration_candidate_properties_values_all**](ConfigurationApi.md#configuration_candidate_properties_values_all) | **GET** /configuration/candidate-properties/{id}/values | Get Candidate Property values
[**configuration_candidate_properties_values_create**](ConfigurationApi.md#configuration_candidate_properties_values_create) | **POST** /configuration/candidate-properties/{id}/values | Create candidate property value
[**configuration_candidate_properties_values_get**](ConfigurationApi.md#configuration_candidate_properties_values_get) | **GET** /configuration/candidate-properties/{id}/values/{valueId} | Get Candidate Property value by id
[**configuration_candidate_properties_values_update**](ConfigurationApi.md#configuration_candidate_properties_values_update) | **PUT** /configuration/candidate-properties/{id}/values/{valueId} | Update candidate property value label
[**configuration_company_my**](ConfigurationApi.md#configuration_company_my) | **GET** /configuration/company | Get company information
[**configuration_department_all**](ConfigurationApi.md#configuration_department_all) | **GET** /configuration/departments | Get departments
[**configuration_department_create**](ConfigurationApi.md#configuration_department_create) | **POST** /configuration/departments | Creates department
[**configuration_department_get**](ConfigurationApi.md#configuration_department_get) | **GET** /configuration/departments/{id} | Get department
[**configuration_hiring_process_all**](ConfigurationApi.md#configuration_hiring_process_all) | **GET** /configuration/hiring-processes | Get list of hiring process
[**configuration_hiring_process_get**](ConfigurationApi.md#configuration_hiring_process_get) | **GET** /configuration/hiring-processes/{id} | Get hiring process
[**configuration_job_properties_activate**](ConfigurationApi.md#configuration_job_properties_activate) | **PUT** /configuration/job-properties/{id}/activation | Activate a job property
[**configuration_job_properties_all**](ConfigurationApi.md#configuration_job_properties_all) | **GET** /configuration/job-properties | Get a list of available job properties
[**configuration_job_properties_create**](ConfigurationApi.md#configuration_job_properties_create) | **POST** /configuration/job-properties | Create a job property
[**configuration_job_properties_deactivate**](ConfigurationApi.md#configuration_job_properties_deactivate) | **DELETE** /configuration/job-properties/{id}/activation | Deactivate a job property
[**configuration_job_properties_dependents_all**](ConfigurationApi.md#configuration_job_properties_dependents_all) | **GET** /configuration/job-properties/{id}/dependents | Get job property&#39;s dependents
[**configuration_job_properties_dependents_create**](ConfigurationApi.md#configuration_job_properties_dependents_create) | **POST** /configuration/job-properties/{id}/dependents | Create job property dependents
[**configuration_job_properties_dependents_remove**](ConfigurationApi.md#configuration_job_properties_dependents_remove) | **DELETE** /configuration/job-properties/{id}/dependents/{dependentId} | Remove job property&#39;s dependent
[**configuration_job_properties_dependents_values_add**](ConfigurationApi.md#configuration_job_properties_dependents_values_add) | **POST** /configuration/job-properties/{id}/values/{valueId}/dependents/{dependentId}/values | Add job property&#39;s dependent value
[**configuration_job_properties_dependents_values_all**](ConfigurationApi.md#configuration_job_properties_dependents_values_all) | **GET** /configuration/job-properties/{id}/dependents/{dependentId}/values | Get dependent job property&#39;s values
[**configuration_job_properties_dependents_values_get**](ConfigurationApi.md#configuration_job_properties_dependents_values_get) | **GET** /configuration/job-properties/{id}/values/{valueId}/dependents/{dependentId}/values | Get job property&#39;s dependent values
[**configuration_job_properties_dependents_values_remove**](ConfigurationApi.md#configuration_job_properties_dependents_values_remove) | **DELETE** /configuration/job-properties/{id}/values/{valueId}/dependents/{dependentId}/values/{dependentValueId} | Remove job property&#39;s dependent values relationship
[**configuration_job_properties_get**](ConfigurationApi.md#configuration_job_properties_get) | **GET** /configuration/job-properties/{id} | Get job property by id
[**configuration_job_properties_update**](ConfigurationApi.md#configuration_job_properties_update) | **PATCH** /configuration/job-properties/{id} | Update a job property
[**configuration_job_properties_values_archive**](ConfigurationApi.md#configuration_job_properties_values_archive) | **PUT** /configuration/job-properties/{id}/archive-values/{valueId} | Archive a job property value
[**configuration_job_properties_values_create**](ConfigurationApi.md#configuration_job_properties_values_create) | **POST** /configuration/job-properties/{id}/values | Create a job property value
[**configuration_job_properties_values_deprecated_archive**](ConfigurationApi.md#configuration_job_properties_values_deprecated_archive) | **DELETE** /configuration/job-properties/{id}/values/{valueId} | Archive a job property value
[**configuration_job_properties_values_deprecated_unarchive**](ConfigurationApi.md#configuration_job_properties_values_deprecated_unarchive) | **PUT** /configuration/job-properties/{id}/values/{valueId} | Unarchive a job property value
[**configuration_job_properties_values_get**](ConfigurationApi.md#configuration_job_properties_values_get) | **GET** /configuration/job-properties/{id}/values | Get available job property values
[**configuration_job_properties_values_unarchive**](ConfigurationApi.md#configuration_job_properties_values_unarchive) | **DELETE** /configuration/job-properties/{id}/archive-values/{valueId} | Unarchive a job property value
[**configuration_job_properties_values_update**](ConfigurationApi.md#configuration_job_properties_values_update) | **PATCH** /configuration/job-properties/{id}/values/{valueId} | Update a job property value
[**configuration_offer_properties_all**](ConfigurationApi.md#configuration_offer_properties_all) | **GET** /configuration/offer-properties | Get a list of available offer properties
[**configuration_reasons_rejection_all**](ConfigurationApi.md#configuration_reasons_rejection_all) | **GET** /configuration/rejection-reasons | Get rejection reasons
[**configuration_reasons_withdrawal_all**](ConfigurationApi.md#configuration_reasons_withdrawal_all) | **GET** /configuration/withdrawal-reasons | Get withdrawal reasons
[**configuration_source_types**](ConfigurationApi.md#configuration_source_types) | **GET** /configuration/sources | List candidate source types with subtypes
[**configuration_source_values_all**](ConfigurationApi.md#configuration_source_values_all) | **GET** /configuration/sources/{sourceType}/values | List candidate sources
[**configuration_source_values_single**](ConfigurationApi.md#configuration_source_values_single) | **GET** /configuration/sources/{sourceType}/values/{sourceValueId} | Get a candidate source


# **configuration_candidate_properties_all**
> CandidatePropertyDefinitionList configuration_candidate_properties_all()

Get a list of available candidate properties

Get all candidate properties and their configuration for a company

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
api_instance = smartrecruiters_python_client.ConfigurationApi()

try: 
    # Get a list of available candidate properties
    api_response = api_instance.configuration_candidate_properties_all()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ConfigurationApi->configuration_candidate_properties_all: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**CandidatePropertyDefinitionList**](CandidatePropertyDefinitionList.md)

### Authorization

[key](../README.md#key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json; charset=utf-8

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **configuration_candidate_properties_get**
> CandidatePropertyDefinition configuration_candidate_properties_get(id)

Get candidate property by id

Get candidate property details and its configuration by id.

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
api_instance = smartrecruiters_python_client.ConfigurationApi()
id = 'id_example' # str | Identifier of candidate property

try: 
    # Get candidate property by id
    api_response = api_instance.configuration_candidate_properties_get(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ConfigurationApi->configuration_candidate_properties_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Identifier of candidate property | 

### Return type

[**CandidatePropertyDefinition**](CandidatePropertyDefinition.md)

### Authorization

[key](../README.md#key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json; charset=utf-8

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **configuration_candidate_properties_values_all**
> CandidatePropertyValueList configuration_candidate_properties_values_all(id)

Get Candidate Property values

Lists all available values for given candidate property id. This endpoint is available only for SINGLE_SELECT candidate property type.

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
api_instance = smartrecruiters_python_client.ConfigurationApi()
id = 'id_example' # str | Identifier of candidate property

try: 
    # Get Candidate Property values
    api_response = api_instance.configuration_candidate_properties_values_all(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ConfigurationApi->configuration_candidate_properties_values_all: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Identifier of candidate property | 

### Return type

[**CandidatePropertyValueList**](CandidatePropertyValueList.md)

### Authorization

[key](../README.md#key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json; charset=utf-8

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **configuration_candidate_properties_values_create**
> CandidatePropertyValue configuration_candidate_properties_values_create(id, candidate_property_value)

Create candidate property value

Create SINGLE_SELECT candidate property value

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
api_instance = smartrecruiters_python_client.ConfigurationApi()
id = 'id_example' # str | Identifier of candidate property
candidate_property_value = smartrecruiters_python_client.CandidatePropertyValue() # CandidatePropertyValue | Candidate property value.

try: 
    # Create candidate property value
    api_response = api_instance.configuration_candidate_properties_values_create(id, candidate_property_value)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ConfigurationApi->configuration_candidate_properties_values_create: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Identifier of candidate property | 
 **candidate_property_value** | [**CandidatePropertyValue**](CandidatePropertyValue.md)| Candidate property value. | 

### Return type

[**CandidatePropertyValue**](CandidatePropertyValue.md)

### Authorization

[key](../README.md#key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json; charset=utf-8

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **configuration_candidate_properties_values_get**
> CandidatePropertyValue configuration_candidate_properties_values_get(id, value_id)

Get Candidate Property value by id

Get Candidate Property value by its id.

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
api_instance = smartrecruiters_python_client.ConfigurationApi()
id = 'id_example' # str | Identifier of candidate property
value_id = 'value_id_example' # str | Identifier of candidate property value

try: 
    # Get Candidate Property value by id
    api_response = api_instance.configuration_candidate_properties_values_get(id, value_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ConfigurationApi->configuration_candidate_properties_values_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Identifier of candidate property | 
 **value_id** | **str**| Identifier of candidate property value | 

### Return type

[**CandidatePropertyValue**](CandidatePropertyValue.md)

### Authorization

[key](../README.md#key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json; charset=utf-8

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **configuration_candidate_properties_values_update**
> CandidatePropertyValue configuration_candidate_properties_values_update(id, value_id, candidate_property_value_label)

Update candidate property value label

Update candidate property value label

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
api_instance = smartrecruiters_python_client.ConfigurationApi()
id = 'id_example' # str | Identifier of candidate property
value_id = 'value_id_example' # str | Identifier of candidate property value
candidate_property_value_label = smartrecruiters_python_client.CandidatePropertyValueLabel() # CandidatePropertyValueLabel | Candidate property value label.

try: 
    # Update candidate property value label
    api_response = api_instance.configuration_candidate_properties_values_update(id, value_id, candidate_property_value_label)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ConfigurationApi->configuration_candidate_properties_values_update: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Identifier of candidate property | 
 **value_id** | **str**| Identifier of candidate property value | 
 **candidate_property_value_label** | [**CandidatePropertyValueLabel**](CandidatePropertyValueLabel.md)| Candidate property value label. | 

### Return type

[**CandidatePropertyValue**](CandidatePropertyValue.md)

### Authorization

[key](../README.md#key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json; charset=utf-8

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **configuration_company_my**
> CompanyConfiguration configuration_company_my()

Get company information

Get all information about your company.

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
api_instance = smartrecruiters_python_client.ConfigurationApi()

try: 
    # Get company information
    api_response = api_instance.configuration_company_my()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ConfigurationApi->configuration_company_my: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**CompanyConfiguration**](CompanyConfiguration.md)

### Authorization

[key](../README.md#key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json; charset=utf-8

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **configuration_department_all**
> Departments configuration_department_all()

Get departments

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
api_instance = smartrecruiters_python_client.ConfigurationApi()

try: 
    # Get departments
    api_response = api_instance.configuration_department_all()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ConfigurationApi->configuration_department_all: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**Departments**](Departments.md)

### Authorization

[key](../README.md#key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json; charset=utf-8

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **configuration_department_create**
> Department configuration_department_create(department)

Creates department

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
api_instance = smartrecruiters_python_client.ConfigurationApi()
department = smartrecruiters_python_client.Department() # Department | department to be created

try: 
    # Creates department
    api_response = api_instance.configuration_department_create(department)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ConfigurationApi->configuration_department_create: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **department** | [**Department**](Department.md)| department to be created | 

### Return type

[**Department**](Department.md)

### Authorization

[key](../README.md#key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json; charset=utf-8

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **configuration_department_get**
> Department configuration_department_get(id)

Get department

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
api_instance = smartrecruiters_python_client.ConfigurationApi()
id = 'id_example' # str | Identifier of a department

try: 
    # Get department
    api_response = api_instance.configuration_department_get(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ConfigurationApi->configuration_department_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Identifier of a department | 

### Return type

[**Department**](Department.md)

### Authorization

[key](../README.md#key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json; charset=utf-8

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **configuration_hiring_process_all**
> HiringProcesses configuration_hiring_process_all()

Get list of hiring process

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
api_instance = smartrecruiters_python_client.ConfigurationApi()

try: 
    # Get list of hiring process
    api_response = api_instance.configuration_hiring_process_all()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ConfigurationApi->configuration_hiring_process_all: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**HiringProcesses**](HiringProcesses.md)

### Authorization

[key](../README.md#key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json; charset=utf-8

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **configuration_hiring_process_get**
> HiringProcess configuration_hiring_process_get(id)

Get hiring process

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
api_instance = smartrecruiters_python_client.ConfigurationApi()
id = 'id_example' # str | Identifier of a hiring process

try: 
    # Get hiring process
    api_response = api_instance.configuration_hiring_process_get(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ConfigurationApi->configuration_hiring_process_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Identifier of a hiring process | 

### Return type

[**HiringProcess**](HiringProcess.md)

### Authorization

[key](../README.md#key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json; charset=utf-8

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **configuration_job_properties_activate**
> configuration_job_properties_activate(id)

Activate a job property

Activates a job property with given id.

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
api_instance = smartrecruiters_python_client.ConfigurationApi()
id = 'id_example' # str | Identifier of a job property

try: 
    # Activate a job property
    api_instance.configuration_job_properties_activate(id)
except ApiException as e:
    print("Exception when calling ConfigurationApi->configuration_job_properties_activate: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Identifier of a job property | 

### Return type

void (empty response body)

### Authorization

[key](../README.md#key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json; charset=utf-8

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **configuration_job_properties_all**
> JobPropertyDefinitionList configuration_job_properties_all()

Get a list of available job properties

Get a list of available job properties.

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
api_instance = smartrecruiters_python_client.ConfigurationApi()

try: 
    # Get a list of available job properties
    api_response = api_instance.configuration_job_properties_all()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ConfigurationApi->configuration_job_properties_all: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**JobPropertyDefinitionList**](JobPropertyDefinitionList.md)

### Authorization

[key](../README.md#key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json; charset=utf-8

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **configuration_job_properties_create**
> JobPropertyDefinition configuration_job_properties_create(job_property_definition=job_property_definition)

Create a job property

Creates a job property

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
api_instance = smartrecruiters_python_client.ConfigurationApi()
job_property_definition = smartrecruiters_python_client.JobPropertyDefinition() # JobPropertyDefinition | job property to be created (optional)

try: 
    # Create a job property
    api_response = api_instance.configuration_job_properties_create(job_property_definition=job_property_definition)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ConfigurationApi->configuration_job_properties_create: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **job_property_definition** | [**JobPropertyDefinition**](JobPropertyDefinition.md)| job property to be created | [optional] 

### Return type

[**JobPropertyDefinition**](JobPropertyDefinition.md)

### Authorization

[key](../README.md#key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json; charset=utf-8

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **configuration_job_properties_deactivate**
> configuration_job_properties_deactivate(id)

Deactivate a job property

Deactivates a job property.

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
api_instance = smartrecruiters_python_client.ConfigurationApi()
id = 'id_example' # str | Identifier of a job property

try: 
    # Deactivate a job property
    api_instance.configuration_job_properties_deactivate(id)
except ApiException as e:
    print("Exception when calling ConfigurationApi->configuration_job_properties_deactivate: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Identifier of a job property | 

### Return type

void (empty response body)

### Authorization

[key](../README.md#key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json; charset=utf-8

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **configuration_job_properties_dependents_all**
> DependentJobProperties configuration_job_properties_dependents_all(id)

Get job property's dependents

Get list of job property's dependents

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
api_instance = smartrecruiters_python_client.ConfigurationApi()
id = 'id_example' # str | Identifier of a job property

try: 
    # Get job property's dependents
    api_response = api_instance.configuration_job_properties_dependents_all(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ConfigurationApi->configuration_job_properties_dependents_all: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Identifier of a job property | 

### Return type

[**DependentJobProperties**](DependentJobProperties.md)

### Authorization

[key](../README.md#key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json; charset=utf-8

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **configuration_job_properties_dependents_create**
> DependentJobProperties configuration_job_properties_dependents_create(id, dependent_job_properties_ids)

Create job property dependents

Create dependencies between job properties

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
api_instance = smartrecruiters_python_client.ConfigurationApi()
id = 'id_example' # str | Identifier of a job property
dependent_job_properties_ids = smartrecruiters_python_client.DependentJobPropertiesIds() # DependentJobPropertiesIds | Job properties' id

try: 
    # Create job property dependents
    api_response = api_instance.configuration_job_properties_dependents_create(id, dependent_job_properties_ids)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ConfigurationApi->configuration_job_properties_dependents_create: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Identifier of a job property | 
 **dependent_job_properties_ids** | [**DependentJobPropertiesIds**](DependentJobPropertiesIds.md)| Job properties&#39; id | 

### Return type

[**DependentJobProperties**](DependentJobProperties.md)

### Authorization

[key](../README.md#key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json; charset=utf-8

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **configuration_job_properties_dependents_remove**
> configuration_job_properties_dependents_remove(id, dependent_id)

Remove job property's dependent

Remove dependency between job properties

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
api_instance = smartrecruiters_python_client.ConfigurationApi()
id = 'id_example' # str | Identifier of a job property
dependent_id = 'dependent_id_example' # str | Identifier of a job property's dependent

try: 
    # Remove job property's dependent
    api_instance.configuration_job_properties_dependents_remove(id, dependent_id)
except ApiException as e:
    print("Exception when calling ConfigurationApi->configuration_job_properties_dependents_remove: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Identifier of a job property | 
 **dependent_id** | **str**| Identifier of a job property&#39;s dependent | 

### Return type

void (empty response body)

### Authorization

[key](../README.md#key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json; charset=utf-8

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **configuration_job_properties_dependents_values_add**
> configuration_job_properties_dependents_values_add(id, value_id, dependent_id, dependent_job_property_value_id)

Add job property's dependent value

Add job property's dependent value for specific job property's value

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
api_instance = smartrecruiters_python_client.ConfigurationApi()
id = 'id_example' # str | Identifier of a job property
value_id = 'value_id_example' # str | Identifier of a job property value
dependent_id = 'dependent_id_example' # str | Identifier of job property's dependent
dependent_job_property_value_id = smartrecruiters_python_client.Identifiable() # Identifiable | Identifier of job property's dependent value

try: 
    # Add job property's dependent value
    api_instance.configuration_job_properties_dependents_values_add(id, value_id, dependent_id, dependent_job_property_value_id)
except ApiException as e:
    print("Exception when calling ConfigurationApi->configuration_job_properties_dependents_values_add: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Identifier of a job property | 
 **value_id** | **str**| Identifier of a job property value | 
 **dependent_id** | **str**| Identifier of job property&#39;s dependent | 
 **dependent_job_property_value_id** | [**Identifiable**](Identifiable.md)| Identifier of job property&#39;s dependent value | 

### Return type

void (empty response body)

### Authorization

[key](../README.md#key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json; charset=utf-8

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **configuration_job_properties_dependents_values_all**
> DependentJobPropertyValuesRelations configuration_job_properties_dependents_values_all(id, dependent_id)

Get dependent job property's values

Get dependent job property's values with corelation to the parent field.

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
api_instance = smartrecruiters_python_client.ConfigurationApi()
id = 'id_example' # str | Identifier of a job property
dependent_id = 'dependent_id_example' # str | Identifier of dependent job property

try: 
    # Get dependent job property's values
    api_response = api_instance.configuration_job_properties_dependents_values_all(id, dependent_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ConfigurationApi->configuration_job_properties_dependents_values_all: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Identifier of a job property | 
 **dependent_id** | **str**| Identifier of dependent job property | 

### Return type

[**DependentJobPropertyValuesRelations**](DependentJobPropertyValuesRelations.md)

### Authorization

[key](../README.md#key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json; charset=utf-8

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **configuration_job_properties_dependents_values_get**
> DependentJobPropertyValues configuration_job_properties_dependents_values_get(id, value_id, dependent_id)

Get job property's dependent values

Get list of job property's dependent values for specific job property's value

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
api_instance = smartrecruiters_python_client.ConfigurationApi()
id = 'id_example' # str | Identifier of a job property
value_id = 'value_id_example' # str | Identifier of a job property value
dependent_id = 'dependent_id_example' # str | Identifier of job property's dependent

try: 
    # Get job property's dependent values
    api_response = api_instance.configuration_job_properties_dependents_values_get(id, value_id, dependent_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ConfigurationApi->configuration_job_properties_dependents_values_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Identifier of a job property | 
 **value_id** | **str**| Identifier of a job property value | 
 **dependent_id** | **str**| Identifier of job property&#39;s dependent | 

### Return type

[**DependentJobPropertyValues**](DependentJobPropertyValues.md)

### Authorization

[key](../README.md#key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json; charset=utf-8

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **configuration_job_properties_dependents_values_remove**
> configuration_job_properties_dependents_values_remove(id, value_id, dependent_id, dependent_value_id)

Remove job property's dependent values relationship

Remove relationship between dependent job properties values

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
api_instance = smartrecruiters_python_client.ConfigurationApi()
id = 'id_example' # str | Identifier of a job property
value_id = 'value_id_example' # str | Identifier of a job property value
dependent_id = 'dependent_id_example' # str | Identifier of job property's dependent
dependent_value_id = 'dependent_value_id_example' # str | Identifier of job property's dependent value

try: 
    # Remove job property's dependent values relationship
    api_instance.configuration_job_properties_dependents_values_remove(id, value_id, dependent_id, dependent_value_id)
except ApiException as e:
    print("Exception when calling ConfigurationApi->configuration_job_properties_dependents_values_remove: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Identifier of a job property | 
 **value_id** | **str**| Identifier of a job property value | 
 **dependent_id** | **str**| Identifier of job property&#39;s dependent | 
 **dependent_value_id** | **str**| Identifier of job property&#39;s dependent value | 

### Return type

void (empty response body)

### Authorization

[key](../README.md#key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json; charset=utf-8

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **configuration_job_properties_get**
> JobPropertyDefinition configuration_job_properties_get(id)

Get job property by id

Get job property by id

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
api_instance = smartrecruiters_python_client.ConfigurationApi()
id = 'id_example' # str | Identifier of a job property

try: 
    # Get job property by id
    api_response = api_instance.configuration_job_properties_get(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ConfigurationApi->configuration_job_properties_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Identifier of a job property | 

### Return type

[**JobPropertyDefinition**](JobPropertyDefinition.md)

### Authorization

[key](../README.md#key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json; charset=utf-8

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **configuration_job_properties_update**
> JobPropertyDefinition configuration_job_properties_update(id, json_patch=json_patch)

Update a job property

Updates a job property.

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
api_instance = smartrecruiters_python_client.ConfigurationApi()
id = 'id_example' # str | Identifier of a job property
json_patch = smartrecruiters_python_client.JSONPatch() # JSONPatch | patch request (optional)

try: 
    # Update a job property
    api_response = api_instance.configuration_job_properties_update(id, json_patch=json_patch)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ConfigurationApi->configuration_job_properties_update: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Identifier of a job property | 
 **json_patch** | [**JSONPatch**](JSONPatch.md)| patch request | [optional] 

### Return type

[**JobPropertyDefinition**](JobPropertyDefinition.md)

### Authorization

[key](../README.md#key)

### HTTP request headers

 - **Content-Type**: application/json-patch+json
 - **Accept**: application/json; charset=utf-8

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **configuration_job_properties_values_archive**
> configuration_job_properties_values_archive(id, value_id)

Archive a job property value

Archive a job property value

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
api_instance = smartrecruiters_python_client.ConfigurationApi()
id = 'id_example' # str | Identifier of a job property
value_id = 'value_id_example' # str | Identifier of a job property value to be archived

try: 
    # Archive a job property value
    api_instance.configuration_job_properties_values_archive(id, value_id)
except ApiException as e:
    print("Exception when calling ConfigurationApi->configuration_job_properties_values_archive: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Identifier of a job property | 
 **value_id** | **str**| Identifier of a job property value to be archived | 

### Return type

void (empty response body)

### Authorization

[key](../README.md#key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json; charset=utf-8

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **configuration_job_properties_values_create**
> JobPropertyValueDefinition configuration_job_properties_values_create(id, job_property_value_definition=job_property_value_definition)

Create a job property value

Creates a job property value.

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
api_instance = smartrecruiters_python_client.ConfigurationApi()
id = 'id_example' # str | Identifier of a job property
job_property_value_definition = smartrecruiters_python_client.JobPropertyValueDefinition() # JobPropertyValueDefinition | job property object to be created (optional)

try: 
    # Create a job property value
    api_response = api_instance.configuration_job_properties_values_create(id, job_property_value_definition=job_property_value_definition)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ConfigurationApi->configuration_job_properties_values_create: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Identifier of a job property | 
 **job_property_value_definition** | [**JobPropertyValueDefinition**](JobPropertyValueDefinition.md)| job property object to be created | [optional] 

### Return type

[**JobPropertyValueDefinition**](JobPropertyValueDefinition.md)

### Authorization

[key](../README.md#key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json; charset=utf-8

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **configuration_job_properties_values_deprecated_archive**
> configuration_job_properties_values_deprecated_archive(id, value_id)

Archive a job property value

Archive a job property value. Please use `PUT /configuration/job-properties/{id}/archive-values/{valueId}` instead.

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
api_instance = smartrecruiters_python_client.ConfigurationApi()
id = 'id_example' # str | Identifier of a job property
value_id = 'value_id_example' # str | Identifier of a job property value to be archived

try: 
    # Archive a job property value
    api_instance.configuration_job_properties_values_deprecated_archive(id, value_id)
except ApiException as e:
    print("Exception when calling ConfigurationApi->configuration_job_properties_values_deprecated_archive: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Identifier of a job property | 
 **value_id** | **str**| Identifier of a job property value to be archived | 

### Return type

void (empty response body)

### Authorization

[key](../README.md#key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json; charset=utf-8

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **configuration_job_properties_values_deprecated_unarchive**
> configuration_job_properties_values_deprecated_unarchive(id, value_id)

Unarchive a job property value

Unarchive a job property value. `DELETE /configuration/job-properties/{id}/archive-values/{valueId}` instead.

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
api_instance = smartrecruiters_python_client.ConfigurationApi()
id = 'id_example' # str | Identifier of a job property
value_id = 'value_id_example' # str | Identifier of a job property value to be unarchived

try: 
    # Unarchive a job property value
    api_instance.configuration_job_properties_values_deprecated_unarchive(id, value_id)
except ApiException as e:
    print("Exception when calling ConfigurationApi->configuration_job_properties_values_deprecated_unarchive: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Identifier of a job property | 
 **value_id** | **str**| Identifier of a job property value to be unarchived | 

### Return type

void (empty response body)

### Authorization

[key](../README.md#key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json; charset=utf-8

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **configuration_job_properties_values_get**
> JobPropertyValueDefinitionList configuration_job_properties_values_get(id)

Get available job property values

Get available job property values.

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
api_instance = smartrecruiters_python_client.ConfigurationApi()
id = 'id_example' # str | Identifier of a job property

try: 
    # Get available job property values
    api_response = api_instance.configuration_job_properties_values_get(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ConfigurationApi->configuration_job_properties_values_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Identifier of a job property | 

### Return type

[**JobPropertyValueDefinitionList**](JobPropertyValueDefinitionList.md)

### Authorization

[key](../README.md#key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json; charset=utf-8

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **configuration_job_properties_values_unarchive**
> configuration_job_properties_values_unarchive(id, value_id)

Unarchive a job property value

Unarchive a job property value

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
api_instance = smartrecruiters_python_client.ConfigurationApi()
id = 'id_example' # str | Identifier of a job property
value_id = 'value_id_example' # str | Identifier of a job property value to be unarchived

try: 
    # Unarchive a job property value
    api_instance.configuration_job_properties_values_unarchive(id, value_id)
except ApiException as e:
    print("Exception when calling ConfigurationApi->configuration_job_properties_values_unarchive: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Identifier of a job property | 
 **value_id** | **str**| Identifier of a job property value to be unarchived | 

### Return type

void (empty response body)

### Authorization

[key](../README.md#key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json; charset=utf-8

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **configuration_job_properties_values_update**
> JobPropertyValueDefinition configuration_job_properties_values_update(id, value_id, json_patch=json_patch)

Update a job property value

Update a job property value. Returns an updated job property value object.

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
api_instance = smartrecruiters_python_client.ConfigurationApi()
id = 'id_example' # str | Identifier of a job property
value_id = 'value_id_example' # str | Identifier of a job property value to be updated
json_patch = smartrecruiters_python_client.JSONPatch() # JSONPatch | patch request (optional)

try: 
    # Update a job property value
    api_response = api_instance.configuration_job_properties_values_update(id, value_id, json_patch=json_patch)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ConfigurationApi->configuration_job_properties_values_update: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Identifier of a job property | 
 **value_id** | **str**| Identifier of a job property value to be updated | 
 **json_patch** | [**JSONPatch**](JSONPatch.md)| patch request | [optional] 

### Return type

[**JobPropertyValueDefinition**](JobPropertyValueDefinition.md)

### Authorization

[key](../README.md#key)

### HTTP request headers

 - **Content-Type**: application/json-patch+json
 - **Accept**: application/json; charset=utf-8

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **configuration_offer_properties_all**
> OfferPropertiesDefinition configuration_offer_properties_all()

Get a list of available offer properties

Get a list of available offer properties.

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
api_instance = smartrecruiters_python_client.ConfigurationApi()

try: 
    # Get a list of available offer properties
    api_response = api_instance.configuration_offer_properties_all()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ConfigurationApi->configuration_offer_properties_all: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**OfferPropertiesDefinition**](OfferPropertiesDefinition.md)

### Authorization

[key](../README.md#key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json; charset=utf-8

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **configuration_reasons_rejection_all**
> Properties configuration_reasons_rejection_all()

Get rejection reasons

Get rejection reasons

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
api_instance = smartrecruiters_python_client.ConfigurationApi()

try: 
    # Get rejection reasons
    api_response = api_instance.configuration_reasons_rejection_all()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ConfigurationApi->configuration_reasons_rejection_all: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**Properties**](Properties.md)

### Authorization

[key](../README.md#key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json; charset=utf-8

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **configuration_reasons_withdrawal_all**
> Properties configuration_reasons_withdrawal_all()

Get withdrawal reasons

Get withdrawal reasons

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
api_instance = smartrecruiters_python_client.ConfigurationApi()

try: 
    # Get withdrawal reasons
    api_response = api_instance.configuration_reasons_withdrawal_all()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ConfigurationApi->configuration_reasons_withdrawal_all: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**Properties**](Properties.md)

### Authorization

[key](../README.md#key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json; charset=utf-8

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **configuration_source_types**
> SourceTypes configuration_source_types()

List candidate source types with subtypes

Get a list of all available candidate source type with subtypes

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
api_instance = smartrecruiters_python_client.ConfigurationApi()

try: 
    # List candidate source types with subtypes
    api_response = api_instance.configuration_source_types()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ConfigurationApi->configuration_source_types: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**SourceTypes**](SourceTypes.md)

### Authorization

[key](../README.md#key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json; charset=utf-8

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **configuration_source_values_all**
> Sources configuration_source_values_all(source_type, source_sub_type=source_sub_type, limit=limit, offset=offset)

List candidate sources

Get a list of all available candidate sources by type.

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
api_instance = smartrecruiters_python_client.ConfigurationApi()
source_type = 'source_type_example' # str | Source type from /configuration/sources
source_sub_type = 'source_sub_type_example' # str | Source SubType (optional)
limit = 100 # int | number of elements to return. max value is 100 (optional) (default to 100)
offset = 0 # int | number of elements to skip while processing result (optional) (default to 0)

try: 
    # List candidate sources
    api_response = api_instance.configuration_source_values_all(source_type, source_sub_type=source_sub_type, limit=limit, offset=offset)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ConfigurationApi->configuration_source_values_all: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **source_type** | **str**| Source type from /configuration/sources | 
 **source_sub_type** | **str**| Source SubType | [optional] 
 **limit** | **int**| number of elements to return. max value is 100 | [optional] [default to 100]
 **offset** | **int**| number of elements to skip while processing result | [optional] [default to 0]

### Return type

[**Sources**](Sources.md)

### Authorization

[key](../README.md#key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json; charset=utf-8

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **configuration_source_values_single**
> Source configuration_source_values_single(source_type, source_value_id, source_sub_type=source_sub_type)

Get a candidate source

Get a single candidate sources for a given type.

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
api_instance = smartrecruiters_python_client.ConfigurationApi()
source_type = 'source_type_example' # str | Source type from /configuration/sources
source_value_id = 'source_value_id_example' # str | Source id
source_sub_type = 'source_sub_type_example' # str | Source SubType from  /configuration/sources (optional)

try: 
    # Get a candidate source
    api_response = api_instance.configuration_source_values_single(source_type, source_value_id, source_sub_type=source_sub_type)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ConfigurationApi->configuration_source_values_single: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **source_type** | **str**| Source type from /configuration/sources | 
 **source_value_id** | **str**| Source id | 
 **source_sub_type** | **str**| Source SubType from  /configuration/sources | [optional] 

### Return type

[**Source**](Source.md)

### Authorization

[key](../README.md#key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json; charset=utf-8

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)


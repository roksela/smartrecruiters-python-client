# smartrecruiters_python_client.UsersApi

All URIs are relative to *https://api.smartrecruiters.com/*

Method | HTTP request | Description
------------- | ------------- | -------------
[**users_activation_activate**](UsersApi.md#users_activation_activate) | **PUT** /users/{id}/activation | Activate a user
[**users_activation_deactivate**](UsersApi.md#users_activation_deactivate) | **DELETE** /users/{id}/activation | Deactivate a user
[**users_activation_delete**](UsersApi.md#users_activation_delete) | **DELETE** /users/{id} | Deactivate a user
[**users_activation_email_send**](UsersApi.md#users_activation_email_send) | **POST** /users/{id}/activation-email | Send an activation email to a user
[**users_all**](UsersApi.md#users_all) | **GET** /users | List users of your company
[**users_avatar_update**](UsersApi.md#users_avatar_update) | **PUT** /users/{id}/avatar | Update user avatar
[**users_create**](UsersApi.md#users_create) | **POST** /users | Create a new user.
[**users_get**](UsersApi.md#users_get) | **GET** /users/{id} | Get details of a user with given id
[**users_me**](UsersApi.md#users_me) | **GET** /users/me | Get details of my user
[**users_update**](UsersApi.md#users_update) | **PATCH** /users/{id} | Update a user


# **users_activation_activate**
> users_activation_activate(id)

Activate a user

Activate a user with given id. Users created via an API are not active. This method allows activating a user so he/she can sign in straight away. 

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
api_instance = smartrecruiters_python_client.UsersApi()
id = 'id_example' # str | Identifier of a user

try: 
    # Activate a user
    api_instance.users_activation_activate(id)
except ApiException as e:
    print("Exception when calling UsersApi->users_activation_activate: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Identifier of a user | 

### Return type

void (empty response body)

### Authorization

[key](../README.md#key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json; charset=utf-8

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **users_activation_deactivate**
> users_activation_deactivate(id)

Deactivate a user

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
api_instance = smartrecruiters_python_client.UsersApi()
id = 'id_example' # str | Identifier of a user

try: 
    # Deactivate a user
    api_instance.users_activation_deactivate(id)
except ApiException as e:
    print("Exception when calling UsersApi->users_activation_deactivate: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Identifier of a user | 

### Return type

void (empty response body)

### Authorization

[key](../README.md#key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json; charset=utf-8

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **users_activation_delete**
> users_activation_delete(id)

Deactivate a user

Deactivates a User with given Id. Please use `DELETE /users/{id}/activation` instead.

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
api_instance = smartrecruiters_python_client.UsersApi()
id = 'id_example' # str | Identifier of a user

try: 
    # Deactivate a user
    api_instance.users_activation_delete(id)
except ApiException as e:
    print("Exception when calling UsersApi->users_activation_delete: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Identifier of a user | 

### Return type

void (empty response body)

### Authorization

[key](../README.md#key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json; charset=utf-8

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **users_activation_email_send**
> users_activation_email_send(id)

Send an activation email to a user

Send an activation email to a user with given id. Users created via an API are not active. This method is an alternative to activating a user directly and allows sending an activation email in which a user will have to open a link and follow instructions on a screen to activate his/her account. 

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
api_instance = smartrecruiters_python_client.UsersApi()
id = 'id_example' # str | Identifier of a user

try: 
    # Send an activation email to a user
    api_instance.users_activation_email_send(id)
except ApiException as e:
    print("Exception when calling UsersApi->users_activation_email_send: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Identifier of a user | 

### Return type

void (empty response body)

### Authorization

[key](../README.md#key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json; charset=utf-8

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **users_all**
> Users users_all(q=q, limit=limit, offset=offset, updated_after=updated_after)

List users of your company

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
api_instance = smartrecruiters_python_client.UsersApi()
q = 'q_example' # str | full-text search query based on firstName, lastName, email (optional)
limit = 100 # int | number of elements to return. max value is 100 (optional) (default to 100)
offset = 0 # int | number of elements to skip while processing result (optional) (default to 0)
updated_after = '2013-10-20T19:20:30+01:00' # datetime | ISO8601-formatted time boundaries for the user update time, Format: yyyy-MM-ddTHH:mm:ss.SSSZZ (optional)

try: 
    # List users of your company
    api_response = api_instance.users_all(q=q, limit=limit, offset=offset, updated_after=updated_after)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UsersApi->users_all: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **q** | **str**| full-text search query based on firstName, lastName, email | [optional] 
 **limit** | **int**| number of elements to return. max value is 100 | [optional] [default to 100]
 **offset** | **int**| number of elements to skip while processing result | [optional] [default to 0]
 **updated_after** | **datetime**| ISO8601-formatted time boundaries for the user update time, Format: yyyy-MM-ddTHH:mm:ss.SSSZZ | [optional] 

### Return type

[**Users**](Users.md)

### Authorization

[key](../README.md#key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json; charset=utf-8

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **users_avatar_update**
> users_avatar_update(id, file)

Update user avatar

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
api_instance = smartrecruiters_python_client.UsersApi()
id = 'id_example' # str | Identifier of an user
file = '/path/to/file.txt' # file | The file to upload.

try: 
    # Update user avatar
    api_instance.users_avatar_update(id, file)
except ApiException as e:
    print("Exception when calling UsersApi->users_avatar_update: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Identifier of an user | 
 **file** | **file**| The file to upload. | 

### Return type

void (empty response body)

### Authorization

[key](../README.md#key)

### HTTP request headers

 - **Content-Type**: multipart/form-data
 - **Accept**: application/json; charset=utf-8

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **users_create**
> UserEntity users_create(user=user)

Create a new user.

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
api_instance = smartrecruiters_python_client.UsersApi()
user = smartrecruiters_python_client.NewUser() # NewUser | User object to be created (optional)

try: 
    # Create a new user.
    api_response = api_instance.users_create(user=user)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UsersApi->users_create: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **user** | [**NewUser**](NewUser.md)| User object to be created | [optional] 

### Return type

[**UserEntity**](UserEntity.md)

### Authorization

[key](../README.md#key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json; charset=utf-8

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **users_get**
> UserEntity users_get(id)

Get details of a user with given id

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
api_instance = smartrecruiters_python_client.UsersApi()
id = 'id_example' # str | Identifier of a user

try: 
    # Get details of a user with given id
    api_response = api_instance.users_get(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UsersApi->users_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Identifier of a user | 

### Return type

[**UserEntity**](UserEntity.md)

### Authorization

[key](../README.md#key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json; charset=utf-8

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **users_me**
> UserEntity users_me()

Get details of my user

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
api_instance = smartrecruiters_python_client.UsersApi()

try: 
    # Get details of my user
    api_response = api_instance.users_me()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UsersApi->users_me: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**UserEntity**](UserEntity.md)

### Authorization

[key](../README.md#key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json; charset=utf-8

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **users_update**
> UserEntity users_update(id, json_patch=json_patch)

Update a user

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
api_instance = smartrecruiters_python_client.UsersApi()
id = 'id_example' # str | Identifier of an user
json_patch = smartrecruiters_python_client.JSONPatch() # JSONPatch | patch request (optional)

try: 
    # Update a user
    api_response = api_instance.users_update(id, json_patch=json_patch)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UsersApi->users_update: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Identifier of an user | 
 **json_patch** | [**JSONPatch**](JSONPatch.md)| patch request | [optional] 

### Return type

[**UserEntity**](UserEntity.md)

### Authorization

[key](../README.md#key)

### HTTP request headers

 - **Content-Type**: application/json-patch+json
 - **Accept**: application/json; charset=utf-8

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)


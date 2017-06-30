# smartrecruiters_python_client.MessagesApi

All URIs are relative to *https://api.smartrecruiters.com/*

Method | HTTP request | Description
------------- | ------------- | -------------
[**messages_shares_create**](MessagesApi.md#messages_shares_create) | **POST** /messages/shares | Shares new messages on Hireloop with Users, Hiring Teams or Everyone and sends emails.
[**messages_shares_delete**](MessagesApi.md#messages_shares_delete) | **DELETE** /messages/shares/{id} | Delete a message


# **messages_shares_create**
> MessageDetails messages_shares_create(message=message)

Shares new messages on Hireloop with Users, Hiring Teams or Everyone and sends emails.

How does it work: * In **content** field, provide a text to be shared. No HTML tags are allowed. * @-mention users to send them an email   * In **content** field use **@[USER:id]** to mention a User, e.g. @[USER:324132421] * Email responses are added as comments to your update * \\#-tag candidates to link updates to their profiles   * In **content** field use **#[CANDIDATE:id]** to tag a candidate, e.g. #[CANDIDATE:9847954623] * Use **shareWith** to share a feed update with individuals, hiring teams or everyone   * In **users** field, provide an array of User IDs with which you want to share, e.g. \"users\": [\"12343542356\",\"12343542357\"].   * In **hiringTeamOf** field, provide an array of Job IDs, this will share message with a full hiring team of those jobs, e.g. \"hiringTeamOf\": [\"123423432322\",\"123423432324\"].   * **everyone** flag allows sharing with everyone in a company. If not provided, defaults to **false**.   * **openNote** flag allows sharing with everyone in a company that has access to the candidate. If not provided, defaults to **false** 

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
api_instance = smartrecruiters_python_client.MessagesApi()
message = smartrecruiters_python_client.Message() # Message | Message to post (optional)

try: 
    # Shares new messages on Hireloop with Users, Hiring Teams or Everyone and sends emails.
    api_response = api_instance.messages_shares_create(message=message)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling MessagesApi->messages_shares_create: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **message** | [**Message**](Message.md)| Message to post | [optional] 

### Return type

[**MessageDetails**](MessageDetails.md)

### Authorization

[key](../README.md#key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json; charset=utf-8

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **messages_shares_delete**
> messages_shares_delete(id)

Delete a message

Delete a message with a given id. Deleted message is no longer visible on Hireloop.

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
api_instance = smartrecruiters_python_client.MessagesApi()
id = 'id_example' # str | identifier of a message

try: 
    # Delete a message
    api_instance.messages_shares_delete(id)
except ApiException as e:
    print("Exception when calling MessagesApi->messages_shares_delete: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| identifier of a message | 

### Return type

void (empty response body)

### Authorization

[key](../README.md#key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json; charset=utf-8

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)


# JobDetails

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | [optional] 
**title** | **str** |  | [optional] 
**ref_number** | **str** |  | [optional] 
**created_on** | **datetime** |  | [optional] 
**updated_on** | **datetime** | Job modification date | [optional] 
**last_activity_on** | **datetime** | Indicates last activity associated with a job | [optional] 
**department** | [**Department**](Department.md) |  | [optional] 
**location** | [**Location**](Location.md) |  | [optional] 
**status** | [**JobStatus**](JobStatus.md) |  | [optional] 
**posting_status** | [**PostingStatus**](PostingStatus.md) |  | [optional] 
**target_hiring_date** | **datetime** |  | [optional] 
**industry** | [**ModelProperty**](ModelProperty.md) |  | [optional] 
**function** | [**ModelProperty**](ModelProperty.md) |  | [optional] 
**type_of_employment** | [**ModelProperty**](ModelProperty.md) |  | [optional] 
**experience_level** | [**ModelProperty**](ModelProperty.md) |  | [optional] 
**eeo_category** | [**ModelProperty**](ModelProperty.md) |  | [optional] 
**template** | **bool** |  | [optional] 
**creator** | [**UserIdentity**](UserIdentity.md) |  | [optional] 
**compensation** | [**Compensation**](Compensation.md) |  | [optional] 
**job_ad** | [**JobAdInput**](JobAdInput.md) |  | [optional] 
**properties** | [**list[JobProperty]**](JobProperty.md) |  | [optional] 
**actions** | [**JobDetailsActions**](JobDetailsActions.md) |  | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



# ScreeningAnswer

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | Id of Question to which answer was responded | 
**type** | **str** |  | 
**category** | **str** | UUID for custom questions or fixed value for predefined questions:  - eeoInformation  - ofccpDisability  - ofccpVeteransForm  - veteranStatus  - disabilityStatus  - ofccpReasonableAccommodation  - ethnicity  - ethnicGroupsDescriptions  - todaysDate  - yourName  - preferredWorkShifts  - languages  - previousEmployment  - drivingRevoked  - drivingCurrent  - criminalRecord  - workPermit  | 
**name** | **str** | Question name visible to administrator on questions library list | 
**label** | **str** | Question text shown to candidate | 
**records** | [**list[AnswerRecord]**](AnswerRecord.md) | Multiple records may be used for example for questions (Preferred Work Shifts, Languages) | 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



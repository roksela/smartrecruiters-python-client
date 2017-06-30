# coding: utf-8

"""
    Customer API - version 1

    No description provided (generated by Swagger Codegen https://github.com/swagger-api/swagger-codegen)

    OpenAPI spec version: 1
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


from __future__ import absolute_import

import sys
import os
import re

# python 2 and python 3 compatibility library
from six import iteritems

from ..configuration import Configuration
from ..api_client import ApiClient


class AnalyticsApi(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    Ref: https://github.com/swagger-api/swagger-codegen
    """

    def __init__(self, api_client=None):
        config = Configuration()
        if api_client:
            self.api_client = api_client
        else:
            if not config.api_client:
                config.api_client = ApiClient()
            self.api_client = config.api_client

    def analytics_applications(self, **kwargs):
        """
        Get the list of applications.
        Get the list of applications. Fore more comprehensive description see [Analytics API](https://dev.smartrecruiters.com/customer-api/analytics-api/) and [Applications Data Service](https://dev.smartrecruiters.com/customer-api/analytics-api/applications-data-service/). 
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.analytics_applications(callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param str date_format: Defines response date format
        :return: ApplicationsReport
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('callback'):
            return self.analytics_applications_with_http_info(**kwargs)
        else:
            (data) = self.analytics_applications_with_http_info(**kwargs)
            return data

    def analytics_applications_with_http_info(self, **kwargs):
        """
        Get the list of applications.
        Get the list of applications. Fore more comprehensive description see [Analytics API](https://dev.smartrecruiters.com/customer-api/analytics-api/) and [Applications Data Service](https://dev.smartrecruiters.com/customer-api/analytics-api/applications-data-service/). 
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.analytics_applications_with_http_info(callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param str date_format: Defines response date format
        :return: ApplicationsReport
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['date_format']
        all_params.append('callback')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method analytics_applications" % key
                )
            params[key] = val
        del params['kwargs']


        collection_formats = {}

        resource_path = '/analytics/applications'.replace('{format}', 'json')
        path_params = {}

        query_params = {}
        if 'date_format' in params:
            query_params['dateFormat'] = params['date_format']

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.\
            select_header_accept(['application/json; charset=utf-8', 'text/csv'])

        # Authentication setting
        auth_settings = ['key']

        return self.api_client.call_api(resource_path, 'GET',
                                        path_params,
                                        query_params,
                                        header_params,
                                        body=body_params,
                                        post_params=form_params,
                                        files=local_var_files,
                                        response_type='ApplicationsReport',
                                        auth_settings=auth_settings,
                                        callback=params.get('callback'),
                                        _return_http_data_only=params.get('_return_http_data_only'),
                                        _preload_content=params.get('_preload_content', True),
                                        _request_timeout=params.get('_request_timeout'),
                                        collection_formats=collection_formats)

    def analytics_hiring_team(self, **kwargs):
        """
        Get the list of hiring team members.
        Get the list of hiring team members. Fore more comprehensive description see [Analytics API](https://dev.smartrecruiters.com/customer-api/analytics-api/) and [Hiring Team Data Service](https://dev.smartrecruiters.com/customer-api/analytics-api/hiring-team-data-service/). 
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.analytics_hiring_team(callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :return: HiringTeamReport
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('callback'):
            return self.analytics_hiring_team_with_http_info(**kwargs)
        else:
            (data) = self.analytics_hiring_team_with_http_info(**kwargs)
            return data

    def analytics_hiring_team_with_http_info(self, **kwargs):
        """
        Get the list of hiring team members.
        Get the list of hiring team members. Fore more comprehensive description see [Analytics API](https://dev.smartrecruiters.com/customer-api/analytics-api/) and [Hiring Team Data Service](https://dev.smartrecruiters.com/customer-api/analytics-api/hiring-team-data-service/). 
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.analytics_hiring_team_with_http_info(callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :return: HiringTeamReport
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = []
        all_params.append('callback')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method analytics_hiring_team" % key
                )
            params[key] = val
        del params['kwargs']

        collection_formats = {}

        resource_path = '/analytics/hiring-team'.replace('{format}', 'json')
        path_params = {}

        query_params = {}

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.\
            select_header_accept(['application/json; charset=utf-8', 'text/csv'])

        # Authentication setting
        auth_settings = ['key']

        return self.api_client.call_api(resource_path, 'GET',
                                        path_params,
                                        query_params,
                                        header_params,
                                        body=body_params,
                                        post_params=form_params,
                                        files=local_var_files,
                                        response_type='HiringTeamReport',
                                        auth_settings=auth_settings,
                                        callback=params.get('callback'),
                                        _return_http_data_only=params.get('_return_http_data_only'),
                                        _preload_content=params.get('_preload_content', True),
                                        _request_timeout=params.get('_request_timeout'),
                                        collection_formats=collection_formats)

    def analytics_interviews(self, **kwargs):
        """
        Get the list of interviews.
        Get the list of interviews. Fore more comprehensive description see [Analytics API](https://dev.smartrecruiters.com/customer-api/analytics-api/) and [Interviews Data Service](https://dev.smartrecruiters.com/customer-api/analytics-api/interviews-data-service/). 
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.analytics_interviews(callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param str date_format: Defines response date format
        :return: InterviewsReport
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('callback'):
            return self.analytics_interviews_with_http_info(**kwargs)
        else:
            (data) = self.analytics_interviews_with_http_info(**kwargs)
            return data

    def analytics_interviews_with_http_info(self, **kwargs):
        """
        Get the list of interviews.
        Get the list of interviews. Fore more comprehensive description see [Analytics API](https://dev.smartrecruiters.com/customer-api/analytics-api/) and [Interviews Data Service](https://dev.smartrecruiters.com/customer-api/analytics-api/interviews-data-service/). 
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.analytics_interviews_with_http_info(callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param str date_format: Defines response date format
        :return: InterviewsReport
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['date_format']
        all_params.append('callback')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method analytics_interviews" % key
                )
            params[key] = val
        del params['kwargs']


        collection_formats = {}

        resource_path = '/analytics/interviews'.replace('{format}', 'json')
        path_params = {}

        query_params = {}
        if 'date_format' in params:
            query_params['dateFormat'] = params['date_format']

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.\
            select_header_accept(['application/json; charset=utf-8', 'text/csv'])

        # Authentication setting
        auth_settings = ['key']

        return self.api_client.call_api(resource_path, 'GET',
                                        path_params,
                                        query_params,
                                        header_params,
                                        body=body_params,
                                        post_params=form_params,
                                        files=local_var_files,
                                        response_type='InterviewsReport',
                                        auth_settings=auth_settings,
                                        callback=params.get('callback'),
                                        _return_http_data_only=params.get('_return_http_data_only'),
                                        _preload_content=params.get('_preload_content', True),
                                        _request_timeout=params.get('_request_timeout'),
                                        collection_formats=collection_formats)

    def analytics_job_fields(self, **kwargs):
        """
        Get the list of job fields.
        Get the list of job fields. Fore more comprehensive description see [Analytics API](https://dev.smartrecruiters.com/customer-api/analytics-api/) and [Job Fields Data Service](https://dev.smartrecruiters.com/customer-api/analytics-api/job-fields-data-service/). 
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.analytics_job_fields(callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :return: JobFieldsReport
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('callback'):
            return self.analytics_job_fields_with_http_info(**kwargs)
        else:
            (data) = self.analytics_job_fields_with_http_info(**kwargs)
            return data

    def analytics_job_fields_with_http_info(self, **kwargs):
        """
        Get the list of job fields.
        Get the list of job fields. Fore more comprehensive description see [Analytics API](https://dev.smartrecruiters.com/customer-api/analytics-api/) and [Job Fields Data Service](https://dev.smartrecruiters.com/customer-api/analytics-api/job-fields-data-service/). 
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.analytics_job_fields_with_http_info(callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :return: JobFieldsReport
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = []
        all_params.append('callback')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method analytics_job_fields" % key
                )
            params[key] = val
        del params['kwargs']

        collection_formats = {}

        resource_path = '/analytics/job-fields'.replace('{format}', 'json')
        path_params = {}

        query_params = {}

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.\
            select_header_accept(['application/json; charset=utf-8', 'text/csv'])

        # Authentication setting
        auth_settings = ['key']

        return self.api_client.call_api(resource_path, 'GET',
                                        path_params,
                                        query_params,
                                        header_params,
                                        body=body_params,
                                        post_params=form_params,
                                        files=local_var_files,
                                        response_type='JobFieldsReport',
                                        auth_settings=auth_settings,
                                        callback=params.get('callback'),
                                        _return_http_data_only=params.get('_return_http_data_only'),
                                        _preload_content=params.get('_preload_content', True),
                                        _request_timeout=params.get('_request_timeout'),
                                        collection_formats=collection_formats)

    def analytics_jobs(self, **kwargs):
        """
        Get the list of jobs.
        Get the list of jobs. Fore more comprehensive description see [Analytics API](https://dev.smartrecruiters.com/customer-api/analytics-api/) and [Jobs Data Service](https://dev.smartrecruiters.com/customer-api/analytics-api/jobs-data-service/). 
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.analytics_jobs(callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param str date_format: Defines response date format
        :return: JobsReport
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('callback'):
            return self.analytics_jobs_with_http_info(**kwargs)
        else:
            (data) = self.analytics_jobs_with_http_info(**kwargs)
            return data

    def analytics_jobs_with_http_info(self, **kwargs):
        """
        Get the list of jobs.
        Get the list of jobs. Fore more comprehensive description see [Analytics API](https://dev.smartrecruiters.com/customer-api/analytics-api/) and [Jobs Data Service](https://dev.smartrecruiters.com/customer-api/analytics-api/jobs-data-service/). 
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.analytics_jobs_with_http_info(callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param str date_format: Defines response date format
        :return: JobsReport
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['date_format']
        all_params.append('callback')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method analytics_jobs" % key
                )
            params[key] = val
        del params['kwargs']


        collection_formats = {}

        resource_path = '/analytics/jobs'.replace('{format}', 'json')
        path_params = {}

        query_params = {}
        if 'date_format' in params:
            query_params['dateFormat'] = params['date_format']

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.\
            select_header_accept(['application/json; charset=utf-8', 'text/csv'])

        # Authentication setting
        auth_settings = ['key']

        return self.api_client.call_api(resource_path, 'GET',
                                        path_params,
                                        query_params,
                                        header_params,
                                        body=body_params,
                                        post_params=form_params,
                                        files=local_var_files,
                                        response_type='JobsReport',
                                        auth_settings=auth_settings,
                                        callback=params.get('callback'),
                                        _return_http_data_only=params.get('_return_http_data_only'),
                                        _preload_content=params.get('_preload_content', True),
                                        _request_timeout=params.get('_request_timeout'),
                                        collection_formats=collection_formats)

    def analytics_positions(self, **kwargs):
        """
        Get the list of job positions.
        Get the list of job positions. Fore more comprehensive description see [Analytics API](https://dev.smartrecruiters.com/customer-api/analytics-api/) and [Positions Data Service](https://dev.smartrecruiters.com/customer-api/analytics-api/positions/). 
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.analytics_positions(callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param str date_format: Defines response date format
        :return: PositionsReport
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('callback'):
            return self.analytics_positions_with_http_info(**kwargs)
        else:
            (data) = self.analytics_positions_with_http_info(**kwargs)
            return data

    def analytics_positions_with_http_info(self, **kwargs):
        """
        Get the list of job positions.
        Get the list of job positions. Fore more comprehensive description see [Analytics API](https://dev.smartrecruiters.com/customer-api/analytics-api/) and [Positions Data Service](https://dev.smartrecruiters.com/customer-api/analytics-api/positions/). 
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.analytics_positions_with_http_info(callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param str date_format: Defines response date format
        :return: PositionsReport
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['date_format']
        all_params.append('callback')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method analytics_positions" % key
                )
            params[key] = val
        del params['kwargs']


        collection_formats = {}

        resource_path = '/analytics/positions'.replace('{format}', 'json')
        path_params = {}

        query_params = {}
        if 'date_format' in params:
            query_params['dateFormat'] = params['date_format']

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.\
            select_header_accept(['application/json; charset=utf-8', 'text/csv'])

        # Authentication setting
        auth_settings = ['key']

        return self.api_client.call_api(resource_path, 'GET',
                                        path_params,
                                        query_params,
                                        header_params,
                                        body=body_params,
                                        post_params=form_params,
                                        files=local_var_files,
                                        response_type='PositionsReport',
                                        auth_settings=auth_settings,
                                        callback=params.get('callback'),
                                        _return_http_data_only=params.get('_return_http_data_only'),
                                        _preload_content=params.get('_preload_content', True),
                                        _request_timeout=params.get('_request_timeout'),
                                        collection_formats=collection_formats)
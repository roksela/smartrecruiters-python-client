# coding: utf-8

"""
    Unofficial python library for the SmartRecruiters API

    The SmartRecruiters API provides a platform to integrate services or applications, build apps and create fully customizable career sites. It exposes SmartRecruiters functionality and allows to connect and build software enhancing it.

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


class OffersApi(object):
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

    def candidates_offers_all(self, id, job_id, **kwargs):
        """
        Get candidate's offers
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.candidates_offers_all(id, job_id, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param str id: Identifier of a Candidate (required)
        :param str job_id: Identifier of a Job (required)
        :return: Offers
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('callback'):
            return self.candidates_offers_all_with_http_info(id, job_id, **kwargs)
        else:
            (data) = self.candidates_offers_all_with_http_info(id, job_id, **kwargs)
            return data

    def candidates_offers_all_with_http_info(self, id, job_id, **kwargs):
        """
        Get candidate's offers
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.candidates_offers_all_with_http_info(id, job_id, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param str id: Identifier of a Candidate (required)
        :param str job_id: Identifier of a Job (required)
        :return: Offers
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['id', 'job_id']
        all_params.append('callback')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method candidates_offers_all" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'id' is set
        if ('id' not in params) or (params['id'] is None):
            raise ValueError("Missing the required parameter `id` when calling `candidates_offers_all`")
        # verify the required parameter 'job_id' is set
        if ('job_id' not in params) or (params['job_id'] is None):
            raise ValueError("Missing the required parameter `job_id` when calling `candidates_offers_all`")


        collection_formats = {}

        resource_path = '/candidates/{id}/jobs/{jobId}/offers'.replace('{format}', 'json')
        path_params = {}
        if 'id' in params:
            path_params['id'] = params['id']
        if 'job_id' in params:
            path_params['jobId'] = params['job_id']

        query_params = {}

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.\
            select_header_accept(['application/json; charset=utf-8'])

        # Authentication setting
        auth_settings = ['key']

        return self.api_client.call_api(resource_path, 'GET',
                                        path_params,
                                        query_params,
                                        header_params,
                                        body=body_params,
                                        post_params=form_params,
                                        files=local_var_files,
                                        response_type='Offers',
                                        auth_settings=auth_settings,
                                        callback=params.get('callback'),
                                        _return_http_data_only=params.get('_return_http_data_only'),
                                        _preload_content=params.get('_preload_content', True),
                                        _request_timeout=params.get('_request_timeout'),
                                        collection_formats=collection_formats)

    def candidates_offers_find(self, **kwargs):
        """
        Search offers
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.candidates_offers_find(callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param int limit: number of elements to return. max value is 100
        :param int offset: number of elements to skip while processing result
        :param datetime created_after: ISO8601-formatted time boundaries for the offer creation time, Format: yyyy-MM-ddTHH:mm:ss.SSSZZ
        :param datetime created_before: ISO8601-formatted time boundaries for the offer creation time, Format: yyyy-MM-ddTHH:mm:ss.SSSZZ
        :param str age: word-based offer age; when age is specified createdAfter and createdBefore are ignored, Examples: 10 days, 7 hours, 1 week, etc.
        :param list[str] status: offer states that need to be included in the results; by default all states are included
        :return: Offers
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('callback'):
            return self.candidates_offers_find_with_http_info(**kwargs)
        else:
            (data) = self.candidates_offers_find_with_http_info(**kwargs)
            return data

    def candidates_offers_find_with_http_info(self, **kwargs):
        """
        Search offers
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.candidates_offers_find_with_http_info(callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param int limit: number of elements to return. max value is 100
        :param int offset: number of elements to skip while processing result
        :param datetime created_after: ISO8601-formatted time boundaries for the offer creation time, Format: yyyy-MM-ddTHH:mm:ss.SSSZZ
        :param datetime created_before: ISO8601-formatted time boundaries for the offer creation time, Format: yyyy-MM-ddTHH:mm:ss.SSSZZ
        :param str age: word-based offer age; when age is specified createdAfter and createdBefore are ignored, Examples: 10 days, 7 hours, 1 week, etc.
        :param list[str] status: offer states that need to be included in the results; by default all states are included
        :return: Offers
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['limit', 'offset', 'created_after', 'created_before', 'age', 'status']
        all_params.append('callback')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method candidates_offers_find" % key
                )
            params[key] = val
        del params['kwargs']

        if 'limit' in params and params['limit'] > 100:
            raise ValueError("Invalid value for parameter `limit` when calling `candidates_offers_find`, must be a value less than or equal to `100`")
        if 'limit' in params and params['limit'] < 1:
            raise ValueError("Invalid value for parameter `limit` when calling `candidates_offers_find`, must be a value greater than or equal to `1`")
        if 'offset' in params and params['offset'] < 0:
            raise ValueError("Invalid value for parameter `offset` when calling `candidates_offers_find`, must be a value greater than or equal to `0`")

        collection_formats = {}

        resource_path = '/offers'.replace('{format}', 'json')
        path_params = {}

        query_params = {}
        if 'limit' in params:
            query_params['limit'] = params['limit']
        if 'offset' in params:
            query_params['offset'] = params['offset']
        if 'created_after' in params:
            query_params['createdAfter'] = params['created_after']
        if 'created_before' in params:
            query_params['createdBefore'] = params['created_before']
        if 'age' in params:
            query_params['age'] = params['age']
        if 'status' in params:
            query_params['status'] = params['status']
            collection_formats['status'] = 'csv'

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.\
            select_header_accept(['application/json; charset=utf-8'])

        # Authentication setting
        auth_settings = ['key']

        return self.api_client.call_api(resource_path, 'GET',
                                        path_params,
                                        query_params,
                                        header_params,
                                        body=body_params,
                                        post_params=form_params,
                                        files=local_var_files,
                                        response_type='Offers',
                                        auth_settings=auth_settings,
                                        callback=params.get('callback'),
                                        _return_http_data_only=params.get('_return_http_data_only'),
                                        _preload_content=params.get('_preload_content', True),
                                        _request_timeout=params.get('_request_timeout'),
                                        collection_formats=collection_formats)

    def candidates_offers_get(self, id, job_id, offer_id, **kwargs):
        """
        Get candidate's offer
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.candidates_offers_get(id, job_id, offer_id, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param str id: Identifier of a Candidate (required)
        :param str job_id: Identifier of a Job (required)
        :param str offer_id: Identifier of a Offer (required)
        :return: Offer
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('callback'):
            return self.candidates_offers_get_with_http_info(id, job_id, offer_id, **kwargs)
        else:
            (data) = self.candidates_offers_get_with_http_info(id, job_id, offer_id, **kwargs)
            return data

    def candidates_offers_get_with_http_info(self, id, job_id, offer_id, **kwargs):
        """
        Get candidate's offer
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.candidates_offers_get_with_http_info(id, job_id, offer_id, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param str id: Identifier of a Candidate (required)
        :param str job_id: Identifier of a Job (required)
        :param str offer_id: Identifier of a Offer (required)
        :return: Offer
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['id', 'job_id', 'offer_id']
        all_params.append('callback')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method candidates_offers_get" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'id' is set
        if ('id' not in params) or (params['id'] is None):
            raise ValueError("Missing the required parameter `id` when calling `candidates_offers_get`")
        # verify the required parameter 'job_id' is set
        if ('job_id' not in params) or (params['job_id'] is None):
            raise ValueError("Missing the required parameter `job_id` when calling `candidates_offers_get`")
        # verify the required parameter 'offer_id' is set
        if ('offer_id' not in params) or (params['offer_id'] is None):
            raise ValueError("Missing the required parameter `offer_id` when calling `candidates_offers_get`")


        collection_formats = {}

        resource_path = '/candidates/{id}/jobs/{jobId}/offers/{offerId}'.replace('{format}', 'json')
        path_params = {}
        if 'id' in params:
            path_params['id'] = params['id']
        if 'job_id' in params:
            path_params['jobId'] = params['job_id']
        if 'offer_id' in params:
            path_params['offerId'] = params['offer_id']

        query_params = {}

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.\
            select_header_accept(['application/json; charset=utf-8'])

        # Authentication setting
        auth_settings = ['key']

        return self.api_client.call_api(resource_path, 'GET',
                                        path_params,
                                        query_params,
                                        header_params,
                                        body=body_params,
                                        post_params=form_params,
                                        files=local_var_files,
                                        response_type='Offer',
                                        auth_settings=auth_settings,
                                        callback=params.get('callback'),
                                        _return_http_data_only=params.get('_return_http_data_only'),
                                        _preload_content=params.get('_preload_content', True),
                                        _request_timeout=params.get('_request_timeout'),
                                        collection_formats=collection_formats)

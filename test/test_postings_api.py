# coding: utf-8

"""
    Unofficial python library for the SmartRecruiters API

    The SmartRecruiters API provides a platform to integrate services or applications, build apps and create fully customizable career sites. It exposes SmartRecruiters functionality and allows to connect and build software enhancing it.

    OpenAPI spec version: 1
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


from __future__ import absolute_import

import os
import sys
import unittest

import smartrecruiters_python_client
from smartrecruiters_python_client.rest import ApiException
from smartrecruiters_python_client.apis.postings_api import PostingsApi


class TestPostingsApi(unittest.TestCase):
    """ PostingsApi unit test stubs """

    def setUp(self):
        self.api = smartrecruiters_python_client.apis.postings_api.PostingsApi()

    def tearDown(self):
        pass

    def test_v1_get_posting(self):
        """
        Test case for v1_get_posting

        Get posting by posting id for given company
        """
        pass

    def test_v1_list_departments(self):
        """
        Test case for v1_list_departments

        List departments for given company
        """
        pass

    def test_v1_list_postings(self):
        """
        Test case for v1_list_postings

        Lists active postings published by given company
        """
        pass


if __name__ == '__main__':
    unittest.main()

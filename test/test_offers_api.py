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
from smartrecruiters_python_client.apis.offers_api import OffersApi


class TestOffersApi(unittest.TestCase):
    """ OffersApi unit test stubs """

    def setUp(self):
        self.api = smartrecruiters_python_client.apis.offers_api.OffersApi()

    def tearDown(self):
        pass

    def test_candidates_offers_all(self):
        """
        Test case for candidates_offers_all

        Get candidate's offers
        """
        pass

    def test_candidates_offers_find(self):
        """
        Test case for candidates_offers_find

        Search offers
        """
        pass

    def test_candidates_offers_get(self):
        """
        Test case for candidates_offers_get

        Get candidate's offer
        """
        pass


if __name__ == '__main__':
    unittest.main()

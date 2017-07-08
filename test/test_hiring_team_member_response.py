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
from smartrecruiters_python_client.models.hiring_team_member_response import HiringTeamMemberResponse


class TestHiringTeamMemberResponse(unittest.TestCase):
    """ HiringTeamMemberResponse unit test stubs """

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def testHiringTeamMemberResponse(self):
        """
        Test HiringTeamMemberResponse
        """
        model = smartrecruiters_python_client.models.hiring_team_member_response.HiringTeamMemberResponse()


if __name__ == '__main__':
    unittest.main()

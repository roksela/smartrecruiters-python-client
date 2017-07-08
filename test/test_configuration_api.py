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
from smartrecruiters_python_client.apis.configuration_api import ConfigurationApi


class TestConfigurationApi(unittest.TestCase):
    """ ConfigurationApi unit test stubs """

    def setUp(self):
        self.api = smartrecruiters_python_client.apis.configuration_api.ConfigurationApi()

    def tearDown(self):
        pass

    def test_configuration_candidate_properties_all(self):
        """
        Test case for configuration_candidate_properties_all

        Get a list of available candidate properties
        """
        pass

    def test_configuration_candidate_properties_get(self):
        """
        Test case for configuration_candidate_properties_get

        Get candidate property by id
        """
        pass

    def test_configuration_candidate_properties_values_all(self):
        """
        Test case for configuration_candidate_properties_values_all

        Get Candidate Property values
        """
        pass

    def test_configuration_candidate_properties_values_create(self):
        """
        Test case for configuration_candidate_properties_values_create

        Create candidate property value
        """
        pass

    def test_configuration_candidate_properties_values_get(self):
        """
        Test case for configuration_candidate_properties_values_get

        Get Candidate Property value by id
        """
        pass

    def test_configuration_candidate_properties_values_update(self):
        """
        Test case for configuration_candidate_properties_values_update

        Update candidate property value label
        """
        pass

    def test_configuration_company_my(self):
        """
        Test case for configuration_company_my

        Get company information
        """
        pass

    def test_configuration_department_all(self):
        """
        Test case for configuration_department_all

        Get departments
        """
        pass

    def test_configuration_department_create(self):
        """
        Test case for configuration_department_create

        Creates department
        """
        pass

    def test_configuration_department_get(self):
        """
        Test case for configuration_department_get

        Get department
        """
        pass

    def test_configuration_hiring_process_all(self):
        """
        Test case for configuration_hiring_process_all

        Get list of hiring process
        """
        pass

    def test_configuration_hiring_process_get(self):
        """
        Test case for configuration_hiring_process_get

        Get hiring process
        """
        pass

    def test_configuration_job_properties_activate(self):
        """
        Test case for configuration_job_properties_activate

        Activate a job property
        """
        pass

    def test_configuration_job_properties_all(self):
        """
        Test case for configuration_job_properties_all

        Get a list of available job properties
        """
        pass

    def test_configuration_job_properties_create(self):
        """
        Test case for configuration_job_properties_create

        Create a job property
        """
        pass

    def test_configuration_job_properties_deactivate(self):
        """
        Test case for configuration_job_properties_deactivate

        Deactivate a job property
        """
        pass

    def test_configuration_job_properties_dependents_all(self):
        """
        Test case for configuration_job_properties_dependents_all

        Get job property's dependents
        """
        pass

    def test_configuration_job_properties_dependents_create(self):
        """
        Test case for configuration_job_properties_dependents_create

        Create job property dependents
        """
        pass

    def test_configuration_job_properties_dependents_remove(self):
        """
        Test case for configuration_job_properties_dependents_remove

        Remove job property's dependent
        """
        pass

    def test_configuration_job_properties_dependents_values_add(self):
        """
        Test case for configuration_job_properties_dependents_values_add

        Add job property's dependent value
        """
        pass

    def test_configuration_job_properties_dependents_values_all(self):
        """
        Test case for configuration_job_properties_dependents_values_all

        Get dependent job property's values
        """
        pass

    def test_configuration_job_properties_dependents_values_get(self):
        """
        Test case for configuration_job_properties_dependents_values_get

        Get job property's dependent values
        """
        pass

    def test_configuration_job_properties_dependents_values_remove(self):
        """
        Test case for configuration_job_properties_dependents_values_remove

        Remove job property's dependent values relationship
        """
        pass

    def test_configuration_job_properties_get(self):
        """
        Test case for configuration_job_properties_get

        Get job property by id
        """
        pass

    def test_configuration_job_properties_update(self):
        """
        Test case for configuration_job_properties_update

        Update a job property
        """
        pass

    def test_configuration_job_properties_values_archive(self):
        """
        Test case for configuration_job_properties_values_archive

        Archive a job property value
        """
        pass

    def test_configuration_job_properties_values_create(self):
        """
        Test case for configuration_job_properties_values_create

        Create a job property value
        """
        pass

    def test_configuration_job_properties_values_deprecated_archive(self):
        """
        Test case for configuration_job_properties_values_deprecated_archive

        Archive a job property value
        """
        pass

    def test_configuration_job_properties_values_deprecated_unarchive(self):
        """
        Test case for configuration_job_properties_values_deprecated_unarchive

        Unarchive a job property value
        """
        pass

    def test_configuration_job_properties_values_get(self):
        """
        Test case for configuration_job_properties_values_get

        Get available job property values
        """
        pass

    def test_configuration_job_properties_values_unarchive(self):
        """
        Test case for configuration_job_properties_values_unarchive

        Unarchive a job property value
        """
        pass

    def test_configuration_job_properties_values_update(self):
        """
        Test case for configuration_job_properties_values_update

        Update a job property value
        """
        pass

    def test_configuration_offer_properties_all(self):
        """
        Test case for configuration_offer_properties_all

        Get a list of available offer properties
        """
        pass

    def test_configuration_reasons_rejection_all(self):
        """
        Test case for configuration_reasons_rejection_all

        Get rejection reasons
        """
        pass

    def test_configuration_reasons_withdrawal_all(self):
        """
        Test case for configuration_reasons_withdrawal_all

        Get withdrawal reasons
        """
        pass

    def test_configuration_source_types(self):
        """
        Test case for configuration_source_types

        List candidate source types with subtypes
        """
        pass

    def test_configuration_source_values_all(self):
        """
        Test case for configuration_source_values_all

        List candidate sources
        """
        pass

    def test_configuration_source_values_single(self):
        """
        Test case for configuration_source_values_single

        Get a candidate source
        """
        pass


if __name__ == '__main__':
    unittest.main()

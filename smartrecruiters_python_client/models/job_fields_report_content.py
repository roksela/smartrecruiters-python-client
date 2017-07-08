# coding: utf-8

"""
    Unofficial python library for the SmartRecruiters API

    The SmartRecruiters API provides a platform to integrate services or applications, build apps and create fully customizable career sites. It exposes SmartRecruiters functionality and allows to connect and build software enhancing it.

    OpenAPI spec version: 1
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


from pprint import pformat
from six import iteritems
import re


class JobFieldsReportContent(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    """
    def __init__(self, job_id=None, job_field_name=None, job_field_value=None):
        """
        JobFieldsReportContent - a model defined in Swagger

        :param dict swaggerTypes: The key is attribute name
                                  and the value is attribute type.
        :param dict attributeMap: The key is attribute name
                                  and the value is json key in definition.
        """
        self.swagger_types = {
            'job_id': 'str',
            'job_field_name': 'str',
            'job_field_value': 'str'
        }

        self.attribute_map = {
            'job_id': 'jobId',
            'job_field_name': 'jobFieldName',
            'job_field_value': 'jobFieldValue'
        }

        self._job_id = job_id
        self._job_field_name = job_field_name
        self._job_field_value = job_field_value

    @property
    def job_id(self):
        """
        Gets the job_id of this JobFieldsReportContent.

        :return: The job_id of this JobFieldsReportContent.
        :rtype: str
        """
        return self._job_id

    @job_id.setter
    def job_id(self, job_id):
        """
        Sets the job_id of this JobFieldsReportContent.

        :param job_id: The job_id of this JobFieldsReportContent.
        :type: str
        """

        self._job_id = job_id

    @property
    def job_field_name(self):
        """
        Gets the job_field_name of this JobFieldsReportContent.

        :return: The job_field_name of this JobFieldsReportContent.
        :rtype: str
        """
        return self._job_field_name

    @job_field_name.setter
    def job_field_name(self, job_field_name):
        """
        Sets the job_field_name of this JobFieldsReportContent.

        :param job_field_name: The job_field_name of this JobFieldsReportContent.
        :type: str
        """

        self._job_field_name = job_field_name

    @property
    def job_field_value(self):
        """
        Gets the job_field_value of this JobFieldsReportContent.

        :return: The job_field_value of this JobFieldsReportContent.
        :rtype: str
        """
        return self._job_field_value

    @job_field_value.setter
    def job_field_value(self, job_field_value):
        """
        Sets the job_field_value of this JobFieldsReportContent.

        :param job_field_value: The job_field_value of this JobFieldsReportContent.
        :type: str
        """

        self._job_field_value = job_field_value

    def to_dict(self):
        """
        Returns the model properties as a dict
        """
        result = {}

        for attr, _ in iteritems(self.swagger_types):
            value = getattr(self, attr)
            if isinstance(value, list):
                result[attr] = list(map(
                    lambda x: x.to_dict() if hasattr(x, "to_dict") else x,
                    value
                ))
            elif hasattr(value, "to_dict"):
                result[attr] = value.to_dict()
            elif isinstance(value, dict):
                result[attr] = dict(map(
                    lambda item: (item[0], item[1].to_dict())
                    if hasattr(item[1], "to_dict") else item,
                    value.items()
                ))
            else:
                result[attr] = value

        return result

    def to_str(self):
        """
        Returns the string representation of the model
        """
        return pformat(self.to_dict())

    def __repr__(self):
        """
        For `print` and `pprint`
        """
        return self.to_str()

    def __eq__(self, other):
        """
        Returns true if both objects are equal
        """
        if not isinstance(other, JobFieldsReportContent):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other

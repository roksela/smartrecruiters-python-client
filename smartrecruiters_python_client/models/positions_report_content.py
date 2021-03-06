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


class PositionsReportContent(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    """
    def __init__(self, position_id=None, job_id=None, job_ref_id=None, job_title=None, job_create_date=None, position_create_date=None, position_open_date=None, position_target_start_date=None, position_hire_date=None, position_actual_start_date=None, position_type=None, position_incumbent_name=None):
        """
        PositionsReportContent - a model defined in Swagger

        :param dict swaggerTypes: The key is attribute name
                                  and the value is attribute type.
        :param dict attributeMap: The key is attribute name
                                  and the value is json key in definition.
        """
        self.swagger_types = {
            'position_id': 'str',
            'job_id': 'str',
            'job_ref_id': 'str',
            'job_title': 'str',
            'job_create_date': 'str',
            'position_create_date': 'str',
            'position_open_date': 'str',
            'position_target_start_date': 'str',
            'position_hire_date': 'str',
            'position_actual_start_date': 'str',
            'position_type': 'str',
            'position_incumbent_name': 'str'
        }

        self.attribute_map = {
            'position_id': 'positionId',
            'job_id': 'jobId',
            'job_ref_id': 'jobRefId',
            'job_title': 'jobTitle',
            'job_create_date': 'jobCreateDate',
            'position_create_date': 'positionCreateDate',
            'position_open_date': 'positionOpenDate',
            'position_target_start_date': 'positionTargetStartDate',
            'position_hire_date': 'positionHireDate',
            'position_actual_start_date': 'positionActualStartDate',
            'position_type': 'positionType',
            'position_incumbent_name': 'positionIncumbentName'
        }

        self._position_id = position_id
        self._job_id = job_id
        self._job_ref_id = job_ref_id
        self._job_title = job_title
        self._job_create_date = job_create_date
        self._position_create_date = position_create_date
        self._position_open_date = position_open_date
        self._position_target_start_date = position_target_start_date
        self._position_hire_date = position_hire_date
        self._position_actual_start_date = position_actual_start_date
        self._position_type = position_type
        self._position_incumbent_name = position_incumbent_name

    @property
    def position_id(self):
        """
        Gets the position_id of this PositionsReportContent.

        :return: The position_id of this PositionsReportContent.
        :rtype: str
        """
        return self._position_id

    @position_id.setter
    def position_id(self, position_id):
        """
        Sets the position_id of this PositionsReportContent.

        :param position_id: The position_id of this PositionsReportContent.
        :type: str
        """

        self._position_id = position_id

    @property
    def job_id(self):
        """
        Gets the job_id of this PositionsReportContent.

        :return: The job_id of this PositionsReportContent.
        :rtype: str
        """
        return self._job_id

    @job_id.setter
    def job_id(self, job_id):
        """
        Sets the job_id of this PositionsReportContent.

        :param job_id: The job_id of this PositionsReportContent.
        :type: str
        """

        self._job_id = job_id

    @property
    def job_ref_id(self):
        """
        Gets the job_ref_id of this PositionsReportContent.

        :return: The job_ref_id of this PositionsReportContent.
        :rtype: str
        """
        return self._job_ref_id

    @job_ref_id.setter
    def job_ref_id(self, job_ref_id):
        """
        Sets the job_ref_id of this PositionsReportContent.

        :param job_ref_id: The job_ref_id of this PositionsReportContent.
        :type: str
        """

        self._job_ref_id = job_ref_id

    @property
    def job_title(self):
        """
        Gets the job_title of this PositionsReportContent.

        :return: The job_title of this PositionsReportContent.
        :rtype: str
        """
        return self._job_title

    @job_title.setter
    def job_title(self, job_title):
        """
        Sets the job_title of this PositionsReportContent.

        :param job_title: The job_title of this PositionsReportContent.
        :type: str
        """

        self._job_title = job_title

    @property
    def job_create_date(self):
        """
        Gets the job_create_date of this PositionsReportContent.

        :return: The job_create_date of this PositionsReportContent.
        :rtype: str
        """
        return self._job_create_date

    @job_create_date.setter
    def job_create_date(self, job_create_date):
        """
        Sets the job_create_date of this PositionsReportContent.

        :param job_create_date: The job_create_date of this PositionsReportContent.
        :type: str
        """

        self._job_create_date = job_create_date

    @property
    def position_create_date(self):
        """
        Gets the position_create_date of this PositionsReportContent.

        :return: The position_create_date of this PositionsReportContent.
        :rtype: str
        """
        return self._position_create_date

    @position_create_date.setter
    def position_create_date(self, position_create_date):
        """
        Sets the position_create_date of this PositionsReportContent.

        :param position_create_date: The position_create_date of this PositionsReportContent.
        :type: str
        """

        self._position_create_date = position_create_date

    @property
    def position_open_date(self):
        """
        Gets the position_open_date of this PositionsReportContent.

        :return: The position_open_date of this PositionsReportContent.
        :rtype: str
        """
        return self._position_open_date

    @position_open_date.setter
    def position_open_date(self, position_open_date):
        """
        Sets the position_open_date of this PositionsReportContent.

        :param position_open_date: The position_open_date of this PositionsReportContent.
        :type: str
        """

        self._position_open_date = position_open_date

    @property
    def position_target_start_date(self):
        """
        Gets the position_target_start_date of this PositionsReportContent.

        :return: The position_target_start_date of this PositionsReportContent.
        :rtype: str
        """
        return self._position_target_start_date

    @position_target_start_date.setter
    def position_target_start_date(self, position_target_start_date):
        """
        Sets the position_target_start_date of this PositionsReportContent.

        :param position_target_start_date: The position_target_start_date of this PositionsReportContent.
        :type: str
        """

        self._position_target_start_date = position_target_start_date

    @property
    def position_hire_date(self):
        """
        Gets the position_hire_date of this PositionsReportContent.

        :return: The position_hire_date of this PositionsReportContent.
        :rtype: str
        """
        return self._position_hire_date

    @position_hire_date.setter
    def position_hire_date(self, position_hire_date):
        """
        Sets the position_hire_date of this PositionsReportContent.

        :param position_hire_date: The position_hire_date of this PositionsReportContent.
        :type: str
        """

        self._position_hire_date = position_hire_date

    @property
    def position_actual_start_date(self):
        """
        Gets the position_actual_start_date of this PositionsReportContent.

        :return: The position_actual_start_date of this PositionsReportContent.
        :rtype: str
        """
        return self._position_actual_start_date

    @position_actual_start_date.setter
    def position_actual_start_date(self, position_actual_start_date):
        """
        Sets the position_actual_start_date of this PositionsReportContent.

        :param position_actual_start_date: The position_actual_start_date of this PositionsReportContent.
        :type: str
        """

        self._position_actual_start_date = position_actual_start_date

    @property
    def position_type(self):
        """
        Gets the position_type of this PositionsReportContent.

        :return: The position_type of this PositionsReportContent.
        :rtype: str
        """
        return self._position_type

    @position_type.setter
    def position_type(self, position_type):
        """
        Sets the position_type of this PositionsReportContent.

        :param position_type: The position_type of this PositionsReportContent.
        :type: str
        """
        allowed_values = ["NEW_HEADCOUNT", "REPLACEMENT"]
        if position_type not in allowed_values:
            raise ValueError(
                "Invalid value for `position_type` ({0}), must be one of {1}"
                .format(position_type, allowed_values)
            )

        self._position_type = position_type

    @property
    def position_incumbent_name(self):
        """
        Gets the position_incumbent_name of this PositionsReportContent.

        :return: The position_incumbent_name of this PositionsReportContent.
        :rtype: str
        """
        return self._position_incumbent_name

    @position_incumbent_name.setter
    def position_incumbent_name(self, position_incumbent_name):
        """
        Sets the position_incumbent_name of this PositionsReportContent.

        :param position_incumbent_name: The position_incumbent_name of this PositionsReportContent.
        :type: str
        """

        self._position_incumbent_name = position_incumbent_name

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
        if not isinstance(other, PositionsReportContent):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other

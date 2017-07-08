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


class AssignmentActions(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    """
    def __init__(self, source_details=None):
        """
        AssignmentActions - a model defined in Swagger

        :param dict swaggerTypes: The key is attribute name
                                  and the value is attribute type.
        :param dict attributeMap: The key is attribute name
                                  and the value is json key in definition.
        """
        self.swagger_types = {
            'source_details': 'Action'
        }

        self.attribute_map = {
            'source_details': 'sourceDetails'
        }

        self._source_details = source_details

    @property
    def source_details(self):
        """
        Gets the source_details of this AssignmentActions.

        :return: The source_details of this AssignmentActions.
        :rtype: Action
        """
        return self._source_details

    @source_details.setter
    def source_details(self, source_details):
        """
        Sets the source_details of this AssignmentActions.

        :param source_details: The source_details of this AssignmentActions.
        :type: Action
        """

        self._source_details = source_details

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
        if not isinstance(other, AssignmentActions):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other

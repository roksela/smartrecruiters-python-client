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


class HiringTeamReport(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    """
    def __init__(self, content=None):
        """
        HiringTeamReport - a model defined in Swagger

        :param dict swaggerTypes: The key is attribute name
                                  and the value is attribute type.
        :param dict attributeMap: The key is attribute name
                                  and the value is json key in definition.
        """
        self.swagger_types = {
            'content': 'list[HiringTeamReportContent]'
        }

        self.attribute_map = {
            'content': 'content'
        }

        self._content = content

    @property
    def content(self):
        """
        Gets the content of this HiringTeamReport.

        :return: The content of this HiringTeamReport.
        :rtype: list[HiringTeamReportContent]
        """
        return self._content

    @content.setter
    def content(self, content):
        """
        Sets the content of this HiringTeamReport.

        :param content: The content of this HiringTeamReport.
        :type: list[HiringTeamReportContent]
        """

        self._content = content

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
        if not isinstance(other, HiringTeamReport):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other

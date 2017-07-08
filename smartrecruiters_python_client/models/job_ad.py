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


class JobAd(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    """
    def __init__(self, sections=None, language=None):
        """
        JobAd - a model defined in Swagger

        :param dict swaggerTypes: The key is attribute name
                                  and the value is attribute type.
        :param dict attributeMap: The key is attribute name
                                  and the value is json key in definition.
        """
        self.swagger_types = {
            'sections': 'JobAdSections',
            'language': 'Language'
        }

        self.attribute_map = {
            'sections': 'sections',
            'language': 'language'
        }

        self._sections = sections
        self._language = language

    @property
    def sections(self):
        """
        Gets the sections of this JobAd.

        :return: The sections of this JobAd.
        :rtype: JobAdSections
        """
        return self._sections

    @sections.setter
    def sections(self, sections):
        """
        Sets the sections of this JobAd.

        :param sections: The sections of this JobAd.
        :type: JobAdSections
        """

        self._sections = sections

    @property
    def language(self):
        """
        Gets the language of this JobAd.

        :return: The language of this JobAd.
        :rtype: Language
        """
        return self._language

    @language.setter
    def language(self, language):
        """
        Sets the language of this JobAd.

        :param language: The language of this JobAd.
        :type: Language
        """

        self._language = language

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
        if not isinstance(other, JobAd):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other

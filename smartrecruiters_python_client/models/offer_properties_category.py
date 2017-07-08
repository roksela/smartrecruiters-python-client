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


class OfferPropertiesCategory(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    """
    def __init__(self, id=None, properties=None):
        """
        OfferPropertiesCategory - a model defined in Swagger

        :param dict swaggerTypes: The key is attribute name
                                  and the value is attribute type.
        :param dict attributeMap: The key is attribute name
                                  and the value is json key in definition.
        """
        self.swagger_types = {
            'id': 'str',
            'properties': 'list[OfferPropertyDefinition]'
        }

        self.attribute_map = {
            'id': 'id',
            'properties': 'properties'
        }

        self._id = id
        self._properties = properties

    @property
    def id(self):
        """
        Gets the id of this OfferPropertiesCategory.

        :return: The id of this OfferPropertiesCategory.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """
        Sets the id of this OfferPropertiesCategory.

        :param id: The id of this OfferPropertiesCategory.
        :type: str
        """

        self._id = id

    @property
    def properties(self):
        """
        Gets the properties of this OfferPropertiesCategory.

        :return: The properties of this OfferPropertiesCategory.
        :rtype: list[OfferPropertyDefinition]
        """
        return self._properties

    @properties.setter
    def properties(self, properties):
        """
        Sets the properties of this OfferPropertiesCategory.

        :param properties: The properties of this OfferPropertiesCategory.
        :type: list[OfferPropertyDefinition]
        """

        self._properties = properties

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
        if not isinstance(other, OfferPropertiesCategory):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other

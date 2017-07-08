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


class WebProfile(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    """
    def __init__(self, skype=None, linkedin=None, facebook=None, twitter=None, website=None):
        """
        WebProfile - a model defined in Swagger

        :param dict swaggerTypes: The key is attribute name
                                  and the value is attribute type.
        :param dict attributeMap: The key is attribute name
                                  and the value is json key in definition.
        """
        self.swagger_types = {
            'skype': 'str',
            'linkedin': 'str',
            'facebook': 'str',
            'twitter': 'str',
            'website': 'str'
        }

        self.attribute_map = {
            'skype': 'skype',
            'linkedin': 'linkedin',
            'facebook': 'facebook',
            'twitter': 'twitter',
            'website': 'website'
        }

        self._skype = skype
        self._linkedin = linkedin
        self._facebook = facebook
        self._twitter = twitter
        self._website = website

    @property
    def skype(self):
        """
        Gets the skype of this WebProfile.

        :return: The skype of this WebProfile.
        :rtype: str
        """
        return self._skype

    @skype.setter
    def skype(self, skype):
        """
        Sets the skype of this WebProfile.

        :param skype: The skype of this WebProfile.
        :type: str
        """

        self._skype = skype

    @property
    def linkedin(self):
        """
        Gets the linkedin of this WebProfile.

        :return: The linkedin of this WebProfile.
        :rtype: str
        """
        return self._linkedin

    @linkedin.setter
    def linkedin(self, linkedin):
        """
        Sets the linkedin of this WebProfile.

        :param linkedin: The linkedin of this WebProfile.
        :type: str
        """

        self._linkedin = linkedin

    @property
    def facebook(self):
        """
        Gets the facebook of this WebProfile.

        :return: The facebook of this WebProfile.
        :rtype: str
        """
        return self._facebook

    @facebook.setter
    def facebook(self, facebook):
        """
        Sets the facebook of this WebProfile.

        :param facebook: The facebook of this WebProfile.
        :type: str
        """

        self._facebook = facebook

    @property
    def twitter(self):
        """
        Gets the twitter of this WebProfile.

        :return: The twitter of this WebProfile.
        :rtype: str
        """
        return self._twitter

    @twitter.setter
    def twitter(self, twitter):
        """
        Sets the twitter of this WebProfile.

        :param twitter: The twitter of this WebProfile.
        :type: str
        """

        self._twitter = twitter

    @property
    def website(self):
        """
        Gets the website of this WebProfile.

        :return: The website of this WebProfile.
        :rtype: str
        """
        return self._website

    @website.setter
    def website(self, website):
        """
        Sets the website of this WebProfile.

        :param website: The website of this WebProfile.
        :type: str
        """

        self._website = website

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
        if not isinstance(other, WebProfile):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other

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


class CandidatePropertyAvailability(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    """
    def __init__(self, to_users=None, context=None, for_org_fields=None):
        """
        CandidatePropertyAvailability - a model defined in Swagger

        :param dict swaggerTypes: The key is attribute name
                                  and the value is attribute type.
        :param dict attributeMap: The key is attribute name
                                  and the value is json key in definition.
        """
        self.swagger_types = {
            'to_users': 'str',
            'context': 'list[str]',
            'for_org_fields': 'list[CandidatePropertyFilter]'
        }

        self.attribute_map = {
            'to_users': 'toUsers',
            'context': 'context',
            'for_org_fields': 'forOrgFields'
        }

        self._to_users = to_users
        self._context = context
        self._for_org_fields = for_org_fields

    @property
    def to_users(self):
        """
        Gets the to_users of this CandidatePropertyAvailability.

        :return: The to_users of this CandidatePropertyAvailability.
        :rtype: str
        """
        return self._to_users

    @to_users.setter
    def to_users(self, to_users):
        """
        Sets the to_users of this CandidatePropertyAvailability.

        :param to_users: The to_users of this CandidatePropertyAvailability.
        :type: str
        """
        allowed_values = ["ALL", "FULL_ACCESS"]
        if to_users not in allowed_values:
            raise ValueError(
                "Invalid value for `to_users` ({0}), must be one of {1}"
                .format(to_users, allowed_values)
            )

        self._to_users = to_users

    @property
    def context(self):
        """
        Gets the context of this CandidatePropertyAvailability.

        :return: The context of this CandidatePropertyAvailability.
        :rtype: list[str]
        """
        return self._context

    @context.setter
    def context(self, context):
        """
        Sets the context of this CandidatePropertyAvailability.

        :param context: The context of this CandidatePropertyAvailability.
        :type: list[str]
        """
        allowed_values = ["HIRE_FORM", "OFFER_MANAGEMENT", "CANDIDATE_PROFILE"]
        if not set(context).issubset(set(allowed_values)):
            raise ValueError(
                "Invalid values for `context` [{0}], must be a subset of [{1}]"
                .format(", ".join(map(str, set(context)-set(allowed_values))),
                        ", ".join(map(str, allowed_values)))
            )

        self._context = context

    @property
    def for_org_fields(self):
        """
        Gets the for_org_fields of this CandidatePropertyAvailability.

        :return: The for_org_fields of this CandidatePropertyAvailability.
        :rtype: list[CandidatePropertyFilter]
        """
        return self._for_org_fields

    @for_org_fields.setter
    def for_org_fields(self, for_org_fields):
        """
        Sets the for_org_fields of this CandidatePropertyAvailability.

        :param for_org_fields: The for_org_fields of this CandidatePropertyAvailability.
        :type: list[CandidatePropertyFilter]
        """

        self._for_org_fields = for_org_fields

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
        if not isinstance(other, CandidatePropertyAvailability):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other

# coding: utf-8

"""
    Customer API - version 1

    No description provided (generated by Swagger Codegen https://github.com/swagger-api/swagger-codegen)

    OpenAPI spec version: 1
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


from pprint import pformat
from six import iteritems
import re


class JobPropertyDefinition(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    """
    def __init__(self, id=None, label=None, category=None, active=None, visible=None, required=None, actions=None):
        """
        JobPropertyDefinition - a model defined in Swagger

        :param dict swaggerTypes: The key is attribute name
                                  and the value is attribute type.
        :param dict attributeMap: The key is attribute name
                                  and the value is json key in definition.
        """
        self.swagger_types = {
            'id': 'str',
            'label': 'str',
            'category': 'str',
            'active': 'bool',
            'visible': 'bool',
            'required': 'bool',
            'actions': 'Actions'
        }

        self.attribute_map = {
            'id': 'id',
            'label': 'label',
            'category': 'category',
            'active': 'active',
            'visible': 'visible',
            'required': 'required',
            'actions': 'actions'
        }

        self._id = id
        self._label = label
        self._category = category
        self._active = active
        self._visible = visible
        self._required = required
        self._actions = actions

    @property
    def id(self):
        """
        Gets the id of this JobPropertyDefinition.

        :return: The id of this JobPropertyDefinition.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """
        Sets the id of this JobPropertyDefinition.

        :param id: The id of this JobPropertyDefinition.
        :type: str
        """

        self._id = id

    @property
    def label(self):
        """
        Gets the label of this JobPropertyDefinition.

        :return: The label of this JobPropertyDefinition.
        :rtype: str
        """
        return self._label

    @label.setter
    def label(self, label):
        """
        Sets the label of this JobPropertyDefinition.

        :param label: The label of this JobPropertyDefinition.
        :type: str
        """
        if label is None:
            raise ValueError("Invalid value for `label`, must not be `None`")

        self._label = label

    @property
    def category(self):
        """
        Gets the category of this JobPropertyDefinition.

        :return: The category of this JobPropertyDefinition.
        :rtype: str
        """
        return self._category

    @category.setter
    def category(self, category):
        """
        Sets the category of this JobPropertyDefinition.

        :param category: The category of this JobPropertyDefinition.
        :type: str
        """
        allowed_values = ["job", "organization"]
        if category not in allowed_values:
            raise ValueError(
                "Invalid value for `category` ({0}), must be one of {1}"
                .format(category, allowed_values)
            )

        self._category = category

    @property
    def active(self):
        """
        Gets the active of this JobPropertyDefinition.

        :return: The active of this JobPropertyDefinition.
        :rtype: bool
        """
        return self._active

    @active.setter
    def active(self, active):
        """
        Sets the active of this JobPropertyDefinition.

        :param active: The active of this JobPropertyDefinition.
        :type: bool
        """

        self._active = active

    @property
    def visible(self):
        """
        Gets the visible of this JobPropertyDefinition.

        :return: The visible of this JobPropertyDefinition.
        :rtype: bool
        """
        return self._visible

    @visible.setter
    def visible(self, visible):
        """
        Sets the visible of this JobPropertyDefinition.

        :param visible: The visible of this JobPropertyDefinition.
        :type: bool
        """
        if visible is None:
            raise ValueError("Invalid value for `visible`, must not be `None`")

        self._visible = visible

    @property
    def required(self):
        """
        Gets the required of this JobPropertyDefinition.

        :return: The required of this JobPropertyDefinition.
        :rtype: bool
        """
        return self._required

    @required.setter
    def required(self, required):
        """
        Sets the required of this JobPropertyDefinition.

        :param required: The required of this JobPropertyDefinition.
        :type: bool
        """

        self._required = required

    @property
    def actions(self):
        """
        Gets the actions of this JobPropertyDefinition.

        :return: The actions of this JobPropertyDefinition.
        :rtype: Actions
        """
        return self._actions

    @actions.setter
    def actions(self, actions):
        """
        Sets the actions of this JobPropertyDefinition.

        :param actions: The actions of this JobPropertyDefinition.
        :type: Actions
        """

        self._actions = actions

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
        if not isinstance(other, JobPropertyDefinition):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other
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


class JobAdItem(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    """
    def __init__(self, id=None, title=None, language=None, job_ad=None, created_on=None, updated_on=None, apply_url=None, posting_status=None, default=None, actions=None, creator=None):
        """
        JobAdItem - a model defined in Swagger

        :param dict swaggerTypes: The key is attribute name
                                  and the value is attribute type.
        :param dict attributeMap: The key is attribute name
                                  and the value is json key in definition.
        """
        self.swagger_types = {
            'id': 'str',
            'title': 'str',
            'language': 'Language',
            'job_ad': 'JobAdSections',
            'created_on': 'datetime',
            'updated_on': 'datetime',
            'apply_url': 'str',
            'posting_status': 'str',
            'default': 'bool',
            'actions': 'JobAdItemActions',
            'creator': 'Identifiable'
        }

        self.attribute_map = {
            'id': 'id',
            'title': 'title',
            'language': 'language',
            'job_ad': 'jobAd',
            'created_on': 'createdOn',
            'updated_on': 'updatedOn',
            'apply_url': 'applyUrl',
            'posting_status': 'postingStatus',
            'default': 'default',
            'actions': 'actions',
            'creator': 'creator'
        }

        self._id = id
        self._title = title
        self._language = language
        self._job_ad = job_ad
        self._created_on = created_on
        self._updated_on = updated_on
        self._apply_url = apply_url
        self._posting_status = posting_status
        self._default = default
        self._actions = actions
        self._creator = creator

    @property
    def id(self):
        """
        Gets the id of this JobAdItem.

        :return: The id of this JobAdItem.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """
        Sets the id of this JobAdItem.

        :param id: The id of this JobAdItem.
        :type: str
        """
        if id is None:
            raise ValueError("Invalid value for `id`, must not be `None`")

        self._id = id

    @property
    def title(self):
        """
        Gets the title of this JobAdItem.

        :return: The title of this JobAdItem.
        :rtype: str
        """
        return self._title

    @title.setter
    def title(self, title):
        """
        Sets the title of this JobAdItem.

        :param title: The title of this JobAdItem.
        :type: str
        """
        if title is None:
            raise ValueError("Invalid value for `title`, must not be `None`")

        self._title = title

    @property
    def language(self):
        """
        Gets the language of this JobAdItem.

        :return: The language of this JobAdItem.
        :rtype: Language
        """
        return self._language

    @language.setter
    def language(self, language):
        """
        Sets the language of this JobAdItem.

        :param language: The language of this JobAdItem.
        :type: Language
        """
        if language is None:
            raise ValueError("Invalid value for `language`, must not be `None`")

        self._language = language

    @property
    def job_ad(self):
        """
        Gets the job_ad of this JobAdItem.

        :return: The job_ad of this JobAdItem.
        :rtype: JobAdSections
        """
        return self._job_ad

    @job_ad.setter
    def job_ad(self, job_ad):
        """
        Sets the job_ad of this JobAdItem.

        :param job_ad: The job_ad of this JobAdItem.
        :type: JobAdSections
        """
        if job_ad is None:
            raise ValueError("Invalid value for `job_ad`, must not be `None`")

        self._job_ad = job_ad

    @property
    def created_on(self):
        """
        Gets the created_on of this JobAdItem.

        :return: The created_on of this JobAdItem.
        :rtype: datetime
        """
        return self._created_on

    @created_on.setter
    def created_on(self, created_on):
        """
        Sets the created_on of this JobAdItem.

        :param created_on: The created_on of this JobAdItem.
        :type: datetime
        """
        if created_on is None:
            raise ValueError("Invalid value for `created_on`, must not be `None`")

        self._created_on = created_on

    @property
    def updated_on(self):
        """
        Gets the updated_on of this JobAdItem.

        :return: The updated_on of this JobAdItem.
        :rtype: datetime
        """
        return self._updated_on

    @updated_on.setter
    def updated_on(self, updated_on):
        """
        Sets the updated_on of this JobAdItem.

        :param updated_on: The updated_on of this JobAdItem.
        :type: datetime
        """
        if updated_on is None:
            raise ValueError("Invalid value for `updated_on`, must not be `None`")

        self._updated_on = updated_on

    @property
    def apply_url(self):
        """
        Gets the apply_url of this JobAdItem.

        :return: The apply_url of this JobAdItem.
        :rtype: str
        """
        return self._apply_url

    @apply_url.setter
    def apply_url(self, apply_url):
        """
        Sets the apply_url of this JobAdItem.

        :param apply_url: The apply_url of this JobAdItem.
        :type: str
        """

        self._apply_url = apply_url

    @property
    def posting_status(self):
        """
        Gets the posting_status of this JobAdItem.

        :return: The posting_status of this JobAdItem.
        :rtype: str
        """
        return self._posting_status

    @posting_status.setter
    def posting_status(self, posting_status):
        """
        Sets the posting_status of this JobAdItem.

        :param posting_status: The posting_status of this JobAdItem.
        :type: str
        """
        allowed_values = ["PUBLISHED", "NOT_PUBLISHED"]
        if posting_status not in allowed_values:
            raise ValueError(
                "Invalid value for `posting_status` ({0}), must be one of {1}"
                .format(posting_status, allowed_values)
            )

        self._posting_status = posting_status

    @property
    def default(self):
        """
        Gets the default of this JobAdItem.

        :return: The default of this JobAdItem.
        :rtype: bool
        """
        return self._default

    @default.setter
    def default(self, default):
        """
        Sets the default of this JobAdItem.

        :param default: The default of this JobAdItem.
        :type: bool
        """
        if default is None:
            raise ValueError("Invalid value for `default`, must not be `None`")

        self._default = default

    @property
    def actions(self):
        """
        Gets the actions of this JobAdItem.

        :return: The actions of this JobAdItem.
        :rtype: JobAdItemActions
        """
        return self._actions

    @actions.setter
    def actions(self, actions):
        """
        Sets the actions of this JobAdItem.

        :param actions: The actions of this JobAdItem.
        :type: JobAdItemActions
        """

        self._actions = actions

    @property
    def creator(self):
        """
        Gets the creator of this JobAdItem.

        :return: The creator of this JobAdItem.
        :rtype: Identifiable
        """
        return self._creator

    @creator.setter
    def creator(self, creator):
        """
        Sets the creator of this JobAdItem.

        :param creator: The creator of this JobAdItem.
        :type: Identifiable
        """
        if creator is None:
            raise ValueError("Invalid value for `creator`, must not be `None`")

        self._creator = creator

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
        if not isinstance(other, JobAdItem):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other

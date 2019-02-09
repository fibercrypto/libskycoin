# coding: utf-8

"""
    Skycoin REST API.

    Skycoin is a next-generation cryptocurrency.  # noqa: E501

    OpenAPI spec version: 0.25.0
    Contact: skycoin.doe@example.com
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


import pprint
import re  # noqa: F401

import six


class InlineResponse2002Version(object):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """

    """
    Attributes:
      swagger_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    swagger_types = {
        'branch': 'str',
        'commit': 'str',
        'version': 'str'
    }

    attribute_map = {
        'branch': 'branch',
        'commit': 'commit',
        'version': 'version'
    }

    def __init__(self, branch=None, commit=None, version=None):  # noqa: E501
        """InlineResponse2002Version - a model defined in Swagger"""  # noqa: E501

        self._branch = None
        self._commit = None
        self._version = None
        self.discriminator = None

        if branch is not None:
            self.branch = branch
        if commit is not None:
            self.commit = commit
        if version is not None:
            self.version = version

    @property
    def branch(self):
        """Gets the branch of this InlineResponse2002Version.  # noqa: E501


        :return: The branch of this InlineResponse2002Version.  # noqa: E501
        :rtype: str
        """
        return self._branch

    @branch.setter
    def branch(self, branch):
        """Sets the branch of this InlineResponse2002Version.


        :param branch: The branch of this InlineResponse2002Version.  # noqa: E501
        :type: str
        """

        self._branch = branch

    @property
    def commit(self):
        """Gets the commit of this InlineResponse2002Version.  # noqa: E501


        :return: The commit of this InlineResponse2002Version.  # noqa: E501
        :rtype: str
        """
        return self._commit

    @commit.setter
    def commit(self, commit):
        """Sets the commit of this InlineResponse2002Version.


        :param commit: The commit of this InlineResponse2002Version.  # noqa: E501
        :type: str
        """

        self._commit = commit

    @property
    def version(self):
        """Gets the version of this InlineResponse2002Version.  # noqa: E501


        :return: The version of this InlineResponse2002Version.  # noqa: E501
        :rtype: str
        """
        return self._version

    @version.setter
    def version(self, version):
        """Sets the version of this InlineResponse2002Version.


        :param version: The version of this InlineResponse2002Version.  # noqa: E501
        :type: str
        """

        self._version = version

    def to_dict(self):
        """Returns the model properties as a dict"""
        result = {}

        for attr, _ in six.iteritems(self.swagger_types):
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
        """Returns the string representation of the model"""
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        """For `print` and `pprint`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, InlineResponse2002Version):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other

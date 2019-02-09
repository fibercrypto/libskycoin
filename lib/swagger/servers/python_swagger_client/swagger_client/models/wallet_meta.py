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


class WalletMeta(object):
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
        'coin': 'str',
        'crypto_type': 'str',
        'encrypted': 'bool',
        'filename': 'str',
        'label': 'str',
        'timestamp': 'int',
        'type': 'str',
        'version': 'str'
    }

    attribute_map = {
        'coin': 'coin',
        'crypto_type': 'crypto_type',
        'encrypted': 'encrypted',
        'filename': 'filename',
        'label': 'label',
        'timestamp': 'timestamp',
        'type': 'type',
        'version': 'version'
    }

    def __init__(self, coin=None, crypto_type=None, encrypted=None, filename=None, label=None, timestamp=None, type=None, version=None):  # noqa: E501
        """WalletMeta - a model defined in Swagger"""  # noqa: E501

        self._coin = None
        self._crypto_type = None
        self._encrypted = None
        self._filename = None
        self._label = None
        self._timestamp = None
        self._type = None
        self._version = None
        self.discriminator = None

        if coin is not None:
            self.coin = coin
        if crypto_type is not None:
            self.crypto_type = crypto_type
        if encrypted is not None:
            self.encrypted = encrypted
        if filename is not None:
            self.filename = filename
        if label is not None:
            self.label = label
        if timestamp is not None:
            self.timestamp = timestamp
        if type is not None:
            self.type = type
        if version is not None:
            self.version = version

    @property
    def coin(self):
        """Gets the coin of this WalletMeta.  # noqa: E501


        :return: The coin of this WalletMeta.  # noqa: E501
        :rtype: str
        """
        return self._coin

    @coin.setter
    def coin(self, coin):
        """Sets the coin of this WalletMeta.


        :param coin: The coin of this WalletMeta.  # noqa: E501
        :type: str
        """

        self._coin = coin

    @property
    def crypto_type(self):
        """Gets the crypto_type of this WalletMeta.  # noqa: E501


        :return: The crypto_type of this WalletMeta.  # noqa: E501
        :rtype: str
        """
        return self._crypto_type

    @crypto_type.setter
    def crypto_type(self, crypto_type):
        """Sets the crypto_type of this WalletMeta.


        :param crypto_type: The crypto_type of this WalletMeta.  # noqa: E501
        :type: str
        """

        self._crypto_type = crypto_type

    @property
    def encrypted(self):
        """Gets the encrypted of this WalletMeta.  # noqa: E501


        :return: The encrypted of this WalletMeta.  # noqa: E501
        :rtype: bool
        """
        return self._encrypted

    @encrypted.setter
    def encrypted(self, encrypted):
        """Sets the encrypted of this WalletMeta.


        :param encrypted: The encrypted of this WalletMeta.  # noqa: E501
        :type: bool
        """

        self._encrypted = encrypted

    @property
    def filename(self):
        """Gets the filename of this WalletMeta.  # noqa: E501


        :return: The filename of this WalletMeta.  # noqa: E501
        :rtype: str
        """
        return self._filename

    @filename.setter
    def filename(self, filename):
        """Sets the filename of this WalletMeta.


        :param filename: The filename of this WalletMeta.  # noqa: E501
        :type: str
        """

        self._filename = filename

    @property
    def label(self):
        """Gets the label of this WalletMeta.  # noqa: E501


        :return: The label of this WalletMeta.  # noqa: E501
        :rtype: str
        """
        return self._label

    @label.setter
    def label(self, label):
        """Sets the label of this WalletMeta.


        :param label: The label of this WalletMeta.  # noqa: E501
        :type: str
        """

        self._label = label

    @property
    def timestamp(self):
        """Gets the timestamp of this WalletMeta.  # noqa: E501


        :return: The timestamp of this WalletMeta.  # noqa: E501
        :rtype: int
        """
        return self._timestamp

    @timestamp.setter
    def timestamp(self, timestamp):
        """Sets the timestamp of this WalletMeta.


        :param timestamp: The timestamp of this WalletMeta.  # noqa: E501
        :type: int
        """

        self._timestamp = timestamp

    @property
    def type(self):
        """Gets the type of this WalletMeta.  # noqa: E501


        :return: The type of this WalletMeta.  # noqa: E501
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this WalletMeta.


        :param type: The type of this WalletMeta.  # noqa: E501
        :type: str
        """

        self._type = type

    @property
    def version(self):
        """Gets the version of this WalletMeta.  # noqa: E501


        :return: The version of this WalletMeta.  # noqa: E501
        :rtype: str
        """
        return self._version

    @version.setter
    def version(self, version):
        """Sets the version of this WalletMeta.


        :param version: The version of this WalletMeta.  # noqa: E501
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
        if not isinstance(other, WalletMeta):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other

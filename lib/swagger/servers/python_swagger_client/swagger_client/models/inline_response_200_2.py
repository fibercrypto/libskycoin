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

from swagger_client.models.inline_response2002_blockchain import InlineResponse2002Blockchain  # noqa: F401,E501
from swagger_client.models.inline_response2002_unconfirmed_verify_transaction import InlineResponse2002UnconfirmedVerifyTransaction  # noqa: F401,E501
from swagger_client.models.inline_response2002_version import InlineResponse2002Version  # noqa: F401,E501


class InlineResponse2002(object):
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
        'blockchain': 'InlineResponse2002Blockchain',
        'coin': 'str',
        'csp_enabled': 'bool',
        'csrf_enabled': 'bool',
        'gui_enabled': 'bool',
        'incoming_connections': 'int',
        'json_rpc_enabled': 'bool',
        'open_connections': 'int',
        'outgoing_connections': 'int',
        'started_at': 'int',
        'unconfirmed_verify_transaction': 'InlineResponse2002UnconfirmedVerifyTransaction',
        'unversioned_api_enabled': 'bool',
        'uptime': 'str',
        'user_agent': 'str',
        'user_verify_transaction': 'InlineResponse2002UnconfirmedVerifyTransaction',
        'version': 'InlineResponse2002Version',
        'wallet_api_enabled': 'bool'
    }

    attribute_map = {
        'blockchain': 'blockchain',
        'coin': 'coin',
        'csp_enabled': 'csp_enabled',
        'csrf_enabled': 'csrf_enabled',
        'gui_enabled': 'gui_enabled',
        'incoming_connections': 'incoming_connections',
        'json_rpc_enabled': 'json_rpc_enabled',
        'open_connections': 'open_connections',
        'outgoing_connections': 'outgoing_connections',
        'started_at': 'started_at',
        'unconfirmed_verify_transaction': 'unconfirmed_verify_transaction',
        'unversioned_api_enabled': 'unversioned_api_enabled',
        'uptime': 'uptime',
        'user_agent': 'user_agent',
        'user_verify_transaction': 'user_verify_transaction',
        'version': 'version',
        'wallet_api_enabled': 'wallet_api_enabled'
    }

    def __init__(self, blockchain=None, coin=None, csp_enabled=None, csrf_enabled=None, gui_enabled=None, incoming_connections=None, json_rpc_enabled=None, open_connections=None, outgoing_connections=None, started_at=None, unconfirmed_verify_transaction=None, unversioned_api_enabled=None, uptime=None, user_agent=None, user_verify_transaction=None, version=None, wallet_api_enabled=None):  # noqa: E501
        """InlineResponse2002 - a model defined in Swagger"""  # noqa: E501

        self._blockchain = None
        self._coin = None
        self._csp_enabled = None
        self._csrf_enabled = None
        self._gui_enabled = None
        self._incoming_connections = None
        self._json_rpc_enabled = None
        self._open_connections = None
        self._outgoing_connections = None
        self._started_at = None
        self._unconfirmed_verify_transaction = None
        self._unversioned_api_enabled = None
        self._uptime = None
        self._user_agent = None
        self._user_verify_transaction = None
        self._version = None
        self._wallet_api_enabled = None
        self.discriminator = None

        if blockchain is not None:
            self.blockchain = blockchain
        if coin is not None:
            self.coin = coin
        if csp_enabled is not None:
            self.csp_enabled = csp_enabled
        if csrf_enabled is not None:
            self.csrf_enabled = csrf_enabled
        if gui_enabled is not None:
            self.gui_enabled = gui_enabled
        if incoming_connections is not None:
            self.incoming_connections = incoming_connections
        if json_rpc_enabled is not None:
            self.json_rpc_enabled = json_rpc_enabled
        if open_connections is not None:
            self.open_connections = open_connections
        if outgoing_connections is not None:
            self.outgoing_connections = outgoing_connections
        if started_at is not None:
            self.started_at = started_at
        if unconfirmed_verify_transaction is not None:
            self.unconfirmed_verify_transaction = unconfirmed_verify_transaction
        if unversioned_api_enabled is not None:
            self.unversioned_api_enabled = unversioned_api_enabled
        if uptime is not None:
            self.uptime = uptime
        if user_agent is not None:
            self.user_agent = user_agent
        if user_verify_transaction is not None:
            self.user_verify_transaction = user_verify_transaction
        if version is not None:
            self.version = version
        if wallet_api_enabled is not None:
            self.wallet_api_enabled = wallet_api_enabled

    @property
    def blockchain(self):
        """Gets the blockchain of this InlineResponse2002.  # noqa: E501


        :return: The blockchain of this InlineResponse2002.  # noqa: E501
        :rtype: InlineResponse2002Blockchain
        """
        return self._blockchain

    @blockchain.setter
    def blockchain(self, blockchain):
        """Sets the blockchain of this InlineResponse2002.


        :param blockchain: The blockchain of this InlineResponse2002.  # noqa: E501
        :type: InlineResponse2002Blockchain
        """

        self._blockchain = blockchain

    @property
    def coin(self):
        """Gets the coin of this InlineResponse2002.  # noqa: E501


        :return: The coin of this InlineResponse2002.  # noqa: E501
        :rtype: str
        """
        return self._coin

    @coin.setter
    def coin(self, coin):
        """Sets the coin of this InlineResponse2002.


        :param coin: The coin of this InlineResponse2002.  # noqa: E501
        :type: str
        """

        self._coin = coin

    @property
    def csp_enabled(self):
        """Gets the csp_enabled of this InlineResponse2002.  # noqa: E501


        :return: The csp_enabled of this InlineResponse2002.  # noqa: E501
        :rtype: bool
        """
        return self._csp_enabled

    @csp_enabled.setter
    def csp_enabled(self, csp_enabled):
        """Sets the csp_enabled of this InlineResponse2002.


        :param csp_enabled: The csp_enabled of this InlineResponse2002.  # noqa: E501
        :type: bool
        """

        self._csp_enabled = csp_enabled

    @property
    def csrf_enabled(self):
        """Gets the csrf_enabled of this InlineResponse2002.  # noqa: E501


        :return: The csrf_enabled of this InlineResponse2002.  # noqa: E501
        :rtype: bool
        """
        return self._csrf_enabled

    @csrf_enabled.setter
    def csrf_enabled(self, csrf_enabled):
        """Sets the csrf_enabled of this InlineResponse2002.


        :param csrf_enabled: The csrf_enabled of this InlineResponse2002.  # noqa: E501
        :type: bool
        """

        self._csrf_enabled = csrf_enabled

    @property
    def gui_enabled(self):
        """Gets the gui_enabled of this InlineResponse2002.  # noqa: E501


        :return: The gui_enabled of this InlineResponse2002.  # noqa: E501
        :rtype: bool
        """
        return self._gui_enabled

    @gui_enabled.setter
    def gui_enabled(self, gui_enabled):
        """Sets the gui_enabled of this InlineResponse2002.


        :param gui_enabled: The gui_enabled of this InlineResponse2002.  # noqa: E501
        :type: bool
        """

        self._gui_enabled = gui_enabled

    @property
    def incoming_connections(self):
        """Gets the incoming_connections of this InlineResponse2002.  # noqa: E501


        :return: The incoming_connections of this InlineResponse2002.  # noqa: E501
        :rtype: int
        """
        return self._incoming_connections

    @incoming_connections.setter
    def incoming_connections(self, incoming_connections):
        """Sets the incoming_connections of this InlineResponse2002.


        :param incoming_connections: The incoming_connections of this InlineResponse2002.  # noqa: E501
        :type: int
        """

        self._incoming_connections = incoming_connections

    @property
    def json_rpc_enabled(self):
        """Gets the json_rpc_enabled of this InlineResponse2002.  # noqa: E501


        :return: The json_rpc_enabled of this InlineResponse2002.  # noqa: E501
        :rtype: bool
        """
        return self._json_rpc_enabled

    @json_rpc_enabled.setter
    def json_rpc_enabled(self, json_rpc_enabled):
        """Sets the json_rpc_enabled of this InlineResponse2002.


        :param json_rpc_enabled: The json_rpc_enabled of this InlineResponse2002.  # noqa: E501
        :type: bool
        """

        self._json_rpc_enabled = json_rpc_enabled

    @property
    def open_connections(self):
        """Gets the open_connections of this InlineResponse2002.  # noqa: E501


        :return: The open_connections of this InlineResponse2002.  # noqa: E501
        :rtype: int
        """
        return self._open_connections

    @open_connections.setter
    def open_connections(self, open_connections):
        """Sets the open_connections of this InlineResponse2002.


        :param open_connections: The open_connections of this InlineResponse2002.  # noqa: E501
        :type: int
        """

        self._open_connections = open_connections

    @property
    def outgoing_connections(self):
        """Gets the outgoing_connections of this InlineResponse2002.  # noqa: E501


        :return: The outgoing_connections of this InlineResponse2002.  # noqa: E501
        :rtype: int
        """
        return self._outgoing_connections

    @outgoing_connections.setter
    def outgoing_connections(self, outgoing_connections):
        """Sets the outgoing_connections of this InlineResponse2002.


        :param outgoing_connections: The outgoing_connections of this InlineResponse2002.  # noqa: E501
        :type: int
        """

        self._outgoing_connections = outgoing_connections

    @property
    def started_at(self):
        """Gets the started_at of this InlineResponse2002.  # noqa: E501


        :return: The started_at of this InlineResponse2002.  # noqa: E501
        :rtype: int
        """
        return self._started_at

    @started_at.setter
    def started_at(self, started_at):
        """Sets the started_at of this InlineResponse2002.


        :param started_at: The started_at of this InlineResponse2002.  # noqa: E501
        :type: int
        """

        self._started_at = started_at

    @property
    def unconfirmed_verify_transaction(self):
        """Gets the unconfirmed_verify_transaction of this InlineResponse2002.  # noqa: E501


        :return: The unconfirmed_verify_transaction of this InlineResponse2002.  # noqa: E501
        :rtype: InlineResponse2002UnconfirmedVerifyTransaction
        """
        return self._unconfirmed_verify_transaction

    @unconfirmed_verify_transaction.setter
    def unconfirmed_verify_transaction(self, unconfirmed_verify_transaction):
        """Sets the unconfirmed_verify_transaction of this InlineResponse2002.


        :param unconfirmed_verify_transaction: The unconfirmed_verify_transaction of this InlineResponse2002.  # noqa: E501
        :type: InlineResponse2002UnconfirmedVerifyTransaction
        """

        self._unconfirmed_verify_transaction = unconfirmed_verify_transaction

    @property
    def unversioned_api_enabled(self):
        """Gets the unversioned_api_enabled of this InlineResponse2002.  # noqa: E501


        :return: The unversioned_api_enabled of this InlineResponse2002.  # noqa: E501
        :rtype: bool
        """
        return self._unversioned_api_enabled

    @unversioned_api_enabled.setter
    def unversioned_api_enabled(self, unversioned_api_enabled):
        """Sets the unversioned_api_enabled of this InlineResponse2002.


        :param unversioned_api_enabled: The unversioned_api_enabled of this InlineResponse2002.  # noqa: E501
        :type: bool
        """

        self._unversioned_api_enabled = unversioned_api_enabled

    @property
    def uptime(self):
        """Gets the uptime of this InlineResponse2002.  # noqa: E501


        :return: The uptime of this InlineResponse2002.  # noqa: E501
        :rtype: str
        """
        return self._uptime

    @uptime.setter
    def uptime(self, uptime):
        """Sets the uptime of this InlineResponse2002.


        :param uptime: The uptime of this InlineResponse2002.  # noqa: E501
        :type: str
        """

        self._uptime = uptime

    @property
    def user_agent(self):
        """Gets the user_agent of this InlineResponse2002.  # noqa: E501


        :return: The user_agent of this InlineResponse2002.  # noqa: E501
        :rtype: str
        """
        return self._user_agent

    @user_agent.setter
    def user_agent(self, user_agent):
        """Sets the user_agent of this InlineResponse2002.


        :param user_agent: The user_agent of this InlineResponse2002.  # noqa: E501
        :type: str
        """

        self._user_agent = user_agent

    @property
    def user_verify_transaction(self):
        """Gets the user_verify_transaction of this InlineResponse2002.  # noqa: E501


        :return: The user_verify_transaction of this InlineResponse2002.  # noqa: E501
        :rtype: InlineResponse2002UnconfirmedVerifyTransaction
        """
        return self._user_verify_transaction

    @user_verify_transaction.setter
    def user_verify_transaction(self, user_verify_transaction):
        """Sets the user_verify_transaction of this InlineResponse2002.


        :param user_verify_transaction: The user_verify_transaction of this InlineResponse2002.  # noqa: E501
        :type: InlineResponse2002UnconfirmedVerifyTransaction
        """

        self._user_verify_transaction = user_verify_transaction

    @property
    def version(self):
        """Gets the version of this InlineResponse2002.  # noqa: E501


        :return: The version of this InlineResponse2002.  # noqa: E501
        :rtype: InlineResponse2002Version
        """
        return self._version

    @version.setter
    def version(self, version):
        """Sets the version of this InlineResponse2002.


        :param version: The version of this InlineResponse2002.  # noqa: E501
        :type: InlineResponse2002Version
        """

        self._version = version

    @property
    def wallet_api_enabled(self):
        """Gets the wallet_api_enabled of this InlineResponse2002.  # noqa: E501


        :return: The wallet_api_enabled of this InlineResponse2002.  # noqa: E501
        :rtype: bool
        """
        return self._wallet_api_enabled

    @wallet_api_enabled.setter
    def wallet_api_enabled(self, wallet_api_enabled):
        """Sets the wallet_api_enabled of this InlineResponse2002.


        :param wallet_api_enabled: The wallet_api_enabled of this InlineResponse2002.  # noqa: E501
        :type: bool
        """

        self._wallet_api_enabled = wallet_api_enabled

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
        if not isinstance(other, InlineResponse2002):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other

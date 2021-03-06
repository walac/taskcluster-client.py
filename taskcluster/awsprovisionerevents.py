# coding=utf-8
#####################################################
# THIS FILE IS AUTOMATICALLY GENERATED. DO NOT EDIT #
#####################################################
# noqa: E128,E201
from .client import BaseClient
from .client import createApiClient
from .client import config
from .client import createTemporaryCredentials
from .client import createSession
_defaultConfig = config


class AwsProvisionerEvents(BaseClient):
    """
    Exchanges from the provisioner... more docs later
    """

    classOptions = {
        "exchangePrefix": "exchange/taskcluster-aws-provisioner/v1/"
    }

    """
    WorkerType Created Message

    When a new `workerType` is created a message will be published to this
    exchange.

    This exchange outputs: ``http://schemas.taskcluster.net/aws-provisioner/v1/worker-type-message.json#``This exchange takes the following keys:

     * routingKeyKind: Identifier for the routing-key kind. This is always `'primary'` for the formalized routing key. (required)

     * workerType: WorkerType that this message concerns. (required)

     * reserved: Space reserved for future routing-key entries, you should always match this entry with `#`. As automatically done by our tooling, if not specified.
    """

    def workerTypeCreated(self, *args, **kwargs):
        return self._makeTopicExchange({'name': 'workerTypeCreated', 'schema': 'http://schemas.taskcluster.net/aws-provisioner/v1/worker-type-message.json#', 'routingKey': [{'summary': "Identifier for the routing-key kind. This is always `'primary'` for the formalized routing key.", 'name': 'routingKeyKind', 'multipleWords': False, 'constant': 'primary', 'required': True}, {'summary': 'WorkerType that this message concerns.', 'name': 'workerType', 'multipleWords': False, 'required': True}, {'summary': 'Space reserved for future routing-key entries, you should always match this entry with `#`. As automatically done by our tooling, if not specified.', 'name': 'reserved', 'multipleWords': True, 'required': False}], 'exchange': 'worker-type-created'}, *args, **kwargs)

    """
    WorkerType Updated Message

    When a `workerType` is updated a message will be published to this
    exchange.

    This exchange outputs: ``http://schemas.taskcluster.net/aws-provisioner/v1/worker-type-message.json#``This exchange takes the following keys:

     * routingKeyKind: Identifier for the routing-key kind. This is always `'primary'` for the formalized routing key. (required)

     * workerType: WorkerType that this message concerns. (required)

     * reserved: Space reserved for future routing-key entries, you should always match this entry with `#`. As automatically done by our tooling, if not specified.
    """

    def workerTypeUpdated(self, *args, **kwargs):
        return self._makeTopicExchange({'name': 'workerTypeUpdated', 'schema': 'http://schemas.taskcluster.net/aws-provisioner/v1/worker-type-message.json#', 'routingKey': [{'summary': "Identifier for the routing-key kind. This is always `'primary'` for the formalized routing key.", 'name': 'routingKeyKind', 'multipleWords': False, 'constant': 'primary', 'required': True}, {'summary': 'WorkerType that this message concerns.', 'name': 'workerType', 'multipleWords': False, 'required': True}, {'summary': 'Space reserved for future routing-key entries, you should always match this entry with `#`. As automatically done by our tooling, if not specified.', 'name': 'reserved', 'multipleWords': True, 'required': False}], 'exchange': 'worker-type-updated'}, *args, **kwargs)

    """
    WorkerType Removed Message

    When a `workerType` is removed a message will be published to this
    exchange.

    This exchange outputs: ``http://schemas.taskcluster.net/aws-provisioner/v1/worker-type-message.json#``This exchange takes the following keys:

     * routingKeyKind: Identifier for the routing-key kind. This is always `'primary'` for the formalized routing key. (required)

     * workerType: WorkerType that this message concerns. (required)

     * reserved: Space reserved for future routing-key entries, you should always match this entry with `#`. As automatically done by our tooling, if not specified.
    """

    def workerTypeRemoved(self, *args, **kwargs):
        return self._makeTopicExchange({'name': 'workerTypeRemoved', 'schema': 'http://schemas.taskcluster.net/aws-provisioner/v1/worker-type-message.json#', 'routingKey': [{'summary': "Identifier for the routing-key kind. This is always `'primary'` for the formalized routing key.", 'name': 'routingKeyKind', 'multipleWords': False, 'constant': 'primary', 'required': True}, {'summary': 'WorkerType that this message concerns.', 'name': 'workerType', 'multipleWords': False, 'required': True}, {'summary': 'Space reserved for future routing-key entries, you should always match this entry with `#`. As automatically done by our tooling, if not specified.', 'name': 'reserved', 'multipleWords': True, 'required': False}], 'exchange': 'worker-type-removed'}, *args, **kwargs)

    funcinfo = {
    }


__all__ = ['createTemporaryCredentials', 'config', '_defaultConfig', 'createApiClient', 'createSession', 'AwsProvisionerEvents']

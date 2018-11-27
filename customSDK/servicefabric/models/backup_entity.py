# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for
# license information.
#
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is
# regenerated.
# --------------------------------------------------------------------------

from msrest.serialization import Model


class BackupEntity(Model):
    """Describes the Service Fabric entity that is configured for backup.

    You probably want to use the sub-classes and not this class directly. Known
    sub-classes are: ApplicationBackupEntity, ServiceBackupEntity,
    PartitionBackupEntity

    :param entity_kind: Constant filled by server.
    :type entity_kind: str
    """

    _validation = {
        'entity_kind': {'required': True},
    }

    _attribute_map = {
        'entity_kind': {'key': 'EntityKind', 'type': 'str'},
    }

    _subtype_map = {
        'entity_kind': {'Application': 'ApplicationBackupEntity', 'Service': 'ServiceBackupEntity', 'Partition': 'PartitionBackupEntity'}
    }

    def __init__(self):
        super(BackupEntity, self).__init__()
        self.entity_kind = None

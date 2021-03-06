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


class ReplicaLifecycleDescription(Model):
    """Describes how the replica will behave.

    :param is_singleton_replica_move_allowed_during_upgrade: If set to true,
     replicas with a target replica set size of 1 will be permitted to move
     during upgrade.
    :type is_singleton_replica_move_allowed_during_upgrade: bool
    :param restore_replica_location_after_upgrade: If set to true, move/swap
     replica to original location after upgrade.
    :type restore_replica_location_after_upgrade: bool
    """

    _attribute_map = {
        'is_singleton_replica_move_allowed_during_upgrade': {'key': 'IsSingletonReplicaMoveAllowedDuringUpgrade', 'type': 'bool'},
        'restore_replica_location_after_upgrade': {'key': 'RestoreReplicaLocationAfterUpgrade', 'type': 'bool'},
    }

    def __init__(self, *, is_singleton_replica_move_allowed_during_upgrade: bool=None, restore_replica_location_after_upgrade: bool=None, **kwargs) -> None:
        super(ReplicaLifecycleDescription, self).__init__(**kwargs)
        self.is_singleton_replica_move_allowed_during_upgrade = is_singleton_replica_move_allowed_during_upgrade
        self.restore_replica_location_after_upgrade = restore_replica_location_after_upgrade

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


class ClusterHealthPolicy(Model):
    """Defines a health policy used to evaluate the health of the cluster or of a
    cluster node.

    :param consider_warning_as_error: Indicates whether warnings are treated
     with the same severity as errors. Default value: False .
    :type consider_warning_as_error: bool
    :param max_percent_unhealthy_nodes: The maximum allowed percentage of
     unhealthy nodes before reporting an error. For example, to allow 10% of
     nodes to be unhealthy, this value would be 10.
     The percentage represents the maximum tolerated percentage of nodes that
     can be unhealthy before the cluster is considered in error.
     If the percentage is respected but there is at least one unhealthy node,
     the health is evaluated as Warning.
     The percentage is calculated by dividing the number of unhealthy nodes
     over the total number of nodes in the cluster.
     The computation rounds up to tolerate one failure on small numbers of
     nodes. Default percentage is zero.
     In large clusters, some nodes will always be down or out for repairs, so
     this percentage should be configured to tolerate that. Default value: 0 .
    :type max_percent_unhealthy_nodes: int
    :param max_percent_unhealthy_applications: The maximum allowed percentage
     of unhealthy applications before reporting an error. For example, to allow
     10% of applications to be unhealthy, this value would be 10.
     The percentage represents the maximum tolerated percentage of applications
     that can be unhealthy before the cluster is considered in error.
     If the percentage is respected but there is at least one unhealthy
     application, the health is evaluated as Warning.
     This is calculated by dividing the number of unhealthy applications over
     the total number of application instances in the cluster, excluding
     applications of application types that are included in the
     ApplicationTypeHealthPolicyMap.
     The computation rounds up to tolerate one failure on small numbers of
     applications. Default percentage is zero. Default value: 0 .
    :type max_percent_unhealthy_applications: int
    :param application_type_health_policy_map: Defines a map with max
     percentage unhealthy applications for specific application types.
     Each entry specifies as key the application type name and as value an
     integer that represents the MaxPercentUnhealthyApplications percentage
     used to evaluate the applications of the specified application type.
     The application type health policy map can be used during cluster health
     evaluation to describe special application types.
     The application types included in the map are evaluated against the
     percentage specified in the map, and not with the global
     MaxPercentUnhealthyApplications defined in the cluster health policy.
     The applications of application types specified in the map are not counted
     against the global pool of applications.
     For example, if some applications of a type are critical, the cluster
     administrator can add an entry to the map for that application type
     and assign it a value of 0% (that is, do not tolerate any failures).
     All other applications can be evaluated with
     MaxPercentUnhealthyApplications set to 20% to tolerate some failures out
     of the thousands of application instances.
     The application type health policy map is used only if the cluster
     manifest enables application type health evaluation using the
     configuration entry for
     HealthManager/EnableApplicationTypeHealthEvaluation.
    :type application_type_health_policy_map:
     list[~azure.servicefabric.models.ApplicationTypeHealthPolicyMapItem]
    """

    _attribute_map = {
        'consider_warning_as_error': {'key': 'ConsiderWarningAsError', 'type': 'bool'},
        'max_percent_unhealthy_nodes': {'key': 'MaxPercentUnhealthyNodes', 'type': 'int'},
        'max_percent_unhealthy_applications': {'key': 'MaxPercentUnhealthyApplications', 'type': 'int'},
        'application_type_health_policy_map': {'key': 'ApplicationTypeHealthPolicyMap', 'type': '[ApplicationTypeHealthPolicyMapItem]'},
    }

    def __init__(self, *, consider_warning_as_error: bool=False, max_percent_unhealthy_nodes: int=0, max_percent_unhealthy_applications: int=0, application_type_health_policy_map=None, **kwargs) -> None:
        super(ClusterHealthPolicy, self).__init__(**kwargs)
        self.consider_warning_as_error = consider_warning_as_error
        self.max_percent_unhealthy_nodes = max_percent_unhealthy_nodes
        self.max_percent_unhealthy_applications = max_percent_unhealthy_applications
        self.application_type_health_policy_map = application_type_health_policy_map

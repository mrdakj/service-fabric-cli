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


class Probe(Model):
    """Probes have a number of fields that you can use to control their behavior.

    :param initial_delay_seconds: The initial delay in seconds to start
     executing probe once codepackage has started. Default value: 0 .
    :type initial_delay_seconds: int
    :param period_seconds: Periodic seconds to execute probe. Default value:
     10 .
    :type period_seconds: int
    :param timeout_seconds: Period after which probe is considered as failed
     if it hasn't completed successfully. Default value: 1 .
    :type timeout_seconds: int
    :param success_threshold: The count of succcessful probe executions after
     which probe is considered success. Default value: 1 .
    :type success_threshold: int
    :param failure_threshold: The count of failures after which probe is
     considered failed. Default value: 3 .
    :type failure_threshold: int
    :param exec_property: Exec command to run inside the container.
    :type exec_property: ~azure.servicefabric.models.ProbeExec
    :param http_get: Http probe for the container.
    :type http_get: ~azure.servicefabric.models.ProbeHttpGet
    :param tcp_socket: Tcp port to probe inside the container.
    :type tcp_socket: ~azure.servicefabric.models.ProbeTcpSocket
    """

    _attribute_map = {
        'initial_delay_seconds': {'key': 'initialDelaySeconds', 'type': 'int'},
        'period_seconds': {'key': 'periodSeconds', 'type': 'int'},
        'timeout_seconds': {'key': 'timeoutSeconds', 'type': 'int'},
        'success_threshold': {'key': 'successThreshold', 'type': 'int'},
        'failure_threshold': {'key': 'failureThreshold', 'type': 'int'},
        'exec_property': {'key': 'exec', 'type': 'ProbeExec'},
        'http_get': {'key': 'httpGet', 'type': 'ProbeHttpGet'},
        'tcp_socket': {'key': 'tcpSocket', 'type': 'ProbeTcpSocket'},
    }

    def __init__(self, *, initial_delay_seconds: int=0, period_seconds: int=10, timeout_seconds: int=1, success_threshold: int=1, failure_threshold: int=3, exec_property=None, http_get=None, tcp_socket=None, **kwargs) -> None:
        super(Probe, self).__init__(**kwargs)
        self.initial_delay_seconds = initial_delay_seconds
        self.period_seconds = period_seconds
        self.timeout_seconds = timeout_seconds
        self.success_threshold = success_threshold
        self.failure_threshold = failure_threshold
        self.exec_property = exec_property
        self.http_get = http_get
        self.tcp_socket = tcp_socket

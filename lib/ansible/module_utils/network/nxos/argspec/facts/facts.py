#
# -*- coding: utf-8 -*-
# Copyright 2019 Red Hat
# GNU General Public License v3.0+
# (see COPYING or https://www.gnu.org/licenses/gpl-3.0.txt)
"""
The arg spec for the nxos facts module.
"""

CHOICES = [
    'all',
    'bfd_interfaces',
    'lag_interfaces',
    'lldp_global',
    'telemetry',
    'vlans',
    'lacp',
    'lacp_interfaces',
    'interfaces',
    'l3_interfaces',
    'l2_interfaces',
]


class FactsArgs(object):
    """ The arg spec for the nxos facts module
    """

    def __init__(self, **kwargs):
        pass

    argument_spec = {
        'gather_subset': dict(default=['!config'], type='list'),
        'gather_network_resources': dict(choices=CHOICES, type='list'),
    }

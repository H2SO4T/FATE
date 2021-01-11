
settings = {
    'global_vars': [
        {'name': 'enable', 'value': False},
    ],

    'nodes': [
        {
            'node_id': 'config_0',
            'transitions': [
                {
                    'transition_id': 0,
                    'type': 'button',
                    'active': True,
                    'guard': None,
                    'set': None,
                    'destination': 'config_switch_0'
                },
                {
                    'transition_id': 1,
                    'type': 'button',
                    'active': True,
                    'guard': None,
                    'set': None,
                    'destination': 'config_1'
                },
                {
                    'transition_id': 2,
                    'type': 'button',
                    'active': True,
                    'guard': None,
                    'set': None,
                    'destination': 'config_4'
                }
            ]
        },
        {
            'node_id': 'config_switch_0',
            'transitions': [
                {
                    'transition_id': 0,
                    'type': 'button',
                    'active': True,
                    'guard': None,
                    'set': None,
                    'destination': 'config_0'
                },
                {
                    'transition_id': 1,
                    'type': 'button',
                    'active': True,
                    'guard': 'enable == True',
                    'set': 'enable = False',
                    'destination': 'config_switch_0'
                },
                {
                    'transition_id': 2,
                    'type': 'button',
                    'active': True,
                    'guard': 'enable == False',
                    'set': 'enable = True',
                    'destination': 'config_switch_0'
                },
                {
                    'transition_id': 3,
                    'type': 'button',
                    'active': True,
                    'guard': 'enable == True',
                    'set': None,
                    'destination': 'config_switch_enabled_0'
                },
                {
                    'transition_id': 4,
                    'type': 'button',
                    'active': True,
                    'guard': None,
                    'set': None,
                    'destination': 'config_switch_1'
                }
            ]
        },
        {
            'node_id': 'config_switch_enabled_0',
            'transitions': [
                {
                    'transition_id': 0,
                    'type': 'button',
                    'active': True,
                    'guard': None,
                    'set': None,
                    'destination': 'config_switch_enabled_1'
                },
                {
                    'transition_id': 1,
                    'type': 'button',
                    'active': True,
                    'guard': None,
                    'set': None,
                    'destination': 'config_switch_enabled_2'
                },
                {
                    'transition_id': 2,
                    'type': 'button',
                    'active': True,
                    'guard': None,
                    'set': None,
                    'destination': 'config_switch_enabled_3'
                },
                {
                    'transition_id': 3,
                    'type': 'button',
                    'active': True,
                    'guard': None,
                    'set': None,
                    'destination': 'config_switch_0'
                }
            ]
        },
        {
            'node_id': 'config_switch_enabled_1',
            'transitions': [
                {
                    'transition_id': 0,
                    'type': 'button',
                    'active': True,
                    'guard': None,
                    'set': None,
                    'destination': 'config_switch_enabled_0'
                }
            ]
        },
        {
            'node_id': 'config_switch_enabled_2',
            'transitions': [
                {
                    'transition_id': 0,
                    'type': 'button',
                    'active': True,
                    'guard': None,
                    'set': None,
                    'destination': 'config_switch_enabled_0'
                }
            ]
        },
        {
            'node_id': 'config_switch_enabled_3',
            'transitions': [
                {
                    'transition_id': 0,
                    'type': 'button',
                    'active': True,
                    'guard': None,
                    'set': None,
                    'destination': 'config_switch_enabled_0'
                }
            ]
        },
        {
            'node_id': 'config_switch_1',
            'transitions': [
                {
                    'transition_id': 0,
                    'type': 'button',
                    'active': True,
                    'guard': None,
                    'set': None,
                    'destination': 'config_switch_0'
                },
                {
                    'transition_id': 1,
                    'type': 'button',
                    'active': True,
                    'guard': None,
                    'set': None,
                    'destination': 'config_switch_2'
                },
                {
                    'transition_id': 2,
                    'type': 'button',
                    'active': True,
                    'guard': None,
                    'set': None,
                    'destination': 'config_switch_3'
                },
                {
                    'transition_id': 3,
                    'type': 'button',
                    'active': True,
                    'guard': None,
                    'set': None,
                    'destination': 'config_switch_4'
                }
            ]
        },
        {
            'node_id': 'config_switch_2',
            'transitions': [
                {
                    'transition_id': 0,
                    'type': 'button',
                    'active': True,
                    'guard': None,
                    'set': None,
                    'destination': 'config_switch_1'
                }
            ]
        },
        {
            'node_id': 'config_switch_3',
            'transitions': [
                {
                    'transition_id': 0,
                    'type': 'button',
                    'active': True,
                    'guard': None,
                    'set': None,
                    'destination': 'config_switch_1'
                }
            ]
        },
        {
            'node_id': 'config_switch_4',
            'transitions': [
                {
                    'transition_id': 0,
                    'type': 'button',
                    'active': True,
                    'guard': None,
                    'set': None,
                    'destination': 'config_switch_1'
                }
            ]
        },
        {
            'node_id': 'config_1',
            'transitions': [
                {
                    'transition_id': 0,
                    'type': 'button',
                    'active': True,
                    'guard': None,
                    'set': None,
                    'destination': 'config_0'
                },
                {
                    'transition_id': 1,
                    'type': 'button',
                    'active': True,
                    'guard': None,
                    'set': None,
                    'destination': 'config_2'
                },
                {
                    'transition_id': 2,
                    'type': 'button',
                    'active': True,
                    'guard': None,
                    'set': None,
                    'destination': 'config_3'
                }
            ]
        },
        {
            'node_id': 'config_2',
            'transitions': [
                {
                    'transition_id': 0,
                    'type': 'button',
                    'active': True,
                    'guard': None,
                    'set': None,
                    'destination': 'config_1'
                }
            ]
        },
        {
            'node_id': 'config_3',
            'transitions': [
                {
                    'transition_id': 0,
                    'type': 'button',
                    'active': True,
                    'guard': None,
                    'set': None,
                    'destination': 'config_1'
                }
            ]
        },
        {
            'node_id': 'config_4',
            'transitions': [
                {
                    'transition_id': 0,
                    'type': 'button',
                    'active': True,
                    'guard': None,
                    'set': None,
                    'destination': 'config_0'
                },
                {
                    'transition_id': 1,
                    'type': 'button',
                    'active': True,
                    'guard': None,
                    'set': None,
                    'destination': 'config_5'
                },
                {
                    'transition_id': 2,
                    'type': 'button',
                    'active': True,
                    'guard': None,
                    'set': None,
                    'destination': 'config_10'
                }
            ]
        },
        {
            'node_id': 'config_5',
            'transitions': [
                {
                    'transition_id': 0,
                    'type': 'button',
                    'active': True,
                    'guard': None,
                    'set': None,
                    'destination': 'config_4'
                },
                {
                    'transition_id': 1,
                    'type': 'button',
                    'active': True,
                    'guard': None,
                    'set': None,
                    'destination': 'config_6'
                },
                {
                    'transition_id': 2,
                    'type': 'button',
                    'active': True,
                    'guard': None,
                    'set': None,
                    'destination': 'config_7'
                },

                {
                    'transition_id': 3,
                    'type': 'button',
                    'active': True,
                    'guard': None,
                    'set': None,
                    'destination': 'config_8'
                },
                {
                    'transition_id': 4,
                    'type': 'button',
                    'active': True,
                    'guard': None,
                    'set': None,
                    'destination': 'config_9'
                }
            ]
        },
        {
            'node_id': 'config_6',
            'transitions': [
                {
                    'transition_id': 0,
                    'type': 'button',
                    'active': True,
                    'guard': None,
                    'set': None,
                    'destination': 'config_5'
                }
            ]
        },
        {
            'node_id': 'config_7',
            'transitions': [
                {
                    'transition_id': 0,
                    'type': 'button',
                    'active': True,
                    'guard': None,
                    'set': None,
                    'destination': 'config_5'
                }
            ]
        },
        {
            'node_id': 'config_8',
            'transitions': [
                {
                    'transition_id': 0,
                    'type': 'button',
                    'active': True,
                    'guard': None,
                    'set': None,
                    'destination': 'config_5'
                }
            ]
        },
        {
            'node_id': 'config_9',
            'transitions': [
                {
                    'transition_id': 0,
                    'type': 'button',
                    'active': True,
                    'guard': None,
                    'set': None,
                    'destination': 'config_5'
                }
            ]
        },
        {
            'node_id': 'config_10',
            'transitions': [
                {
                    'transition_id': 0,
                    'type': 'button',
                    'active': True,
                    'guard': None,
                    'set': None,
                    'destination': 'config_4'
                },
                {
                    'transition_id': 1,
                    'type': 'button',
                    'active': True,
                    'guard': None,
                    'set': None,
                    'destination': 'config_11'
                },
                {
                    'transition_id': 2,
                    'type': 'button',
                    'active': True,
                    'guard': None,
                    'set': None,
                    'destination': 'config_12'
                },
                {
                    'transition_id': 3,
                    'type': 'button',
                    'active': True,
                    'guard': None,
                    'set': None,
                    'destination': 'config_13'
                }
            ]
        },
        {
            'node_id': 'config_11',
            'transitions': [
                {
                    'transition_id': 0,
                    'type': 'button',
                    'active': True,
                    'guard': None,
                    'set': None,
                    'destination': 'config_10'
                }
            ]
        },
        {
            'node_id': 'config_12',
            'transitions': [
                {
                    'transition_id': 0,
                    'type': 'button',
                    'active': True,
                    'guard': None,
                    'set': None,
                    'destination': 'config_10'
                }
            ]
        },
        {
            'node_id': 'config_13',
            'transitions': [
                {
                    'transition_id': 0,
                    'type': 'button',
                    'active': True,
                    'guard': None,
                    'set': None,
                    'destination': 'config_10'
                }
            ]
        }
    ]
}

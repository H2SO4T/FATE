
social_mod_5 = {
    'global_vars': [
        {'name': 'username', 'value': 'tonio_cartonio'},
        {'name': 'password', 'value': 'accipigna'},
        {'name': 'login_check', 'value': False},
        {'name': 'count_messages', 'value': 0},
        {'name': 'count_post', 'value': 0},
        {'name': 'user_field', 'value': ''},
        {'name': 'pass_field', 'value': ''}
    ],
    'nodes': [
        {
            'node_id': 'login',
            'transitions': [
                {
                    'transition_id': 0,
                    'type': 'button',
                    'active': True,
                    'guard': '(pass_field==password) & (user_field == username)',
                    'set': 'login_check = True',
                    'destination': 'main_act'
                },
                {
                    'transition_id': 1,
                    'type': 'editText',
                    'active': True,
                    'guard': None,
                    'set': 'user_field = input_text',
                    'destination': 'login',
                },
                {
                    'transition_id': 2,
                    'type': 'editText',
                    'active': True,
                    'guard': None,
                    'set': 'pass_field = input_text',
                    'destination': 'login',
                },
                {
                    "transition_id": 3,
                    "type": "button",
                    "active": True,
                    "guard": None,
                    "set": None,
                    "destination": "login"
                },
                {
                    "transition_id": 4,
                    "type": "button",
                    "active": True,
                    "guard": None,
                    "set": None,
                    "destination": "login"
                },
                {
                    "transition_id": 5,
                    "type": "button",
                    "active": True,
                    "guard": None,
                    "set": None,
                    "destination": "login"
                },
                {
                    "transition_id": 6,
                    "type": "button",
                    "active": True,
                    "guard": None,
                    "set": None,
                    "destination": "login"
                },
                {
                    "transition_id": 7,
                    "type": "button",
                    "active": True,
                    "guard": None,
                    "set": None,
                    "destination": "login"
                }
            ]
        },
        {
            'node_id': 'main_act',
            'transitions': [
                {
                    'transition_id': 0,
                    'type': 'button',
                    'active': True,
                    'guard': None,
                    'set': None,
                    'destination': 'messages'
                },
                {
                    'transition_id': 1,
                    'type': 'button',
                    'active': True,
                    'guard': None,
                    'set': None,
                    'destination': 'my_profile'
                }
            ]
        },
        {
            'node_id': 'messages',
            'transitions': [
                    {
                        'transition_id': 0,
                        'type': 'button',
                        'active': True,
                        'guard': None,
                        'set': 'count_messages = count_messages + 1',
                        'destination': 'messages'
                    },
                    {
                        'transition_id': 1,
                        'type': 'button',
                        'active': True,
                        'guard': 'count_messages > 0',
                        'set': 'count_messages = count_messages - 1',
                        'destination': 'messages'
                    },
                    {
                        'transition_id': 2,
                        'type': 'button',
                        'active': True,
                        'guard': 'count_messages >= 1',
                        'set': None,
                        'destination': 'chat_x'
                    },
                    {
                        'transition_id': 3,
                        'type': 'button',
                        'active': True,
                        'guard': None,
                        'set': None,
                        'destination': 'my_profile'
                    },
                    {
                        'transition_id': 4,
                        'type': 'button',
                        'active': True,
                        'guard': None,
                        'set': None,
                        'destination': 'main_act'
                    }
                ]
        },
        {
            'node_id': 'chat_x',
            'transitions': [
                {
                    'transition_id': 0,
                    'type': 'button',
                    'active': True,
                    'guard': None,
                    'set': None,
                    'destination': 'messages'
                }
            ]
        },
        {
            'node_id': 'my_profile',
            'transitions': [
                {
                    'transition_id': 0,
                    'type': 'button',
                    'active': True,
                    'guard': None,
                    'set': 'count_post = count_post + 1',
                    'destination': 'my_profile'
                },
                {
                    'transition_id': 1,
                    'type': 'button',
                    'active': True,
                    'guard': 'count_post > 0',
                    'set': 'count_post = count_post - 1',
                    'destination': 'my_profile'
                },
                {
                    'transition_id': 2,
                    'type': 'button',
                    'active': True,
                    'guard': 'count_post > 0',
                    'set': None,
                    'destination': 'my_posts'
                },
                {
                    'transition_id': 3,
                    'type': 'button',
                    'active': True,
                    'guard': None,
                    'set': None,
                    'destination': 'messages'
                },
                {
                    'transition_id': 4,
                    'type': 'button',
                    'active': True,
                    'guard': None,
                    'set': None,
                    'destination': 'main_act'
                },
                {
                    'transition_id': 5,
                    'type': 'button',
                    'active': True,
                    'guard': None,
                    'set': None,
                    'destination': 'prefs'
                }
            ]
        },
        {
            'node_id': 'my_posts',
            'transitions': [
                {
                    'transition_id': 0,
                    'type': 'button',
                    'active': True,
                    'guard': None,
                    'set': None,
                    'destination': 'my_profile'
                }
            ]
        },
        {
            'node_id': 'prefs',
            'transitions': [
                {
                    'transition_id': 0,
                    'type': 'button',
                    'active': True,
                    'guard': None,
                    'set': None,
                    'destination': 'pref_0'
                },
                {
                    'transition_id': 1,
                    'type': 'button',
                    'active': True,
                    'guard': None,
                    'set': None,
                    'destination': 'pref_1'
                },
                {
                    'transition_id': 2,
                    'type': 'button',
                    'active': True,
                    'guard': None,
                    'set': None,
                    'destination': 'pref_2'
                },
                {
                    'transition_id': 3,
                    'type': 'button',
                    'active': True,
                    'guard': None,
                    'set': None,
                    'destination': 'my_profile'
                }

            ]
        },
        {
            'node_id': 'pref_0',
            'transitions': [
                {
                    'transition_id': 0,
                    'type': 'button',
                    'active': True,
                    'guard': None,
                    'set': None,
                    'destination': 'prefs'
                }
            ]
        },
        {
            'node_id': 'pref_1',
            'transitions': [
                {
                    'transition_id': 0,
                    'type': 'button',
                    'active': True,
                    'guard': None,
                    'set': None,
                    'destination': 'prefs'
                }
            ]
        },
        {
            'node_id': 'pref_2',
            'transitions': [
                {
                    'transition_id': 0,
                    'type': 'button',
                    'active': True,
                    'guard': None,
                    'set': None,
                    'destination': 'prefs'
                }
            ]
        }
    ]
}


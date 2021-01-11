
market = {
    'global_vars': [
        {'name': 'username', 'value': 'tonio_cartonio'},
        {'name': 'password', 'value': 'accipigna'},
        {'name': 'login_check', 'value': False},
        {'name': 'product', 'value': 0},
        {'name': 'orders', 'value': 0},
        {'name': 'user_field', 'value': ''},
        {'name': 'pass_field', 'value': ''}
    ],
    'nodes': [
        {
            'node_id': 'search_products',
            'transitions': [
                {
                    'transition_id': 0,
                    'type': 'button',
                    'active': True,
                    'guard': None,
                    'set': None,
                    'destination': 'view_product',
                },
                {
                    'transition_id': 1,
                    'type': 'button',
                    'active': True,
                    'guard': 'product >=1',
                    'set': None,
                    'destination': 'cart',
                },
                {
                    'transition_id': 2,
                    'type': 'button',
                    'active': True,
                    'guard': None,
                    'set': None,
                    'destination': 'login'
                }
            ]
        },
        {
            'node_id': 'view_product',
            'transitions': [
                {
                    'transition_id': 0,
                    'type': 'button',
                    'active': True,
                    'guard': None,
                    'set': 'product = product + 1',
                    'destination': 'view_product'
                },
                {
                    'transition_id': 1,
                    'type': 'button',
                    'active': True,
                    'guard': None,
                    'set': None,
                    'destination': 'search_products'
                }
            ]
        },
        {
            'node_id': 'login',
            'transitions': [
                {
                    'transition_id': 0,
                    'type': 'button',
                    'active': True,
                    'guard': None,
                    'set': None,
                    'destination': 'search_products'
                },
                {
                    'transition_id': 1,
                    'type': 'button',
                    'active': True,
                    'guard': '(pass_field==password) & (user_field==username)',
                    'set': 'login_check = True',
                    'destination': 'login'
                },
                {
                    'transition_id': 2,
                    'type': 'editText',
                    'active': True,
                    'guard': None,
                    'set': 'user_field = input_text',
                    'destination': 'login',
                },
                {
                    'transition_id': 3,
                    'type': 'editText',
                    'active': True,
                    'guard': None,
                    'set': 'pass_field = input_text',
                    'destination': 'login',
                },
                {
                    'transition_id': 4,
                    'type': 'button',
                    'active': True,
                    'guard': 'login_check == True',
                    'set': None,
                    'destination': 'my_account'
                }
            ]
        },
        {
            'node_id': 'my_account',
            'transitions': [
                {
                    'transition_id': 0,
                    'type': 'button',
                    'active': True,
                    'guard': None,
                    'set': None,
                    'destination': 'search_products'
                },
                {
                    'transition_id': 1,
                    'type': 'button',
                    'active': True,
                    'guard': 'orders > 0',
                    'set': None,
                    'destination': 'my_orders'
                },
                {
                    'transition_id': 2,
                    'type': 'button',
                    'active': True,
                    'guard': None,
                    'set': None,
                    'destination': 'prefs'
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
                    'destination': 'my_account'
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
        },
        {
            'node_id': 'cart',
            'transitions': [
                {
                    'transition_id': 0,
                    'type': 'button',
                    'active': True,
                    'guard': 'product > 0',
                    'set': 'product = product - 1',
                    'destination': 'cart'
                },
                {
                    'transition_id': 1,
                    'type': 'button',
                    'active': True,
                    'guard': '(product > 0) & (login_check == True)',
                    'set': 'orders = product\nproduct = 0',
                    'destination': 'pay'
                },
                {
                    'transition_id': 2,
                    'type': 'button',
                    'active': True,
                    'guard': None,
                    'set': None,
                    'destination': 'search_products'
                }
            ]
        },
        {
            'node_id': 'pay',
            'transitions': [
                {
                    'transition_id': 0,
                    'type': 'button',
                    'active': True,
                    'guard': None,
                    'set': None,
                    'destination': 'my_orders'
                },
                {
                    'transition_id': 1,
                    'type': 'button',
                    'active': True,
                    'guard': None,
                    'set': None,
                    'destination': 'search_products'
                }
            ]
        },
        {
            'node_id': 'my_orders',
            'transitions': [
                {
                    'transition_id': 0,
                    'type': 'button',
                    'active': True,
                    'guard': None,
                    'set': None,
                    'destination': 'order_detail'
                },
                {
                    'transition_id': 1,
                    'type': 'button',
                    'active': True,
                    'guard': None,
                    'set': None,
                    'destination': 'search_products'
                }
            ]
        },
        {
            'node_id': 'order_detail',
            'transitions': [
                {
                    'transition_id': 0,
                    'type': 'button',
                    'active': True,
                    'guard': None,
                    'set': None,
                    'destination': 'my_orders'
                }
            ]
        }

    ]
}

bank_mod_5 = {
    "global_vars": [
        {"name": "username", "value": "tonio_cartonio"},
        {"name": "password", "value": "accipigna"},
        {"name": "insert_pass", "value": ""},
        {"name": "user_field", "value": ""},
        {"name": "pass_field", "value": ""},
        {"name":  "login_check", "value":  True}
    ],
    "nodes": [
        {
            "node_id": "login",
            "transitions": [
                {
                    "transition_id": 0,
                    "type": "button",
                    "active": True,
                    "guard": "(user_field==username) & (pass_field==password)",
                    "set": "login_check = True",
                    "destination": "manage_money"
                },
                {
                    "transition_id": 1,
                    "type": "editText",
                    "active": True,
                    "guard": None,
                    "set": "user_field = input_text",
                    "destination": "login"
                },
                {
                    "transition_id": 2,
                    "type": "editText",
                    "active": True,
                    "guard": None,
                    "set": "pass_field = input_text",
                    "destination": "login"
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
            "node_id": "manage_money",
            "transitions": [
                {
                    "transition_id": 0,
                    "type": "button",
                    "active": True,
                    "guard": None,
                    "set": None,
                    "destination": "my_account"
                },
                {
                    "transition_id": 1,
                    "type": "button",
                    "active": True,
                    "guard": None,
                    "set": "insert_pass=\"\"",
                    "destination": "send_money"
                },
                {
                    "transition_id": 2,
                    "type": "button",
                    "active": True,
                    "guard": None,
                    "set": "insert_pass=\"\"",
                    "destination": "pay"
                },
                {
                    "transition_id": 3,
                    "type": "button",
                    "active": True,
                    "guard": None,
                    "set": None,
                    "destination": "transactions_history"
                }
            ]
        },
        {
            "node_id": "transactions_history",
            "transitions": [
                {
                    "transition_id": 0,
                    "type": "button",
                    "active": True,
                    "guard": None,
                    "set": None,
                    "destination": "manage_money"
                },
                {
                    "transition_id": 1,
                    "type": "button",
                    "active": True,
                    "guard": None,
                    "set": None,
                    "destination": "view_transaction"
                }
            ]
        },
        {
            "node_id": "view_transaction",
            "transitions": [
                {
                    "transition_id": 0,
                    "type": "button",
                    "active": True,
                    "guard": None,
                    "set": None,
                    "destination": "view_transaction"
                },
                {
                    "transition_id": 1,
                    "type": "button",
                    "active": True,
                    "guard": None,
                    "set": None,
                    "destination": "transactions_history"
                }
            ]
        },
        {
            "node_id": "pay",
            "transitions": [
                {
                    "transition_id": 0,
                    "type": "button",
                    "active": True,
                    "guard": None,
                    "set": None,
                    "destination": "manage_money"
                },
                {
                    "transition_id": 1,
                    "type": "editText",
                    "active": True,
                    "guard": None,
                    "set": "insert_pass=input_text",
                    "destination": "pay"
                },
                {
                    "transition_id": 2,
                    "type": "button",
                    "active": True,
                    "guard": "insert_pass == password",
                    "set": None,
                    "destination": "confirm_pay"
                }
            ]
        },
        {
            "node_id": "confirm_pay",
            "transitions": [
                {
                    "transition_id": 0,
                    "type": "button",
                    "active": True,
                    "guard": None,
                    "set": None,
                    "destination": "pay"
                }
            ]
        },
        {
            "node_id": "send_money",
            "transitions": [
                {
                    "transition_id": 0,
                    "type": "button",
                    "active": True,
                    "guard": None,
                    "set": None,
                    "destination": "manage_money"
                },
                {
                    "transition_id": 1,
                    "type": "editText",
                    "active": True,
                    "guard": None,
                    "set": "insert_pass = input_text",
                    "destination": "send_money"
                },
                {
                    "transition_id": 2,
                    "type": "button",
                    "active": True,
                    "guard": None,
                    "set": None,
                    "destination": "confirm_send"
                }
            ]
        },
        {
            "node_id": "confirm_send",
            "transitions": [
                {
                    "transition_id": 0,
                    "type": "button",
                    "active": True,
                    "guard": None,
                    "set": None,
                    "destination": "send_money"
                }
            ]
        },
        {
            "node_id": "my_account",
            "transitions": [
                {
                    "transition_id": 0,
                    "type": "button",
                    "active": True,
                    "guard": None,
                    "set": None,
                    "destination": "manage_money"
                },
                {
                    "transition_id": 1,
                    "type": "button",
                    "active": True,
                    "guard": None,
                    "set": "insert_pass=\"\"",
                    "destination": "modify_mail"
                },
                {
                    "transition_id": 2,
                    "type": "button",
                    "active": True,
                    "guard": None,
                    "set": "insert_pass=\"\"",
                    "destination": "manage_card"
                }
            ]
        },
        {
            "node_id": "modify_mail",
            "transitions": [
                {
                    "transition_id": 0,
                    "type": "button",
                    "active": True,
                    "guard": None,
                    "set": None,
                    "destination": "my_account"
                },
                {
                    "transition_id": 1,
                    "type": "editText",
                    "active": True,
                    "guard": None,
                    "set": "insert_pass = input_text",
                    "destination": "modify_mail"
                },
                {
                    "transition_id": 2,
                    "type": "button",
                    "active": True,
                    "guard": "insert_pass == password",
                    "set": None,
                    "destination": "confirm_pass"
                }
            ]
        },
        {
            "node_id": "confirm_pass",
            "transitions": [
                {
                    "transition_id": 0,
                    "type": "button",
                    "active": True,
                    "guard": None,
                    "set": None,
                    "destination": "modify_mail"
                }
            ]
        },
        {
            "node_id": "manage_card",
            "transitions": [
                {
                    "transition_id": 0,
                    "type": "button",
                    "active": True,
                    "guard": None,
                    "set": None,
                    "destination": "my_account"
                },
                {
                    "transition_id": 1,
                    "type": "button",
                    "active": True,
                    "guard": None,
                    "set": "insert_pass = \"\"",
                    "destination": "daily_withdrawal"
                },
                {
                    "transition_id": 2,
                    "type": "button",
                    "active": True,
                    "guard": None,
                    "set": "insert_pass = \"\"",
                    "destination": "daily_internet"
                }
            ]
        },
        {
            "node_id": "daily_withdrawal",
            "transitions": [
                {
                    "transition_id": 0,
                    "type": "button",
                    "active": True,
                    "guard": None,
                    "set": None,
                    "destination": "manage_card"
                },
                {
                    "transition_id": 1,
                    "type": "editText",
                    "active": True,
                    "guard": None,
                    "set": "insert_pass = input_text",
                    "destination": "daily_withdrawal"
                },
                {
                    "transition_id": 2,
                    "type": "button",
                    "active": True,
                    "guard": "insert_pass == password",
                    "set": None,
                    "destination": "confirm_withdrawal"
                }
            ]
        },
        {
            "node_id": "confirm_withdrawal",
            "transitions": [
                {
                    "transition_id": 0,
                    "type": "button",
                    "active": True,
                    "guard": None,
                    "set": None,
                    "destination": "daily_withdrawal"
                }
            ]
        },
        {
            "node_id": "daily_internet",
            "transitions": [
                {
                    "transition_id": 0,
                    "type": "button",
                    "active": True,
                    "guard": None,
                    "set": None,
                    "destination": "manage_card"
                },
                {
                    "transition_id": 1,
                    "type": "editText",
                    "active": True,
                    "guard": None,
                    "set": "insert_pass=input_text",
                    "destination": "daily_internet"
                },
                {
                    "transition_id": 2,
                    "type": "button",
                    "active": True,
                    "guard": "insert_pass == password",
                    "set": None,
                    "destination": "confirm_internet"
                }
            ]
        },
        {
            "node_id": "confirm_internet",
            "transitions": [
                {
                    "transition_id": 0,
                    "type": "button",
                    "active": True,
                    "guard": None,
                    "set": None,
                    "destination": "daily_internet"
                }
            ]
        }
    ]
}

game_settings_func = {
    'type': 'function',
    'function': {
        'name': 'game_settings',
        'description': 'The settings of the game',
        'parameters': {
            'type': 'object',
            'properties': {
                'style': {
                    'type': 'string',
                    'description': "A 50 characters short summary of the game style selected by the user.",
                    'maxLength': 50,
                },
                'plot': {
                    'type': 'string',
                    'description': "A 200 characters summary of the the game story.",
                    'maxLength': 200,
                }
            },
            'required': ['style', 'plot']
        }
    }
}

player_settings_func = {
    'type': 'function',
    'function': {
        'name': 'player_settings',
        'description': "The player properties based on the user's description",
        'parameters': {
            'type': 'object',
            'properties': {
                'genre': {
                    'type': 'string',
                    'description': "A single word for the player's genre. One of male or female",
                    'enum': ['male', 'female'],
                },
                'fight_style': {
                    'type': 'string',
                    'description': "A single word for the player's fight style.",
                    'enum': ['melee', 'marksman', 'spellcaster', 'tactician'],
                },
                'category': {
                    'type': 'string',
                    'description': "The category of the fighter generated from the description from the user",
                    'maxLength': 20
                },
                'attack_weapon': {
                    'type': 'string',
                    'description': "The attack weapon of the fighter generated from the description from the user",
                    'maxLength': 20
                }
            },
            'required': ['genre', 'fight_style', 'category', 'attack_weapon']
        }
    }
}

battle_plot_func = {
    'type': 'function',
    'function': {
        'name': 'battle_plot',
        'description': "Generate a plot for an battle turn for the RPG game based on the user's current situation.",
        'parameters': {
            'type': 'object',
            'properties': {
                'battle_plot': {
                    'type': 'string',
                    'description': "Full description of the battle turn."
                },
            }
        },
        'required': ['battle_plot']
    }
}

battle_result_func = {
    'type': 'function',
    'function': {
        'name': 'battle_plot',
        'description': "Generate a result for the battle turn for the RPG game based on the user's situation.",
        'parameters': {
            'type': 'object',
            'properties': {
                'battle_result': {
                    'type': 'string',
                    'description': "Choose the result of the battle based on 35% chance to win, 15% to lose and 50% chance to remain in the battle.",
                    'enum': ['won', 'lost', 'remain'],
                },
                'battle_result_description': {
                    'type': 'string',
                    'description': "Full description of the battle result."
                },
            }
        },
        'required': ['battle_result']
    }
}

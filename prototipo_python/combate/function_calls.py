battle_plot_func = {
    'type': 'function',
    'function': {
        'name': 'battle_plot',
        'description': "Generate a plot for a start of a battle turn for the RPG game based on the user's current situation.",
        'parameters': {
            'type': 'object',
            'properties': {
                'battle_plot': {
                    'type': 'string',
                    'description': "Description of the start of the battle."
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
                    'description': "The result of the battle whether the user won, lost or remain in the battle.",
                    'enum': ['won', 'lost', 'remain'],
                },
                'battle_result_description': {
                    'type': 'string',
                    'description': "Create the description of the battle result."
                },
            }
        },
        'required': ['battle_result']
    }
}

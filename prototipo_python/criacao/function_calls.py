start_rpg_adventure = {
    'type': 'function',
    'function': {
        'name': 'start_rpg_adventure',
        'description': 'Generate a full story text of the game',
        'parameters': {
            'type': 'object',
            'properties': {
                'full_story': {
                    'type': 'string',
                    'description': 'The new story text for the game with at most 500 characters.',
                    'maxLength': 500,
                }
            },
            'required': ['full_story']
        }
    }
}

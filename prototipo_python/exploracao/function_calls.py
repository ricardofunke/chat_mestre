exploration_plot_func = {
    'type': 'function',
    'function': {
        'name': 'exploration_plot',
        'description': 'Generate a plot for an exploration turn for the RPG game without battles and no items to collect.',
        'parameters': {
            'type': 'object',
            'properties': {
                'exploration_plot': {
                    'type': 'string',
                    'description': "Full description of the exploration turn with a begin, middle and end."
                },
                'first_iteration': {
                    'type': 'string',
                    'description': "the first iteration of the player with this exploration scenary, with a 100 characters description.",
                    'maxLength': 100,
                }
            }
        },
        'required': ['exploration_plot', 'first_iteration']
    }
}

exploration_options_func = {
    'type': 'function',
    'function': {
        'name': 'exploration_options',
        'description': 'Give 4 options for the user to continue the exploration',
        'parameters': {
            'type': 'object',
            'properties': {
                'option_1': {
                    'type': 'string',
                    'description': 'A 100 characters long description of the first option for the player.',
                    'maxLength': 100,
                },
                'option_2': {
                    'type': 'string',
                    'description': 'A 100 characters long description of the second option for the player.',
                    'maxLength': 100,
                },
                'option_3': {
                    'type': 'string',
                    'description': 'A 100 characters long description of the third option for the player.',
                    'maxLength': 100,
                },
                'option_4': {
                    'type': 'string',
                    'description': 'A 100 characters long description of the fourth option for the player.',
                    'maxLength': 100,
                }
            },
            'required': ['option_1', 'option_2', 'option_3', 'option_4']
        }
    }
}

exploration_next_iteration_func = {
    'type': 'function',
    'function': {
        'name': 'exploration_next_iteration',
        'description': "The next iteration of the user in this exploration, based on the context story and his previous iteration.",
        'parameters': {
            'type': 'object',
            'properties': {
                'next_iteration': {
                    'type': 'string',
                    'description': "A 100 characters description of this next iteration.",
                    'maxLength': 100,
                }
            },
            'required': ['next_iteration']
        }
    }
}

exploration_final_iteration_func = {
    'type': 'function',
    'function': {
        'name': 'exploration_final_iteration',
        'description': "The last iteration of the user in this exploration, based on the context story and his previous iteration.",
        'parameters': {
            'type': 'object',
            'properties': {
                'last_iteration': {
                    'type': 'string',
                    'description': "A 100 characters description of this last iteration.",
                    'maxLength': 100,
                }
            },
            'required': ['last_iteration']
        }
    }
}

exploration_final_options_func = {
    'type': 'function',
    'function': {
        'name': 'exploration_final_options',
        'description': 'Give 4 options for the user to finish the exploration',
        'parameters': {
            'type': 'object',
            'properties': {
                'option_1': {
                    'type': 'string',
                    'description': 'A 100 characters long description of the first option for the player.',
                    'maxLength': 100,
                },
                'option_2': {
                    'type': 'string',
                    'description': 'A 100 characters long description of the second option for the player.',
                    'maxLength': 100,
                },
                'option_3': {
                    'type': 'string',
                    'description': 'A 100 characters long description of the third option for the player.',
                    'maxLength': 100,
                },
                'option_4': {
                    'type': 'string',
                    'description': 'A 100 characters long description of the fourth option for the player.',
                    'maxLength': 100,
                }
            },
            'required': ['option_1', 'option_2', 'option_3', 'option_4']
        }
    }
}

exploration_finale = {
    'type': 'function',
    'function': {
        'name': 'exploration_finale',
        'description': "Give an end to the exploration for the user, based on the context story and his previous iteration.",
        'parameters': {
            'type': 'object',
            'properties': {
                'end_of_exploration': {
                    'type': 'string',
                    'description': "A 100 characters long of the end story of this exploration based on the user's previous iteration.",
                    'maxLength': 100,
                }
            },
            'required': ['end_of_exploration']
        }
    }
}

import json
import sys
from time import sleep

import openai

from common.env_vars import OPENAI_KEY

openai.api_key = OPENAI_KEY

start_rpg_adventure = {
    'type': 'function',
    'function': {
        'name': 'start_rpg_adventure',
        'description': 'Get the adventure text and its summary',
        'parameters': {
            'type': 'object',
            'properties': {
                'begin_history_text': {
                    'type': 'string',
                    'description': 'The full text generated to begin the RPG adventure. '
                                   'This field must have a max length of 500 characters',
                    'maxLength': 500,
                },
                'next_iteration_summary': {
                    'type': 'string',
                    'description': 'A brief summary of begin_history_text with all its most important topics to be used in the next iteration. '
                                   'This field must have a max length of 100 characters',
                    'maxLength': 100,
                }
            },
            'required': ['begin_history_text', 'next_iteration_summary']
        }
    }
}

exploration_mode = {
    'type': 'function',
    'function': {
        'name': 'exploration_mode',
        'description': 'Continue the RPG game in the exploration mode',
        'parameters': {
            'type': 'object',
            'properties': {
                'choice_consequence': {
                    'type': 'string',
                    'description': "The continuation from the player's choice if any. "
                                   "If no previous choice was made, just return an empty string. "
                                   "This field must have a max length of 100 characters"
                },
                'exploration_context': {
                    'type': 'string',
                    'description': 'The context for the exploration. '
                                   'The exploration context cannot ever go into a battle of any kind. '
                                   'This field must have a max length of 500 characters',
                    'maxLength': 500,
                },
                'option1': {
                    'type': 'string',
                    'description': 'The first option for the player. '
                                   'This field must have a max length of 50 characters',
                    'maxLength': 50,
                },
                'option2': {
                    'type': 'string',
                    'description': 'The second option for the player. '
                                   'This field must have a max length of 50 characters',
                    'maxLength': 50,
                }
            },
            'required': ['choice_consequence', 'exploration_context', 'option1', 'option2']
        }
    }
}


def call_openai(messages: list, function_call: dict, temperature=1, model='gpt-3.5-turbo', timeout=60) -> dict:

    max_retries = 3
    errors = []
    for retry in range(max_retries):
        try:
            response = openai.chat.completions.create(
                model=model,
                messages=messages,
                tools=[function_call],
                tool_choice={'type': 'function', 'function': {'name': function_call['function']['name']}},
                temperature=temperature,
                timeout=timeout
            )
        except (openai.APIError,
                openai.APITimeoutError,
                openai.APIConnectionError,
                openai.InternalServerError) as error:
            errors.append(error)
            print(f"Falha ao obter resposta da OpenAI, tentando novamente... ({retry+1}/{max_retries}): {error}")
            sleep(5)
            continue

        return json.loads(response.choices[0].message.tool_calls[0].function.arguments)

    print(f"Falha ao obter resposta da OpenAI: {errors}")


if __name__ == '__main__':
    game_style = 'A standard medieval game with wizard, elves, dwarfs and all.'
    result = call_openai(
        messages=[{
            'role': 'system',
            'content': f'You are the master of an RPG game based on {game_style}.\n'
                       f'Start the game telling a short story for the beginning of the adventure.',
        }],
        function_call=start_rpg_adventure,
    )
    begin = result['begin_history_text']
    summary = result['next_iteration_summary']

    print(begin)
    print()
    print(summary)
    print()

    result = call_openai(
        messages=[{
            'role': 'system',
            'content': (f'You are the master of an RPG game based on {game_style}.\n'
                        f'You will continue the game based on the summary bellow between <> in the exploration mode.\n'
                        f'<{summary}>\n'
                        f'1) Start an exploration from the beginning based on the summary above.\n'
                        f'2) Give the player two options to continue the exploration.\n'
                        f'3) The exploration mode cannot ever go into any battles.')
        }],
        function_call=exploration_mode,
    )

    choice = result['choice_consequence']
    context = result['exploration_context']
    option1 = result['option1']
    option2 = result['option2']

    print(f'{choice = }')
    print(f'{context = }')
    print(f'{option1 = }')
    print(f'{option2 = }')

    print()

    option = int(input('Select the option: '))
    match option:
        case int():
            match option:
                case 1:
                    selected_option = option1
                case 2:
                    selected_option = option2
                case _:
                    print(f'Unknown option: {option}')
                    sys.exit(1)
        case _:
            print(f'Unknown option: {option}')
            sys.exit(1)

    print()

    while True:
        result = call_openai(
            messages=[
                {
                    'role': 'system',
                    'content': (f'You are the master of an RPG game based on {game_style}.\n'
                                f'You are continuing the game which its context summary is the text bellow between <>\n'
                                f'{summary}'),
                },
                {
                    'role': 'system',
                    'content': f"This is the context of the exploration: {context}\n"
                               f"This is the next step of the user's exploration: {choice}",
                },
                {
                    'role': 'assistant',
                    'content': context,
                },
                {
                    'role': 'user',
                    'content': selected_option,
                },
                {
                    'role': 'system',
                    'content': f"Follow the following instructions:\n"
                               f"1) Tell the user the result of his choice.\n"
                               f"2) Go further creating a detailed narrative from the result of the user's choice.\n"
                               f"3) Give the user two more option for the next exploration step."
                               f"4) The exploration mode cannot go into any battles."
                }
            ],
            function_call=exploration_mode,
        )

        choice = result['choice_consequence']
        context = result['exploration_context']
        option1 = result['option1']
        option2 = result['option2']

        print(f'{choice = }')
        print(f'{context = }')
        print(f'{option1 = }')
        print(f'{option2 = }')

        option = int(input('Select the option: '))
        match option:
            case 1:
                selected_option = option1
            case 2:
                selected_option = option2
            case _:
                print(f'Unknown option: {option}')
                break

        print()

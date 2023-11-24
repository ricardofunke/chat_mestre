from textwrap import dedent

from common.openai_calls import call_openai
from controle.function_calls import game_settings_func, player_settings_func
from controle.game_settings import PlayerCharacter, GameSettings


def get_game_settings(game_style, player_description):
    prompt_create_story = dedent(f"""\
        You are the master of an RPG game.
        Based on the game style given by the user between <> bellow
        <{game_style}>
        Create the story of this game.\
        """)

    game = call_openai(
        [{
            'role': 'system',
            'content': prompt_create_story
        }],
        game_settings_func
    )

    prompt_create_player = dedent(f"""\
        Based on the game plot bellow between <>
        <{game['plot']}>
        Create a character for the user based on his description of that player between <> bellow
        <{player_description}>
        \
        """)

    player = call_openai(
        [{
            'role': 'system',
            'content': prompt_create_player
        }],
        player_settings_func
    )

    player_character = PlayerCharacter(
        player['fight_style'],
        player['genre'],
        player['category'],
        player['attack_weapon']
    )
    game_settings = GameSettings(
        game['style'],
        game['plot'],
        player_character
    )

    return game_settings

import json
from dataclasses import asdict
from textwrap import dedent

from common.openai_calls import call_openai
from controle.game_settings import GameSettings
from criacao.function_calls import start_rpg_adventure


def start_adventure(game_settings: GameSettings):
    game_settings_json = json.dumps(asdict(game_settings), indent=4)
    prompt = dedent(f"""\
        f"Generate a full and detailed story new text based on the settings between <> bellow"
        <{game_settings_json}>\
        """)

    result = call_openai(
        messages=[{
            'role': 'system',
            'content': prompt,
        }],
        function_call=start_rpg_adventure,
    )

    return result

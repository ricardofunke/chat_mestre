import json
from dataclasses import asdict
from textwrap import dedent

from combate.function_calls import battle_plot_func, battle_result_func
from common.openai_calls import call_openai


def create_battle_scene(game_settings, current_situation):
    game_settings_json = json.dumps(asdict(game_settings), indent=4)
    prompt = dedent(f"""\
        Using the main goal of the game and based on its properties between <> bellow
        <{game_settings_json}>
        And also based on the current situation of the player described bellow between <>
        <{current_situation}>
        Start a battle scene for the user to chose between fight or flee.
        Do not finish the battle yet, just make the start of it.\
    """)

    exploration = call_openai(
        messages=[{'role': 'system', 'content': prompt}],
        function_call=battle_plot_func
    )

    return exploration


def run_battle_iteration(game_settings, current_situation, user_action, fight_outcome):
    game_settings_json = json.dumps(asdict(game_settings), indent=4)
    match user_action:
        case 'fight':
            match fight_outcome:
                case 'won':
                    prompt = dedent(f"""\
                        Using the main goal of the game and based on its properties between <> bellow
                        <{game_settings_json}>
                        And using the current situation of the game between <> bellow
                        <{current_situation}>
                        Create a text that tells the user won the battle.\
                    """)
                case 'lost':
                    prompt = dedent(f"""\
                        Using the main goal of the game and based on its properties between <> bellow
                        <{game_settings_json}>
                        And using the current situation of the game between <> bellow
                        <{current_situation}>
                        Create a text that tells the user lost the battle.\
                    """)
                case _:
                    prompt = dedent(f"""\
                        Using the main goal of the game and based on its properties between <> bellow
                        <{game_settings_json}>
                        And using the current situation of the game between <> bellow
                        <{current_situation}>
                        Create a text that tells the user did not won or lost but remains in the battle.\
                    """)
        case 'flee':
            prompt = dedent(f"""\
                Using the main goal of the game and based on its properties between <> bellow
                <{game_settings_json}>
                With the current situation of the game between <> bellow
                <{current_situation}>
                Create a text that tells the user fleeing from the battle.\
            """)
        case _:
            raise Exception(f"Battle option \"{user_action}\" not implemented.")

    next_iteration = call_openai(
        messages=[{'role': 'system', 'content': prompt}],
        function_call=battle_result_func
    )

    return next_iteration

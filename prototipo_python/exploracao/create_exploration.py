import json
from dataclasses import asdict
from textwrap import dedent

from common.openai_calls import call_openai
from controle.game_settings import GameSettings
from exploracao.function_calls import (exploration_plot_func, exploration_next_iteration_func, exploration_options_func,
                                       exploration_final_iteration_func, exploration_final_options_func,
                                       exploration_finale)


def create_exploration_scenery(game_settings: GameSettings):
    game_settings_json = json.dumps(asdict(game_settings), indent=4)
    prompt = dedent(f"""\
        With the main goal of the game in mind, create an the exploration scenery for the user based on the settings of the RPG game between <> bellow
        <{game_settings_json}>
        Still following the main goal of the game, create a short description of the first iteration of the player 
        in this exploration scenery you created and fill in the first_iteration parameter.
        This exploration plot and the first iteration must NOT include any battles or any items to collect, only paths and places.
        This exploration plot does not need to be peaceful, it can be dangerous and hard to pass through.\
    """)

    exploration = call_openai(
        messages=[{'role': 'system', 'content': prompt}],
        function_call=exploration_plot_func
    )

    return exploration


def generate_options(exploration_plot, previous_iteration):
    prompt = dedent(f"""\
        Generate 4 options for the user to choose for the exploration turn based on the user's previous iteration between <> bellow
        <{previous_iteration}>
        Keep the context of the exploration between <> bellow 
        <{exploration_plot}>
        None of these options should include leaving the exploration.\
    """)

    exploration_options = call_openai(
        messages=[{'role': 'system', 'content': prompt}],
        function_call=exploration_options_func
    )

    return exploration_options


def run_next_iteration(exploration_plot, previous_iteration):
    prompt = dedent(f"""\
        Using the context of the exploration plot between <> bellow
        <{exploration_plot}>
        And based on the user's previous iteration with this exploration plot described between <> bellow
        <{previous_iteration}>
        Create a text that tells the result of this previous interation and fill in the "next_iteration" parameter with it.\
    """)

    next_iteration = call_openai(
        messages=[{'role': 'system', 'content': prompt}],
        function_call=exploration_next_iteration_func
    )

    return next_iteration


def finish_exploration(exploration_plot, previous_iteration):
    prompt = dedent(f"""\
        Generate the final iteration for the exploration turn based on its plot between <> bellow
        <{exploration_plot}>
        And also based on the user's previous iteration between <> bellow
        <{previous_iteration}>\
    """)

    final_iteration = call_openai(
        messages=[{'role': 'system', 'content': prompt}],
        function_call=exploration_final_iteration_func
    )

    return final_iteration


def generate_final_options(exploration_plot, previous_iteration):
    prompt = dedent(f"""\
        Based on the the exploration plot between <> bellow
        <{exploration_plot}>
        And also based on the user's previous iteration between <> bellow
        <{previous_iteration}>
        Generate 4 final options for the user to choose one to end the exploration turn and leave the scene.
        Do not give options to continue the story, just options to give an end to it.\
    """)

    exploration_final_options = call_openai(
        messages=[{'role': 'system', 'content': prompt}],
        function_call=exploration_final_options_func
    )

    return exploration_final_options


def end_exploration(exploration_plot, previous_iteration):
    prompt = dedent(f"""\
            Give an end story to the exploration turn based on its plot between <> bellow
            <{exploration_plot}>
            And also based on the user's previous iteration between <> bellow
            <{previous_iteration}>\
        """)

    exploration_end_story = call_openai(
        messages=[{'role': 'system', 'content': prompt}],
        function_call=exploration_finale
    )

    return exploration_end_story

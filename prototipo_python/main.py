import json
import sys
from dataclasses import asdict
from time import sleep

from combate.battle_calculation import fight_outcome
from combate.create_battle import create_battle_scene, run_battle_iteration
from common.user_input import exploration_options, battle_options
from controle.set_the_game import get_game_settings
from criacao.create_story import start_adventure
from exploracao.create_exploration import create_exploration_scenery, run_next_iteration, generate_options, \
    finish_exploration, generate_final_options, end_exploration

if __name__ == '__main__':
    # the_style = "A classic medieval game with wizards, elves, dwarfs and so on"
    the_style = input("Describe the style of the game you want to play: ")
    # the_player = "A smart and agile archer with a very good eye"
    # the_player = "A strong and honorable knight"
    the_player = input("Describe your character for the game: ")

    settings = get_game_settings(the_style, the_player)
    print(json.dumps(asdict(settings), indent=4))
    print()
    print('---')
    print()

    sleep(3)

    story = start_adventure(settings)
    print(json.dumps(story, indent=4))
    print()
    print('---')
    print()

    sleep(3)

    exploration = create_exploration_scenery(settings)

    print(json.dumps(exploration, indent=4))
    print()
    print('---')
    print()

    sleep(3)

    expl_options = generate_options(settings, exploration['exploration_plot'], exploration['first_iteration'])

    print(json.dumps(expl_options, indent=4))
    print()
    print('---')
    print()

    sleep(3)

    expl_opt = exploration_options()
    if not expl_opt:
        sys.exit(0)

    next_iter = run_next_iteration(settings, exploration['exploration_plot'], expl_options[f'option_{expl_opt}'])

    print(f"Selected \"option_{expl_opt}\": \"{expl_options[f'option_{expl_opt}']}\"")
    print()

    print(json.dumps(next_iter, indent=4))
    print()
    print('---')
    print()

    sleep(3)

    n = 3
    for i in range(n):
        expl_options = generate_options(settings, exploration['exploration_plot'], next_iter['next_iteration'])

        print(json.dumps(expl_options, indent=4))
        print()
        print('---')
        print()

        sleep(3)

        expl_opt = exploration_options()
        if not expl_opt:
            sys.exit(0)

        next_iter = run_next_iteration(settings, exploration['exploration_plot'], expl_options[f'option_{expl_opt}'])

        print(f"Selected \"option_{expl_opt}\": \"{expl_options[f'option_{expl_opt}']}\"")
        print()

        print(json.dumps(next_iter, indent=4))
        print()
        print('---')
        print()

        sleep(3)

    expl_options = generate_options(settings, exploration['exploration_plot'], next_iter['next_iteration'])

    print(json.dumps(expl_options, indent=4))
    print()
    print('---')
    print()

    sleep(3)

    expl_opt = exploration_options()
    if not expl_opt:
        sys.exit(0)

    next_iter = run_next_iteration(settings, exploration['exploration_plot'], expl_options[f'option_{expl_opt}'])

    print(f"Selected \"option_{expl_opt}\": \"{expl_options[f'option_{expl_opt}']}\"")
    print()

    print(json.dumps(next_iter, indent=4))
    print()
    print('---')
    print()

    battle_scene = create_battle_scene(settings, next_iter['next_iteration'])

    print(json.dumps(battle_scene, indent=4))
    print()
    print('---')
    print()

    sleep(3)

    battle_opt = battle_options()
    if not battle_opt:
        sys.exit(0)

    if battle_opt == 'fight':
        fight_result = fight_outcome()
    else:
        fight_result = 'lost'

    battle_res = run_battle_iteration(settings, battle_scene['battle_plot'], battle_opt, fight_result)

    print()
    print(f"Selected \"{battle_opt}\"")
    print()

    print(json.dumps(battle_res, indent=4))
    print()
    print('---')
    print()

    sleep(3)

    while battle_res['battle_result'] == 'remain':
        battle_opt = battle_options()
        if not battle_opt:
            sys.exit(0)

        if battle_opt == 'fight':
            fight_result = fight_outcome()
        else:
            fight_result = 'lost'

        battle_res = run_battle_iteration(settings, battle_res['battle_result_description'], battle_opt, fight_result)

        print(f"Selected \"{battle_opt}\"")
        print()

        print(json.dumps(battle_res, indent=4))
        print()
        print('---')
        print()

        sleep(3)

    final_iter = finish_exploration(settings, exploration['exploration_plot'], battle_res['battle_result_description'])

    print(json.dumps(final_iter, indent=4))
    print()
    print('---')
    print()

    sleep(3)

    final_opts = generate_final_options(settings, exploration['exploration_plot'], final_iter['last_iteration'])

    print(json.dumps(final_opts, indent=4))
    print()
    print('---')
    print()

    sleep(3)

    expl_opt = exploration_options()
    if not expl_opt:
        sys.exit(0)

    ending = end_exploration(settings, exploration['exploration_plot'], final_opts[f'option_{expl_opt}'])

    print(f"Selected \"option_{expl_opt}\": \"{final_opts[f'option_{expl_opt}']}\"")
    print()

    print(json.dumps(ending, indent=4))
    print()
    print('---')
    print()

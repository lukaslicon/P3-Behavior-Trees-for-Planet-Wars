# bt_bot.py

import logging
import traceback
import sys
import os
import inspect

# Original log file for other messages
logging.basicConfig(filename=__file__[:-3] + '.log', filemode='w', level=logging.DEBUG)

# FileHandler for the 'treetostring.log' file
tree_log_file = __file__[:-3] + '_treetostring.log'
tree_log_handler = logging.FileHandler(tree_log_file)
tree_log_handler.setLevel(logging.INFO)

# Logger for tree-related logs
tree_logger = logging.getLogger('tree_logger')
tree_logger.addHandler(tree_log_handler)

currentdir = os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))
parentdir = os.path.dirname(currentdir)
sys.path.append(parentdir)

from behavior_tree_bot.behaviors import spread, attack, defend
from behavior_tree_bot.checks import if_neutral_planet_available, have_largest_fleet, if_enemy_planet_available
from behavior_tree_bot.bt_nodes import Selector, Sequence, Action, Check
from planet_wars import PlanetWars, finish_turn

def setup_behavior_tree():
    root = Selector(name='High Level Ordering of Strategies')
    # Use the tree_logger for logging the tree information
    tree_logger.info('\n' + root.tree_to_string())
    spread_sequence = Sequence(name='Spread Strategy')
    neutral_planet_check = Check(if_neutral_planet_available)
    spread_action = Action(spread)
    spread_sequence.child_nodes = [neutral_planet_check, spread_action]

    attack_sequence = Sequence(name='Attack Strategy')
    enemy_planet_check = Check(if_enemy_planet_available)
    attack_action = Action(attack)
    attack_sequence.child_nodes = [enemy_planet_check, attack_action]

    defend_sequence = Sequence(name='Defend Strategy')
    largest_fleet_check = Check(have_largest_fleet)
    defend_action = Action(defend)
    defend_sequence.child_nodes = [largest_fleet_check, defend_action]

    root.child_nodes = [defend_sequence, spread_sequence, spread_sequence, attack_sequence]
    return root

def do_turn(state):
    behavior_tree.execute(state)
    finish_turn()

if __name__ == '__main__':
    behavior_tree = setup_behavior_tree()
    try:
        map_data = ''
        while True:
            current_line = input()
            if len(current_line) >= 2 and current_line.startswith("go"):
                planet_wars = PlanetWars(map_data)
                do_turn(planet_wars)
                map_data = ''
            else:
                map_data += current_line + '\n'

    except KeyboardInterrupt:
        print('ctrl-c, leaving ...')
    except Exception:
        traceback.print_exc(file=sys.stdout)
        logging.exception("Error in bot.")


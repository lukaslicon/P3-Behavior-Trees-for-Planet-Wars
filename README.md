# P3-Behavior-Trees-for-Planet-WarsHere is a GitHub README for your Planet Wars bot project:

---

# Behavior Trees for Planet Wars

## Overview
This project involves implementing a bot that plays Planet Wars using Behavior Trees in Python. Planet Wars is a real-time strategy game where the objective is to conquer a galaxy, planet by planet. Each planet produces ships per turn, which can be used to take over other planets from the enemy or neutral forces.

## Project Structure
- `run.py`: Main entry point to run and test the bot.
- `behaviour_tree_bot/bt_bot.py`: Contains the main strategy for the bot.
- `behaviour_tree_bot/behaviors.py`: Contains functions for action nodes (e.g., issuing orders).
- `behaviour_tree_bot/checks.py`: Contains functions for state-based conditional checks.
- `behaviour_tree_bot/bt_nodes.py`: Contains node classes for building the behavior tree.
- `planet_wars.py`: Contains classes for planets, fleets, and the game state, as well as utility functions.

## How to Run
To run the game and test your bot interactively, execute the following command in the `/src` folder:
```sh
python run.py
```
This will open a window displaying the initial state of the match, where you can watch your bot play against predefined bots. The match can also be run without the graphical interface using the `test` function, which reports results in the console.

## Bot Implementation
### Behavior Tree
The behavior tree for the bot is defined in `bt_bot.py`. The example tree includes:
- **Selector**: High-level strategy selector.
  - **Sequence (Offensive Strategy)**: Attacks the weakest enemy planet if the bot has the largest fleet.
  - **Sequence (Spread Strategy)**: Spreads to the weakest neutral planet if available.
  - **Action**: Attacks the weakest enemy planet as a fallback.

### Node Types
- **Check**: Checks conditions without issuing orders.
- **Action**: Executes actions, typically issuing orders.
- **Selector**: Executes child nodes in order until one succeeds.
- **Sequence**: Executes child nodes in order until one fails.

### Custom Nodes
Optional: Implement additional behavior tree nodes like decorators (e.g., Inverter, LoopUntilFailed, AlwaysSucceed) or Random Selector.

## Requirements
- Submit a bot that wins against all five predefined bots.
- Ensure the bot operates within a 1-second per turn time constraint.
- Provide a text file showing the behavior tree using `print(root.tree_to_string())`.

## Tips
- Use the `do_nothing_bot` for testing without an active opponent.
- Utilize Python's `logging` module for debugging, as print statements are ineffective due to stdout communication with the Java game.

## References
- [Behavior Trees Overview](http://gamasutra.com/blogs/ChrisSimpson/20140717/221339/Behavior_trees_for_AI_How_they_work.php)
- [Decorators](http://aigamedev.com/open/article/decorator/)
- [Planet Wars Game Description](http://franz.com/services/conferences_seminars/webinar_1-20-11.gm.pdf)

## Submission Instructions
Submit a zip file named `Lastname1-Lastname2-P3.zip` containing:
- The `behavior_tree_bot` folder with all files.
- A text file with the output of `tree_to_string()`.

---

This README provides an overview of the project, instructions on how to run and implement the bot, and references for further information. Adjust the file paths and any specific details as needed.

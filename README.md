# Python Programs

A collection of Python learning examples and exercises organized as a 10-day sequence. The programs introduce core Python syntax and data structures, then apply those concepts in a modular calculator and a playable Snake game.

## Learning path

| Day | Program(s) | Concepts |
| --- | --- | --- |
| 1 | [`Day1.py`](./Day1.py) | First program, `print()`, variables, basic values, and displaying variable contents |
| 2 | [`Day2.py`](./Day2.py) | Python data types and mutability: mutable and immutable values, reassignment, and in-place changes |
| 3 | [`Day3.py`](./Day3.py) | Conditional logic with `if`, `elif`, `else`, nested conditions, Boolean operators, the conditional expression, and user input |
| 4 | [`Day4.py`](./Day4.py), [`Day4_Assignments.py`](./Day4_Assignments.py) | `for` loops, `range()`, iterating through collections, nested loops, `break`, `continue`, `enumerate()`, and dictionary iteration |
| 5 | [`Day5.py`](./Day5.py) | Lists, indexing and slicing, updating and removing elements, sorting, searching, copying, nested lists, and list comprehensions |
| 6 | [`Day6.py`](./Day6.py), [`Day6_Assignments.py`](./Day6_Assignments.py) | Dictionaries, key-value access and methods, iteration, nested dictionaries, comprehensions, and merging dictionaries |
| 7 | [`Day7.py`](./Day7.py), [`Day7_Assignments.py`](./Day7_Assignments.py) | Sets and frozensets, uniqueness, membership, set operations, comparisons, comprehensions, and immutability |
| 8 | [`Day8.py`](./Day8.py), [`Day8_Assignments.py`](./Day8_Assignments.py) | Functions, parameters, return values, defaults, keyword arguments, `*args`, `**kwargs`, lambda expressions, recursion, and a calculator exercise |
| 9 | [`Day9_Module/`](./Day9_Module/) | Creating and importing a module, calling functions through a module, and organizing calculator operations across files |
| 10 | [`Day10.py`](./Day10.py) | Applying Python fundamentals in a Pygame Snake game: functions, loops, conditions, lists, tuples, random food placement, keyboard events, collisions, scoring, and game state |

## Run a program

Install Python 3, open a terminal in this folder, and run the lesson you want:

```bash
python Day1.py
```

Replace `Day1.py` with another filename to run a different lesson. Some lessons prompt for input; follow the instructions shown in the terminal. To run the Day 9 module example, run it from this folder:

```bash
python Day9_Module/main.py
```

## Day 10: Snake Game

Day 10 is the interactive project in the series. Guide the snake to eat food and earn 10 points per item while avoiding the walls and the snake's body. The game ends on a collision or when there is no free cell left.

Install the additional Pygame dependency:

```bash
python -m pip install pygame
```

Run the game with:

```bash
python Day10.py
```

| Key | Action |
| --- | --- |
| Arrow keys or W/A/S/D | Move the snake |
| Space | Pause or resume |
| R | Restart after game over |
| Q | Quit |

The board uses a 30-by-25 grid of 20-pixel cells (600 by 500 pixels). The snake starts at a moderate speed and accelerates as the score increases.

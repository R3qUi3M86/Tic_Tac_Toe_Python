# Tic Tac Toe

## Story

In this project your job is to implement [Tic-Tac-Toe](https://en.wikipedia.org/wiki/Tic-tac-toe) for two players.
You also can try writing some AI to play the game. If you find it easy, try to make it unbeatable.

## What are you going to learn?

- variables
- functions
- loops and conditionals
- nested lists
- print formatting
- external modules
- user input handling
- error handling


## Tasks

1. Implement `init_board()` to return an empty 3-by-3 board, a list of lists filled with dots. The inner lists are rows.
    - A list of lists is returned that represents a list of rows.
    - Every cell of the returned value is `.`
    - The rows of the returned value are independent, changing one row does not affect the others.
    - Printing the result of the `init_board()` function shows the following in the terminal.
```
[ [ '.','.','.' ],[ '.','.','.' ],[ '.','.','.' ] ]
```

2. Implement `get_move()` that asks for user input and returns the coordinates of a valid move on board.
    - The accepts coordinates as a letter and a number: `A2` is first row and second column, `C1` is third row and first column, and so on.
    - The function returns a tuple of two integers (row, col).
    - The returned coordinates start from 0.
    - The integers indicate a valid (empty) position on the board.
    - The program keeps asking for coordinates if the coordinates provided are outside of board.
    - The program keeps asking for coordinates if the coordinates provided are taken.
    - The program keeps asking for coordinates if the coordinates provided do not match the format.

3. Implement `mark()` that writes the value of `player` (`X` or `0`) into the `row` & `col` element of `board`.
    - If the cell at `row` and `col` is empty (contains a dot `.`), it is marked with `player`.
    - Out-of-bounds coordinates are not interpreted as moves.
    - Coordinates of already occupied cells are not interpreted as moves.

4. Implement `has_won()` that returns `True` if `player` (`X` or `0`) has three of their marks in a horizontal, vertical, or diagonal row on `board`.
    - The `has_won()` function returns `True` if `player` has a three-in-a-row on `board`.
    - The `has_won()` function returns `False` if `player` does not have a three-in-a-row on `board`

5. Implement `is_full()` that returns `True` if the board is full.
    - The `is_full()` function returns `True` if there are no empty cells on the board.
    - The `is_full()` returns `False` if there are empty cells on the board.

6. Implement `print_board()` that prints the board to the screen.
    - Players are indicated with `X` and `0`. Empty fields are indicated with dots (`.`).
    - Coordinates are displayed around the board.
    - The board is displayed in the following format:
```
   1   2   3
A  . | . | .
  ---+---+---
B  . | . | .
  ---+---+---
C  . | . | .
```

7. Implement `print-result()` that displays the result of the game.
    - If player `X` wins, "X has won!" is printed.
    - If player `0` wins, "0 has won!" is printed.
    - If nobody wins, "It's a tie!" is printed.

8. Use the implemented functions to write a `tictactoe_game()` function that runs a whole 2-players game.
    - Player X starts the game.
    - Players alternate their moves (`X`, `0`, `X`, `0`...).
    - The board is displayed before each move, and at the end of game.
    - The game ends when someone wins or the board is full.
    - The game handles bad input (wrong coordinates) without crashing.

9. [OPTIONAL] Allow players to quit the game anytime by typing `quit`.
    - Typing `quit` instead of coordinates results in the program exiting.

10. Implement player-against-AI mode. The AI can drive one of the players, and the game is fully playable against the computer.
    - When `tictactoe_game()` is called with the argument `'HUMAN-AI'`, `get_ai_move()` is called instead of `get_move()` when it's Player `0` turn.
    - When `tictactoe_game()` is called with the argument `'AI-HUMAN'`, `get_ai_move()` is called instead of `get_move()` when it's Player `X` turn.
    - Function `get_ai_move()` returns a valid move (if possible) without asking for any input.
    - Function `get_ai_move()` returns `None` if the board is full.
    - Function `main_menu()` is implemented as a menu for between choosing 2-player mode and against-AI mode by pressing 1 or 2, respectively.

11. [OPTIONAL] AI is capable of recognizing the opportunity to win the game with one move.
    - Function `get_ai_move()` picks the winning move if there is one on the board.

12. [OPTIONAL] AI is capable of recognizing if its enemy could win the game with the next move, and (supposing there is no direct winning move) moves against it.
    - Function `get_ai_move()` (when there is no winning move in one step) picks a move which prevents a certain winning move for its enemy.
    - When there is a direct winning move, function `get_ai_move()` still picks that.
    - When there are multiple one-step options for the enemy, `get_ai_move()` tries to prevent one of them.

13. [OPTIONAL] AI is unbeatable in all cases.
    - There is no strategy or combination of steps that can win the game against the AI.

14. [OPTIONAL] AI can play against itself
    - When `tictactoe_game()` is called with the argument `'AI-AI'`, it calls `get_ai_move` for both players.
    - The game ends without any user input.
    - There is a one second delay between moves to make gameplay easier to follow.

## General requirements

None

## Hints

- You don't have to come up with an AI strategy. You can search the internet
  for strategy descriptions. Do not use external code; implement written instructions instead.
- You don't have to implement a general playing strategy. Tic-Tac-Toe has a rather
  easy unbeatable strategy that can be expressed as a sequence of conditionals.
- Ideal team size is 3. Maximum team size is 3.

## Background materials

- None

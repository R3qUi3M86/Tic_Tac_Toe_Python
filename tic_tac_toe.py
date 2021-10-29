import os
import random
import time
from enum import Enum
from copy import deepcopy

class Mode(Enum):
    HUMAN_HUMAN = 0
    AI_HUMAN = 1
    HUMAN_AI = 2
    AI_AI = 3

SINGLE_AI = 0
FIRST_AI = 1
SECOND_AI = 2

#OUTPUT LAYER
#Wipes console from previous prints
def clear_console():
    command = 'clear'
    if os.name in ('nt', 'dos'):  # If Machine is running on Windows, use cls
        command = 'cls'
    os.system(command)

#Intro screen
def intro():
    board = init_board()
    mark(board, 1, 0, 0)
    mark(board, 2, 1, 0)
    mark(board, 1, 0, 2)
    mark(board, 2, 0, 1)
    clear_console()
    print_board(board)
    print("\n")
    time.sleep(1)
    clear_console()
    mark(board, 1, 2, 2)
    print_board(board)
    print("\nTic!\n")
    time.sleep(1)
    clear_console()
    mark(board, 2, 1, 1)
    print_board(board)
    print("\nTic! Tac!\n")
    time.sleep(1)
    clear_console()
    mark(board, 1, 1, 2)
    print_board(board)
    print("\nTic! Tac! Toe!\n")
    time.sleep(1)
    input("Press Enter to continue...")


#Draws game board
def print_board(board):
    print("   1   2   3")
    print(f"A  {board[0][0]} | {board[0][1]} | {board[0][2]}")
    print("  ---+---+---")
    print(f"B  {board[1][0]} | {board[1][1]} | {board[1][2]}")
    print("  ---+---+---")
    print(f"C  {board[2][0]} | {board[2][1]} | {board[2][2]}\n")


#Prints who won the game
def print_result(winner):
    if winner == 1:
        print("X has won!\n")
    elif winner == 2:
        print("O has won!\n")
    else:
        print("It's a tie!\n")


#Leaves the game
def leave_game():
    print("\nGoodbye!\n")
    exit()



#INPUT LAYER
#Asks user to provide game input
def get_user_input(board):
    while True:
        clear_console()
        print_board(board)
        user_inp = input("What is your move?\n(example: C2)\n\n")
        
        if user_inp == "quit":
            leave_game()
        elif len(user_inp) == 2:
            return user_inp

#Checks if user wants to play again
def tryagain_promt(board, winner):
    while True:
        clear_console()
        print_board(board)
        print_result(winner)

        user_input = input("Would you like to play again?(y/n): ")
        
        if user_input.lower() == "y":
            main_menu()
        elif user_input.lower() == "n" or user_input.lower() == "quit":
            leave_game()
    
#Asks user to select game mode (VS HUMAN, VS AI or AI VS AI)
def select_game_mode_prompt():
    while True:
        clear_console()
        user_input = input("Please select game mode.\nvs HUMAN - 1\nvs AI - 2\nAI vs AI - 3\nYour answer (1,2 or 3): ")
        
        if user_input == "1":
            return Mode.HUMAN_HUMAN
        elif user_input == "2":
            return random.choice((Mode.AI_HUMAN, Mode.HUMAN_AI))
        elif user_input == "3":
            return Mode.AI_AI
        elif user_input == "quit":
            leave_game()

#Asks user to select difficulty for AI player
def select_difficulty_prompt(AI_Prompt):
    while True:
        clear_console()
        
        if AI_Prompt == SINGLE_AI:
            print("Please select AI difficulty.")
        elif AI_Prompt == FIRST_AI:
            print("Please select first AI difficulty.")
        elif AI_Prompt == SECOND_AI:
            print("Please select second AI difficulty.")
        
        user_input = input("Easy - 1\nMedium - 2\nHard - 3\nUnbeatable - U\nYour answer (1, 2, 3 or U): ")

        if user_input == "1":
            return 1
        elif user_input == "2":
            return 2
        elif user_input == "3":
            return 3
        elif user_input.lower() == "u":
            return 4
        elif user_input == "quit":
            leave_game()
        

#LOGIC LAYER
#Game board initialization
def init_board():
    board = [['.', '.', '.'],['.', '.', '.'],['.', '.', '.']]
    return board


#Gets player move as integer tuple
def get_move(board): 
    row, col = 0, 0
    rows = ["A","B","C"]
    valid_moves = get_valid_moves(board)

    while True:
        coordinates = list(get_user_input(board))
        if coordinates[0].upper() in ["A", "B", "C"] and coordinates[1].isnumeric() and int(coordinates[1]) > 0 and int(coordinates[1]) < 4:
            row = int(rows.index(coordinates[0].upper()))
            col = int(coordinates[1])-1
            if [row, col] in valid_moves:
                return row, col



#Marks place on board with X or O
def mark(board, player, row, col):
    if player == 1:
        board[row][col] = "X"
    else:
        board[row][col] = "O"



#Determines if win condition is met for either of players
def has_won(board, player):
    
    has_won = False
    #checks if any row is won by either player
    has_won = row_is_won(board, player)
    if has_won == True:
        return has_won

    #checks if any column is won by either player
    has_won = col_is_won(board, player)
    if has_won == True:
        return has_won

    #checks if any diagonal is won by either player
    if (board[0][0] == board[1][1] and board[1][1] == board[2][2]) or (board[0][2] == board[1][1] and board[1][1] == board[2][0]):
        
        if board[1][1] == "X" and player == 1:
            has_won = True
        elif board[1][1] == "O" and player == 2:
            has_won = True

    return has_won

#Checks if column is won by either player
def col_is_won(board, player):
    for y in range(3):
        Xs_count = 0
        Os_count = 0
        for x in range(3):
            if board[x][y] == "X":
                Xs_count += 1
            if board[x][y] == "O":
                Os_count += 1
        
        if Xs_count == 3 and player == 1:
            return True
        elif Os_count == 3 and player == 2:
            return True
    return False

#Checks if row is won by either player
def row_is_won(board, player):
    for x in range(3):
        Xs_count = 0
        Os_count = 0
        for y in range(3):
            if board[x][y] == "X":
                Xs_count += 1
            if board[x][y] == "O":
                Os_count += 1
        
        if Xs_count == 3 and player == 1:
            return True
        elif Os_count == 3 and player == 2:
            return True
    return False

#Checks if the board is fully occupied
def is_full(board):
    valid_moves = get_valid_moves(board)
    if len(valid_moves) == 0:
        return True
    else:
        return False


#Main game loop
def tictactoe_game(mode):
    board = init_board()
    move_number = 1
    difficulty1 = 0
    difficulty2 = 0
    
    if mode == Mode.AI_HUMAN or mode == Mode.HUMAN_AI:
        difficulty1 = select_difficulty_prompt(SINGLE_AI)
    elif mode == Mode.AI_AI:
        difficulty1 = select_difficulty_prompt(FIRST_AI)
        difficulty2 = select_difficulty_prompt(SECOND_AI)
        
    while is_full(board) == False:

        if mode == Mode.HUMAN_HUMAN:
            row, col = get_move(board)

        elif mode == Mode.HUMAN_AI:
            if move_number % 2 == 1:
                row, col = get_move(board)
            else:
                row, col = get_ai_move(board, 2, difficulty1)

        elif mode == Mode.AI_HUMAN:
            if move_number % 2 == 1:
                row, col = get_ai_move(board, 1, difficulty1)
            else:
                row, col = get_move(board)

        elif mode == Mode.AI_AI:
            if move_number % 2 == 1:
                row, col = get_ai_move(board, 1, difficulty1)
            else:
                row, col = get_ai_move(board, 2, difficulty2)

        mark(board, move_number % 2, row, col)
        move_number += 1
        if has_won(board, 1) or has_won(board, 2):
            break

    end_game(board)


#Finishes game
def end_game(board):
    if has_won(board, 1):
        winner = 1
    elif has_won(board, 2):
        winner = 2
    else:
        winner = 0

    tryagain_promt(board, winner)

#Determines game mode
def main_menu():
    tictactoe_game(select_game_mode_prompt())

#AI Logical block starts from here
#Gets move for AI player
def get_ai_move(board, player, difficulty):
    clear_console()
    print_board(board)
    print("Thinking...")
    time.sleep(1)

    #Easy AI intentionally avoids making wining move or preventing winning move from oponent
    if difficulty == 1:
        valid_moves = get_valid_moves(board)
        
        if winning_move(board, 1) != False:
            valid_moves.remove(winning_move(board, 1))

        if winning_move(board, 2) != False and winning_move(board, 2) in valid_moves:
            valid_moves.remove(winning_move(board, 2))
        
        if len(valid_moves) > 0:
            return random.choice(valid_moves)
        else:
            valid_moves = get_valid_moves(board)
            return random.choice(valid_moves)

    #Medium AI makes purely random move
    if difficulty == 2:
        valid_moves = get_valid_moves(board)
        return random.choice(valid_moves)

    #Hard and unbeatable AI goes for instant win if possible or prevents it from enemy 
    if player == 1:
            
        if winning_move(board, 1) != False:
            return winning_move(board, 1)
        elif winning_move(board, 2) != False:
            return winning_move(board, 2)

    elif player == 2:

        if winning_move(board, 2) != False:
            return winning_move(board, 2)
        elif winning_move(board, 1) != False:
            return winning_move(board, 1)

    #Hard AI makes purely random move from all remaining choices
    if difficulty == 3:
        valid_moves = get_valid_moves(board)
        return random.choice(valid_moves)

    #Unbeatable AI makes the best move possible
    if difficulty == 4:
        return make_strategic_move(board, player)
    

#Checks if given player can win in next move
def winning_move(board, player):
    valid_moves = get_valid_moves(board)

    for move in valid_moves:

        theoretical_board = make_mark_on_theoretical_board(board, move, player)

        if has_won(theoretical_board, player) == True:
            return move

    return False

#Returns theoretical board with appropriate marked sign
def make_mark_on_theoretical_board(board, move, player):
    theoretical_board = deepcopy(board)

    if player == 1:
        theoretical_board[move[0]][move[1]] = 'X'
    else:
        theoretical_board[move[0]][move[1]] = 'O'

    return theoretical_board

#Returns list of valid moves for AI player
def get_valid_moves(board):
    valid_moves = []
    i = 0

    for row in board:
        j = 0

        for position in row:
            if position == ".":
                valid_moves.append([i, j])
            j += 1

        i += 1

    return valid_moves

#Returns best strategic move if there is no instant win for either player
def make_strategic_move(board, player):
    enemy_player = (player % 2) + 1 #determines which player is the enemy (make helper)
    valid_moves = get_valid_moves(board)
    valid_moves_potential = [0] * len(valid_moves)

    for move in valid_moves:
        valid_moves_potential[valid_moves.index(move)] = score_field_potential(board, move, player, enemy_player)

    return get_best_move(valid_moves, valid_moves_potential)

#Returns best move based on available moves and their winning potential
def get_best_move(valid_moves, valid_moves_potential):
    max_potential = 0

    for move in valid_moves:
        if max_potential < valid_moves_potential[valid_moves.index(move)]:
            max_potential = valid_moves_potential[valid_moves.index(move)]

    return valid_moves[valid_moves_potential.index(max_potential)]

#Scores given field on the board based on its possible winning potential
def score_field_potential(board, move, player, enemy_player):
    move_score = 0
    
    #Checks if move will lead to current player forking his oponent
    if move_leads_to_fork(board, move, player) == True:
        move_score += 200

    #Checks if move will allow enemy player forking current player    
    if move_leads_to_fork(board, move, enemy_player) == True:
        move_score += 50

    #Checks if move will force specific move onto oponent without forcing unwanted fork
    if forcing_move(board, move, player) == True:
        theoretical_board = make_mark_on_theoretical_board(board, move, player)
        counter_move = winning_move(theoretical_board, player)

        if move_leads_to_fork(theoretical_board, counter_move, enemy_player) == False:
            move_score += 100

    #Makes center more valuable over other fields
    if move == [1, 1]:
        move_score += 20

    #Makes corners more valuable over sides
    elif move == [0, 0] or move == [0, 2] or move == [2, 0] or move == [2, 2]:
        move_score += 10
    
    #Adds randomnes to fields potential to make AI pick random field if potentials are equal
    move_score += random.choice(range(9))
    return move_score

#Determines if move will lead to forced response from enemy (immediate threat of winning)
def forcing_move(board, move, player):
    theoretical_board = make_mark_on_theoretical_board(board, move, player)

    if winning_move(theoretical_board, player) != False:
        return True
    else:
        return False

#Determines if given move will lead to a fork by given player
def move_leads_to_fork(board, move, player):
    theoretical_board = make_mark_on_theoretical_board(board, move, player)
    next_winning_move = 0, 0

    if winning_move(theoretical_board, player) != False:
        next_winning_move = winning_move(theoretical_board, player)
        theoretical_board[next_winning_move[0]][next_winning_move[1]] = "$"
        
        if winning_move(theoretical_board, player) != False:
            return True
        else:
            return False

    else:
        return False

#AI Logical block ends here

if __name__ == '__main__':
    intro()
    main_menu()
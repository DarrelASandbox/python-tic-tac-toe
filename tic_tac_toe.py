import os
import random


def display_board(board):

    os.system("clear")
    print(" " + board[7] + " | " + board[8] + " | " + board[9])
    print(" " + board[4] + " | " + board[5] + " | " + board[6])
    print(" " + board[1] + " | " + board[2] + " | " + board[3])


def player_input():
    marker = ""

    while marker != "X" and marker != "O":
        marker = input("Player1: Choose X or O: ").upper()
        if marker.upper() == "X":
            return ("X", "O")
        else:
            return ("O", "X")


def place_marker(board, marker, position):
    board[position] = marker


def win_check(board, marker):
    return (
        (board[1] == board[2] == board[3] == marker)  # 3 rows
        or (board[4] == board[5] == board[6] == marker)
        or (board[7] == board[8] == board[9] == marker)
        or (board[1] == board[5] == board[9] == marker)  # 2 diagonals
        or (board[3] == board[5] == board[7] == marker)
    )


def choose_first():
    if random.randint(0, 1) == 0:
        return "Player 2"
    else:
        return "Player 1"


def position_check(board, position):
    return board[position] == " "


def full_board_check(board):
    for i in range(0, 10):
        if position_check(board, i):
            return False
    return True


def player_choice(board):
    position = 0
    while position not in range(len(board)) or not position_check(board, position):
        position = int(input("Pick a position: (1-9) "))
    return position


def replay():
    response = input("Play again? Enter Y")
    return response.upper() == "Y"


print("Tic Tac Toe!")

while True:
    board = [" "] * 10
    player1_marker, player2_marker = player_input()

    turn = choose_first()
    print(turn + "goes first!")

    game_on = True
    while game_on:
        if turn == "Player 1":
            display_board(board)
            position = player_choice(board)
            place_marker(board, player1_marker, position)
            if win_check(board, player1_marker):
                display_board(board)
                print("Player 2 is a loser!")
                game_on = False
            else:
                if full_board_check(board):
                    display_board(board)
                    print("We have 2 losers! SAD!")
                    game_on = False
                else:
                    turn = "Player 2"

        else:
            display_board(board)
            position = player_choice(board)
            place_marker(board, player2_marker, position)
            if win_check(board, player2_marker):
                display_board(board)
                print("Player 1 is a loser!")
                game_on = False
            else:
                if full_board_check(board):
                    display_board(board)
                    print("We have 2 losers! SAD!")
                    game_on = False
                else:
                    turn = "Player 1"

    if not replay():
        break


from os import system
from copy import deepcopy


def create_board():
    board = []
    for row in range(10):
        row = []
        for _ in range(10):
            row.append(" ")
        board.append(row)
    return board


def print_board(board):
    system('clear')
    temp_board = deep_board(board)
    col_letters = 'abcdefghij'
    for i in range(len(temp_board)):
        for j in range(len(temp_board[i])):
            if temp_board[i][j] == 'Y':
                temp_board[i][j] = ' '

    print('   | ' + ' | '.join(col_letters.upper()) + ' |')
    print("-" * 44)
    for number, row in enumerate(temp_board):
        print(number + 1, ' | ' + ' | '.join(row) + ' |')
        print("-" * 44)

    print('   | ' + ' | '.join(col_letters.upper()) + ' |')
    print("-" * 44)
    for number, row in enumerate(board):
        print(number + 1, ' | ' + ' | '.join(row) + ' |')
        print("-" * 44)


def deep_board(board):
    new_board = deepcopy(board)
    return new_board


col = {"A": 0, "B": 1, "C": 2, "D": 3, "E": 4, "F": 5, "G": 6, "H": 7, "I": 8, "J": 9}
row = {"1": 0, "2": 1, "3": 2, "4": 3, "5": 4, "6": 5, "7": 6, "8": 7, "9": 8, "10": 9}


def hit_ship(board, ship_vertical):
    ship_lengh = []
    for row in ship_vertical[1]:
        for col in ship_vertical[1]:
            if board[row][col] == "$":
                ship_lengh.append("$")
                print(ship_lengh)
    if len(ship_lengh) == 3:
        return True


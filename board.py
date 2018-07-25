#from os import system
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
    #system('clear')
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


def hit_ship(board, ship, parts, direction=None):
    if direction == "ver":
        ship_length = []
        for row in ship[0]:
            if board[row][ship[1][0]] == "$":
                ship_length.append("$")
                # print(ship_length)
        if len(ship_length) == parts:
            return True
    elif direction == "hor":
        ship_length = []
        for col in ship[1]:
            if board[ship[0][0]][col] == "$":
                ship_length.append("$")
                # print(ship_length)
        if len(ship_length) == parts:
            return True
    

def all_fleet_hit(board, parts):
    hits = []
    for i in range(len(board)):
        for j in range(len(board[i])):
            if board[i][j] == "$":
                hits.append("$")
    if len(hits) == parts:
        return True

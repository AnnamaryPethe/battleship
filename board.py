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


def hit_ship_ver(board):
    for row in range(len(board)):
        for col in range(len(board[row])):
            if board[row][col] == '$' and board[row][col + 1] == '$' and board[row][col + 2] == '$':
                return True
    return False

    # ship_lengh = []
    # for row in ship_vertical[1]:
    #     for col in ship_vertical[1]:
    #         if board[row][col] == "$":
    #             ship_lengh.append("$")
    #             print(ship_lengh)
    #             print("This is a boat")
    # if len(ship_lengh) == 3:
    #     return True


def hit_ship_hor(board):
    for row in range(len(board)):
        for col in range(len(board[row])):
            if board[row][col] == '$' and board[row + 1][col] == '$' and board[row + 2][col] == '$':
                return True
    return False


    # ship_lengh = []
    # for row in ship_horizontal[0]:
    #     for col in ship_horizontal[0]:
    #         if board[row][col] == "$":
    #             ship_lengh.append("$")
    #             print(ship_lengh)
    #             print("This is a boat")
    # if len(ship_lengh) == 3:
    #     return True
    # return False


def all_fleet_hit(board):
    if hit_ship_ver(board) and hit_ship_hor(board):
        return True
    return False

    # hit = []
    # for row in range(len(board)):
    #     for col in range(len(board[row])):
    #         if board[row][col] == "$":
    #             hit.append("$")
    # if len(hit) == 6:
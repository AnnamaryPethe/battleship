#from os import system
from copy import deepcopy

col = {"A": 0, "B": 1, "C": 2, "D": 3, "E": 4, "F": 5, "G": 6, "H": 7, "I": 8, "J": 9}
row = {"1": 0, "2": 1, "3": 2, "4": 3, "5": 4, "6": 5, "7": 6, "8": 7, "9": 8, "10": 9}


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


def hit_ship_ver(board, ship_vertical):
    ship_length = []
    for row in ship_vertical[0]:
        if board[row][ship_vertical[1][0]] == "$":
            ship_length.append("$")
            print(ship_length)
    if len(ship_length) == 3:
        return True
    

def hit_ship_hor(board, ship_horizontal):
    ship_length = []
    for col in ship_horizontal[1]:
        if board[ship_horizontal[0][0]][col] == "$":
            ship_length.append("$")
            print(ship_length)
    if len(ship_length) == 3:
        return True


def all_fleet_hit(board):
    hits =[]
    for i in range(len(board)):
        for j in range(len(board[i])):
            if board[i][j] == "$":
                hits.append("$")
    if len(hits) == 6:
        print("Game over")
            
            

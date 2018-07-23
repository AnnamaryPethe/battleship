from random import randint


def gen_random_ship(board, pieces):
    for _ in range(pieces):
        ship1_row = randint(1, len(board) - 1)
        ship1_col = randint(1, len(board[0]) - 1)
        board[ship1_col][ship1_row] = "Y"


        #ship1_row = ship1_row
        #ship1_col = ship1_col + 1
        #board[ship1_col][ship1_row] = " "
        #ship1_row = ship1_row
        #ship1_col = ship1_col + 1
        #board[ship1_col][ship1_row] = " "


def gen_random_ship2(board, pieces):
    for _ in range(pieces):
        ship1_row = randint(1, len(board) - 1)
        ship1_col = randint(1, len(board[0]) - 1)
        board[ship1_col][ship1_row] = "Y"


        #ship1_row = ship1_row + 1
        #ship1_col = ship1_col
        #board[ship1_col][ship1_row] = " "
        #ship1_row = ship1_row + 1
        #ship1_col = ship1_col
        #board[ship1_col][ship1_row] = " "





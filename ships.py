from random import randint


def gen_random_ship_vertical(board, pieces, parts):
    for _ in range(pieces):
        ship1_row = randint(1, len(board) - 3)
        ship1_col = randint(1, len(board[0]) - 3)
        for i in range(parts):
            if board[ship1_row][ship1_col] != "Y":
                board[ship1_row][ship1_col] = "Y"
            else:
                gen_random_ship_vertical(board, pieces, parts)
            ship1_row += 1

        #ship2_row = ship1_row
        #ship2_col = ship1_col + 1
        #board[ship2_row][ship2_col] = "Y"

        #ship3_row = ship2_row
        #ship3_col = ship2_col + 1
        #board[ship3_row][ship3_col] = "Y"


def gen_random_ship_horizontal(board, pieces, parts):
    for _ in range(pieces):
        ship1_row = randint(1, len(board) - 3)
        ship1_col = randint(1, len(board[0]) - 3)
        for i in range(parts):
            if board[ship1_row][ship1_col] != "Y":
                board[ship1_row][ship1_col] = "Y"
            else:
                gen_random_ship_horizontal(board, pieces, parts)
            ship1_col += 1
        
        
        #ship2_row = ship1_row + 1
        #ship2_col = ship1_col
        #board[ship2_row][ship2_col] = "Y"

        #ship3_row = ship2_row + 1
        #ship3_col = ship2_col
        #board[ship3_row][ship3_col] = "Y"

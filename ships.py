from random import randint


def gen_random_ship_horizontal(board, pieces):
    ship_row = []
    ship_col = []
    for _ in range(pieces):

        ship1_row = randint(1, len(board) - 3)
        ship1_col = randint(1, len(board[0]) - 3)
        if board[ship1_row][ship1_col] != "Y":
            ship_row.append(ship1_row)
            ship_col.append(ship1_col)
            board[ship1_row][ship1_col] = "Y"
        else:
            gen_random_ship_vertical(board, pieces)

        ship2_row = ship1_row
        ship2_col = ship1_col + 1
        ship_row.append(ship2_row)
        ship_col.append(ship2_col)
        board[ship2_row][ship2_col] = "Y"

        ship3_row = ship2_row
        ship3_col = ship2_col + 1
        ship_row.append(ship3_row)
        ship_col.append(ship3_col)
        board[ship3_row][ship3_col] = "Y"

    #print(ship_col)
    #print(ship_row)

    return [ship_row, ship_col]


def gen_random_ship_vertical(board, pieces):
    ship_row = []
    ship_col = []
    for _ in range(pieces):

        ship1_row = randint(1, len(board) - 3)
        ship1_col = randint(1, len(board[0]) - 3)
        if board[ship1_row][ship1_col] != "Y":
            ship_row.append(ship1_row)
            ship_col.append(ship1_col)
            board[ship1_row][ship1_col] = "Y"
        else:
            gen_random_ship_vertical(board, pieces)

        ship2_row = ship1_row + 1
        ship2_col = ship1_col
        ship_row.append(ship2_row)
        ship_col.append(ship2_col)
        board[ship2_row][ship2_col] = "Y"

        ship3_row = ship2_row + 1
        ship3_col = ship2_col
        ship_row.append(ship3_row)
        ship_col.append(ship3_col)
        board[ship3_row][ship3_col] = "Y"

    #print(ship_col)
    #print(ship_row)

    return [ship_row, ship_col]



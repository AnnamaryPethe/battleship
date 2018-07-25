from random import randint


def gen_random_ship(board, pieces, parts, direction=None):
    ship_row = []
    ship_col = []
    for _ in range(pieces):
        ship1_row = randint(0, len(board) - (parts + 1))
        ship1_col = randint(0, len(board) - (parts + 1))
        
        if board[ship1_row][ship1_col] != "Y" and board[ship1_row + (parts - 1)][ship1_col] != "Y":
            board[ship1_row][ship1_col] = "Y"
        elif board[ship1_row][ship1_col] != "Y" and board[ship1_row - (parts - 1)][ship1_col] != "Y":
            board[ship1_row][ship1_col] = "Y"
        elif board[ship1_row][ship1_col] != "Y" and board[ship1_row][ship1_col + (parts - 1)] != "Y":
            board[ship1_row][ship1_col] = "Y"
        elif board[ship1_row][ship1_col] != "Y" and board[ship1_row][ship1_col - (parts - 1)] != "Y":
            board[ship1_row][ship1_col] = "Y"
        else:
            ship1_row = randint(0, len(board) - (parts + 1))
            ship1_col = randint(0, len(board) - (parts + 1))
        
        ship_row.append(ship1_row)
        ship_col.append(ship1_col)

        for i in range(parts - 1):
            if direction == "ver":
                ship_col.append(ship1_col)
                ship1_row += 1
                ship_row.append(ship1_row)
                board[ship1_row][ship1_col] = "Y"
            elif direction == "hor":
                ship_row.append(ship1_row) 
                ship1_col += 1
                ship_col.append(ship1_col)
                board[ship1_row][ship1_col] = "Y"
    return [ship_row, ship_col]           


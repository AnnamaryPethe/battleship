from random import randint



def gen_random_ship_vertical(board, pieces):
    ship_row = []
    ship_col = []
    for _ in range(pieces):
        ship1_row = randint(1, len(board) - 3)
        ship1_col = randint(1, len(board[0]) - 3)
        if board[ship1_col][ship1_row] != "Y":
            ship_row.append(ship1_row)
            ship_col.append(ship1_col)
            board[ship1_col][ship1_row] = "Y"
        else:
            gen_random_ship_vertical(board, pieces)

        ship_row.append(ship1_row)
        ship_col.append(ship1_col)
        board[ship1_col][ship1_row] = "Y"

        ship2_row = ship1_row
        ship2_col = ship1_col + 1
        ship_row.append(ship2_row)
        ship_col.append(ship2_col)
        board[ship2_col][ship2_row] = "Y"

        ship3_row = ship2_row
        ship3_col = ship2_col + 1
        ship_row.append(ship3_row)
        ship_col.append(ship3_col)
        board[ship3_col][ship3_row] = "Y"
    
    #with open(filename, "w") as f:
        #file = csv.writer(f)
        #file.writerow(ship_row)
        #file.writerow(ship_col)
        
    print(ship_row)
    print(ship_col)

    return [ship_row, ship_col]

def gen_random_ship_horizontal(board, pieces):
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





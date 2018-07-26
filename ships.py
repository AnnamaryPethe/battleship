from random import randint


def gen_random_ship(board, parts, direction=None):
    ship_row = []
    ship_col = []
    gen_ship = True

    while gen_ship:
        ship1_row = randint(0, len(board) - (parts + 1))
        ship1_col = randint(0, len(board) - (parts + 1))
     
        if direction == "ver":
            if board[ship1_row][ship1_col] != "Y" \
                and board[ship1_row + (parts - 1)][ship1_col] != "Y" \
                and board[ship1_row + parts][ship1_col] != "Y" \
                and board[ship1_row - 1][ship1_col] != "Y" \
                and board[ship1_row][ship1_col - 1] != "Y" \
                and board[ship1_row][ship1_col + 1] != "Y":
                    board[ship1_row][ship1_col] = "Y"
                    ship_row.append(ship1_row)
                    ship_col.append(ship1_col)
                    for i in range(parts - 1):
                        ship_col.append(ship1_col)
                        ship1_row += 1
                        ship_row.append(ship1_row)
                        board[ship1_row][ship1_col] = "Y"
                    gen_ship = False    
            else:
                gen_ship = True 

        elif direction == "hor":
            if board[ship1_row][ship1_col] != "Y" \
                and board[ship1_row][ship1_col + (parts - 1)] != "Y" \
                and board[ship1_row][ship1_col + parts] != "Y" \
                and board[ship1_row][ship1_col - 1] != "Y" \
                and board[ship1_row - 1][ship1_col] != "Y" \
                and board[ship1_row + 1][ship1_col] != "Y":
                    board[ship1_row][ship1_col] = "Y"
                    ship_row.append(ship1_row)
                    ship_col.append(ship1_col)
                    for i in range(parts - 1):
                        ship_row.append(ship1_row) 
                        ship1_col += 1
                        ship_col.append(ship1_col)
                        board[ship1_row][ship1_col] = "Y"
                    gen_ship = False
            else:
                gen_ship = True 
                
    return [ship_row, ship_col]           




def validate(guess_row, guess_col, board):
    hit_row_list = []
    hit_col_list = []
    if board[guess_row][guess_col] == "Y":
        board[guess_row][guess_col] = "$"
<<<<<<< HEAD
        hit_row_list.append(guess_row)
        hit_col_list.append(guess_col)
    elif board[guess_col][guess_row] == " ":
        return True
    elif board[guess_col][guess_row] == "$":
        return False
    elif board[guess_col][guess_row] == "X":
        return False
    
    
=======
    elif board[guess_row][guess_col] == " ":
        return True
    elif board[guess_row][guess_col] == '$':
        return False
    elif board[guess_row][guess_col] == "X":
        return False

>>>>>>> ecc11329b8da88d4953bc6df5253df1b4e294da5

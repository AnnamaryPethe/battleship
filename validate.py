

def validate(guess_row, guess_col, board):
    hit_row_list = []
    hit_col_list = []
    if board[guess_row][guess_col] == "Y":
        board[guess_row][guess_col] = "$"
        hit_row_list.append(guess_row)
        hit_col_list.append(guess_col)
    elif board[guess_col][guess_row] == " ":
        return True
    elif board[guess_col][guess_row] == "$":
        return False
    elif board[guess_col][guess_row] == "X":
        return False
    
    
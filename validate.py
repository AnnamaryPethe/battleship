def validate(guess_row, guess_col, board):
    if board[guess_row][guess_col] == "Y":
        board[guess_row][guess_col] = "$"
    elif board[guess_col][guess_row] == " ":
        return True
    elif board[guess_col][guess_row] == "X":
        return False

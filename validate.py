

def validate(guess_row, guess_col, board):
    if board[guess_row][guess_col] == "Y":
        board[guess_row][guess_col] = "$"
        return True
    elif board[guess_row][guess_col] == " ":
        board[guess_row][guess_col] = "🤔"
        return True
    elif board[guess_row][guess_col] == '$':
        return False
    elif board[guess_row][guess_col] == "🤔":
        return False


from board import row, col
from validate import validate


def player(board, name):
    print(name)
    guessRow = row[input("What row do you guess? \n")]
    guessCol = col[input("What column do you guess? \n")]
    if validate(guessRow, guessCol, board):
        board[guessRow][guessCol] = "X"
    else:
        print("Wrong")      
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


# def player1(board1, name):
#     print(name)
#     guessRow = row[input("What row do you guess? \n")]
#     guessCol = col[input("What column do you guess? \n")]
#     if validate(guessRow, guessCol, board1):
#         board1[guessRow][guessCol] = "X"
#     else:
#         print("Wrong")
#
#
# def player2(board2, name):
#     print(name)
#     guessRow = row[input("What row do you guess? \n")]
#     guessCol = col[input("What column do you guess? \n")]
#     if validate(guessRow, guessCol, board2):
#         board2[guessRow][guessCol] = "X"
#     else:
#         print("Wrong")


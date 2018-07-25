from validate import validate


def player(board, name):
    print(name)
    col = {"A": 0, "B": 1, "C": 2, "D": 3, "E": 4, "F": 5, "G": 6, "H": 7, "I": 8, "J": 9}
    row = {"1": 0, "2": 1, "3": 2, "4": 3, "5": 4, "6": 5, "7": 6, "8": 7, "9": 8, "10": 9}
    guess_row = row[input("What row do you guess? \n")]
    guess_col = col[input("What column do you guess? \n")]
    if not validate(guess_row, guess_col, board):
        print("Wrong")


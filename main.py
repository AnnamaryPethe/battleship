from board import print_board, create_board
from ships import gen_random_ship, gen_random_ship2
from players import player2, player1


board1 = create_board()
board2 = create_board()
gen_random_ship(board1, 1)
gen_random_ship2(board1, 1)
gen_random_ship(board2, 1)
gen_random_ship2(board2, 1)


player1_name = input('First players name: ')
player2_name = input('Second players name: ')

#print_board(board1)

while True:
    print("\033[1;34;40m Bright Blue \n")
    player1(board1, player1_name)
    print_board(board1)
    print("\033[0;32;47m Green \n")
    player2(board2, player2_name)
    print_board(board2)


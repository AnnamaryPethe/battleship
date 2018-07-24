from board import print_board, create_board, hit_ship
from ships import gen_random_ship_vertical, gen_random_ship_horizontal
from players import player


board1 = create_board()
board2 = create_board()

player1_name = input('First players name: ')
player2_name = input('Second players name: ')

<<<<<<< HEAD
#player1 = player(board1, player1_name)
#player2 = player(board2, player2_name)


ship1_coordinate = gen_random_ship_vertical(board1, 1)
gen_random_ship_horizontal(board1, 1)
gen_random_ship_vertical(board2, 1)
gen_random_ship_horizontal(board2, 1)

while True:
    print("\033[1;34;40m \n")
    print_board(board1)
    player(board1, player1_name)
    if hit_ship(board1, ship1_coordinate):
        print("Ennyi.")
    print("\033[0;32;47m \n")
    print_board(board2)
    player(board2, player2_name)


=======

gen_random_ship_horizontal(board1, 1)
ship1_coordinate = gen_random_ship_vertical(board1, 1)
#ship2_coordinate = gen_random_ship_vertical(board2, 1)
gen_random_ship_horizontal(board2, 1)
gen_random_ship_vertical(board2, 1)

print(ship1_coordinate)
#print(ship2_coordinate)

print_board(board1)

while True:
    print("\033[1;34;40m \n")
    player(board1, player1_name)
    print_board(board1)
    if hit_ship(board1, ship1_coordinate):
        print("Yuhuu")
    # print("\033[0;32;47m \n")
    # player(board2, player2_name)
    # print_board(board2)
    # if hit_ship(board2, ship2_coordinate):
    #     print("Yuhuu")
>>>>>>> ecc11329b8da88d4953bc6df5253df1b4e294da5



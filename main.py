from board import print_board, create_board, hit_ship_ver, hit_ship_hor, all_fleet_hit
from ships import gen_random_ship_vertical, gen_random_ship_horizontal
from players import player


board1 = create_board()
board2 = create_board()

player1_name = input('First players name: ')
player2_name = input('Second players name: ')

#Vertical and horizontal ships for board1
ship1_coordinate_hor = gen_random_ship_horizontal(board1, 1)
ship1_coordinate_ver = gen_random_ship_vertical(board1, 1)

#Vertical and horizontal ships for board2
ship2_coordinate_hor = gen_random_ship_horizontal(board2, 1)
ship2_coordinate_ver = gen_random_ship_vertical(board2, 1)

#Print coordinates for easier testing
print("Vertical ship on board1: ", ship1_coordinate_ver)
print("Horizontal ship on board1: ", ship1_coordinate_hor)
print("Vertical ship on board2: ", ship2_coordinate_ver)
print("Horizontal ship on board2: ", ship2_coordinate_hor)

print_board(board1)

while True:
    print("\033[1;34;40m \n")
    player(board1, player1_name)
    print_board(board1)
    if hit_ship_ver(board1, ship1_coordinate_ver):
        print("Yuhuu")
    if hit_ship_hor(board1, ship1_coordinate_hor):
        print("Yuhuu")
    all_fleet_hit(board1)

    print("\033[0;32;47m \n")
    player(board2, player2_name)
    print_board(board2)
    if hit_ship_ver(board2, ship2_coordinate_ver):
        print("Yuhuu")
    if hit_ship_hor(board2, ship2_coordinate_hor):
        print("Yuhuu")
    all_fleet_hit(board2)



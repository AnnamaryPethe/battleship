from board import print_board, create_board, hit_ship, hit_ship
from ships import gen_random_ship
from players import player


def main():
    board1 = create_board()
    board2 = create_board()

    player1_name = input('First players name: ')
    player2_name = input('Second players name: ')

    ship1_ver1 = gen_random_ship(board1, 1, 4, "ver")
    ship1_hor1 = gen_random_ship(board1, 1, 2, "hor")
    ship2_ver1 = gen_random_ship(board2, 1, 3, "ver")
    ship2_hor1 = gen_random_ship(board2, 1, 3, "hor")


    while True:
        print("\033[1;34;40m \n")
        print(ship1_ver1)
        print(ship1_hor1)
        print(ship2_ver1)
        print(ship2_hor1)
        print_board(board1)
        player(board1, player1_name)
        print_board(board1)
        if hit_ship(board1, ship1_ver1, 4, "ver") or hit_ship(board1, ship1_hor1, 2, "hor"):
            print("It was a boat")

        '''if all_fleet_hit(board1):
            answer = input("{} WIN. Game over \n New game? Y/N".format(player1_name))
            if answer == "Y":
                main()
            else:
                exit()'''

        '''print("\033[0;32;47m \n")
        print_board(board2)
        player(board2, player2_name)
        print_board(board2)
        if hit_ship(board2, ship2_ver1, 3, "ver") or hit_ship(board2, ship2_hor1, 3, "hor"):
            print("It was a boat")'''





        '''if all_fleet_hit(board2):
            answer2 = input("{} WIN. Game over \n New game? Y/N".format(player2_name))
            if answer2 == "Y":
                main()
            else:
                exit()'''


main()

from board import print_board, create_board, hit_ship_hor, hit_ship_ver, all_fleet_hit
from ships import gen_random_ship_vertical, gen_random_ship_horizontal
from players import player


def main():
    board1 = create_board()
    board2 = create_board()

    player1_name = input('First players name: ')
    player2_name = input('Second players name: ')

    gen_random_ship_vertical(board1, 1)
    gen_random_ship_horizontal(board1, 1)
    gen_random_ship_horizontal(board2, 1)
    gen_random_ship_vertical(board2, 1)

    while True:
        print("\033[1;34;40m \n")
        print_board(board1)
        player(board1, player1_name)
        print_board(board1)
        if hit_ship_ver(board1) or hit_ship_hor(board1):
            print("It was a ship!")
        if all_fleet_hit(board1):
            answer = input("{} WIN. Game over \n New game? Y/N".format(player1_name))
            if answer == "Y":
                main()
            else:
                exit()

        print("\033[0;32;47m \n")
        print_board(board2)
        player(board2, player2_name)
        print_board(board2)
        if hit_ship_ver(board2) or hit_ship_hor(board2):
            print("It was a boat")
        if all_fleet_hit(board2):
            answer2 = input("{} WIN. Game over \n New game? Y/N".format(player2_name))
            if answer2 == "Y":
                main()
            else:
                exit()


main()

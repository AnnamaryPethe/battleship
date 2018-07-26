from board import print_board, create_board, hit_ship, hit_ship, all_fleet_hit
from ships import gen_random_ship
from players import player


def main():
    # creating boards for player1 and player2
    board1 = create_board()
    board2 = create_board()
    
    # input players' name
    player1_name = input('First players name: ')
    player2_name = input('Second players name: ')
    
    # creating ships on player1's board
    ship1_ver1 = gen_random_ship(board1, 4, "ver")
    ship1_ver2 = gen_random_ship(board1, 3, "ver")
    ship1_hor1 = gen_random_ship(board1, 2, "hor")
    ship1_hor2 = gen_random_ship(board1, 3, "hor")

    # creating ships on player2's board
    ship2_ver1 = gen_random_ship(board2, 4, "ver")
    ship2_ver2 = gen_random_ship(board2, 3, "ver")
    ship2_hor1 = gen_random_ship(board2, 3, "hor")
    ship2_hor2 = gen_random_ship(board2, 2, "hor")
    
    print_board(board1)

    while True:
        print("\033[1;34;40m \n")
        print(ship1_ver1)
        print(ship1_ver2)
        print(ship1_hor1)
        print(ship2_ver1)
        print(ship2_ver2)
        print(ship2_hor2)
        
        # board, guessing, hit count for player1
        player(board1, player1_name)
        print_board(board1)
        if hit_ship(board1, ship1_ver1, 4, "ver") \
           or hit_ship(board1, ship1_ver2, 3, "ver") \
           or hit_ship(board1, ship1_hor1, 2, "hor") \
           or hit_ship(board1, ship1_hor2, 3, "hor"):
            print("It was a boat")

        # end play for player1
        if all_fleet_hit(board1, 12):
            answer = input("{} WIN. Game over \n New game? Y/N".format(player1_name))
            if answer == "Y":
                main()
            else:
                exit()

        # board, guessing, hit count for player2
        print("\033[0;32;47m \n")
        print_board(board2)
        player(board2, player2_name)
        print_board(board2)
        if hit_ship(board2, ship2_ver1, 4, "ver") \
           or hit_ship(board2, ship2_ver2, 3, "ver") \
           or hit_ship(board2, ship2_hor2, 2, "hor")\
           or hit_ship(board2, ship2_hor1, 3, "hor"):
            print("It was a boat")

        # end play for player2
        if all_fleet_hit(board2, 12):
            answer2 = input("{} WIN. Game over \n New game? Y/N".format(player2_name))
            if answer2 == "Y":
                main()
            else:
                exit()


main()

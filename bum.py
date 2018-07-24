from validate import validate
from ships import gen_random_ship_vertical

hits = validate()
ver_ship = gen_random_ship_vertical()


def bum(hits, ver_ship):
    if hit_row_list == ship_row and hit_col_list == ship_col:
        print("You hit a boat!")
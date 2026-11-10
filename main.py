from validation import *
from printer import *
from manager import *


def main():
    while True:
        t = turn()
        print(f"turn {t}")
        choose = str_to_int(print_table())

        print(f"Player {t}, choose a cell (1-9): {choose}")
        while not is_good_num(choose) or available(choose):
            print("invalid choose\n choose again: ")
            choose = str_to_int(print_table())
        board[int(choose) - 1] = t

        if check_win(t):
            print_table()
            print(f"player {t} win")
            break

        if check_tie():
            print_table()
            print("tie")
            break
main()
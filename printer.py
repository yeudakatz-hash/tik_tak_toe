from winner import *



def print_table():
    choose = input(f"""
[1]{board[0]} | [2]{board[1]} | [3]{board[2]}
------+-------+----
[4]{board[3]} | [5]{board[4]} | [6]{board[5]}
------+-------+----
[7]{board[6]} | [8]{board[7]} | [9]{board[8]}
    """)


    return choose

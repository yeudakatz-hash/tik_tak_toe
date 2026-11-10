from printer import board
t = 0



def str_to_int(num):
    try:
        # num = int(num)
        return int(num)
    except:
        return 0


def is_good_num(num):
    return 0 < str_to_int(num) < 10


def available(num):
    if not is_good_num(num):
        return False
    return board[num - 1] == "X" or board[num - 1] == "O"


def turn():
    global t
    t += 1
    return "X" if t % 2 == 1 else "O"
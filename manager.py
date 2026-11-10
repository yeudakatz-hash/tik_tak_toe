

t = 0

def turn():
    global t
    t += 1
    return "X" if t % 2 == 1 else "O"



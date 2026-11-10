board = ["","","","","","","","",""]


WINNING_LINES = [
(0, 1, 2),
(3, 4, 5),
(6, 7, 8),
(0, 3, 6),
(1, 4, 7),
(2, 5, 8),
(0, 4, 8),
(2, 4, 6),
]


def check_win(player):
    for a, b, c in WINNING_LINES:
        if board[a] == board[b] == board[c] == player:
            return True
    return False


def check_tie():
    return "" not in board
# Задача Кольки

class Level:
    def __init__(self, old, custom=False):
        if custom:
            old.nowLevel = 25
        else:
            old.nowLevel = 2
        old.po = [8 * old.cell_size, 7 * old.cell_size]
        old.count = 0
        old.countBox = 6

        # стены 
        old.board[5][7] = 1

        old.board[5][6] = 1
        old.board[6][6] = 1
        old.board[7][6] = 1
        old.board[8][6] = 1
        old.board[9][6] = 1
        old.board[10][6] = 1
        old.board[10][7] = 1
        old.board[10][8] = 1
        old.board[10][9] = 1
        old.board[11][9] = 1
        old.board[11][10] = 1
        old.board[11][11] = 1
        old.board[11][12] = 1
        old.board[10][12] = 1
        old.board[9][12] = 1
        old.board[9][13] = 1
        old.board[9][14] = 1
        old.board[9][15] = 1
        old.board[10][15] = 1
        old.board[11][15] = 1
        old.board[12][15] = 1
        old.board[13][15] = 1
        old.board[13][16] = old.board[13][17] = old.board[13][18] = 1
        old.board[12][18] = old.board[11][18] = old.board[10][18] = old.board[9][18] = old.board[8][18] = 1
        old.board[7][18] = old.board[6][18] = old.board[5][18] = old.board[4][18] = 1
        old.board[4][17] = old.board[4][16] = 1
        old.board[3][16] = old.board[3][15] = old.board[3][14] = old.board[3][13] = 1
        old.board[4][13] = old.board[4][12] = old.board[4][11] = old.board[4][10] = 1
        old.board[5][10] = old.board[5][9] = old.board[5][8] = 1

        # ящики
        old.board[6][10] = 2 
        old.board[9][11] = 2
        old.board[6][13] = 2
        old.board[7][13] = 2
        old.board[8][13] = 2
        old.board[7][14] = 2

        # кресты 
        old.board[8][7] = 3
        old.board[9][7] = 3
        old.board[4][14] = 3
        old.board[4][15] = 3
        old.board[11][17] = 3
        old.board[12][16] = 3
        # hello
# Задача Андрея
class Level:
    def __init__(self, old, custom=False) -> None:
        if custom is False:
            old.nowLevel = 1
        else:
            old.nowLevel = 25
        # Стены по периметру
        old.board[3][10] = old.board[3][12] = old.board[3][11] = old.board[4][12] = old.board[4][13] = 1
        old.board[4][10] = old.board[5][10] = old.board[6][10] = 1
        old.board[6][9] = old.board[7][9] = old.board[8][9] = old.board[9][9] = old.board[10][9] = old.board[12][9] = 1
        old.board[12][9] = old.board[12][10] = old.board[12][11] = old.board[12][12] = old.board[12][13] = 1 # Пол
        old.board[12][16] = 1
        old.board[12][14] = old.board[12][15] = old.board[11][16] = old.board[11][9] = 1
        old.board[10][16] = old.board[9][16] = old.board[8][16] = old.board[7][16] = old.board[6][16] = 1
        old.board[5][16] = old.board[5][15] = old.board[5][14] = old.board[4][14] = 1

        # Внутренние стены
        old.board[10][13] = 1
        old.board[6][11] = old.board[7][11] = old.board[8][11] = 1
        old.board[8][13] = 1

        # Кресты
        old.board[5][13] = old.board[5][11] = old.board[5][12] = 3

        # Ящики
        old.board[8][12] = old.board[9][13] = old.board[10][11] = 2
        old.countBox = 3
        old.count = 0

        
        old.po = [11 * old.cell_size, 8 * old.cell_size]

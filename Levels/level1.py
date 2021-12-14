# Задача Андрея
class Level1:
    def __init__(self, old) -> None:
        # Стены по периметру
        old.board[3][10] = old.board[3][12] = old.board[3][11] = old.board[4][12] = old.board[4][13] = 1
        old.board[4][10] = old.board[5][10] = old.board[6][10] = 1
        old.board[6][9] = old.board[7][9] = old.board[8][9] = old.board[9][9] = old.board[10][9] = 1
        old.board[11][9] = old.board[11][10] = old.board[11][11] = old.board[11][12] = old.board[11][13] = 1
        old.board[11][14] = old.board[11][15] = 1
        old.board[10][15] = old.board[9][15] = old.board[8][15] = old.board[7][15] = old.board[6][15] = 1
        old.board[5][15] = old.board[5][14] = 1

        # Ящики
        # old.board[8][10] = old.board[8][11] = 2
        # old.board[7][12] = 2
        # old.board[9][13] = old.board[9][15] = 2
        # Кресты
        # old.board[4][11] = old.board[5][11] = old.board[5][12] = 3
        old.po = [1 * old.cell_size, 1 * old.cell_size]

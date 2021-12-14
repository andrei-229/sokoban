# Задача Кольки
class Level2:
    def __init__(self, old):
<<<<<<< HEAD
        old.board[10][10] = old.board[10][9] = old.board[10][8] = 1
        old.board[9][8] = old.board[8][8] = old.board[7][8] = old.board[6][8] = 1
        old.board[6][9] = old.board[6][10] = old.board[6][11] = 1
        old.board[5][11] = old.board[7][11] = 1
        old.board[5][12] = old.board[5][13] = old.board[5][14] = old.board[5][15] = 1
        old.board[6][15] = old.board[7][15] = 1
        old.board[7][16] = old.board[7][17] = old.board[7][18] = 1
        old.board[8][18] = old.board[9][18] = old.board[10][18] = old.board[11][18] = old.board[12][18] = 1
        old.board[11][9] = old.board[12][9] = old.board[13][9] = 1
        old.board[13][10] = old.board[13][11] = old.board[13][12] = old.board[13][13] = old.board[13][14] = old.board[13][15] = old.board[13][16] = old.board[13][17] = old.board[13][18] = 1
        # Внутри
        old.board[11][12] = old.board[11][13] = old.board[11][14] = old.board[11][15] = old.board[11][16] = 1
        old.board[10][12] = old.board[9][12] = 1
        old.board[10][16] = old.board[9][16] = 1
        # Ящики
        old.board[8][10] = old.board[8][11] = 2
        old.board[7][12] = 2
        old.board[9][13] = old.board[9][15] = 2
        # Кресты
        old.board[12][12] = old.board[12][13] = old.board[12][14] = old.board[12][15] = old.board[12][16] = 3
        old.po = [10 * old.cell_size, 10 * old.cell_size]
        old.count_box = 5
        old.nowLevel = 3
=======
        # стены
        old.board[5][7] = old.board[5][6] = old.board[6][6] = 1
        old.board[7][6] = old.board[8][6] = old.board[9][6] = 1
        old.board[10][6] = old.board[10][7] = old.board[10][8] = old.board[10][9] = 1
        old.board[11][9] = old.board[11][10] = old.board[11][11] = old.board[11][12] = old.board[10][12]= 1
        old.board[9][12] = old.board[9][13] = old.board[9][14] = old.board[9][15] = 1 
        old.board[10][15] = old.board[11][15] = old.board[12][15] = old.board[13][15] = 1
        old.board[13][16] = old.board[13][17] = old.board[13][18] = 1
        old.board[12][18] = old.board[11][18] = old.board[10][18] = old.board[9][18] = 1
        old.board[8][18] = old.board[7][18] = old.board[6][18] = old.board[5][18] = old.board[4][18] = 1
        old.board[4][17] = old.board[4][16] = 1
        old.board[3][16] = old.board[3][15] = old.board[3][14] = old.board[3][13] = 1
        old.board[4][13] = old.board[4][12] = old.board[4][11] = old.board[4][10] = 1
        old.board[5][10] = old.board[5][9] = old.board[5][8] = 1

        # ящики 
        old.board[6][10] = old.board[9][11] = old.board[6][13] = old.board[7][13] = old.board[8][13] = old.board[7][14] = 2
        
        # кресты
        old.board[9][7] = old.board[8][7] = 3
        old.board[4][14] = old.board[4][15] = 3
        old.board[11][17] = old.board[12][16] = 3


        old.po = [8 * old.cell_size, 7 * old.cell_size]
>>>>>>> 53d33a500fb25bc45460c6b90e97d3058d259891

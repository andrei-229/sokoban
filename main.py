import pygame  # Import pygame
import pygame_gui
from Levels.level3 import Level3
from Levels.level2 import Level2
from Levels.level1 import Level1


class Board:
    def __init__(self, screen, width, height, level):
        self.left = 0  # левая граница поля
        self.top = 0  # верхняя граница поля
        self.cell_size = 30  # размер клетки
        self.count = 0
        self.countBox = 0
        self.nowLevel = level
        self.screen = screen

        self.width = width  # ширина поля
        self.height = height  # высота поля
        # список списков с состояниями каждой клетки
        self.board = [[0] * width for _ in range(height)]
        # Размещение одной стены первое число это по Y второе по X
        self.po = [0, 0]
        # Level1(self)
        self.krest = []
        self.coor = []

        # спрайты
        self.scale = pygame.image.load(
            'animation/r1.png')  # изображение игрока
        self.scale = pygame.transform.scale(
            self.scale, (self.cell_size, self.cell_size))  # масштабирование изображения
        self.leftChar = pygame.image.load(
            'animation/l1.png')  # изображение игрока
        self.leftChar = pygame.transform.scale(
            self.leftChar, (self.cell_size, self.cell_size))  # масштабирование изображения
        self.bor = pygame.image.load('animation/wall.png')
        self.bor = pygame.transform.scale(
            self.bor, (self.cell_size, self.cell_size))
        self.boxs = pygame.image.load('animation/woodBox5.jpg')
        self.boxs = pygame.transform.scale(
            self.boxs, (self.cell_size, self.cell_size))
        self.primChar = pygame.image.load(
            'animation/b1.png')  # изображение игрока
        self.primChar = pygame.transform.scale(
            self.primChar, (self.cell_size, self.cell_size))
        self.backChar = pygame.image.load(
            'animation/b2.png')  # изображение игрока
        self.backChar = pygame.transform.scale(
            self.backChar, (self.cell_size, self.cell_size))

        # значения по умолчанию
        self.save_po = self.po  # сохранение координат игрока

    # отрисовка поля
    def render(self, screen):
        screen.fill((0, 0, 0))  # очистка экрана
        if self.count == self.countBox:
            if self.nowLevel == 0:
                self.board = [[0] * self.width for _ in range(self.height)]
                self.countBox = 3
                self.count = 0
                Level1(self)
            elif self.nowLevel == 1:
                self.board = [[0] * self.width for _ in range(self.height)]
                self.countBox = 6
                self.count = 0
                Level2(self)
            elif self.nowLevel == 2:
                self.board = [[0] * self.width for _ in range(self.height)]
                self.countBox = 5
                self.count = 0
                Level3(self)
            else:
                print('ПОБЕДА! Вам BAN!')
        try:  # проверка на наличие клетки в списке
            # проверка на препятствие
            if self.board[(int(self.po[1] / self.cell_size)) - 1][(int(self.po[0] / self.cell_size)) - 1] == 1 or self.po[0] <= 0 or self.po[1] <= 0:
                self.po = self.save_po  # возвращение координат игрока
        except:  # если клетки нет в списке
            self.po = self.save_po  # возвращение координат игрока
        for i in range(self.height):  # перебор всех строк
            for j in range(self.width):  # перебор всех столбцов
                x = self.left + j * self.cell_size
                y = self.top + i * self.cell_size
                if self.board[i][j] == 0:  # если клетка пустая
                    pass  # отрисовка клетки
                elif self.board[i][j] == 2:
                    self.boxs_rect = self.boxs.get_rect(
                        bottomright=(x + self.cell_size, y + self.cell_size))
                    screen.blit(self.boxs, self.boxs_rect)
                elif self.board[i][j] == 3:
                    pygame.draw.line(screen, (255, 255, 255), (x, y),
                                     (x + self.cell_size, y + self.cell_size),
                                     width=1)
                    pygame.draw.line(screen, (255, 255, 255), (x, y + self.cell_size),
                                     (x + self.cell_size, y),
                                     width=2)
                elif self.board[i][j] == 4:
                    self.boxs_rect = self.boxs.get_rect(
                        bottomright=(x + self.cell_size, y + self.cell_size))
                    screen.blit(self.boxs, (x, y))
                else:  # если клетка занята стеной
                    self.bor_rect = self.bor.get_rect(
                        bottomright=(x + self.cell_size, y + self.cell_size))
                    screen.blit(self.bor, self.bor_rect)
        self.draw_player(screen, self.po, 'primo')

    # отрисовка игрока (Ничего не трогал, все работает по вашему коду)
    def draw_player(self, screen, xy, lico):
        if lico == 'right':
            self.man_rect = self.scale.get_rect(bottomright=(xy[0], xy[1]))
            screen.blit(self.scale, self.man_rect)
            pygame.display.update()
            self.po[0] = xy[0]
            self.po[1] = xy[1]
        elif lico == 'left':
            self.man_rect = self.leftChar.get_rect(bottomright=(xy[0], xy[1]))
            screen.blit(self.leftChar, self.man_rect)
            pygame.display.update()
            self.po[0] = xy[0]
            self.po[1] = xy[1]
        elif lico == 'primo':
            self.man_rect = self.primChar.get_rect(bottomright=(xy[0], xy[1]))
            screen.blit(self.primChar, self.man_rect)
            pygame.display.update()
            self.po[0] = xy[0]
            self.po[1] = xy[1]
        elif lico == 'back':
            self.man_rect = self.backChar.get_rect(bottomright=(xy[0], xy[1]))
            screen.blit(self.backChar, self.man_rect)
            pygame.display.update()
            self.po[0] = xy[0]
            self.po[1] = xy[1]

    def barier(self, y, x):
        self.board[y][x] = 1

    def box(self, y, x):
        self.board[y][x] = 2

    def krests(self, y, x):
        self.board[y][x] = 3
        self.krest.append([y, x])
        print(self.krest)

    # перемещение налево
    def move_left(self):
        self.save_po = []  # сохранение координат игрока
        for i in self.po:  # перебор координат игрока
            self.save_po.append(i)  # добавление координат в список
        # все действия выше сделаны по причине проблемы изменения save_po при изменении po (Один и тот же id в оперативной памяти)
        # перемещение игрока на одну клетку влево
        self.po[0] = self.po[0] - self.cell_size
        # получение координат игрока по оси Х
        now_board_x = int(self.po[0] / self.cell_size)
        # получение координат игрока по оси Y
        now_board_y = int(self.po[1] / self.cell_size)
        # если игрок на клетке с коробкой или крестом
        if self.board[now_board_y - 1][now_board_x - 1] == 2 or self.board[now_board_y - 1][now_board_x - 1] == 1:
            if self.board[now_board_y - 1][now_board_x - 1] != 1:
                if self.board[(int(self.po[1] / self.cell_size)) - 1][(int(self.po[0] / self.cell_size)) - 2] == 1 or self.board[(int(self.po[1] / self.cell_size)) - 1][(int(self.po[0] / self.cell_size)) - 2] == 2 or self.board[(int(self.po[1] / self.cell_size)) - 1][(int(self.po[0] / self.cell_size)) - 2] == 4:
                    self.po = self.save_po
                # проверка на крестик
                elif self.board[(int(self.po[1] / self.cell_size)) - 1][(int(self.po[0] / self.cell_size)) - 2] == 3:
                    # перемещение на крестик
                    self.board[(int(self.po[1] / self.cell_size)) -
                               1][(int(self.po[0] / self.cell_size)) - 2] = 4
                    self.count += 1
                    # перемещение на пустую клетку
                    self.board[(int(self.po[1] / self.cell_size)) -
                               1][(int(self.po[0] / self.cell_size)) - 1] = 0
                elif self.board[(int(self.po[1] / self.cell_size)) - 1][(int(self.po[0] / self.cell_size)) - 2] == 4:
                    self.board[(int(self.po[1] / self.cell_size)) -
                               1][(int(self.po[0] / self.cell_size)) - 2] = 0
                    self.board[(int(self.po[1] / self.cell_size)) -
                               1][(int(self.po[0] / self.cell_size)) - 1] = 2
                else:
                    self.board[(int(self.po[1] / self.cell_size)) -
                               1][(int(self.po[0] / self.cell_size)) - 1] = 0
                    self.board[(int(self.po[1] / self.cell_size)) -
                               1][(int(self.po[0] / self.cell_size)) - 2] = 2
            else:
                self.po = self.save_po
        elif self.board[(int(self.po[1] / self.cell_size)) - 1][(int(self.po[0] / self.cell_size)) - 1] == 4:
            if self.board[(int(self.po[1] / self.cell_size)) - 1][(int(self.po[0] / self.cell_size)) - 2] != 1:
                if self.board[(int(self.po[1] / self.cell_size)) - 1][(int(self.po[0] / self.cell_size)) - 2] == 3:
                    self.board[(int(self.po[1] / self.cell_size)) -
                               1][(int(self.po[0] / self.cell_size)) - 2] = 4
                    self.board[(int(self.po[1] / self.cell_size)) -
                               1][(int(self.po[0] / self.cell_size)) - 1] = 3
                elif self.board[(int(self.po[1] / self.cell_size)) - 1][(int(self.po[0] / self.cell_size)) - 2] == 4 or self.board[(int(self.po[1] / self.cell_size)) - 1][(int(self.po[0] / self.cell_size)) - 2] == 2:
                    self.po = self.save_po
                else:
                    self.board[(int(self.po[1] / self.cell_size)) -
                               1][(int(self.po[0] / self.cell_size)) - 2] = 2
                    self.count -= 1
                    self.board[(int(self.po[1] / self.cell_size)) -
                               1][(int(self.po[0] / self.cell_size)) - 1] = 3
            else:
                self.po = self.save_po
        self.screen.fill((0, 0, 0))  # очистка экрана
        self.render(self.screen)  # отрисовка поля
        self.draw_player(self.screen, self.po, 'left')  # отрисовка игрока
        pygame.display.update()

    # перемещение направо
    def move_right(self):
        self.save_po = []  # сохранение координат игрока
        for i in self.po:  # перебор координат игрока
            self.save_po.append(i)  # добавление координат в список
        # все действия выше сделаны по причине проблемы изменения save_po при изменении po (Один и тот же id в оперативной памяти)
        # перемещение игрока на одну клетку вправо
        self.po[0] = self.po[0] + self.cell_size
        try:
            if self.board[(int(self.po[1] / self.cell_size)) - 1][(int(self.po[0] / self.cell_size)) - 1] == 2 or self.board[(int(self.po[1] / self.cell_size)) - 1][(int(self.po[0] / self.cell_size)) - 1] == 1:
                if self.board[(int(self.po[1] / self.cell_size)) - 1][(int(self.po[0] / self.cell_size)) - 1] != 1:
                    if self.board[(int(self.po[1] / self.cell_size)) - 1][(int(self.po[0] / self.cell_size))] == 1 or self.board[(int(self.po[1] / self.cell_size)) - 1][(int(self.po[0] / self.cell_size))] == 2 or self.board[(int(self.po[1] / self.cell_size)) - 1][(int(self.po[0] / self.cell_size))] == 4:
                        self.po = self.save_po
                    elif self.board[(int(self.po[1] / self.cell_size)) - 1][(int(self.po[0] / self.cell_size))] == 3:
                        self.board[(int(self.po[1] / self.cell_size)) -
                                   1][(int(self.po[0] / self.cell_size))] = 4
                        self.count += 1
                        self.board[(int(self.po[1] / self.cell_size)) -
                                   1][(int(self.po[0] / self.cell_size)) - 1] = 0
                    elif self.board[(int(self.po[1] / self.cell_size)) - 1][(int(self.po[0] / self.cell_size))] == 4:
                        self.board[(int(self.po[1] / self.cell_size)) -
                                   1][(int(self.po[0] / self.cell_size))] = 0
                        self.board[(int(self.po[1] / self.cell_size)) -
                                   1][(int(self.po[0] / self.cell_size)) - 1] = 2
                    else:
                        self.board[(int(self.po[1] / self.cell_size)) -
                                   1][(int(self.po[0] / self.cell_size))] = 2
                        self.board[(int(self.po[1] / self.cell_size)) -
                                   1][(int(self.po[0] / self.cell_size)) - 1] = 0
                else:
                    self.po = self.save_po
            elif self.board[(int(self.po[1] / self.cell_size)) - 1][(int(self.po[0] / self.cell_size)) - 1] == 4:
                if self.board[(int(self.po[1] / self.cell_size)) - 1][(int(self.po[0] / self.cell_size))] != 1:
                    if self.board[(int(self.po[1] / self.cell_size)) - 1][(int(self.po[0] / self.cell_size))] == 3:
                        self.board[(int(self.po[1] / self.cell_size)) -
                                   1][(int(self.po[0] / self.cell_size))] = 4
                        self.board[(int(self.po[1] / self.cell_size)) -
                                   1][(int(self.po[0] / self.cell_size)) - 1] = 3
                    elif self.board[(int(self.po[1] / self.cell_size)) - 1][(int(self.po[0] / self.cell_size))] == 4 or self.board[(int(self.po[1] / self.cell_size)) - 1][(int(self.po[0] / self.cell_size))] == 2:
                        self.po = self.save_po
                    else:
                        self.board[(int(self.po[1] / self.cell_size)) -
                                   1][(int(self.po[0] / self.cell_size))] = 2
                        self.count -= 1
                        self.board[(int(self.po[1] / self.cell_size)) -
                                   1][(int(self.po[0] / self.cell_size)) - 1] = 3
                else:
                    self.po = self.save_po
        except:
            self.po = self.save_po
        self.screen.fill((0, 0, 0))  # очистка экрана
        self.render(self.screen)  # отрисовка поля
        self.draw_player(self.screen, self.po, 'right')  # отрисовка игрока
        pygame.display.update()

    # перемещение вверх
    def move_up(self):
        self.save_po = []  # сохранение координат игрока
        for i in self.po:  # перебор координат игрока
            self.save_po.append(i)  # добавление координат в список
        # все действия выше сделаны по причине проблемы изменения save_po при изменении po (Один и тот же id в оперативной памяти)
        # перемещение игрока на одну клетку вверх
        self.po[1] = self.po[1] - self.cell_size
        try:
            if self.board[(int(self.po[1] / self.cell_size)) - 1][(int(self.po[0] / self.cell_size)) - 1] == 2 or self.board[(int(self.po[1] / self.cell_size)) - 1][(int(self.po[0] / self.cell_size)) - 1] == 1:  # если на клетке препятствие
                # если на клетке не препятствие
                if self.board[(int(self.po[1] / self.cell_size)) - 1][(int(self.po[0] / self.cell_size)) - 1] != 1:
                    if self.board[(int(self.po[1] / self.cell_size)) - 2][(int(self.po[0] / self.cell_size)) - 1] == 1 or self.board[(int(self.po[1] / self.cell_size)) - 2][(int(self.po[0] / self.cell_size)) - 1] == 2 or self.board[(int(self.po[1] / self.cell_size)) - 2][(int(self.po[0] / self.cell_size)) - 1] == 4:  # если на клетке препятствие
                        self.po = self.save_po
                    # если на клетке ящик
                    elif self.board[(int(self.po[1] / self.cell_size)) - 2][(int(self.po[0] / self.cell_size)) - 1] == 3:
                        # перемещение ящика на клетку вверх
                        self.board[(int(self.po[1] / self.cell_size)) -
                                   2][(int(self.po[0] / self.cell_size)) - 1] = 4
                        self.count += 1
                        self.board[(int(self.po[1] / self.cell_size)) - 1][(
                            int(self.po[0] / self.cell_size)) - 1] = 0  # очистка клетки
                    elif self.board[(int(self.po[1] / self.cell_size)) - 2][(int(self.po[0] / self.cell_size)) - 1] == 4:
                        self.board[(int(self.po[1] / self.cell_size)) -
                                   2][(int(self.po[0] / self.cell_size)) - 1] = 0
                        self.board[(int(self.po[1] / self.cell_size)) -
                                   1][(int(self.po[0] / self.cell_size)) - 1] = 2
                    else:
                        self.board[(int(self.po[1] / self.cell_size)) -
                                   2][(int(self.po[0] / self.cell_size)) - 1] = 2
                        self.board[(int(self.po[1] / self.cell_size)) -
                                   1][(int(self.po[0] / self.cell_size)) - 1] = 0
                else:
                    self.po = self.save_po
            elif self.board[(int(self.po[1] / self.cell_size)) - 1][(int(self.po[0] / self.cell_size)) - 1] == 4:
                if self.board[(int(self.po[1] / self.cell_size)) - 2][(int(self.po[0] / self.cell_size)) - 1] != 1:
                    if self.board[(int(self.po[1] / self.cell_size)) - 2][(int(self.po[0] / self.cell_size)) - 1] == 3:
                        self.board[(int(self.po[1] / self.cell_size)) -
                                   2][(int(self.po[0] / self.cell_size)) - 1] = 4
                        self.board[(int(self.po[1] / self.cell_size)) -
                                   1][(int(self.po[0] / self.cell_size)) - 1] = 3
                    elif self.board[(int(self.po[1] / self.cell_size)) - 2][(int(self.po[0] / self.cell_size)) - 1] == 4 or self.board[(int(self.po[1] / self.cell_size)) - 2][(int(self.po[0] / self.cell_size)) - 1] == 2:
                        self.po = self.save_po
                    else:
                        self.board[(int(self.po[1] / self.cell_size)) -
                                   2][(int(self.po[0] / self.cell_size)) - 1] = 2
                        self.count -= 1
                        self.board[(int(self.po[1] / self.cell_size)) -
                                   1][(int(self.po[0] / self.cell_size)) - 1] = 3
                else:
                    self.po = self.save_po
        except:
            if self.board[(int(self.po[1] / self.cell_size))][(int(self.po[0] / self.cell_size))] == 2:
                self.board[(int(self.po[1] / self.cell_size)) -
                           1][(int(self.po[0] / self.cell_size)) - 1] = 2
                self.board[(int(self.po[1] / self.cell_size))
                           ][(int(self.po[0] / self.cell_size)) - 1] = 0

        self.screen.fill((0, 0, 0))  # очистка экрана
        self.render(self.screen)  # отрисовка поля
        self.draw_player(self.screen, self.po, 'back')  # отрисовка игрока
        pygame.display.update()

    # перемещение вниз
    def move_down(self):
        self.save_po = []  # сохранение координат игрока
        for i in self.po:  # перебор координат игрока
            self.save_po.append(i)  # добавление координат в список
        # все действия выше сделаны по причине проблемы изменения save_po при изменении po (Один и тот же id в оперативной памяти)
        # перемещение игрока на одну клетку вниз
        self.po[1] = self.po[1] + self.cell_size
        try:
            if self.board[(int(self.po[1] / self.cell_size)) - 1][(int(self.po[0] / self.cell_size)) - 1] == 2 or self.board[(int(self.po[1] / self.cell_size)) - 1][(int(self.po[0] / self.cell_size)) - 1] == 1:
                if self.board[(int(self.po[1] / self.cell_size)) - 1][(int(self.po[0] / self.cell_size)) - 1] != 1:
                    if self.board[(int(self.po[1] / self.cell_size))][(int(self.po[0] / self.cell_size)) - 1] == 1 or self.board[(int(self.po[1] / self.cell_size))][(int(self.po[0] / self.cell_size)) - 1] == 2 or self.board[(int(self.po[1] / self.cell_size))][(int(self.po[0] / self.cell_size)) - 1] == 4:
                        self.po = self.save_po
                    elif self.board[(int(self.po[1] / self.cell_size))][(int(self.po[0] / self.cell_size)) - 1] == 3:
                        self.board[(int(self.po[1] / self.cell_size))
                                   ][(int(self.po[0] / self.cell_size)) - 1] = 4
                        self.count += 1
                        self.board[(int(self.po[1] / self.cell_size)) -
                                   1][(int(self.po[0] / self.cell_size)) - 1] = 0
                    elif self.board[(int(self.po[1] / self.cell_size))][(int(self.po[0] / self.cell_size)) - 1] == 4:
                        self.board[(int(self.po[1] / self.cell_size))
                                   ][(int(self.po[0] / self.cell_size)) - 1] = 0
                        self.board[(int(self.po[1] / self.cell_size)) -
                                   1][(int(self.po[0] / self.cell_size)) - 1] = 2
                    else:
                        self.board[(int(self.po[1] / self.cell_size))
                                   ][(int(self.po[0] / self.cell_size)) - 1] = 2
                        self.board[(int(self.po[1] / self.cell_size)) -
                                   1][(int(self.po[0] / self.cell_size)) - 1] = 0
                else:
                    self.po = self.save_po
            elif self.board[(int(self.po[1] / self.cell_size)) - 1][(int(self.po[0] / self.cell_size)) - 1] == 4:
                if self.board[(int(self.po[1] / self.cell_size))][(int(self.po[0] / self.cell_size)) - 1] != 1:
                    if self.board[(int(self.po[1] / self.cell_size))][(int(self.po[0] / self.cell_size)) - 1] == 3:
                        self.board[(int(self.po[1] / self.cell_size))
                                   ][(int(self.po[0] / self.cell_size)) - 1] = 4
                        self.board[(int(self.po[1] / self.cell_size)) -
                                   1][(int(self.po[0] / self.cell_size)) - 1] = 3
                    elif self.board[(int(self.po[1] / self.cell_size))][(int(self.po[0] / self.cell_size)) - 1] == 4 or self.board[(int(self.po[1] / self.cell_size))][(int(self.po[0] / self.cell_size)) - 1] == 2:
                        self.po = self.save_po
                    else:
                        self.board[(int(self.po[1] / self.cell_size))
                                   ][(int(self.po[0] / self.cell_size)) - 1] = 2
                        self.count -= 1
                        self.board[(int(self.po[1] / self.cell_size)) -
                                   1][(int(self.po[0] / self.cell_size)) - 1] = 3
                else:
                    self.po = self.save_po
        except:
            self.po = self.save_po
        self.screen.fill((0, 0, 0))  # очистка экрана
        self.render(self.screen)  # отрисовка поля
        self.draw_player(self.screen, self.po, 'primo')  # отрисовка игрока
        pygame.display.update()


# всё далее я не менял, поэтому не буду писать комментарии
if __name__ == '__main__':
    pygame.init()
    width, height = 780, 540
    size = width, height
    screen = pygame.display.set_mode(size)
    screen2 = pygame.Surface(screen.get_size())
    pygame.display.set_caption("SokoBAN")
    pygame.display.set_icon(pygame.image.load('animation/logo.png'))
    manager = pygame_gui.UIManager(screen.get_size())
    screen.fill((255, 255, 255))
    clock = pygame.time.Clock()
    fps = 90
    running = True
    run1 = True
    check = False

    st2 = pygame.image.load('animation/sok.png')
    st = pygame_gui.elements.ui_image.UIImage(relative_rect=pygame.Rect((250, 20), (300, 100)),
                                              manager=manager, image_surface=st2)

    start_button = pygame_gui.elements.UIButton(relative_rect=pygame.Rect((300, 150), (200, 100)),
                                                     text='Start',
                                                     manager=manager)

    levels_button = pygame_gui.elements.UIButton(relative_rect=pygame.Rect((300, 270), (200, 100)),
                                                                text='Levels',
                                                                manager=manager)

    settings_button = pygame_gui.elements.UIButton(relative_rect=pygame.Rect((300, 385), (200, 100)),
                                                text='Settings',
                                                manager=manager)

    
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

            if event.type == pygame.USEREVENT:
                if event.user_type == pygame_gui.UI_BUTTON_PRESSED:
                    if event.ui_element == start_button:
                        check = True
                        run1 = False
                        board = Board(screen, 26, 18, 0)
                        board.render(screen)
                        start_button.kill()
                        settings_button.kill()
                        levels_button.kill()
                        st.kill()
                    elif event.ui_element == levels_button:
                        start_button.kill()
                        settings_button.kill()
                        levels_button.kill()
                        st.kill()
                        first_level = pygame_gui.elements.UIButton(relative_rect=pygame.Rect((35, 270), (220, 50)),
                                                                text='1',
                                                                manager=manager)

                        second_level = pygame_gui.elements.UIButton(relative_rect=pygame.Rect((275, 270), (220, 50)),
                                                                text='2',
                                                                manager=manager)

                        third_level = pygame_gui.elements.UIButton(relative_rect=pygame.Rect((515, 270), (220, 50)),
                                                                text='3',
                                                                manager=manager)
                    elif event.ui_element == first_level:
                        check = True
                        run1 = False
                        board = Board(screen, 26, 18, 0)
                        board.render(screen)
                        first_level.kill()
                        second_level.kill()
                        third_level.kill()
                    elif event.ui_element == second_level:
                        check = True
                        run1 = False
                        board = Board(screen, 26, 18, 1)
                        board.render(screen)
                        first_level.kill()
                        second_level.kill()
                        third_level.kill()
                    elif event.ui_element == third_level:
                        check = True
                        run1 = False
                        board = Board(screen, 26, 18, 2)
                        board.render(screen)
                        first_level.kill()
                        second_level.kill()
                        third_level.kill()
            if check:
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_LEFT:
                        board.move_left()
                    if event.key == pygame.K_RIGHT:
                        board.move_right()
                    if event.key == pygame.K_UP:
                        board.move_up()
                    if event.key == pygame.K_DOWN:
                        board.move_down()
                    if event.key == pygame.K_r:
                        board.board = [[0] * width for _ in range(height)]
                        board.count = board.countBox = 0
                        board.nowLevel -= 1
                        board.render(screen)
            manager.process_events(event)
        if run1:
            manager.update(clock.tick(60))
            screen.blit(screen2, (0, 0))
            manager.draw_ui(screen)
        clock.tick(fps)
        pygame.display.flip()
    pygame.quit()

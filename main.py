import pygame  # Import pygame


class Board:
    def __init__(self, width, height):
        self.left = 0  # левая граница поля
        self.top = 0  # верхняя граница поля
        self.cell_size = 30  # размер клетки
        self.count = 0

        self.width = width  # ширина поля
        self.height = height  # высота поля
        # список списков с состояниями каждой клетки
        self.board = [[0] * width for _ in range(height)]
        # Размещение одной стены первое число это по Y второе по X
        self.board[13][16] = 1
        self.po = [360, 360]  # координаты игрока
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
        self.barier(12, 16)
        self.barier(5, 5)
        self.box(11, 16)
        self.box(11, 17)
        self.box(11, 18)
        self.krests(10, 16)
        self.krests(10, 15)
        self.krests(9, 15)

    # отрисовка поля
    def render(self, screen):
        screen.fill((0, 0, 0))  # очистка экрана
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
                    pygame.draw.rect(screen, (255, 255, 255), (x, y, self.cell_size,
                                     self.cell_size), 1, 1, 1, 1, 1, 1)  # отрисовка клетки
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
                    print('Коробка на кресту', str(self.count))
                    if [i, j] not in self.coor:
                        self.coor.append([i, j])
                        self.count += 1
                else:  # если клетка занята стеной
                    self.bor_rect = self.bor.get_rect(
                        bottomright=(x + self.cell_size, y + self.cell_size))
                    screen.blit(self.bor, self.bor_rect)
        self.draw_player(self.po, 'primo')

    # отрисовка игрока (Ничего не трогал, все работает по вашему коду)
    def draw_player(self, xy, lico):
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
                    self.board[(int(self.po[1] / self.cell_size)) -
                               1][(int(self.po[0] / self.cell_size)) - 1] = 3
            else:
                self.po = self.save_po
        screen.fill((0, 0, 0))  # очистка экрана
        self.render(screen)  # отрисовка поля
        self.draw_player(self.po, 'left')  # отрисовка игрока
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
                        self.board[(int(self.po[1] / self.cell_size)) -
                                   1][(int(self.po[0] / self.cell_size)) - 1] = 3
                else:
                    self.po = self.save_po
        except:
            self.po = self.save_po
        screen.fill((0, 0, 0))  # очистка экрана
        self.render(screen)  # отрисовка поля
        self.draw_player(self.po, 'right')  # отрисовка игрока
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

        screen.fill((0, 0, 0))  # очистка экрана
        self.render(screen)  # отрисовка поля
        self.draw_player(self.po, 'back')  # отрисовка игрока
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
                        self.board[(int(self.po[1] / self.cell_size)) -
                                   1][(int(self.po[0] / self.cell_size)) - 1] = 3
                else:
                    self.po = self.save_po
        except:
            self.po = self.save_po
        screen.fill((0, 0, 0))  # очистка экрана
        self.render(screen)  # отрисовка поля
        self.draw_player(self.po, 'primo')  # отрисовка игрока
        pygame.display.update()


# всё далее я не менял, поэтому не буду писать комментарии
if __name__ == '__main__':
    pygame.init()
    width, height = 780, 540
    size = width, height
    screen = pygame.display.set_mode(size)
    screen2 = pygame.Surface(screen.get_size())
    screen.fill((0, 0, 0))
    clock = pygame.time.Clock()
    board = Board(26, 18)
    board.render(screen)
    fps = 90
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.MOUSEBUTTONDOWN:
                pass
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
                    board = Board(26, 18)
                    board.render(screen)
        clock.tick(fps)
        pygame.display.flip()
    pygame.quit()

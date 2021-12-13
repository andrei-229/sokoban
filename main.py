import pygame  # Import pygame


class Board:
    def __init__(self, width, height):
        self.left = 0  # левая граница поля
        self.top = 0  # верхняя граница поля
        self.cell_size = 30  # размер клетки

        self.width = width  # ширина поля
        self.height = height  # высота поля
        # список списков с состояниями каждой клетки
        self.board = [[0] * width for _ in range(height)]
        # Размещение одной стены первое число это по Y второе по X
        self.board[13][16] = 1
        self.po = [360, 360]  # координаты игрока
        self.coords = {}  # словарь координат клеток
        self.bar = []  # список координат препятствий

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

        # значения по умолчанию
        self.save_po = self.po  # сохранение координат игрока
        self.barier(12, 16)
        self.box(11, 16)

    # отрисовка поля
    def render(self, screen):
        screen.fill((0, 0, 0))  # очистка экрана
        try:  # проверка на наличие клетки в списке
            # проверка на препятствие
            if self.board[(int(self.po[1] / 30)) - 1][(int(self.po[0] / 30)) - 1] == 1 or self.po[0] <= 0 or self.po[1] <= 0:
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
                else:  # если клетка занята стеной
                    self.bor_rect = self.bor.get_rect(
                        bottomright=(x + self.cell_size, y + self.cell_size))
                    screen.blit(self.bor, self.bor_rect)
        # pygame.display.update() # отрисовка стены
        self.draw_player(self.po)  # отрисовка игрока
        self.ui = 1

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

    def barier(self, y, x):
        self.board[y][x] = 1

    def box(self, y, x):
        self.board[y][x] = 2
        return [y, x]

    # перемещение налево
    def move_left(self):
        self.save_po = []  # сохранение координат игрока
        for i in self.po:  # перебор координат игрока
            self.save_po.append(i)  # добавление координат в список
        # все действия выше сделаны по причине проблемы изменения save_po при изменении po (Один и тот же id в оперативной памяти)
        # перемещение игрока на одну клетку влево
        self.po[0] = self.po[0] - self.cell_size
        if self.board[(int(self.po[1] / 30)) - 1][(int(self.po[0] / 30)) - 1] == 2:
            if self.board[(int(self.po[1] / 30)) - 1][(int(self.po[0] / 30)) - 2] != 1:
                self.board[(int(self.po[1] / 30)) -
                           1][(int(self.po[0] / 30)) - 2] = 2
                self.board[(int(self.po[1] / 30)) -
                           1][(int(self.po[0] / 30)) - 1] = 0
            else:
                self.po = self.save_po
        screen.fill((0, 0, 0))  # очистка экрана
        self.render(screen)  # отрисовка поля
        self.draw_player(self.po, 'rigth')  # отрисовка игрока
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
            if self.board[(int(self.po[1] / 30)) - 1][(int(self.po[0] / 30)) - 1] == 2 or self.board[(int(self.po[1] / 30)) - 1][(int(self.po[0] / 30)) - 1] == 1:
                if self.board[(int(self.po[1] / 30)) - 1][(int(self.po[0] / 30))] != 1:
                    self.board[(int(self.po[1] / 30)) -
                               1][(int(self.po[0] / 30))] = 2
                    self.board[(int(self.po[1] / 30)) -
                               1][(int(self.po[0] / 30)) - 1] = 0
                else:
                    self.po = self.save_po
        except:
            self.po = self.save_po
        screen.fill((0, 0, 0))  # очистка экрана
        self.render(screen)  # отрисовка поля
        self.draw_player(self.po)  # отрисовка игрока
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
            if self.board[(int(self.po[1] / 30)) - 1][(int(self.po[0] / 30)) - 1] == 2 or self.board[(int(self.po[1] / 30)) - 1][(int(self.po[0] / 30)) - 1] == 1:
                if self.board[(int(self.po[1] / 30)) - 2][(int(self.po[0] / 30)) - 1] != 1:
                    self.board[(int(self.po[1] / 30)) -
                               2][(int(self.po[0] / 30)) - 1] = 2
                    self.board[(int(self.po[1] / 30)) -
                               1][(int(self.po[0] / 30)) - 1] = 0
                else:
                    self.po = self.save_po
        except:
            if self.board[(int(self.po[1] / 30))][(int(self.po[0] / 30))] == 2:
                self.board[(int(self.po[1] / 30)) -
                           1][(int(self.po[0] / 30)) - 1] = 2
                self.board[(int(self.po[1] / 30))
                           ][(int(self.po[0] / 30)) - 1] = 0

        screen.fill((0, 0, 0))  # очистка экрана
        self.render(screen)  # отрисовка поля
        self.draw_player(self.po)  # отрисовка игрока
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
            if self.board[(int(self.po[1] / 30)) - 1][(int(self.po[0] / 30)) - 1] == 2 or self.board[(int(self.po[1] / 30)) - 1][(int(self.po[0] / 30)) - 1] == 1:
                if self.board[(int(self.po[1] / 30))][(int(self.po[0] / 30)) - 1] != 1:
                    self.board[(int(self.po[1] / 30))
                               ][(int(self.po[0] / 30)) - 1] = 2
                    self.board[(int(self.po[1] / 30)) -
                               1][(int(self.po[0] / 30)) - 1] = 0
                else:
                    self.po = self.save_po
        except:
            self.po = self.save_po
        screen.fill((0, 0, 0))  # очистка экрана
        self.render(screen)  # отрисовка поля
        self.draw_player(self.po)  # отрисовка игрока
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
        clock.tick(fps)
        pygame.display.flip()
    pygame.quit()

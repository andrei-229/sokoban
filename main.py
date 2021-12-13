import pygame # Import pygame


class Board:
    def __init__(self, width, height):
        self.left = 0  # левая граница поля
        self.top = 0  # верхняя граница поля
        self.cell_size = 30  # размер клетки

        self.width = width # ширина поля
        self.height = height # высота поля
        self.board = [[0] * width for _ in range(height)] # список списков с состояниями каждой клетки
        self.board[16][16] = 1 # Размещение одной стены первое число это по Y второе по X
        self.po = [360, 360] # координаты игрока
        self.coords = {} # словарь координат клеток
        self.bar = [] # список координат препятствий
        self.scale = pygame.image.load('animation/r1.png') # изображение игрока
        self.scale = pygame.transform.scale(self.scale, (self.cell_size, self.cell_size)) # масштабирование изображения
        self.bor = pygame.image.load('animation/wall.png')
        self.bor = pygame.transform.scale(self.bor, (self.cell_size, self.cell_size))
        # значения по умолчанию
        self.save_po = self.po  # сохранение координат игрока
    
    # отрисовка поля
    def render(self, screen):
        screen.fill((0, 0, 0)) # очистка экрана
        try: # проверка на наличие клетки в списке
            if self.board[(int(self.po[1] / 30)) - 1][(int(self.po[0] / 30)) - 1] == 1 or self.po[0] <= 0 or self.po[1] <= 0: # проверка на препятствие
                self.po = self.save_po # возвращение координат игрока
        except: # если клетки нет в списке
            self.po = self.save_po # возвращение координат игрока
        for i in range(self.height): # перебор всех строк
            for j in range(self.width): # перебор всех столбцов
                self.barier(15, 16)
                x = self.left + j * self.cell_size
                y = self.top + i * self.cell_size
                if self.board[i][j] == 0: # если клетка пустая
                    pygame.draw.rect(screen, (255, 255, 255), (x, y, self.cell_size, self.cell_size), 1, 1, 1, 1, 1, 1) # отрисовка клетки
                else: # если клетка занята стеной
                    self.bor_rect = self.bor.get_rect(bottomright=(x + self.cell_size, y + self.cell_size))
                    screen.blit(self.bor, self.bor_rect)
        pygame.display.update() # отрисовка стены
        self.draw_player(self.po) # отрисовка игрока
   
    # отрисовка игрока (Ничего не трогал, все работает по вашему коду)
    def draw_player(self, xy):
        self.man_rect = self.scale.get_rect(bottomright=(xy[0], xy[1]))
        screen.blit(self.scale, self.man_rect)
        pygame.display.update()
        self.po[0] = xy[0]
        self.po[1] = xy[1]

    def barier(self, y, x):
        self.board[y][x] = 1


    # перемещение налево
    def move_left(self):
        self.save_po = [] # сохранение координат игрока
        for i in self.po: # перебор координат игрока
            self.save_po.append(i) # добавление координат в список
        # все действия выше сделаны по причине проблемы изменения save_po при изменении po (Один и тот же id в оперативной памяти)
        self.po[0] = self.po[0] - self.cell_size # перемещение игрока на одну клетку влево
        screen.fill((0, 0, 0)) # очистка экрана
        self.render(screen) # отрисовка поля
        self.draw_player(self.po) # отрисовка игрока

    # перемещение направо
    def move_right(self):
        self.save_po = [] # сохранение координат игрока
        for i in self.po: # перебор координат игрока
            self.save_po.append(i) # добавление координат в список
        # все действия выше сделаны по причине проблемы изменения save_po при изменении po (Один и тот же id в оперативной памяти)
        self.po[0] = self.po[0] + self.cell_size # перемещение игрока на одну клетку вправо
        screen.fill((0, 0, 0)) # очистка экрана
        self.render(screen) # отрисовка поля
        self.draw_player(self.po) # отрисовка игрока

    # перемещение вверх
    def move_up(self):
        self.save_po = [] # сохранение координат игрока
        for i in self.po: # перебор координат игрока
            self.save_po.append(i) # добавление координат в список
        # все действия выше сделаны по причине проблемы изменения save_po при изменении po (Один и тот же id в оперативной памяти)
        self.po[1] = self.po[1] - self.cell_size # перемещение игрока на одну клетку вверх
        screen.fill((0, 0, 0)) # очистка экрана
        self.render(screen) # отрисовка поля
        self.draw_player(self.po) # отрисовка игрока

    # перемещение вниз
    def move_down(self):
        self.save_po = [] # сохранение координат игрока
        for i in self.po: # перебор координат игрока
            self.save_po.append(i) # добавление координат в список
        # все действия выше сделаны по причине проблемы изменения save_po при изменении po (Один и тот же id в оперативной памяти)
        self.po[1] = self.po[1] + self.cell_size # перемещение игрока на одну клетку вниз
        screen.fill((0, 0, 0)) # очистка экрана
        self.render(screen) # отрисовка поля
        self.draw_player(self.po) # отрисовка игрока


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
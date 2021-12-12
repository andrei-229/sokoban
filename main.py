import pygame


class Board:
    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.board = [[0] * width for _ in range(height)]
        self.board[16][16] = 1 # Размещение одной стены
        self.po = [360, 360] # координаты игрока
        self.coords = {}
        self.bar = []
        self.scale = pygame.image.load('animation/r1.png')
        self.scale = pygame.transform.scale(self.scale, (30, 30))
        # значения по умолчанию
        self.left = 0
        self.top = 0
        self.cell_size = 30
        self.save_po = self.po
    
    # отрисовка поля
    def render(self, screen):
        screen.fill((0, 0, 0))
        try:
            print(self.po)
            print(self.board[(int(self.po[1] / 30)) - 1][(int(self.po[0] / 30)) - 1])
            print(self.po[1] / 30)
            if self.board[(int(self.po[1] / 30)) - 1][(int(self.po[0] / 30)) - 1] == 1 or self.po[0] <= 0 or self.po[1] <= 0:
                self.po = self.save_po
        except:
            self.po = self.save_po
        for i in range(self.height):
            for j in range(self.width):
                if self.board[i][j] == 0:
                    pygame.draw.rect(screen, (255, 255, 255), (self.left + j * self.cell_size, self.top + i * self.cell_size, self.cell_size, self.cell_size), 1, 1, 1, 1, 1, 1)
                else:
                    pygame.draw.rect(screen, (255, 255, 255), (self.left + j * self.cell_size, self.top + i * self.cell_size, self.cell_size, self.cell_size))
        self.draw_player(self.po)
   
    def draw_player(self, xy):
        self.man_rect = self.scale.get_rect(bottomright=(xy[0], xy[1]))
        screen.blit(self.scale, self.man_rect)
        pygame.display.update()
        self.po[0] = xy[0]
        self.po[1] = xy[1]
        print(self.po)
        print(self.bar)
    
    def move_left(self):
        self.save_po = []
        for i in self.po:
            self.save_po.append(i)
        self.po[0] = self.po[0] - self.cell_size
        screen.fill((0, 0, 0))
        self.render(screen)
        self.draw_player(self.po)

    def move_right(self):
        self.save_po = []
        for i in self.po:
            self.save_po.append(i)
        self.po[0] = self.po[0] + self.cell_size
        screen.fill((0, 0, 0))
        self.render(screen)
        self.draw_player(self.po)

    def move_up(self):
        self.save_po = []
        for i in self.po:
            self.save_po.append(i)
        self.po[1] = self.po[1] - self.cell_size
        screen.fill((0, 0, 0))
        self.render(screen)
        self.draw_player(self.po)

    def move_down(self):
        self.save_po = []
        for i in self.po:
            self.save_po.append(i)
        self.po[1] = self.po[1] + self.cell_size
        screen.fill((0, 0, 0))
        self.render(screen)
        self.draw_player(self.po)


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
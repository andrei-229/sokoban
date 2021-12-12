import pygame
from playerTest import *


class Board:
    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.board = [[0] * width for _ in range(height)]
        self.left = 0
        self.top = 0
        self.cell_size = 30
        self.y = 0
        self.cells = []
        self.coords = {}
        self.man = pygame.image.load('animation/r1.png') # подгружаем картинку
        self.scale = pygame.transform.scale(
            self.man, (self.cell_size, self.cell_size)) # меняем размеры
        self.poloj = []
        self.po = []
        self.bar = []

    def render(self, screen):
        y = self.top
        for j in range(self.height):
            x = self.left
            for i in range(self.width):
                pygame.draw.rect(screen, 'white', ((x, y),
                                                   (self.cell_size, self.cell_size)),
                                                width=1)
                self.coords[(i, j)] = (x, y) # Добавляем координаты
                x += self.cell_size
            y += self.cell_size
            
        self.po = [self.coords[(12, 9)][0], self.coords[(12, 9)][1]]
        
        self.draw_player(self.po) # рисуем игрока на его стартовой позиции

        self.draw_barier(self.coords[(10, 10)])
        self.bar.append(self.coords[(10, 10)])

        self.draw_barier(self.coords[(11, 10)])
        self.bar.append(self.coords[(11, 10)])

        self.draw_barier(self.coords[(12, 10)])
        self.bar.append(self.coords[(12, 10)])

        self.draw_barier(self.coords[(13, 10)])
        self.bar.append(self.coords[(13, 10)])

        self.draw_barier(self.coords[(14, 9)])
        self.bar.append(self.coords[(14, 9)])

        self.draw_barier(self.coords[(14, 8)])
        self.bar.append(self.coords[(14, 8)])

        self.draw_barier(self.coords[(14, 7)])
        self.bar.append(self.coords[(14, 7)])

        
    def draw_player(self, xy):
        self.man_rect = self.scale.get_rect(bottomright=(xy[0], xy[1]))
        screen.blit(self.scale, self.man_rect)
        pygame.display.update()
        self.po[0] = xy[0]
        self.po[1] = xy[1]
    
    def coor(self):
        return self.po
        
    def draw_barier(self, xy):
        pygame.draw.rect(screen, (255, 255, 255), (xy[0], xy[1], self.cell_size, self.cell_size))
    
    def move_left(self):
        if (self.po[0], self.po[1]) not in self.bar:
            self.po[0] = self.po[0] - self.cell_size
            self.draw_player(self.po)

    def move_right(self):
        if (self.po[0], self.po[1]) not in self.bar:
            self.po[0] = self.po[0] + self.cell_size
            self.draw_player(self.po)

    def move_up(self):
        if (self.po[0], self.po[1]) not in self.bar:
            self.po[1] = self.po[0] - self.cell_size
            self.draw_player(self.po)

    def move_down(self):
        if (self.po[0], self.po[1]) not in self.bar:
            self.po[1] = self.po[1] + self.cell_size
            self.draw_player(self.po)
    
    def set_view(self, left, top, cell_size):
        self.left = left
        self.top = top
        self.cell_size = cell_size

'''
class Player(pygame.sprite.Sprite):
    def __init__(self, x, y):
        pygame.sprite.Sprite.__init__(self)
        self.walk_right = [pygame.image.load('R1.png'), pygame.image.load('R2.png'), pygame.image.load('R3.png'), pygame.image.load('R4.png'), pygame.image.load('R5.png'), pygame.image.load('R6.png'), pygame.image.load('R7.png'), pygame.image.load('R8.png'), pygame.image.load('R9.png')]
        player_image = pygame.image.load('R1.png')

    def update(self):
        pass
'''

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
    # hero = Player(12, 9)
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
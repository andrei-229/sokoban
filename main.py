import pygame


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
        
        self.draw_player(self.coords[(12, 9)])

        self.draw_barier(self.coords[(10, 10)])
        
    def draw_player(self, xy):
        pygame.draw.ellipse(screen, (255, 0, 0), (xy[0], xy[1], self.cell_size, self.cell_size))
    
    def draw_barier(self, xy):
        pygame.draw.rect(screen, (0, 0, 0), (xy[0], xy[1], self.cell_size, self.cell_size))
    
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
    screen.fill((0, 0, 0))
    clock = pygame.time.Clock()
    board = Board(26, 18)
    print(board.render(screen))
    fps = 60
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.MOUSEBUTTONDOWN:
                pass
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    pass
                if event.key == pygame.K_RIGHT:
                    walk_right = pygame.image.load('R1.png')
                if event.key == pygame.K_UP:
                    pass
                if event.key == pygame.K_DOWN:
                    pass
        
        clock.tick(fps)
        pygame.display.flip()
    pygame.quit()
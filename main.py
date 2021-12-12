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

    def render(self, screen):
        y = self.top
        for j in range(self.height):
            x = self.left
            for i in range(self.width):
                pygame.draw.rect(screen, 'white', ((x, y),
                                                   (self.cell_size, self.cell_size)),
                                 width=1)
                x += self.cell_size
            y += self.cell_size

    def set_view(self, left, top, cell_size):
        self.left = left
        self.top = top
        self.cell_size = cell_size

if __name__ == '__main__':
    pygame.init()
    width, height = 780, 540
    size = width, height
    screen = pygame.display.set_mode(size)
    board = Board(26, 18)
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
        screen.fill((0, 0, 0))
        board.render(screen)
        pygame.display.flip()
import pygame


class Board:
    # создание поля
    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.board = [[0] * width for _ in range(height)]
        # значения по умолчанию
        self.left = 10
        self.top = 10
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

    # настройка внешнего вида
    def set_view(self, left, top, cell_size):
        self.left = left
        self.top = top
        self.cell_size = cell_size

if __name__ == '__main__':
    pygame.init()
    width, height = 400, 400
    size = width, height
    screen = pygame.display.set_mode(size)
    pygame.display.set_caption('Инцилизация игры')
    board = Board(4, 3)
    board.set_view(100, 100, 50)
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
        screen.fill((0, 0, 0))
        board.render(screen)
        pygame.display.flip()
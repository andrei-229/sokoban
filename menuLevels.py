import pygame
import pygame_gui
from main import Board

class levelsM:
    def __init__(self, manager):

        self.level_1 = pygame_gui.elements.UIButton(relative_rect=pygame.Rect((100, 75), (50, 50)),
                                                    text='1',
                                                    manager=manager)

        self.level_2 = pygame_gui.elements.UIButton(relative_rect=pygame.Rect((170, 75), (50, 50)),
                                                    text='2',
                                                    manager=manager)

        self.level_3 = pygame_gui.elements.UIButton(relative_rect=pygame.Rect((240, 75), (50, 50)),
                                                    text='3',
                                                    manager=manager)

        self.level_2.disable()
        self.level_3.disable()
    
    def ret(self):
        return self.level_1

    def go(self, board):
        self.level_1.kill()
        self.level_2.kill()
        self.level_3.kill()
        board.render(screen)
        


if __name__ == '__main__':
    pygame.init()

    pygame.display.set_caption('Sokoban')
    manager = pygame_gui.UIManager((780, 540))
    screen = pygame.display.set_mode((780, 540))

    background = pygame.Surface((780, 540))
    background.fill(pygame.Color('Black'))

    clock = pygame.time.Clock()
    board = Board(screen, 26, 18)
    is_running = True

    while is_running:
        time_delta = clock.tick(60)
        manager.draw_ui(screen)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                is_running = False

            if event.type == pygame.USEREVENT:
                if event.user_type == pygame_gui.UI_BUTTON_PRESSED:
                    if event.ui_element == levelsM.ret():
                       levelsM.go(board)
                       pygame.display.flip()
                       
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    board.move_left()
                if event.key == pygame.K_RIGHT:
                    board.move_right()
                if event.key == pygame.K_UP:
                    board.move_up()
                if event.key == pygame.K_DOWN:
                    board.move_down()

            manager.process_events(event)

        manager.update(time_delta)


        pygame.display.flip()

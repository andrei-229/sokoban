import pygame
import pygame_gui
from main import Board

pygame.init()

pygame.display.set_caption('Quick Start')
screen = pygame.display.set_mode((780, 540))

background = pygame.Surface((780, 540))
background.fill(pygame.Color('Black'))

clock = pygame.time.Clock()
board = Board(screen, 26, 18)

manager = pygame_gui.UIManager((780, 540))
levels_button = pygame_gui.elements.UIButton(relative_rect=pygame.Rect((300, 275), (200, 100)),
                                             text='Levels',
                                             manager=manager)

settings_button = pygame_gui.elements.UIButton(relative_rect=pygame.Rect((300, 385), (200, 100)),
                                               text='Settings',
                                               manager=manager)

st = pygame_gui.elements.UITextBox(relative_rect=pygame.Rect((300, 115), (200, 100)),
                                   html_text='Menu',
                                   manager=manager,
                                   wrap_to_height=True)

is_running = True

screen.blit(background, (0, 0))
pygame.display.update()

while is_running:
    time_delta = clock.tick(60)
    manager.draw_ui(screen)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            is_running = False

        if event.type == pygame.USEREVENT:
            if event.user_type == pygame_gui.UI_BUTTON_PRESSED:
                if event.ui_element == levels_button:
                    board.render(screen)
                    pygame.display.flip()
                    levels_button.kill()
                    st.kill()
                    settings_button.kill()
                elif event.ui_element == settings_button:
                    print('Open settings')

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

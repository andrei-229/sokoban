import pygame
import pygame_gui

pygame.init()

pygame.display.set_caption('Quick Start')
window_surface = pygame.display.set_mode((780, 540))

background = pygame.Surface((780, 540))
background.fill(pygame.Color('Black'))

clock = pygame.time.Clock()

manager = pygame_gui.UIManager((780, 540))
levels_button = pygame_gui.elements.UIButton(relative_rect=pygame.Rect((300, 275), (200, 100)),
                                             text='Levels',
                                             manager=manager)

settings_button = pygame_gui.elements.UIButton(relative_rect=pygame.Rect((300, 385), (200, 100)),
                                               text='Settings',
                                               manager=manager)

st = pygame_gui.elements.UITextBox(relative_rect=pygame.Rect((300, 115), (200, 100)),
                                   html_text='<font size = 5>Menu</font>',
                                   manager=manager,
                                   wrap_to_height=True)

is_running = True

while is_running:
    time_delta = clock.tick(60)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            is_running = False

        if event.type == pygame.USEREVENT:
            if event.user_type == pygame_gui.UI_BUTTON_PRESSED:
                if event.ui_element == levels_button:
                    print('Open menu levels')
                elif event.ui_element == settings_button:
                    print('Open settings')

        manager.process_events(event)

    manager.update(time_delta)

    window_surface.blit(background, (0, 0))
    manager.draw_ui(window_surface)

    pygame.display.update()

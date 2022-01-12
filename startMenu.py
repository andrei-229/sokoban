import pygame
import pygame_gui

class Start:
    def __init__(self, screen):
        self.manager = pygame_gui.UIManager((780, 540))
        self.levels_button = pygame_gui.elements.UIButton(relative_rect=pygame.Rect((300, 275), (200, 100)),
                                                    text='Levels',
                                                    manager=self.manager)

        self.settings_button = pygame_gui.elements.UIButton(relative_rect=pygame.Rect((300, 385), (200, 100)),
                                                    text='Settings',
                                                    manager=self.manager)

        self.st = pygame_gui.elements.UITextBox(relative_rect=pygame.Rect((300, 115), (200, 100)),
                                        html_text='Menu',
                                        manager=self.manager,
                                        wrap_to_height=True)

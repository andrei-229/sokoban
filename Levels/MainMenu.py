import pygame

class MainMenu():
    def __init__(self, old) -> None:
        font = pygame.font.SysFont("comicsansms", 30)
        text = font.render("Sokoban", True, (255, 255, 255))
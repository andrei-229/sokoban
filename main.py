from logging import exception
import os
import shutil
import time
import tkinter
from tkinter import filedialog
import pygame  # Import pygame
import pygame_gui
from Levels.level3 import Level as Level3
from Levels.level2 import Level as Level2
from Levels.level1 import Level as Level1
import moviepy.editor
import moviepy.video.fx.all
import pypresence


class Board:
    def __init__(self, screen, width, height, level, soundS):
        self.left = 0  # левая граница поля
        self.top = 0  # верхняя граница поля
        self.cell_size = 30  # размер клетки
        self.count = 0
        self.countBox = 0
        self.nowLevel = level
        self.screen = screen
        self.soundS = soundS
        self.step = 0

        self.width = width  # ширина поля
        self.height = height  # высота поля
        # список списков с состояниями каждой клетки
        self.board = [[0] * width for _ in range(height)]
        # Размещение одной стены первое число это по Y второе по X
        self.po = [0, 0]
        # Level1(self)
        self.krest = []
        self.coor = []
        self.win = False

        # спрайты
        self.scale = pygame.image.load(
            'animation/r1.png')  # изображение игрока
        self.scale = pygame.transform.scale(
            self.scale, (self.cell_size, self.cell_size))  # масштабирование изображения
        self.leftChar = pygame.image.load(
            'animation/l1.png')  # изображение игрока
        self.leftChar = pygame.transform.scale(
            self.leftChar, (self.cell_size, self.cell_size))  # масштабирование изображения
        self.bor = pygame.image.load('animation/wall.png')
        self.bor = pygame.transform.scale(
            self.bor, (self.cell_size, self.cell_size))
        self.boxs = pygame.image.load('animation/woodBox5.jpg')
        self.boxs = pygame.transform.scale(
            self.boxs, (self.cell_size, self.cell_size))
        self.primChar = pygame.image.load(
            'animation/b1.png')  # изображение игрока
        self.primChar = pygame.transform.scale(
            self.primChar, (self.cell_size, self.cell_size))
        self.backChar = pygame.image.load(
            'animation/b2.png')  # изображение игрока
        self.backChar = pygame.transform.scale(
            self.backChar, (self.cell_size, self.cell_size))

        # значения по умолчанию
        self.save_po = self.po  # сохранение координат игрока

    # отрисовка поля
    def render(self, screen):
        screen.fill((0, 0, 0))  # очистка экрана
        if self.count == self.countBox:
            if self.nowLevel == 0:
                pygame.mixer.music.load('GameData/Music/level1.mp3')
                pygame.mixer.music.play(-1)
                pygame.mixer.music.set_volume(self.soundS)
                self.board = [[0] * self.width for _ in range(self.height)]
                # self.countBox = 3
                # self.count = 0
                Level1(self)
            elif self.nowLevel == 1:
                pygame.mixer.music.stop()
                pygame.mixer.music.load('GameData/Music/level2.mp3')
                pygame.mixer.music.play(-1)
                pygame.mixer.music.set_volume(self.soundS)
                self.board = [[0] * self.width for _ in range(self.height)]
                self.countBox = 6
                self.count = 0
                Level2(self)

            elif self.nowLevel == 2:
                pygame.mixer.music.stop()
                pygame.mixer.music.load('GameData/Music/level3.mp3')
                pygame.mixer.music.play(-1)
                self.board = [[0] * self.width for _ in range(self.height)]
                self.countBox = 5
                self.count = 0
                Level3(self)
            elif self.nowLevel == 25:
                pygame.mixer.music.stop()
                pygame.mixer.music.load('GameData/Music/level1.mp3')
                pygame.mixer.music.play(-1)
                pygame.mixer.music.set_volume(self.soundS)
                self.board = [[0] * self.width for _ in range(self.height)]
                Level4(self)
            else:
                pygame.mixer.music.stop()
                pygame.mixer.Sound.play(
                    pygame.mixer.Sound('GameData/Music/win.mp3'))

        try:  # проверка на наличие клетки в списке
            # проверка на препятствие
            if self.board[(int(self.po[1] / self.cell_size)) - 1][(int(self.po[0] / self.cell_size)) - 1] == 1 or self.po[0] <= 0 or self.po[1] <= 0:
                self.po = self.save_po  # возвращение координат игрока
        except:  # если клетки нет в списке
            self.po = self.save_po  # возвращение координат игрока
        for i in range(self.height):  # перебор всех строк
            for j in range(self.width):  # перебор всех столбцов
                x = self.left + j * self.cell_size
                y = self.top + i * self.cell_size
                if self.board[i][j] == 0:  # если клетка пустая
                    pass  # отрисовка клетки
                elif self.board[i][j] == 2:
                    self.boxs_rect = self.boxs.get_rect(
                        bottomright=(x + self.cell_size, y + self.cell_size))
                    screen.blit(self.boxs, self.boxs_rect)
                elif self.board[i][j] == 3:
                    pygame.draw.line(screen, (255, 255, 255), (x, y),
                                     (x + self.cell_size, y + self.cell_size),
                                     width=1)
                    pygame.draw.line(screen, (255, 255, 255), (x, y + self.cell_size),
                                     (x + self.cell_size, y),
                                     width=2)
                elif self.board[i][j] == 4:
                    self.boxs_rect = self.boxs.get_rect(
                        bottomright=(x + self.cell_size, y + self.cell_size))
                    screen.blit(self.boxs, (x, y))
                else:  # если клетка занята стеной
                    self.bor_rect = self.bor.get_rect(
                        bottomright=(x + self.cell_size, y + self.cell_size))
                    screen.blit(self.bor, self.bor_rect)
        self.draw_player(screen, self.po, 'primo')

    # отрисовка игрока (Ничего не трогал, все работает по вашему коду)
    def draw_player(self, screen, xy, lico):
        if lico == 'right':
            self.man_rect = self.scale.get_rect(bottomright=(xy[0], xy[1]))
            screen.blit(self.scale, self.man_rect)
            pygame.display.update()
            self.po[0] = xy[0]
            self.po[1] = xy[1]
        elif lico == 'left':
            self.man_rect = self.leftChar.get_rect(bottomright=(xy[0], xy[1]))
            screen.blit(self.leftChar, self.man_rect)
            pygame.display.update()
            self.po[0] = xy[0]
            self.po[1] = xy[1]
        elif lico == 'primo':
            self.man_rect = self.primChar.get_rect(bottomright=(xy[0], xy[1]))
            screen.blit(self.primChar, self.man_rect)
            pygame.display.update()
            self.po[0] = xy[0]
            self.po[1] = xy[1]
        elif lico == 'back':
            self.man_rect = self.backChar.get_rect(bottomright=(xy[0], xy[1]))
            screen.blit(self.backChar, self.man_rect)
            pygame.display.update()
            self.po[0] = xy[0]
            self.po[1] = xy[1]

    # перемещение налево
    def move_left(self):
        self.save_po = []  # сохранение координат игрока
        for i in self.po:  # перебор координат игрока
            self.save_po.append(i)  # добавление координат в список
        # все действия выше сделаны по причине проблемы изменения save_po при изменении po (Один и тот же id в оперативной памяти)
        # перемещение игрока на одну клетку влево
        self.po[0] = self.po[0] - self.cell_size
        # получение координат игрока по оси Х
        now_board_x = int(self.po[0] / self.cell_size)
        # получение координат игрока по оси Y
        now_board_y = int(self.po[1] / self.cell_size)
        # если игрок на клетке с коробкой или крестом
        if self.board[now_board_y - 1][now_board_x - 1] == 2 or self.board[now_board_y - 1][now_board_x - 1] == 1:
            if self.board[now_board_y - 1][now_board_x - 1] != 1:
                if self.board[(int(self.po[1] / self.cell_size)) - 1][(int(self.po[0] / self.cell_size)) - 2] == 1 or self.board[(int(self.po[1] / self.cell_size)) - 1][(int(self.po[0] / self.cell_size)) - 2] == 2 or self.board[(int(self.po[1] / self.cell_size)) - 1][(int(self.po[0] / self.cell_size)) - 2] == 4:
                    self.po = self.save_po
                # проверка на крестик
                elif self.board[(int(self.po[1] / self.cell_size)) - 1][(int(self.po[0] / self.cell_size)) - 2] == 3:
                    # перемещение на крестик
                    self.board[(int(self.po[1] / self.cell_size)) -
                               1][(int(self.po[0] / self.cell_size)) - 2] = 4
                    pygame.mixer.Sound.play(
                        pygame.mixer.Sound('GameData/Sounds/box.mp3'))
                    self.count += 1
                    if self.count == self.countBox:
                        self.win = True
                    # перемещение на пустую клетку
                    self.board[(int(self.po[1] / self.cell_size)) -
                               1][(int(self.po[0] / self.cell_size)) - 1] = 0
                elif self.board[(int(self.po[1] / self.cell_size)) - 1][(int(self.po[0] / self.cell_size)) - 2] == 4:
                    self.board[(int(self.po[1] / self.cell_size)) -
                               1][(int(self.po[0] / self.cell_size)) - 2] = 0
                    self.board[(int(self.po[1] / self.cell_size)) -
                               1][(int(self.po[0] / self.cell_size)) - 1] = 2
                    pygame.mixer.Sound.play(
                        pygame.mixer.Sound('GameData/Sounds/box.mp3'))
                else:
                    self.board[(int(self.po[1] / self.cell_size)) -
                               1][(int(self.po[0] / self.cell_size)) - 1] = 0
                    self.board[(int(self.po[1] / self.cell_size)) -
                               1][(int(self.po[0] / self.cell_size)) - 2] = 2
                    pygame.mixer.Sound.play(
                        pygame.mixer.Sound('GameData/Sounds/box.mp3'))
            else:
                self.po = self.save_po
        elif self.board[(int(self.po[1] / self.cell_size)) - 1][(int(self.po[0] / self.cell_size)) - 1] == 4:
            if self.board[(int(self.po[1] / self.cell_size)) - 1][(int(self.po[0] / self.cell_size)) - 2] != 1:
                if self.board[(int(self.po[1] / self.cell_size)) - 1][(int(self.po[0] / self.cell_size)) - 2] == 3:
                    self.board[(int(self.po[1] / self.cell_size)) -
                               1][(int(self.po[0] / self.cell_size)) - 2] = 4
                    pygame.mixer.Sound.play(
                        pygame.mixer.Sound('GameData/Sounds/box.mp3'))
                    self.board[(int(self.po[1] / self.cell_size)) -
                               1][(int(self.po[0] / self.cell_size)) - 1] = 3
                elif self.board[(int(self.po[1] / self.cell_size)) - 1][(int(self.po[0] / self.cell_size)) - 2] == 4 or self.board[(int(self.po[1] / self.cell_size)) - 1][(int(self.po[0] / self.cell_size)) - 2] == 2:
                    self.po = self.save_po
                else:
                    self.board[(int(self.po[1] / self.cell_size)) -
                               1][(int(self.po[0] / self.cell_size)) - 2] = 2
                    self.count -= 1
                    self.board[(int(self.po[1] / self.cell_size)) -
                               1][(int(self.po[0] / self.cell_size)) - 1] = 3
                    pygame.mixer.Sound.play(
                        pygame.mixer.Sound('GameData/Sounds/box.mp3'))
            else:
                self.po = self.save_po
        if self.po != self.save_po:
            pygame.mixer.Sound.play(
                pygame.mixer.Sound('GameData/Sounds/move.mp3'))
            self.step += 1
        self.screen.fill((0, 0, 0))  # очистка экрана
        self.render(self.screen)  # отрисовка поля
        self.draw_player(self.screen, self.po, 'left')  # отрисовка игрока
        pygame.display.update()
        return self.win

    # перемещение направо
    def move_right(self):
        self.save_po = []  # сохранение координат игрока
        for i in self.po:  # перебор координат игрока
            self.save_po.append(i)  # добавление координат в список
        # все действия выше сделаны по причине проблемы изменения save_po при изменении po (Один и тот же id в оперативной памяти)
        # перемещение игрока на одну клетку вправо
        self.po[0] = self.po[0] + self.cell_size
        try:
            if self.board[(int(self.po[1] / self.cell_size)) - 1][(int(self.po[0] / self.cell_size)) - 1] == 2 or self.board[(int(self.po[1] / self.cell_size)) - 1][(int(self.po[0] / self.cell_size)) - 1] == 1:
                if self.board[(int(self.po[1] / self.cell_size)) - 1][(int(self.po[0] / self.cell_size)) - 1] != 1:
                    if self.board[(int(self.po[1] / self.cell_size)) - 1][(int(self.po[0] / self.cell_size))] == 1 or self.board[(int(self.po[1] / self.cell_size)) - 1][(int(self.po[0] / self.cell_size))] == 2 or self.board[(int(self.po[1] / self.cell_size)) - 1][(int(self.po[0] / self.cell_size))] == 4:
                        self.po = self.save_po
                    elif self.board[(int(self.po[1] / self.cell_size)) - 1][(int(self.po[0] / self.cell_size))] == 3:
                        self.board[(int(self.po[1] / self.cell_size)) -
                                   1][(int(self.po[0] / self.cell_size))] = 4
                        pygame.mixer.Sound.play(
                            pygame.mixer.Sound('GameData/Sounds/box.mp3'))
                        self.count += 1
                        if self.count == self.countBox:
                            self.win = True
                        self.board[(int(self.po[1] / self.cell_size)) -
                                   1][(int(self.po[0] / self.cell_size)) - 1] = 0
                    elif self.board[(int(self.po[1] / self.cell_size)) - 1][(int(self.po[0] / self.cell_size))] == 4:
                        self.board[(int(self.po[1] / self.cell_size)) -
                                   1][(int(self.po[0] / self.cell_size))] = 0
                        self.board[(int(self.po[1] / self.cell_size)) -
                                   1][(int(self.po[0] / self.cell_size)) - 1] = 2
                        pygame.mixer.Sound.play(
                            pygame.mixer.Sound('GameData/Sounds/box.mp3'))
                    else:
                        self.board[(int(self.po[1] / self.cell_size)) -
                                   1][(int(self.po[0] / self.cell_size))] = 2
                        pygame.mixer.Sound.play(
                            pygame.mixer.Sound('GameData/Sounds/box.mp3'))
                        self.board[(int(self.po[1] / self.cell_size)) -
                                   1][(int(self.po[0] / self.cell_size)) - 1] = 0
                else:
                    self.po = self.save_po
            elif self.board[(int(self.po[1] / self.cell_size)) - 1][(int(self.po[0] / self.cell_size)) - 1] == 4:
                if self.board[(int(self.po[1] / self.cell_size)) - 1][(int(self.po[0] / self.cell_size))] != 1:
                    if self.board[(int(self.po[1] / self.cell_size)) - 1][(int(self.po[0] / self.cell_size))] == 3:
                        self.board[(int(self.po[1] / self.cell_size)) -
                                   1][(int(self.po[0] / self.cell_size))] = 4
                        pygame.mixer.Sound.play(
                            pygame.mixer.Sound('GameData/Sounds/box.mp3'))
                        self.board[(int(self.po[1] / self.cell_size)) -
                                   1][(int(self.po[0] / self.cell_size)) - 1] = 3
                    elif self.board[(int(self.po[1] / self.cell_size)) - 1][(int(self.po[0] / self.cell_size))] == 4 or self.board[(int(self.po[1] / self.cell_size)) - 1][(int(self.po[0] / self.cell_size))] == 2:
                        self.po = self.save_po
                    else:
                        self.board[(int(self.po[1] / self.cell_size)) -
                                   1][(int(self.po[0] / self.cell_size))] = 2
                        pygame.mixer.Sound.play(
                            pygame.mixer.Sound('GameData/Sounds/box.mp3'))
                        self.count -= 1
                        self.board[(int(self.po[1] / self.cell_size)) -
                                   1][(int(self.po[0] / self.cell_size)) - 1] = 3
                else:
                    self.po = self.save_po
        except:
            self.po = self.save_po
        if self.po != self.save_po:
            pygame.mixer.Sound.play(
                pygame.mixer.Sound('GameData/Sounds/move.mp3'))
            self.step += 1
        self.screen.fill((0, 0, 0))  # очистка экрана
        self.render(self.screen)  # отрисовка поля
        self.draw_player(self.screen, self.po, 'right')  # отрисовка игрока
        pygame.display.update()
        return self.win

    # перемещение вверх
    def move_up(self):
        self.save_po = []  # сохранение координат игрока
        for i in self.po:  # перебор координат игрока
            self.save_po.append(i)  # добавление координат в список
        # все действия выше сделаны по причине проблемы изменения save_po при изменении po (Один и тот же id в оперативной памяти)
        # перемещение игрока на одну клетку вверх
        self.po[1] = self.po[1] - self.cell_size
        try:
            if self.board[(int(self.po[1] / self.cell_size)) - 1][(int(self.po[0] / self.cell_size)) - 1] == 2 or self.board[(int(self.po[1] / self.cell_size)) - 1][(int(self.po[0] / self.cell_size)) - 1] == 1:  # если на клетке препятствие
                # если на клетке не препятствие
                if self.board[(int(self.po[1] / self.cell_size)) - 1][(int(self.po[0] / self.cell_size)) - 1] != 1:
                    if self.board[(int(self.po[1] / self.cell_size)) - 2][(int(self.po[0] / self.cell_size)) - 1] == 1 or self.board[(int(self.po[1] / self.cell_size)) - 2][(int(self.po[0] / self.cell_size)) - 1] == 2 or self.board[(int(self.po[1] / self.cell_size)) - 2][(int(self.po[0] / self.cell_size)) - 1] == 4:  # если на клетке препятствие
                        self.po = self.save_po
                    # если на клетке ящик
                    elif self.board[(int(self.po[1] / self.cell_size)) - 2][(int(self.po[0] / self.cell_size)) - 1] == 3:
                        # перемещение ящика на клетку вверх
                        self.board[(int(self.po[1] / self.cell_size)) -
                                   2][(int(self.po[0] / self.cell_size)) - 1] = 4
                        pygame.mixer.Sound.play(
                            pygame.mixer.Sound('GameData/Sounds/box.mp3'))
                        self.count += 1
                        if self.count == self.countBox:
                            self.win = True
                        self.board[(int(self.po[1] / self.cell_size)) - 1][(
                            int(self.po[0] / self.cell_size)) - 1] = 0  # очистка клетки
                    elif self.board[(int(self.po[1] / self.cell_size)) - 2][(int(self.po[0] / self.cell_size)) - 1] == 4:
                        self.board[(int(self.po[1] / self.cell_size)) -
                                   2][(int(self.po[0] / self.cell_size)) - 1] = 0
                        self.board[(int(self.po[1] / self.cell_size)) -
                                   1][(int(self.po[0] / self.cell_size)) - 1] = 2
                        pygame.mixer.Sound.play(
                            pygame.mixer.Sound('GameData/Sounds/box.mp3'))
                    else:
                        self.board[(int(self.po[1] / self.cell_size)) -
                                   2][(int(self.po[0] / self.cell_size)) - 1] = 2
                        pygame.mixer.Sound.play(
                            pygame.mixer.Sound('GameData/Sounds/box.mp3'))
                        self.board[(int(self.po[1] / self.cell_size)) -
                                   1][(int(self.po[0] / self.cell_size)) - 1] = 0
                else:
                    self.po = self.save_po
            elif self.board[(int(self.po[1] / self.cell_size)) - 1][(int(self.po[0] / self.cell_size)) - 1] == 4:
                if self.board[(int(self.po[1] / self.cell_size)) - 2][(int(self.po[0] / self.cell_size)) - 1] != 1:
                    if self.board[(int(self.po[1] / self.cell_size)) - 2][(int(self.po[0] / self.cell_size)) - 1] == 3:
                        self.board[(int(self.po[1] / self.cell_size)) -
                                   2][(int(self.po[0] / self.cell_size)) - 1] = 4
                        pygame.mixer.Sound.play(
                            pygame.mixer.Sound('GameData/Sounds/box.mp3'))
                        self.board[(int(self.po[1] / self.cell_size)) -
                                   1][(int(self.po[0] / self.cell_size)) - 1] = 3
                    elif self.board[(int(self.po[1] / self.cell_size)) - 2][(int(self.po[0] / self.cell_size)) - 1] == 4 or self.board[(int(self.po[1] / self.cell_size)) - 2][(int(self.po[0] / self.cell_size)) - 1] == 2:
                        self.po = self.save_po
                    else:
                        self.board[(int(self.po[1] / self.cell_size)) -
                                   2][(int(self.po[0] / self.cell_size)) - 1] = 2
                        pygame.mixer.Sound.play(
                            pygame.mixer.Sound('GameData/Sounds/box.mp3'))
                        self.count -= 1
                        self.board[(int(self.po[1] / self.cell_size)) -
                                   1][(int(self.po[0] / self.cell_size)) - 1] = 3
                else:
                    self.po = self.save_po
        except:
            if self.board[(int(self.po[1] / self.cell_size))][(int(self.po[0] / self.cell_size))] == 2:
                self.board[(int(self.po[1] / self.cell_size)) -
                           1][(int(self.po[0] / self.cell_size)) - 1] = 2
                pygame.mixer.Sound.play(
                    pygame.mixer.Sound('GameData/Sounds/box.mp3'))
                self.board[(int(self.po[1] / self.cell_size))
                           ][(int(self.po[0] / self.cell_size)) - 1] = 0
        if self.po != self.save_po:
            pygame.mixer.Sound.play(
                pygame.mixer.Sound('GameData/Sounds/move.mp3'))
            self.step += 1
        self.screen.fill((0, 0, 0))  # очистка экрана
        self.render(self.screen)  # отрисовка поля
        self.draw_player(self.screen, self.po, 'back')  # отрисовка игрока
        pygame.display.update()
        return self.win

    # перемещение вниз
    def move_down(self):
        self.save_po = []  # сохранение координат игрока
        for i in self.po:  # перебор координат игрока
            self.save_po.append(i)  # добавление координат в список
        # все действия выше сделаны по причине проблемы изменения save_po при изменении po (Один и тот же id в оперативной памяти)
        # перемещение игрока на одну клетку вниз
        self.po[1] = self.po[1] + self.cell_size
        try:
            if self.board[(int(self.po[1] / self.cell_size)) - 1][(int(self.po[0] / self.cell_size)) - 1] == 2 or self.board[(int(self.po[1] / self.cell_size)) - 1][(int(self.po[0] / self.cell_size)) - 1] == 1:
                if self.board[(int(self.po[1] / self.cell_size)) - 1][(int(self.po[0] / self.cell_size)) - 1] != 1:
                    if self.board[(int(self.po[1] / self.cell_size))][(int(self.po[0] / self.cell_size)) - 1] == 1 or self.board[(int(self.po[1] / self.cell_size))][(int(self.po[0] / self.cell_size)) - 1] == 2 or self.board[(int(self.po[1] / self.cell_size))][(int(self.po[0] / self.cell_size)) - 1] == 4:
                        self.po = self.save_po
                    elif self.board[(int(self.po[1] / self.cell_size))][(int(self.po[0] / self.cell_size)) - 1] == 3:
                        self.board[(int(self.po[1] / self.cell_size))
                                   ][(int(self.po[0] / self.cell_size)) - 1] = 4
                        pygame.mixer.Sound.play(
                            pygame.mixer.Sound('GameData/Sounds/box.mp3'))
                        self.count += 1
                        if self.count == self.countBox:
                            self.win = True
                        self.board[(int(self.po[1] / self.cell_size)) -
                                   1][(int(self.po[0] / self.cell_size)) - 1] = 0
                    elif self.board[(int(self.po[1] / self.cell_size))][(int(self.po[0] / self.cell_size)) - 1] == 4:
                        self.board[(int(self.po[1] / self.cell_size))
                                   ][(int(self.po[0] / self.cell_size)) - 1] = 0
                        self.board[(int(self.po[1] / self.cell_size)) -
                                   1][(int(self.po[0] / self.cell_size)) - 1] = 2
                        pygame.mixer.Sound.play(
                            pygame.mixer.Sound('GameData/Sounds/box.mp3'))
                    else:
                        self.board[(int(self.po[1] / self.cell_size))
                                   ][(int(self.po[0] / self.cell_size)) - 1] = 2
                        pygame.mixer.Sound.play(
                            pygame.mixer.Sound('GameData/Sounds/box.mp3'))
                        self.board[(int(self.po[1] / self.cell_size)) -
                                   1][(int(self.po[0] / self.cell_size)) - 1] = 0
                else:
                    self.po = self.save_po
            elif self.board[(int(self.po[1] / self.cell_size)) - 1][(int(self.po[0] / self.cell_size)) - 1] == 4:
                if self.board[(int(self.po[1] / self.cell_size))][(int(self.po[0] / self.cell_size)) - 1] != 1:
                    if self.board[(int(self.po[1] / self.cell_size))][(int(self.po[0] / self.cell_size)) - 1] == 3:
                        self.board[(int(self.po[1] / self.cell_size))
                                   ][(int(self.po[0] / self.cell_size)) - 1] = 4
                        pygame.mixer.Sound.play(
                            pygame.mixer.Sound('GameData/Sounds/box.mp3'))
                        self.board[(int(self.po[1] / self.cell_size)) -
                                   1][(int(self.po[0] / self.cell_size)) - 1] = 3
                    elif self.board[(int(self.po[1] / self.cell_size))][(int(self.po[0] / self.cell_size)) - 1] == 4 or self.board[(int(self.po[1] / self.cell_size))][(int(self.po[0] / self.cell_size)) - 1] == 2:
                        self.po = self.save_po
                    else:
                        self.board[(int(self.po[1] / self.cell_size))
                                   ][(int(self.po[0] / self.cell_size)) - 1] = 2
                        pygame.mixer.Sound.play(
                            pygame.mixer.Sound('GameData/Sounds/box.mp3'))
                        self.count -= 1
                        self.board[(int(self.po[1] / self.cell_size)) -
                                   1][(int(self.po[0] / self.cell_size)) - 1] = 3
                else:
                    self.po = self.save_po
        except:
            self.po = self.save_po
        if self.po != self.save_po:
            pygame.mixer.Sound.play(
                pygame.mixer.Sound('GameData/Sounds/move.mp3'))
            self.step += 1
        self.screen.fill((0, 0, 0))  # очистка экрана
        self.render(self.screen)  # отрисовка поля
        self.draw_player(self.screen, self.po, 'primo')  # отрисовка игрока
        pygame.display.update()
        return self.win


def UserFile():
    top = tkinter.Tk()
    top.withdraw()  # hide window
    file_name = filedialog.askopenfilename(
        parent=top, filetypes=[("Python files", "*.py")])
    top.destroy()
    return file_name


# всё далее я не менял, поэтому не буду писать комментарии
if __name__ == '__main__':
    pygame.init()
    width, height = 780, 540
    size = width, height
    screen = pygame.display.set_mode(size)
    screen2 = pygame.Surface(screen.get_size())
    pygame.display.set_caption("SokoBAN")
    pygame.display.set_icon(pygame.image.load('animation/logo.png'))
    manager = pygame_gui.UIManager(screen.get_size())
    screen.fill((255, 255, 255))
    clock = pygame.time.Clock()
    soundS = 0.2
    soundS2 = 0.2
    fps = 90
    try:
        client_id = '932641205727146026'
        rpc = pypresence.Presence(client_id)
        rpc.connect()
        rpc.update(state='Играет в игру',
                   large_image='logo', small_image='logo')
    except pypresence.DiscordNotFound:
        pass
    pygame.mixer.init()
    pygame.mixer.music.load('GameData/Music/music.mp3')
    pygame.mixer.music.set_volume(soundS)
    pygame.mixer.music.play(-1)
    video = moviepy.editor.VideoFileClip('animation/Authors.mp4')
    video.preview()
    # time.sleep(7)
    running = True
    run1 = True
    for_text = False
    check = False

    st2 = pygame.image.load('animation/sok.png')
    st = pygame_gui.elements.ui_image.UIImage(relative_rect=pygame.Rect((250, 20), (300, 100)),
                                              manager=manager, image_surface=st2)

    start_button = pygame_gui.elements.UIButton(relative_rect=pygame.Rect((300, 150), (200, 100)),
                                                text='Старт',
                                                manager=manager)

    levels_button = pygame_gui.elements.UIButton(relative_rect=pygame.Rect((300, 270), (200, 100)),
                                                 text='Уровни',
                                                 manager=manager)

    settings_button = pygame_gui.elements.UIButton(relative_rect=pygame.Rect((300, 385), (200, 100)),
                                                   text='Настройки',
                                                   manager=manager)

    lk = False
    ld = False
    ll = False
    r2 = ''
    count2 = 0
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

            if check:
                r2 = False
                board.win = False
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_LEFT:
                        r2 = board.move_left()
                    if event.key == pygame.K_RIGHT:
                        r2 = board.move_right()
                    if event.key == pygame.K_UP:
                        r2 = board.move_up()
                    if event.key == pygame.K_DOWN:
                        r2 = board.move_down()
                    if event.key == pygame.K_r:
                        board.board = [[0] * width for _ in range(height)]
                        board.count = board.countBox = 0
                        board.nowLevel -= 1
                        board.render(screen)
                    if event.key == pygame.K_ESCAPE:
                        screen.fill((0, 0, 0))
                        ld = True
                        check = False
                        run1 = True
                        continueB = pygame_gui.elements.UIButton(relative_rect=pygame.Rect((300, 150), (200, 100)),
                                                                 text='Продолжить',
                                                                 manager=manager)

                        gMenu = pygame_gui.elements.UIButton(relative_rect=pygame.Rect((300, 270), (200, 100)),
                                                             text='Главное меню',
                                                             manager=manager)
                    if r2:
                        check = False
                        run1 = True
                        ll = True
                        screen.fill((0, 0, 0))
                        print(board.step)
                        nextB = pygame_gui.elements.UIButton(relative_rect=pygame.Rect((300, 150), (200, 100)),
                                                             text='Продолжить',
                                                             manager=manager)

                        gMenu2 = pygame_gui.elements.UIButton(relative_rect=pygame.Rect((300, 270), (200, 100)),
                                                              text='Главное меню',
                                                              manager=manager)
                        count2 += 1
            if event.type == pygame.USEREVENT:
                if event.user_type == pygame_gui.UI_BUTTON_PRESSED:
                    if event.ui_element == start_button:
                        count2 = 0
                        check = True
                        run1 = False
                        screen.fill((0, 0, 0))
                        board = Board(screen, 26, 18, 0, soundS)
                        pygame.mixer.music.stop()
                        pygame.mixer.Sound.play(pygame.mixer.Sound(
                            'GameData/Music/levelopen.mp3'))
                        f = pygame.font.Font(None, 30)
                        text = f.render('Загрузка...', True, (255, 255, 255))
                        screen.blit(text, (650, 500))
                        pygame.display.flip()
                        time.sleep(2)
                        board.render(screen)
                        start_button.kill()
                        settings_button.kill()
                        levels_button.kill()
                        st.kill()
                    elif event.ui_element == levels_button:
                        lk = True
                        start_button.kill()
                        settings_button.kill()
                        levels_button.kill()
                        st.kill()
                        pygame.mixer.Sound.play(
                            pygame.mixer.Sound('GameData/Music/Levels.mp3'))
                        for_text = True
                        first_level = pygame_gui.elements.UIButton(relative_rect=pygame.Rect((35, 270), (220, 50)),
                                                                   text='1',
                                                                   manager=manager)

                        second_level = pygame_gui.elements.UIButton(relative_rect=pygame.Rect((275, 270), (220, 50)),
                                                                    text='2',
                                                                    manager=manager)

                        third_level = pygame_gui.elements.UIButton(relative_rect=pygame.Rect((515, 270), (220, 50)),
                                                                   text='3',
                                                                   manager=manager)

                        custom_level = pygame_gui.elements.UIButton(relative_rect=pygame.Rect((275, 370), (220, 50)),
                                                                    text='Custom',
                                                                    manager=manager)

                        escapeB = pygame_gui.elements.UIButton(relative_rect=pygame.Rect((10, 10), (50, 50)),
                                                               text='<-',
                                                               manager=manager)
                    elif event.ui_element == settings_button:
                        print(1)
                    if lk:
                        if event.ui_element == first_level:
                            count2 = 0
                            pygame.mixer.Sound.play(pygame.mixer.Sound(
                                'GameData/Music/levelopen.mp3'))
                            pygame.mixer.music.stop()
                            check = True
                            run1 = False
                            for_text = False
                            screen.fill((0, 0, 0))
                            board = Board(screen, 26, 18, 0, soundS)
                            f = pygame.font.Font(None, 30)
                            text = f.render(
                                'Загрузка...', True, (255, 255, 255))
                            screen.blit(text, (650, 500))
                            pygame.display.flip()
                            time.sleep(2)
                            board.render(screen)
                            if r2:
                                print(2)
                            first_level.kill()
                            second_level.kill()
                            third_level.kill()
                            escapeB.kill()
                            custom_level.kill()
                            # fade(780, 540)
                        elif event.ui_element == custom_level:
                            f = UserFile()
                            if f:
                                try:
                                    shutil.copy(f, 'Levels/level4.py')
                                    from Levels.level4 import Level as Level4
                                    pygame.mixer.Sound.play(pygame.mixer.Sound(
                                        'GameData/Music/levelopen.mp3'))
                                    pygame.mixer.music.stop()
                                    check = True
                                    run1 = False
                                    for_text = False
                                    screen.fill((0, 0, 0))
                                    board = Board(screen, 26, 18, 25, soundS)
                                    f = pygame.font.Font(None, 30)
                                    text = f.render(
                                        'Загрузка...', True, (255, 255, 255))
                                    screen.blit(text, (650, 500))
                                    pygame.display.flip()
                                    time.sleep(2)
                                    board.render(screen)
                                    first_level.kill()
                                    second_level.kill()
                                    third_level.kill()
                                    escapeB.kill()
                                    custom_level.kill()
                                except Exception:
                                    pass

                        elif event.ui_element == second_level:
                            count2 = 1
                            pygame.mixer.Sound.play(pygame.mixer.Sound(
                                'GameData/Music/levelopen.mp3'))
                            pygame.mixer.music.stop()
                            check = True
                            run1 = False
                            for_text = False
                            screen.fill((0, 0, 0))
                            board = Board(screen, 26, 18, 1, soundS)
                            f = pygame.font.Font(None, 30)
                            text = f.render(
                                'Загрузка...', True, (255, 255, 255))
                            screen.blit(text, (650, 500))
                            pygame.display.flip()
                            time.sleep(2)
                            board.render(screen)
                            first_level.kill()
                            second_level.kill()
                            third_level.kill()
                            escapeB.kill()
                            custom_level.kill()
                        elif event.ui_element == third_level:
                            count2 = 2
                            pygame.mixer.Sound.play(pygame.mixer.Sound(
                                'GameData/Music/levelopen.mp3'))
                            pygame.mixer.music.stop()
                            check = True
                            run1 = False
                            for_text = False
                            screen.fill((0, 0, 0))
                            board = Board(screen, 26, 18, 2, soundS)
                            f = pygame.font.Font(None, 30)
                            text = f.render(
                                'Загрузка...', True, (255, 255, 255))
                            screen.blit(text, (650, 500))
                            pygame.display.flip()
                            time.sleep(2)
                            board.render(screen)
                            first_level.kill()
                            second_level.kill()
                            third_level.kill()
                            escapeB.kill()
                            custom_level.kill()
                        elif event.ui_element == escapeB:
                            first_level.kill()
                            second_level.kill()
                            third_level.kill()
                            escapeB.kill()
                            custom_level.kill()
                            for_text = False
                            st = pygame_gui.elements.ui_image.UIImage(relative_rect=pygame.Rect((250, 20), (300, 100)),
                                                                      manager=manager, image_surface=st2)

                            start_button = pygame_gui.elements.UIButton(relative_rect=pygame.Rect((300, 150), (200, 100)),
                                                                        text='Старт',
                                                                        manager=manager)

                            levels_button = pygame_gui.elements.UIButton(relative_rect=pygame.Rect((300, 270), (200, 100)),
                                                                         text='Уровни',
                                                                         manager=manager)

                            settings_button = pygame_gui.elements.UIButton(relative_rect=pygame.Rect((300, 385), (200, 100)),
                                                                           text='Настройки',
                                                                           manager=manager)
                    if ll:
                        if event.ui_element == nextB:
                            f = pygame.font.Font(None, 30)
                            nextB.kill()
                            gMenu2.kill()
                            screen.fill((0, 0, 0))
                            text = f.render(
                                'Загрузка...', True, (255, 255, 255))
                            screen.blit(text, (650, 500))
                            pygame.display.flip()
                            time.sleep(2)
                            board = Board(screen, 26, 18, count2, soundS)
                            board.render(screen)
                            lk = board.win = False
                            ll = False
                            check = True
                            run1 = False
                        elif event.ui_element == gMenu2:
                            pygame.mixer.music.stop()
                            pygame.mixer.music.load('GameData/Music/music.mp3')
                            pygame.mixer.music.play(-1)
                            st = pygame_gui.elements.ui_image.UIImage(relative_rect=pygame.Rect((250, 20), (300, 100)),
                                                                      manager=manager, image_surface=st2)

                            start_button = pygame_gui.elements.UIButton(relative_rect=pygame.Rect((300, 150), (200, 100)),
                                                                        text='Старт',
                                                                        manager=manager)

                            levels_button = pygame_gui.elements.UIButton(relative_rect=pygame.Rect((300, 270), (200, 100)),
                                                                         text='Уровни',
                                                                         manager=manager)

                            settings_button = pygame_gui.elements.UIButton(relative_rect=pygame.Rect((300, 385), (200, 100)),
                                                                           text='Настройки',
                                                                           manager=manager)
                            nextB.kill()
                            gMenu2.kill()
                            lk = board.win = False
                            ll = False

                    if ld:
                        if event.ui_element == gMenu:
                            pygame.mixer.music.stop()
                            pygame.mixer.music.load('GameData/Music/music.mp3')
                            pygame.mixer.music.play(-1)
                            st = pygame_gui.elements.ui_image.UIImage(relative_rect=pygame.Rect((250, 20), (300, 100)),
                                                                      manager=manager, image_surface=st2)

                            start_button = pygame_gui.elements.UIButton(relative_rect=pygame.Rect((300, 150), (200, 100)),
                                                                        text='Старт',
                                                                        manager=manager)

                            levels_button = pygame_gui.elements.UIButton(relative_rect=pygame.Rect((300, 270), (200, 100)),
                                                                         text='Уровни',
                                                                         manager=manager)

                            settings_button = pygame_gui.elements.UIButton(relative_rect=pygame.Rect((300, 385), (200, 100)),
                                                                           text='Настройки',
                                                                           manager=manager)
                            continueB.kill()
                            gMenu.kill()
                            ld = False
                        elif event.ui_element == continueB:
                            board.render(screen)
                            continueB.kill()
                            gMenu.kill()
                            ld = False
                            check = True
                            run1 = False
            manager.process_events(event)
        if run1:
            manager.update(clock.tick(60))
            screen.blit(screen2, (0, 0))
            manager.draw_ui(screen)
        if for_text:
            f = pygame.font.Font(None, 50)
            text = f.render('Выберите уровень:', True, (255, 255, 255))
            screen.blit(text, (225, 20))
        clock.tick(fps)
        pygame.display.flip()
    try:
        rpc.close()
    except Exception:
        pass
    pygame.quit()

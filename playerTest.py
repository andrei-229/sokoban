from pygame import *
import pyganim
import os

MOVE_SPEED = 7
WIDTH = 22
HEIGHT = 32
COLOR =  "#888888"
ANIMATION_DELAY = 0.1 # скорость смены кадров
ICON_DIR = os.path.dirname(__file__) #  Полный путь к каталогу с файлами

ANIMATION_RIGHT = [('%s/animation/r1.png' % ICON_DIR)]
ANIMATION_LEFT = [('%s/animation/l1.png' % ICON_DIR), # !!!
            ('%s/animation/l2.png' % ICON_DIR),
            ('%s/animation/l3.png' % ICON_DIR),
            ('%s/animation/l4.png' % ICON_DIR),
            ('%s/animation/l5.png' % ICON_DIR)]
ANIMATION_DOWN = [('%s/animation/d1.png' % ICON_DIR), # !!!
            ('%s/animation/d2.png' % ICON_DIR),
            ('%s/animation/d3.png' % ICON_DIR),
            ('%s/animation/d4.png' % ICON_DIR),
            ('%s/animation/d5.png' % ICON_DIR)]
ANIMATION_UP = [('%s/animation/u1.png' % ICON_DIR), # !!!
            ('%s/animation/u2.png' % ICON_DIR),
            ('%s/animation/u3.png' % ICON_DIR),
            ('%s/animation/u4.png' % ICON_DIR),
            ('%s/animation/u5.png' % ICON_DIR)]
ANIMATION_STAND = [('%s/animation/s1.png' % ICON_DIR)]
ANIMATION_STAY = [('%s/animation/0.png' % ICON_DIR, 0.1)] # !!!

class Player(sprite.Sprite):
    def __init__(self, x, y):
        sprite.Sprite.__init__(self)
        self.xvel = 0   #скорость перемещения. 0 - стоять на месте
        self.startX = x # Начальная позиция Х, пригодится когда будем переигрывать уровень
        self.startY = y
        self.image = Surface((WIDTH,HEIGHT))
        self.image.fill(Color(COLOR))
        self.rect = Rect(x, y, WIDTH, HEIGHT) # прямоугольный объект
        self.image.set_colorkey(Color(COLOR)) # делаем фон прозрачным
#        Анимация движения вправо
        boltAnim = []
        for anim in ANIMATION_RIGHT:
            boltAnim.append((anim, ANIMATION_DELAY))
        self.boltAnimRight = pyganim.PygAnimation(boltAnim)
        self.boltAnimRight.play()
#        Анимация движения влево        
        boltAnim = []
        for anim in ANIMATION_LEFT:
            boltAnim.append((anim, ANIMATION_DELAY))
        self.boltAnimLeft = pyganim.PygAnimation(boltAnim)
        self.boltAnimLeft.play()
        
        self.boltAnimStay = pyganim.PygAnimation(ANIMATION_STAY)
        self.boltAnimStay.play()
        self.boltAnimStay.blit(self.image, (0, 0)) # По-умолчанию, стоим

        self.boltAnimUp = pyganim.PygAnimation(ANIMATION_UP)
        self.boltAnimUp.play()

        self.boltAnimDown = pyganim.PygAnimation(ANIMATION_DOWN)
        self.boltAnimDown.play()
        

    def update(self, left, right, up, platforms):
        if up:
            self.image.fill(Color(COLOR))
            self.boltAnimUp.blit(self.image, (0, 0))
            self.yvel = -MOVE_SPEED # если нажата клавиша вверх, то движение вверх
        if left:
            self.image.fill(Color(COLOR))
            self.boltAnimLeft.blit(self.image, (0, 0))
            self.xvel = -MOVE_SPEED # если нажата клавиша влево, то движение влево
        if right:
            self.image.fill(Color(COLOR))
            self.boltAnimRight.blit(self.image, (0, 0))
            self.xvel = MOVE_SPEED # если нажата клавиша вправо, то движение вправо
        if not(left or right): # стоим, когда нет указаний идти
            self.xvel = 0
        self.rect.y += self.yvel
        self.collide(0, self.yvel, platforms)
        self.rect.x += self.xvel # переносим свои положение на xvel
        self.collide(self.xvel, 0, platforms)
    def collide(self, xvel, yvel, platforms):
        for p in platforms:
            if sprite.collide_rect(self, p): # если есть пересечение платформы с игроком
                if xvel > 0:                      # если движется вправо
                    self.rect.right = p.rect.left # то не движется вправо
                if xvel < 0:                      # если движется влево
                    self.rect.left = p.rect.right # то не движется влево
                if yvel > 0:                      # если спускается
                    self.rect.bottom = p.rect.top # то не спускается
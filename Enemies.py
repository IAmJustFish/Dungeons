import pygame
import os
from settings import *


def load_image(name, colorkey=-1):
    fullname = os.path.join('data', *name)
    # если файл не существует, то выходим
    if not os.path.isfile(fullname):
        print(f"Файл с изображением '{fullname}' не найден")
        exit('main.py')
    image = pygame.image.load(fullname)
    if colorkey is not None:
        image = image.convert()
        if colorkey == -1:
            colorkey = image.get_at((0, 0))
        image.set_colorkey(colorkey)
    else:
        image = image.convert_alpha()
    return image


class Monster(pygame.sprite.Sprite):
    def __init__(self, groups, lvl, pos):
        super().__init__(*groups)
        self.image = load_image(('data', 'sprites', 'monsters', '0', 'monster.png'))
        self.rect = self.image.get_rect()
        self.rect.center = pos
        self.settings = {'lvl': lvl}

    def update(self):
        pass

    @property
    def is_live(self):
        return True

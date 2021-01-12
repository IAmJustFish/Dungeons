import pygame
import math
import os
from settings import *
from Bullets import Bullet


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


class Gun(pygame.sprite.Sprite):
    def __init__(self, name, groups, all_sprites, player=None):
        super().__init__(groups['weapon'])
        self.groups = groups
        self.player = player
        self.turn = player.turn
        self.all_sprites = all_sprites

        # import settings
        with open(f'data/guns/{name}/specifications.txt') as sp:
            file = sp.read().split('\n')
            self.specifications = {}
            for string in file:
                kv = string.split(' = ')
                self.specifications[kv[0]] = float(kv[1])

        self.r_im = load_image(('guns', name, 'skin_r.png'))
        self.l_im = load_image(('guns', name, 'skin_l.png'))
        self.image = self.r_im
        self.rect = self.image.get_rect()
        self.rect.center = self.player.rect.center
        self.time = 1

    def fire(self):
        if self.time % self.specifications['speed'] == 0:
            self.time = 1
            dx = (self.player.x // BULLETS_SPEED + 10 * math.cos(self.player.angle) - self.player.x)\
                 * self.specifications['bullet_speed'] // BULLETS_SPEED
            dy = (self.player.y // BULLETS_SPEED + 10 * math.sin(self.player.angle) - self.player.y)\
                 * self.specifications['bullet_speed'] // BULLETS_SPEED
            bullet = Bullet(self.groups, self.rect.center, (dx, dy)
                            , self.specifications['damage'], self.turn, self.all_sprites, self.player.bullet_name)

    def update(self):
        if self.rect.x <= HALF_WIDTH:
            self.image = self.l_im
        else:
            self.image = self.r_im
        self.rect.center = self.player.rect.center[0], self.player.rect[1] + 30
        if self.time % self.specifications['speed'] != 0:
            self.time += 1

    def get_player(self, player):
        self.player = player

    def dead(self):
        self.kill()

    def move(self, dx, dy):
        self.rect.x += dx
        self.rect.y += dy

    def can_fire(self):
        return self.time % self.specifications['speed'] == 0

    def hit(self, *args, **kwarks):
        return False

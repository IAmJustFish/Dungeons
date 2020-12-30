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


class Bullet(pygame.sprite.Sprite):
    def __init__(self, groups, pos, vec, damage, turn, all_sprites):
        super().__init__(groups['bullet'])
        self.image = load_image(('sprites', 'bullets', 'bullet.png'), colorkey=-1)
        self.rect = self.image.get_rect()
        self.x, self.y, self.dx, self.dy = pos[0], pos[1], vec[0], vec[1]
        self.rect.center = pos
        self.damage = damage
        self.turn = turn
        self.all_sprites = all_sprites

    def update(self):
        self.rect = self.rect.move(self.dx, self.dy)
        self.is_died()

    def is_died(self):
        collisions = list()
        for sprite in self.all_sprites:
            collision = self.rect.colliderect(sprite.rect)
            if collision:
                collisions.append(collision)
        kill_self = False
        if collisions:
            for sprite in collisions:
                died = self.all_sprites.sprites()[sprite].hit(self.turn, self.damage)
                if died:
                    kill_self = True
            if kill_self:
                self.kill()

    def move(self, dx, dy):
        self.rect.x += dx
        self.rect.y += dy

    def hit(self, *args, **kwarks):
        return False

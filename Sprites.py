import pygame
from settings import *


class Wall(pygame.sprite.Sprite):
    def __init__(self, x, y, images, key, groups):
        super().__init__(*groups)
        self.image = pygame.transform.scale(images[key], (TILE, TILE + SHADOW_TEXTURE_H // TEXTURE_SCALE))
        self.rect = self.image.get_rect().move(x, y)


class Floor(pygame.sprite.Sprite):
    def __init__(self, x, y, images, groups):
        super().__init__(*groups)
        self.image = pygame.transform.scale(images['floor'], (TILE, TILE))
        self.rect = self.image.get_rect().move(x, y)


class Camera:
    def __init__(self, target):
        self.t = target
        self.dx = 0
        self.dy = 0

    def apply(self, sprites):
        for obj in sprites:
            if str(type(obj))[8:-2] == 'player.Player':
                obj.x += self.dx
                obj.y += self.dy
            else:
                obj.rect.x += self.dx
                obj.rect.y += self.dy

    def update(self):
        self.dx = self.t.rect.center[0] - HALF_WIDTH
        self.dy = self.t.rect.center[1] - HALF_HEIGHT

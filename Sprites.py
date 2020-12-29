import pygame
from settings import *


class Wall(pygame.sprite.Sprite):
    def __init__(self, x, y, images, key, groups):
        super().__init__(*groups)
        self.image = pygame.transform.scale(images[key], (TILE, TILE + SHADOW_TEXTURE_H // TEXTURE_SCALE))
        self.rect = self.image.get_rect().move(x, y)
        self.w_rect = self.image.get_rect().move(x, y)

    def move(self, dx, dy):
        self.rect.x += dx
        self.rect.y += dy

    def hit(self, *args, **kwarks):
        return True


class Floor(pygame.sprite.Sprite):
    def __init__(self, x, y, images, groups):
        super().__init__(*groups)
        self.image = pygame.transform.scale(images['floor'], (TILE, TILE))
        self.rect = self.image.get_rect().move(x, y)

    def move(self, dx, dy):
        self.rect.x += dx
        self.rect.y += dy

    def hit(self, *args, **kwarks):
        return False


class Camera:
    def __init__(self, target):
        self.target = target
        self.dx = 0
        self.dy = 0

    def apply(self, sprites):
        for obj in sprites:
            obj.move(self.dx, self.dy)

    def update(self):
        x2, y2 = self.target.rect.x, self.target.rect.y
        x1, y1 = HALF_WIDTH, HALF_HEIGHT
        self.dx = -(x2 - x1)
        self.dy = -(y2 - y1)

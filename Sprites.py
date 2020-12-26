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

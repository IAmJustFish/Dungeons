import pygame
import math
from settings import *
from map import world_map, text_map


class Player:
    def __init__(self):
        self.x, self.y = player_pos
        self.angle = player_angle

    @property
    def pos(self):
        return (self.x, self.y)

    def is_empty(self, x, y):
        xt, yt = int(x // TILE * TILE), int(y // TILE * TILE)
        return not (xt, yt) in list(world_map.keys())

    def movement(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_w]:
            yn = self.y - player_speed
            if self.is_empty(self.x, yn):
                self.y = yn
        if keys[pygame.K_s]:
            yn = self.y + player_speed
            if self.is_empty(self.x, yn):
                self.y = yn
        if keys[pygame.K_a]:
            xn = self.x - player_speed
            if self.is_empty(xn, self.y):
                self.x = xn
        if keys[pygame.K_d]:
            xn = self.x + player_speed
            if self.is_empty(xn, self.y):
                self.x = xn
        if keys[pygame.K_LEFT]:
            self.angle -= 0.03
        if keys[pygame.K_RIGHT]:
            self.angle += 0.03
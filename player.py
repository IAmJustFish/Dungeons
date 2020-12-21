import pygame
import math
from settings import *
from map import text_map


class Player:
    def __init__(self):
        self.x, self.y = player_pos
        self.angle = player_angle

    @property
    def pos(self):
        return (self.x, self.y)
    
    def is_empty(self, x, y):
        xt, yt = int(x // TILE), int(y // TILE)
        return not text_map[yt][xt] == "W"

    def movement(self):
        sin_a = math.sin(self.angle)
        cos_a = math.cos(self.angle)
        keys = pygame.key.get_pressed()
        if keys[pygame.K_w]:
            xn = self.x + player_speed * cos_a
            yn = self.y + player_speed * sin_a
            if self.is_empty(xn, yn):
                self.x = xn
                self.y = yn
        if keys[pygame.K_s]:
            xn = self.x + -player_speed * cos_a
            yn = self.y + -player_speed * sin_a
            if self.is_empty(xn, yn):
                self.x = xn
                self.y = yn
        if keys[pygame.K_a]:
            xn = self.x + player_speed * sin_a
            yn = self.y + -player_speed * cos_a
            if self.is_empty(xn, yn):
                self.x = xn
                self.y = yn
        if keys[pygame.K_d]:
            xn = self.x + -player_speed * sin_a
            yn = self.y + player_speed * cos_a
            if self.is_empty(xn, yn):
                self.x = xn
                self.y = yn
        if keys[pygame.K_LEFT]:
            self.angle -= 0.03
        if keys[pygame.K_RIGHT]:
            self.angle += 0.03

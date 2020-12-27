import pygame
import math
from settings import *
from map import walls_collision


class Player(pygame.sprite.Sprite):
    def __init__(self, *groups, im):
        super().__init__(groups)
        self.x, self.y = player_pos
        self.angle = player_angle
        self.sensitivity = 0.004
        self.image = im
        self.rect = pygame.rect.Rect(self.x, self.y, self.image.get_width(), self.image.get_width())
        self.rect.center = player_pos

    @property
    def pos(self):
        return (self.x, self.y)

    def is_empty(self, dx, dy):
        next_rect = self.rect.move(dx, dy)
        hit_indexes = next_rect.collidelistall(walls_collision)

        if len(hit_indexes):
            delta_x, delta_y = 0, 0
            for hit_index in hit_indexes:
                hit_rect = walls_collision[hit_index]
                if dx > 0:
                    delta_x += next_rect.right - hit_rect.left
                else:
                    delta_x += hit_rect.right - next_rect.left
                if dy > 0:
                    delta_y += next_rect.bottom - hit_rect.top
                else:
                    delta_y += hit_rect.bottom - next_rect.top

            if abs(delta_x - delta_y) < 10:
                dx, dy = 0, 0
            elif delta_x > delta_y:
                dy = 0
            elif delta_y > delta_x:
                dx = 0
        self.x += dx
        self.y += dy

    def movement(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_w]:
            yn = self.y - player_speed
            self.is_empty(0, -player_speed)
        if keys[pygame.K_s]:
            yn = self.y + player_speed
            self.is_empty(0, player_speed)
        if keys[pygame.K_a]:
            xn = self.x - player_speed
            self.is_empty(-player_speed, 0)
        if keys[pygame.K_d]:
            xn = self.x + player_speed
            self.is_empty(player_speed, 0)
        if keys[pygame.K_LEFT]:
            self.angle -= 0.03
        if keys[pygame.K_RIGHT]:
            self.angle += 0.03

        self.rect.center = self.x, self.y
        
        if pygame.mouse.get_focused():
            x2, y2 = pygame.mouse.get_pos()
            x1, y1 = self.x, self.y
            h = y2 - y1
            w = x2 - x1
            t = math.atan2(h, w)
            self.angle = t

    def update(self):
        self.movement()

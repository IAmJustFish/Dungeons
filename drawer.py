import pygame
import os
from settings import *
from map import *


class Drawer:
    def __init__(self, screen, player):
        self.screen = screen
        self.player = player

    def draw_all(self, sprites, FPS=-1):
        self.screen.fill(DARKGRAY)

        self.draw_world(sprites)

        if DRAW_MINI_MAP:
            self.draw_mini_map()

        if FPS >= 0 and SHOW_FPS:
            self.draw_FPS(FPS)

        if SHOW_CROSSHAIR:
            self.draw_crosshair()

    def draw_world(self, sprites):
        sprites['floor'].draw(self.screen)

        sprites_group = self.get_group(sprites)
        sprites_group.draw(self.screen)

    def get_group(self, sprites):
        sprites_group = pygame.sprite.Group()
        player_y = sprites['player'].sprites()[0].pos[1] // TILE * TILE
        for wall in sprites['walls']:
            if player_y == wall.rect.y:
                sprites_group.add(sprites['player'].sprites()[0])
            sprites_group.add(wall)
        return sprites_group

    def draw_FPS(self, FPS):
        f1 = pygame.font.Font(None, 50)
        text1 = f1.render(str(int(FPS)), True,
                          (180, 0, 0))
        self.screen.blit(text1, (50, 50))

    def draw_mini_map(self):

        mini_map = pygame.Surface((MINI_MAP_WIDTH * MINI_MAP_SCALE / 100 * TILE,
                                   MINI_MAP_HEIGHT * MINI_MAP_SCALE / 100 * TILE))
        mini_map.fill(WHITE)

        pygame.draw.line(mini_map, LIGHT_BLUE, (int(self.player.x / MINI_MAP_SCALE), int(self.player.y / MINI_MAP_SCALE)),
                         (self.player.x // MINI_MAP_SCALE + 10 * math.cos(self.player.angle),
                          self.player.y // MINI_MAP_SCALE + 10 * math.sin(self.player.angle)), 2)
        pygame.draw.circle(mini_map, DARK_BLUE,
                           (int(self.player.rect.x / MINI_MAP_SCALE), int(self.player.rect.y / MINI_MAP_SCALE)), 3)

        for x, y in world_map:
            if world_map[(x, y)] == 'W1':
                c = BLUE
            elif world_map[(x, y)] == 'W2':
                c = CYAN
            else:
                c = WHITE
            pygame.draw.rect(mini_map, c,
                             (x // MINI_MAP_SCALE, y // MINI_MAP_SCALE,
                              TILE // MINI_MAP_SCALE, TILE // MINI_MAP_SCALE), 0)

        self.screen.blit(mini_map, (WIDTH - MINI_MAP_WIDTH * MINI_MAP_SCALE / 100 * TILE, 0))

    def draw_crosshair(self):
        pass

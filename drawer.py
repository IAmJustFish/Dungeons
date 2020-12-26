import pygame
import os
from settings import *
from map import *


class Drawer:
    def __init__(self, screen, player):
        self.textures = {'W1': pygame.image.load(os.path.join('data', 'W1.png')).convert_alpha(),
                         'W2': pygame.image.load(os.path.join('data', 'W2.jpg')).convert_alpha(),
                         'floor': 'None',
                         'sky': pygame.image.load(os.path.join('data', 'sky2.jpg')).convert_alpha()}
        self.screen = screen
        self.player = player

    def draw_all(self, sprites, FPS=-1):
        self.screen.fill(DARKGRAY)

        self.draw_world(sprites)

        self.draw_player()

        if DRAW_MINI_MAP:
            self.draw_mini_map()

        if FPS >= 0 and SHOW_FPS:
            self.draw_FPS(FPS)

        if SHOW_CROSSHAIR:
            self.draw_crosshair()

    def draw_world(self, sprites):
        sprites['floor'].draw(self.screen)
        sprites['walls'].draw(self.screen)

    def draw_player(self):
        pygame.draw.circle(self.screen, YELLOW, (self.player.pos), 5, 0)

    def draw_FPS(self, FPS):
        f1 = pygame.font.Font(None, 50)
        text1 = f1.render(str(int(FPS)), True,
                          (180, 0, 0))
        self.screen.blit(text1, (50, 50))

    def draw_mini_map(self):

        mini_map = pygame.Surface((MINI_MAP_WIDTH * MINI_MAP_SCALE, MINI_MAP_HEIGHT * MINI_MAP_SCALE))
        mini_map.fill(DARKGRAY)

        pygame.draw.line(mini_map, GREEN, (int(self.player.x / MINI_MAP_SCALE), int(self.player.y / MINI_MAP_SCALE)),
                         (self.player.x // MINI_MAP_SCALE + 10 * math.cos(self.player.angle),
                          self.player.y // MINI_MAP_SCALE + 10 * math.sin(self.player.angle)), 2)

        pygame.draw.circle(mini_map, YELLOW,
                           (int(self.player.x / MINI_MAP_SCALE), int(self.player.y / MINI_MAP_SCALE)), 12 // 3)

        for x, y in world_map:
            if world_map[(x, y)] == 'W1':
                c = NEFRIT
            elif world_map[(x, y)] == 'W2':
                c = BROWN
            else:
                c = WHITE
            pygame.draw.rect(mini_map, c,
                             (x // MINI_MAP_SCALE, y // MINI_MAP_SCALE,
                              TILE // MINI_MAP_SCALE, TILE // MINI_MAP_SCALE), 0)

        self.screen.blit(mini_map, (WIDTH - MINI_MAP_WIDTH * MINI_MAP_SCALE, 0))

    def draw_crosshair(self):
        pass

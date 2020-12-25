import pygame
import os
from settings import *
from map import *


class Drawer:
    def __init__(self):
        self.textures = {'W1': pygame.image.load(os.path.join('data', 'W1.png')).convert_alpha(),
                         'W2': pygame.image.load(os.path.join('data', 'W2.jpg')).convert_alpha(),
                         'floor': 'None',
                         'sky': pygame.image.load(os.path.join('data', 'sky2.jpg')).convert_alpha()}

    def draw_all(self, screen, player, sprites, FPS=-1):
        screen.fill(DARKGRAY)

        self.draw_world(screen, sprites)

        self.draw_player(screen, player)

        if DRAW_MINI_MAP:
            self.draw_mini_map(screen, player)

        if FPS >= 0 and SHOW_FPS:
            self.draw_FPS(screen, FPS)

        if SHOW_CROSSHAIR:
            self.draw_crosshair(screen)

    def draw_world(self, screen, sprites):
        sprites['floor'].draw(screen)
        sprites['walls'].draw(screen)

    def draw_player(self, screen, player):
        pygame.draw.circle(screen, YELLOW, (player.pos), 5, 0)

    def draw_FPS(self, screen, FPS):
        f1 = pygame.font.Font(None, 50)
        text1 = f1.render(str(int(FPS)), True,
                          (180, 0, 0))
        screen.blit(text1, (50, 50))

    def draw_mini_map(self, screen, player):

        mini_map = pygame.Surface((MINI_MAP_WIDTH * MINI_MAP_SCALE, MINI_MAP_HEIGHT * MINI_MAP_SCALE))
        mini_map.fill(DARKGRAY)

        pygame.draw.line(mini_map, GREEN, (int(player.x / MINI_MAP_SCALE), int(player.y / MINI_MAP_SCALE)),
                         (player.x // MINI_MAP_SCALE + 10 * math.cos(player.angle),
                          player.y // MINI_MAP_SCALE + 10 * math.sin(player.angle)), 2)

        pygame.draw.circle(mini_map, YELLOW,
                           (int(player.x / MINI_MAP_SCALE), int(player.y / MINI_MAP_SCALE)), 12 // 3)

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

        screen.blit(mini_map, (WIDTH - MINI_MAP_WIDTH * MINI_MAP_SCALE, 0))

    def draw_crosshair(self, screen):
        pass

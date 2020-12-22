import pygame
import os
from settings import *
from map import *
from ray_casting import ray_casting


class Drawer:
    def __init__(self):
        self.textures = {'W1': pygame.image.load(os.path.join('data', 'W1.png')).convert_alpha(),
                         'floor': 'None'}

    def draw_all(self, screen, player, FPS=-1):
        screen.fill(BLACK)
        self.draw_ground_and_sky(screen)
        ray_casting(screen, player.pos, player.angle, self.textures)
        if DRAW_MINI_MAP:
            self.draw_mini_map(screen, player)
        if FPS >= 0 and SHOW_FPS:
            self.draw_FPS(screen, FPS)
        if SHOW_CROSSHAIR:
            self.draw_crosshair(screen)

    def draw_FPS(self, screen, FPS):
        f1 = pygame.font.Font(None, 50)
        text1 = f1.render(str(int(FPS)), True,
                          (180, 0, 0))
        screen.blit(text1, (50, 50))

    def draw_mini_map(self, screen, player):
        mini_map = pygame.Surface((WIDTH // MINI_MAP_SCALE, HEIGHT // MINI_MAP_SCALE))
        mini_map.fill(DARKGRAY)

        pygame.draw.line(mini_map, GREEN, (int(player.x / MINI_MAP_SCALE), int(player.y/ MINI_MAP_SCALE)),
                         (player.x // MINI_MAP_SCALE + 10 * math.cos(player.angle),
                          player.y // MINI_MAP_SCALE + 10 * math.sin(player.angle)), 2)

        pygame.draw.circle(mini_map, YELLOW,
                           (int(player.x / MINI_MAP_SCALE), int(player.y / MINI_MAP_SCALE)), 12 // 3)

        for x, y in world_map:
            if world_map[(x, y)] == 'W1':
                c = NEFRIT
            else:
                c = WHITE
            pygame.draw.rect(mini_map, c,
                             (x // MINI_MAP_SCALE, y // MINI_MAP_SCALE,
                              TILE // MINI_MAP_SCALE, TILE // MINI_MAP_SCALE), 0)

        screen.blit(mini_map, (WIDTH - WIDTH / MINI_MAP_SCALE, 0))

    def draw_ground_and_sky(self, screen):
        pygame.draw.rect(screen, BLACK, (0, 0, WIDTH, HALF_HEIGHT))
        pygame.draw.rect(screen, DARKGRAY, (0, HALF_HEIGHT, WIDTH, HALF_HEIGHT))

    def draw_crosshair(self, screen):
        pygame.draw.circle(screen, GREEN, (HALF_WIDTH, HALF_HEIGHT), 4)

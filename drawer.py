import pygame
from settings import *
from map import *
from ray_casting import ray_casting


class Drawer:
    def __init__(self):
        pass

    def draw_all(self, screen, player, FPS=-1):
        screen.fill(BLACK)
        self.draw_ground_and_sky(screen)
        ray_casting(screen, player.pos, player.angle)
        if DRAW_MINI_MAP:
            self.draw_mini_map(screen, player)
        if FPS >= 0:
            self.draw_FPS(screen, FPS)

    def draw_FPS(self, screen, FPS):
        f1 = pygame.font.Font(None, 50)
        text1 = f1.render(str(int(FPS)), True,
                          (180, 0, 0))
        screen.blit(text1, (50, 50))

    def draw_mini_map(self, screen, player):
        pygame.draw.circle(screen, GREEN, (int(player.x), int(player.y)), 12)
        pygame.draw.line(screen, GREEN, player.pos,
                         (player.x + WIDTH * math.cos(player.angle), player.y + WIDTH * math.sin(player.angle)), 2)
        for x, y in world_map:
            pygame.draw.rect(screen, DARKGRAY, (x, y, TILE, TILE), 2)

    def draw_ground_and_sky(self, screen):
        pygame.draw.rect(screen, BLACK, (0, 0, WIDTH, HALF_HEIGHT))
        pygame.draw.rect(screen, DARKGRAY, (0, HALF_HEIGHT, WIDTH, HALF_HEIGHT))

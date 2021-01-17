import pygame
import os
from settings import *
from map import *


class Drawer:
    def __init__(self, screen, player):
        self.screen = screen
        self.player = player

    def draw_all(self, sprites, FPS=-1, pause=False):
        self.screen.fill(DARKGRAY)

        self.draw_world(sprites)

        if DRAW_MINI_MAP:
            self.draw_mini_map()

        if FPS >= 0 and SHOW_FPS:
            self.draw_FPS(FPS)

        if DRAW_CROSSHAIR:
            pygame.mouse.set_visible(False)
            self.draw_crosshair(pygame.mouse.get_pos())
        else:
            pygame.mouse.set_visible(True)

        if DRAW_HUD:
            self.draw_hud(pause)

    def draw_world(self, sprites):
        sprites['floor'].draw(self.screen)

        all_sprites = self.get_group(sprites)
        sprites_group = pygame.sprite.Group()
        for sprite in all_sprites:
            sprites_group.add(sprite)
        sprites_group.draw(self.screen)
        sprites_group.empty()
        sprites['weapon'].draw(self.screen)
        sprites['bullet'].draw(self.screen)

    def get_group(self, sprites):
        walls = sprites['walls'].sprites()
        player = sprites['player'].sprites()
        enemies = sprites['enemy'].sprites()
        all = walls + player + enemies
        all = sorted(all, key=lambda sprite: sprite.rect.y)
        return all

    def draw_FPS(self, FPS):
        f1 = pygame.font.Font(None, 50)
        text1 = f1.render(str(int(FPS)), True,
                          (180, 0, 0))
        self.screen.blit(text1, (50, 50))

    def draw_mini_map(self):

        mini_map = pygame.Surface((MINI_MAP_WIDTH * MINI_MAP_SCALE / 100 * TILE,
                                   MINI_MAP_HEIGHT * MINI_MAP_SCALE / 100 * TILE))
        mini_map.fill(WHITE)

        pygame.draw.line(mini_map, LIGHT_BLUE,
                         (int(self.player.x / MINI_MAP_SCALE), int(self.player.y / MINI_MAP_SCALE)),
                         (self.player.x // MINI_MAP_SCALE + 10 * math.cos(self.player.angle),
                          self.player.y // MINI_MAP_SCALE + 10 * math.sin(self.player.angle)), 2)
        pygame.draw.circle(mini_map, DARK_BLUE,
                           (int(self.player.x / MINI_MAP_SCALE), int(self.player.y / MINI_MAP_SCALE)), 3)

        for x, y in world_map:
            if world_map[(x, y)] == 'W1':
                c = LIGHT_BLUE
            elif world_map[(x, y)] == 'W2':
                c = BLUE
            else:
                c = WHITE
            pygame.draw.rect(mini_map, c,
                             (x // MINI_MAP_SCALE, y // MINI_MAP_SCALE,
                              TILE // MINI_MAP_SCALE, TILE // MINI_MAP_SCALE), 0)

        self.screen.blit(mini_map, (WIDTH - MINI_MAP_WIDTH * MINI_MAP_SCALE / 100 * TILE, 0))

    def draw_crosshair(self, pos):
        x, y = pos
        pygame.draw.line(self.screen, BLACK, (x - CROSSHAIR_SIZE, y),
                         (x + CROSSHAIR_SIZE, y), 1)
        pygame.draw.line(self.screen, BLACK, (x, y - CROSSHAIR_SIZE),
                         (x, y + CROSSHAIR_SIZE), 1)

    def draw_hud(self, pause):
        c = RED
        delta_c = (c[0] - c[0] * 0.1) // self.player.m_lives
        delta = LIVES_WIDTH // self.player.m_lives
        for x in range(self.player.m_lives):
            if self.player.lives > x:
                c = RED
                pygame.draw.rect(self.screen, c, (x * delta, 1, delta, LIVES_HEIGHT - 1), 0)
            else:
                c = BLACK
                pygame.draw.rect(self.screen, c, (x * delta, 1, delta, LIVES_HEIGHT - 1), 0)
        for x in range(self.player.m_lives):
            c = BLACK
            pygame.draw.line(self.screen, c, (x * delta, 0), ((x + 0) * delta, LIVES_HEIGHT), 1)
        pygame.draw.rect(self.screen, BLACK,
                         (0, 0, self.player.m_lives * delta, LIVES_HEIGHT), 1)

        if pause:
            pygame.draw.rect(self.screen, GRAY, (HALF_WIDTH - 30, HALF_HEIGHT - 60, 20, 60))
            pygame.draw.rect(self.screen, GRAY, (HALF_WIDTH + 10, HALF_HEIGHT - 60, 20, 60))

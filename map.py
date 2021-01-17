import pygame
from settings import *

all_images = {}
text_map = list()
MINI_MAP_HEIGHT, MINI_MAP_WIDTH = 0, 0
world_map = dict()
walls_collision = list()


def get_images(images):
    all_images = images


def set_level(level):
    global all_images, text_map, MINI_MAP_HEIGHT, MINI_MAP_WIDTH, world_map, walls_collision
    with open(f'data/level/{level}.txt') as f:
        read = [text_map.append(i.split()) for i in f.read().split('\n')]

    # end settings
    MINI_MAP_HEIGHT, MINI_MAP_WIDTH = len(text_map), len(text_map[0])

    world_map.clear()
    walls_collision.clear()
    for j, row in enumerate(text_map):
        for i, char in enumerate(row):
            if char != '..':
                if char == 'W1':
                    walls_collision.append(pygame.rect.Rect(i * TILE, j * TILE, TILE, TILE))
                    world_map[(i * TILE, j * TILE)] = 'W1'
                if char == 'W2':
                    walls_collision.append(pygame.rect.Rect(i * TILE, j * TILE, TILE, TILE))
                    world_map[(i * TILE, j * TILE)] = 'W2'

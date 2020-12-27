import pygame
from settings import *

all_images = {}


def get_images(images):
    all_images = images


text_map = [
    'W2 W2 W2 W2 W2 W2 W2 W2 W2 W2 W2 W2 W2 W2 W2 W2 W2 W2 W2 W2 W2 W2 W2 W2 W2 W2 W2 W2 W2 W2 W2 W2 W2 W2 W2 W2',
    'W2 .. .. .. .. .. .. .. .. W1 .. .. .. .. .. .. .. .. .. .. .. .. .. .. .. .. .. .. .. .. .. .. .. .. .. W2',
    'W2 .. .. .. .. W1 .. .. .. W1 .. .. .. .. .. .. .. .. .. .. .. .. .. .. .. W1 W1 .. .. .. .. .. .. .. .. W2',
    'W2 W2 W2 W2 .. .. .. W2 .. .. .. .. .. .. .. .. W2 W2 .. .. .. .. .. .. .. W1 W1 .. .. .. .. .. .. .. .. W2',
    'W2 .. .. .. W2 .. .. W2 .. .. .. .. .. .. .. .. .. .. .. .. .. .. .. .. .. .. .. .. .. .. .. .. .. .. .. W2',
    'W2 .. .. .. W2 .. .. W2 W2 W2 .. .. .. .. .. .. .. .. .. .. .. .. .. .. .. .. .. .. .. .. .. .. .. .. .. W2',
    'W2 .. .. .. W2 .. .. .. .. W2 .. .. .. .. .. .. .. .. .. .. .. .. .. .. .. .. .. .. .. .. .. .. .. .. .. W2',
    'W2 .. .. .. .. .. .. .. .. W1 .. .. .. .. .. .. .. .. .. .. .. .. .. .. .. .. .. .. .. .. .. .. .. .. .. W2',
    'W2 .. .. .. .. .. .. .. .. W1 .. .. .. .. .. .. .. .. .. .. .. .. .. .. .. .. .. .. .. .. .. .. .. .. .. W2',
    'W2 .. .. .. .. .. .. .. .. W1 .. .. .. .. .. .. .. .. .. W1 W1 W1 .. .. .. .. .. .. .. .. .. .. .. .. .. W2',
    'W2 .. .. .. .. .. .. .. .. W1 .. .. .. .. .. .. .. .. .. .. .. .. .. .. .. .. .. .. .. .. .. .. .. .. .. W2',
    'W2 .. .. .. .. .. .. .. .. W1 .. .. .. .. .. .. .. .. .. .. .. .. .. .. .. .. .. .. .. .. .. .. .. .. .. W2',
    'W2 .. .. .. .. .. .. .. .. W1 .. .. .. .. .. .. .. .. .. .. .. .. .. .. .. .. .. .. .. .. .. .. .. .. .. W2',
    'W2 .. .. .. .. .. .. .. .. W1 .. .. .. .. .. .. .. .. .. .. .. .. .. .. .. .. .. .. .. .. .. .. .. .. .. W2',
    'W2 W2 W2 W2 W2 W2 W2 W2 W2 W2 W2 W2 W2 W2 W2 W2 W2 W2 W2 W2 W2 W2 W2 W2 W2 W2 W2 W2 W2 W2 W2 W2 W2 W2 W2 W2'
]
text_map = [i.split() for i in text_map]

# end settings
MINI_MAP_HEIGHT, MINI_MAP_WIDTH = len(text_map), len(text_map[0])

world_map = dict()
walls_collision = list()
for j, row in enumerate(text_map):
    for i, char in enumerate(row):
        if char != '..':
            if char == 'W1':
                walls_collision.append(pygame.rect.Rect(i * TILE, j * TILE, TILE, TILE))
                world_map[(i * TILE, j * TILE)] = 'W1'
            if char == 'W2':
                walls_collision.append(pygame.rect.Rect(i * TILE, j * TILE, TILE, TILE))
                world_map[(i * TILE, j * TILE)] = 'W2'

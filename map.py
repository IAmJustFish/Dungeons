import pygame
from settings import *

all_images = {}


def get_images(images):
    all_images = images


text_map = list()
with open('data/level/0.txt') as f:
    read = [text_map.append(i.split()) for i in f.read().split('\n')]

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

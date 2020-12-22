from settings import *

text_map = [
    'W1 W1 W1 W1 W1 W1 W1 W1 W1 W1 W1 W1',
    'W1 W1 .. .. .. .. .. .. .. .. .. W1',
    'W1 .. .. .. .. W1 .. .. .. .. .. W1',
    'W1 .. .. .. .. .. .. .. .. .. .. W1',
    'W1 .. .. .. W1 .. .. W1 .. .. .. W1',
    'W1 .. .. .. W1 .. .. .. W1 .. .. W1',
    'W1 W1 .. .. W1 .. .. .. .. W1 .. W1',
    'W1 W1 W1 W1 W1 W1 W1 W1 W1 W1 W1 W1'
]
text_map = [i.split() for i in text_map]

world_map = {}
for j, row in enumerate(text_map):
    for i, char in enumerate(row):
        if char != '.':
            if char == 'W1':
                world_map[(i * TILE, j * TILE)] = 'W1'

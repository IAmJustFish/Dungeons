import pygame
import Enemies
from settings import *
import random
from map import *


class Room:
    def __init__(self, lvl, groups, cells=None):
        if cells is None:
            cells = []
        self.lvl = lvl
        self.groups = groups
        self.monsters = list()

        # cells from text_map
        self.cells = cells

    def add_cell(self, cell):
        self.cells.append(cell)

    def spawn_monsters(self, *args, **kwarks):
        count = self.lvl // 3 + 1
        for _ in range(count):
            self.spawn_monster(*args, **kwarks)

    def spawn_monster(self, *args, **kwarks):
        pos = random.randint(0, len(self.cells[0]) - 1), random.randint(0, len(self.cells) - 1)
        if self.cells[pos[1]][pos[0]] == '__':
            pos = [i * TILE for i in pos]
            self.monsters.append(Enemies.Virus(*args, **kwarks, pos=pos, lvl=self.lvl))
        else:
            self.spawn_monster(*args, **kwarks)

    def is_clear(self):
        if self.monsters:
            for sprite in self.monsters:
                if sprite.is_live:
                    return False
            return True
        else:
            return False

    def set_cells(self, map=-1):
        if map == -1:
            self.level = random.randint(0, LEVELS - 1)
        else:
            self.level = map
        set_level(self.level)
        self.cells = text_map

    @property
    def get_monsters(self):
        return self.monsters

import pygame
from Enemies import Monster
from settings import *


class Room:
    def __init__(self, doors, lvl, groups, cells=None):
        if cells is None:
            cells = []
        self.doors = doors
        self.lvl = lvl
        self.groups = groups
        self.monsters = list()

        # cells from text_map
        self.cells = cells

    def add_cell(self, cell):
        self.cells.append(cell)

    def spawn_monsters(self):
        pass
        # count = self.lvl // 3 + 1
        # pos = 500, 500
        # for _ in range(count):
        #     self.monsters.append(Monster(self.groups, lvl=self.lvl, pos=pos))

    def is_clear(self):
        if self.monsters:
            for sprite in self.monsters:
                if not sprite.is_live:
                    return False
            return True
        else:
            return False

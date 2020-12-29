import pygame
from settings import *


class Room:
    def __init__(self, doors, lvl, cells=None):
        if cells is None:
            cells = []
        self.doors = doors
        self.lvl = lvl
        self.cells = cells

    def add_cell(self, cell):
        self.cells.append(cell)


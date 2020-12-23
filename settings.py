import math


# resolution
WIDTH = 1280
HEIGHT = 720
HALF_WIDTH = WIDTH // 2
HALF_HEIGHT = HEIGHT // 2

# game
TILE = 100
SHOW_FPS = False
SHOW_CROSSHAIR = True
DRAW_MINI_MAP = True
MINI_MAP_SCALE = 5
MINI_MAP_POS = WIDTH - WIDTH / MINI_MAP_SCALE, 0

# colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (220, 0, 0)
GREEN = (0, 220, 0)
BLUE = (0, 0, 255)
DARKGRAY = (40, 40, 40)
PURPLE = (120, 0, 120)
YELLOW = (250, 250, 0)
NEFRIT = (0, 168, 107)

# player settings
player_pos = (250, 250)
player_angle = 0
player_speed = 2

# ray casting settings
FOV = math.pi / 3
HALF_FOV = FOV / 2
NUM_RAYS = 400
MAX_DEPTH = 800
DELTA_ANGLE = FOV / NUM_RAYS
DIST = NUM_RAYS / (2 * math.tan(HALF_FOV))
PROJ_COEFF = 3 * DIST * TILE
SCALE = WIDTH // NUM_RAYS

# texture
TEXTURE_W = 506
TEXTURE_H = 506
TEXTURE_SCALE = TEXTURE_W // TILE

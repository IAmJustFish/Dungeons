import math


# resolution
WIDTH = 1540
HEIGHT = 865
HALF_WIDTH = WIDTH // 2
HALF_HEIGHT = HEIGHT // 2

# buttons settings
PLAY_BTN_WIDTH = 200
PLAY_BTN_HEIGHT = 100
SOUND_BTN_WIDTH = 50
SOUND_BTN_HEIGHT = 50

# game
TILE = 50
SHOW_FPS = True
DRAW_CROSSHAIR = True
CROSSHAIR_SIZE = 4
DRAW_HUD = True
LIVES_WIDTH = 200
LIVES_HEIGHT = 25
DRAW_MINI_MAP = True
MINI_MAP_SCALE = 10
MINI_MAP_POS = WIDTH - WIDTH / MINI_MAP_SCALE, 0
BULLETS_SPEED = 1
LEVELS = 3

# colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (220, 0, 0)
GREEN = (0, 220, 0)
BLUE = (0, 11, 252)
DARKGRAY = (40, 40, 40)
GRAY = (128, 128, 128)
PURPLE = (120, 0, 120)
YELLOW = (250, 250, 0)
NEFRIT = (0, 168, 107)
BROWN = (135, 75, 15)
CYAN = (31, 204, 255)
DARK_BLUE = (11, 0, 140)
LIGHT_BLUE = (105, 180, 255)

# player settings
player_angle = 45
player_speed = 2
player_lives = 15

# texture
TEXTURE_W = 506
TEXTURE_H = 506
SHADOW_TEXTURE_H = 250
SHADOW_TEXTURE_W = 506
TEXTURE_SCALE = TEXTURE_W // TILE

# enemies
enemie_speed = 2

# music
music = dict()
play_music = 1

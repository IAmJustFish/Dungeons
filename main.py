import pygame
import pygame_gui
import os
from settings import *
from player import Player
from map import *
from Sprites import Wall, Floor
from drawer import Drawer


def load_image(name, colorkey=None):
    fullname = os.path.join('data', *name)
    # если файл не существует, то выходим
    if not os.path.isfile(fullname):
        print(f"Файл с изображением '{fullname}' не найден")
        exit('main.py')
    image = pygame.image.load(fullname)
    if colorkey is not None:
        image = image.convert()
        if colorkey == -1:
            colorkey = image.get_at((0, 0))
        image.set_colorkey(colorkey)
    else:
        image = image.convert_alpha()
    return image


def do_3d(img_name, w, h, s_w, s_h):
    sc = pygame.Surface((w, h + s_h))
    sc2 = pygame.Surface((s_w, s_h))
    sc2.set_alpha(100)
    c = pygame.Color((0, 0, 0, 100))
    pygame.draw.rect(sc2, c, (0, 0, s_w, s_h), 0)
    image2 = load_image(img_name)
    sc.blit(image2, (0, 0))
    sc.blit(sc2, (0, h))
    pygame.transform.scale(sc, (TEXTURE_W, TEXTURE_H + SHADOW_TEXTURE_H))
    return sc


if __name__ == "__main__":
    pygame.init()

    pygame.display.set_caption('Dungeon menu')
    menu_surface = pygame.display.set_mode((WIDTH, HEIGHT))
    background = pygame.Surface(((WIDTH, HEIGHT)))
    background.fill(BLACK)
    pygame.draw.line(background, (128, 128, 128), (0, 100), (WIDTH, 100), 150)
    pygame.draw.line(background, (128, 128, 128), (400, 100), (500, HEIGHT), 150)
    pygame.draw.line(background, (128, 128, 128), (900, 100), (800, HEIGHT), 150)
    main = pygame_gui.UIManager((WIDTH, HEIGHT), "theme.json")

    play_button = pygame_gui.elements.UIButton(relative_rect=pygame.Rect((409, 278), (487, 134)), text="Start",
                                               manager=main)
    sound_button = pygame_gui.elements.UIButton(relative_rect=pygame.Rect((1050, 600), (230, 110)), text="",
                                                manager=main)
    settings_button = pygame_gui.elements.UIButton(relative_rect=pygame.Rect((1, 600), (230, 110)), text="settings",
                                                   manager=main)

    clock = pygame.time.Clock()
    running = True
    game_running = False

    while running:
        time_delta = clock.tick(144) / 1000
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.USEREVENT:
                if event.user_type == pygame_gui.UI_BUTTON_PRESSED:
                    if event.ui_element == play_button:
                        running = False
                        game_running = True
                    if event.ui_element == sound_button:
                        pass
                    if event.ui_element == settings_button:
                        pass

            main.process_events(event)

        main.update(time_delta)

        menu_surface.blit(background, (0, 0))
        main.draw_ui(menu_surface)

        pygame.display.update()
        clock.tick(100)

    if game_running:
        #init window
        pygame.display.set_caption('Dungeon game')
        game_surface = pygame.display.set_mode((WIDTH, HEIGHT))

        # init classes
        player_sprite = pygame.sprite.Group()
        wall_sprites = pygame.sprite.Group()
        floor_sprites = pygame.sprite.Group()
        all_sprites = pygame.sprite.Group()
        player = Player(player_sprite, all_sprites, im=load_image(('sprites', 'player', 'r_0.png'), colorkey=-1))
        drawer = Drawer(game_surface, player)
        images = dict()
        images['W1'] = load_image(('ice_2.png', ))
        images['W2'] = load_image(('ice.png', ))
        images['floor'] = load_image(('ice_floor.png', ))

        #do sprites
        sprites = {
            'player': player_sprite,
            'walls': wall_sprites,
            'floor': floor_sprites,
            'all': all_sprites
        }
        for (x, y), key in world_map.items():
            wall = Wall(x, y, images, key, (wall_sprites, all_sprites))
        for j, row in enumerate(text_map):
            for i in range(len(row)):
                x, y = i * TILE, j * TILE + TILE / 2
                floor = Floor(x, y, images, (floor_sprites, all_sprites))

        print(wall_sprites.sprites()[5].rect)

        while game_running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    exit()
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE:
                        exit()
            all_sprites.update()

            drawer.draw_all(sprites, FPS=clock.get_fps())

            pygame.display.flip()
            clock.tick(100)

pygame.quit()

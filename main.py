import pygame
import pygame_gui
import os
from settings import *
from player import Player
from Enemies import Virus
from Sprites import Wall, Floor, Camera
from map import *
from drawer import Drawer
from Rooms import Room


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


def start_game():
    game_unpaused = 1

    # init classes
    player_sprite = pygame.sprite.Group()
    wall_sprites = pygame.sprite.Group()
    floor_sprites = pygame.sprite.Group()
    all_sprites = pygame.sprite.Group()
    weapon_sprites = pygame.sprite.Group()
    bullet_sprites = pygame.sprite.Group()
    enemy_sprites = pygame.sprite.Group()
    collision_sprites = pygame.sprite.Group()

    groups_for_weapon = {'bullet': (bullet_sprites, all_sprites),
                         'weapon': (weapon_sprites, all_sprites)}

    images = dict()
    images['W1'] = load_image(('image', 'ice_2.png'))
    images['W2'] = load_image(('image', 'ice.png'))
    images['floor'] = load_image(('image', 'ice_floor.png'))

    sprites = {
        'player': player_sprite,
        'walls': wall_sprites,
        'floor': floor_sprites,
        'weapon': weapon_sprites,
        'bullet': bullet_sprites,
        'enemy': enemy_sprites,
        'all': all_sprites
    }

    virus = {
        'name': 'virus',
        'R': 6,
        'L': 6,
        'F': 4
    }

    room = Room(lvl, (enemy_sprites, all_sprites,))
    room.set_cells()
    room.spawn_monsters(all_sprites, enemy_sprites, collision_sprites, monster_type=virus,
                        weapon=('virus_sphere', groups_for_weapon), collisions=collision_sprites)

    for (x, y), key in world_map.items():
        wall = Wall(x, y, images, key, (wall_sprites, all_sprites, collision_sprites))
    for j, row in enumerate(text_map):
        for i in range(len(row)):
            x, y = i * TILE, j * TILE + TILE / 2
            floor = Floor(x, y, images, (floor_sprites, all_sprites))
            if row[i] == 'pl':
                player = Player(player_sprite, all_sprites, collision_sprites,
                                imr=[load_image(('sprites', 'player', 'R', f'{i}.png'), colorkey=-1) for i in
                                     range(7)],
                                iml=[load_image(('sprites', 'player', 'L', f'{i}.png'), colorkey=-1) for i in
                                     range(7)],
                                weapon=('mp5', groups_for_weapon), all_sprites=collision_sprites,
                                player_pos=(x + TILE / 2, y), collisions=collision_sprites)
            elif row[i] == 'e1':
                VM = Virus(all_sprites, enemy_sprites, collision_sprites, lvl=1, monster_type=virus,
                           pos=(x + TILE / 2, y), weapon=('virus_sphere', groups_for_weapon),
                           collisions=collision_sprites)

    drawer = Drawer(game_surface, player, lvl=lvl)
    camera = Camera(player)
    return camera, drawer, player, sprites, room, virus, groups_for_weapon, \
           player_sprite, wall_sprites, floor_sprites, all_sprites, weapon_sprites, \
           bullet_sprites, enemy_sprites, collision_sprites


if __name__ == "__main__":
    pygame.init()
    pygame.mixer.init()

    music['p_f'] = pygame.mixer.Sound(os.path.join('data', 'music', 'player', '0.mp3'))
    music['p_f'].set_volume(0.05)
    music['v_f'] = pygame.mixer.Sound(os.path.join('data', 'music', 'monster', '0.mp3'))
    music['v_f'].set_volume(0.05)
    music['fon'] = pygame.mixer.Sound(os.path.join('data', 'music', 'fon', '0.ogg'))
    pygame.mixer.music.load(os.path.join('data', 'music', 'fon', '0.ogg'))
    pygame.mixer.music.set_volume(0.1)
    pygame.mixer.music.play(loops=-1)

    pygame.display.set_caption('Dungeon menu')
    menu_surface = pygame.display.set_mode((WIDTH, HEIGHT))
    background = pygame.Surface(((WIDTH, HEIGHT)))
    main = pygame_gui.UIManager((WIDTH, HEIGHT), "theme.json")

    play_button = pygame_gui.elements.UIButton(relative_rect=pygame.Rect((HALF_WIDTH - PLAY_BTN_WIDTH // 2,
                                                                          HALF_HEIGHT - PLAY_BTN_HEIGHT // 2),
                                                                         (PLAY_BTN_WIDTH, PLAY_BTN_HEIGHT)),
                                               text="Start",
                                               manager=main)
    sound_button = pygame_gui.elements.UIButton(relative_rect=pygame.Rect((WIDTH - SOUND_BTN_WIDTH,
                                                                           HEIGHT - SOUND_BTN_HEIGHT),
                                                                          (SOUND_BTN_WIDTH, SOUND_BTN_HEIGHT)),
                                                text="sound",
                                                manager=main)

    clock = pygame.time.Clock()
    running = True
    game_running = False

    background = load_image(('image', 'background.png'))

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
                        play_music += 1
                        play_music %= 2
                        if play_music:
                            pygame.mixer.music.play(loops=-1)
                        else:
                            pygame.mixer.music.stop()


            main.process_events(event)

        main.update(time_delta)

        menu_surface.blit(background, (0, 0))
        main.draw_ui(menu_surface)

        pygame.display.update()
        clock.tick(144)

    if game_running:
        #init window
        pygame.display.set_caption('Dungeon game')
        game_surface = pygame.display.set_mode((WIDTH, HEIGHT))

        game_unpaused = 1, 'pause'

        # init classes
        player_sprite = pygame.sprite.Group()
        wall_sprites = pygame.sprite.Group()
        floor_sprites = pygame.sprite.Group()
        all_sprites = pygame.sprite.Group()
        weapon_sprites = pygame.sprite.Group()
        bullet_sprites = pygame.sprite.Group()
        enemy_sprites = pygame.sprite.Group()
        collision_sprites = pygame.sprite.Group()

        groups_for_weapon = {'bullet': (bullet_sprites, all_sprites),
                             'weapon': (weapon_sprites, all_sprites)}

        images = dict()
        images['W1'] = load_image(('image', 'ice_2.png'))
        images['W2'] = load_image(('image', 'ice.png'))
        images['floor'] = load_image(('image', 'ice_floor.png'))

        sprites = {
            'player': player_sprite,
            'walls': wall_sprites,
            'floor': floor_sprites,
            'weapon': weapon_sprites,
            'bullet': bullet_sprites,
            'enemy': enemy_sprites,
            'all': all_sprites
        }

        virus = {
            'name': 'virus',
            'R': 6,
            'L': 6,
            'F': 4
        }

        room = Room(1, (enemy_sprites, all_sprites,))
        room.set_cells()
        room.spawn_monsters(all_sprites, enemy_sprites, collision_sprites, monster_type=virus,
                            weapon=('virus_sphere', groups_for_weapon), collisions=collision_sprites)

        for (x, y), key in world_map.items():
            wall = Wall(x, y, images, key, (wall_sprites, all_sprites, collision_sprites))
        for j, row in enumerate(text_map):
            for i in range(len(row)):
                x, y = i * TILE, j * TILE + TILE / 2
                floor = Floor(x, y, images, (floor_sprites, all_sprites))
                if row[i] == 'pl':
                    player = Player(player_sprite, all_sprites, collision_sprites,
                                    imr=[load_image(('sprites', 'player', 'R', f'{i}.png'), colorkey=-1) for i in
                                         range(7)],
                                    iml=[load_image(('sprites', 'player', 'L', f'{i}.png'), colorkey=-1) for i in
                                         range(7)],
                                    weapon=('mp5', groups_for_weapon), all_sprites=collision_sprites,
                                    player_pos=(x + TILE / 2, y), collisions=collision_sprites)
                elif row[i] == 'e1':
                    VM = Virus(all_sprites, enemy_sprites, collision_sprites, lvl=1, monster_type=virus,
                               pos=(x + TILE / 2, y), weapon=('virus_sphere', groups_for_weapon),
                               collisions=collision_sprites)

        lvl = 1

        drawer = Drawer(game_surface, player, lvl=lvl)
        camera = Camera(player)

        while game_running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    exit()
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE:
                        exit()
                    if event.key == pygame.K_SPACE:
                        game_unpaused = (game_unpaused[0] + 1) % 2, game_unpaused[1]
                        if game_unpaused[1] == 'level complete!':
                            game_unpaused = game_unpaused[0], 'pause'
                if event.type == pygame.MOUSEBUTTONDOWN and game_unpaused:
                    player.start_fire()
                if event.type == pygame.MOUSEBUTTONUP and game_unpaused:
                    player.stop_fire()
            if game_unpaused[0]:
                all_sprites.update()

                if room.is_clear():
                    all_sprites.empty()
                    player_sprite.empty()
                    wall_sprites.empty()
                    floor_sprites.empty()
                    weapon_sprites.empty()
                    bullet_sprites.empty()
                    enemy_sprites.empty()
                    text_map.clear()
                    lvl += 1
                    camera, drawer, player, sprites, room, virus, groups_for_weapon, \
                    player_sprite, wall_sprites, floor_sprites, all_sprites, weapon_sprites, \
                    bullet_sprites, enemy_sprites, collision_sprites = start_game()
                    game_unpaused = 0, 'level complete!'

                if game_running:
                    if not player.is_live:
                        game_running = False

            pause = not game_unpaused[0], game_unpaused[1]

            camera.update()
            camera.apply(all_sprites)

            drawer.draw_all(sprites, pause, FPS=clock.get_fps())
            pygame.display.flip()
            clock.tick(144)
        game_running = True
        end_menu = load_image(('image', 'game_over.png'))

        while game_running:
            game_surface.fill(WHITE)
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    exit()
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE:
                        exit()
            game_surface.blit(end_menu, (0, 0))
            f1 = pygame.font.Font(None, 100)
            text1 = f1.render(f'scores: {int(lvl / 3 * 50)}', True,
                              BLACK)
            game_surface.blit(text1, (HALF_WIDTH - 200, 200))
            pygame.display.flip()
            clock.tick(144)

pygame.quit()

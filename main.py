import pygame
import pygame_gui
import math
from settings import *
from player import Player
from map import *
from drawer import Drawer

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
        clock.tick(144)

    if game_running:
        pygame.display.set_caption('Dungeon game')
        game_surface = pygame.display.set_mode((WIDTH, HEIGHT))
        player = Player()
        drawer = Drawer()

        while game_running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    exit()
            player.movement()
            drawer.draw_all(game_surface, player, FPS=clock.get_fps())

            for x, y in world_map:
                pygame.draw.rect(game_surface, DARKGRAY, (x, y, TILE, TILE), 2)

            pygame.display.flip()
            clock.tick(144)

pygame.quit()

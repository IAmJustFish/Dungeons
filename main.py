import pygame
import pygame_gui
from settings import *
from player import Player


if __name__ == "__main__":
    pygame.init()

    pygame.display.set_caption('Dungeon menu')
    menu_surface = pygame.display.set_mode((WIDTH, HEIGHT))
    background = pygame.Surface(((WIDTH, HEIGHT)))
    background.fill(BLACK)
    pygame.draw.line(background, (128, 128, 128), (0, 100), (WIDTH, 100), 150)
    pygame.draw.line(background, (128, 128, 128), (400, 100), (500, HEIGHT), 150)
    pygame.draw.line(background, (128, 128, 128), (900, 100), (800, HEIGHT), 150)
    main = pygame_gui.UIManager(((WIDTH, HEIGHT)))

    play_button = pygame_gui.elements.UIButton(relative_rect=pygame.Rect((409, 278), (487, 134)), text="Start", manager=main)
    sound_button = pygame_gui.elements.UIButton(relative_rect=pygame.Rect((1050, 600), (230, 110)), text="sound", manager=main)
    settings_button = pygame_gui.elements.UIButton(relative_rect=pygame.Rect((1, 600), (230, 110)), text="settings", manager=main)

    clock = pygame.time.Clock()
    running = True
    game_running = False

    while running:
        time_delta = clock.tick(144)/1000
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
        pass

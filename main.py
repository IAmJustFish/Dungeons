import pygame
import pygame_gui
from settings import *
from player import Player


if __name__ == "__main__":
    pygame.init()

    pygame.display.set_caption('Dungeon menu')
    window_surface = pygame.display.set_mode((WIDTH, HEIGHT))
    background = pygame.Surface(((WIDTH, HEIGHT)))
    background.fill(BLACK)
    manager = pygame_gui.UIManager(((WIDTH, HEIGHT)))

    play_button = pygame_gui.elements.UIButton(relative_rect=pygame.Rect((409, 278), (487, 134)), text="Start", manager=manager)

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

            manager.process_events(event)

        manager.update(time_delta)

        window_surface.blit(background, (0, 0))
        manager.draw_ui(window_surface)

        pygame.display.update()
        clock.tick(144)
    
    
    if game_running:
        pass

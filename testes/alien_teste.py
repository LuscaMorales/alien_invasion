import pygame
from settings_test import Settings
import game_funct as gf
from nave_teste import Nave

def run_game():
    pygame.init()
    my_settings = Settings()
    screen = pygame.display.set_mode((my_settings.screen_widht,my_settings.screen_height))
    pygame.display.set_caption("Alien TESTE")
    nave = Nave(my_settings,screen)
    while True:
        gf.check_events(nave)
        nave.update()
        gf.update_screen(my_settings,screen,nave)


run_game()
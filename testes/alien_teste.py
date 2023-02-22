import pygame
from settings_test import Settings
import game_funct as gf
from nave_teste import Nave
from pygame.sprite import Group

def run_game():
    pygame.init()
    my_settings = Settings()
    screen = pygame.display.set_mode((my_settings.screen_widht,my_settings.screen_height))
    pygame.display.set_caption("Alien TESTE")
    nave = Nave(my_settings,screen)
    tiros = Group()
    while True:
        gf.check_events(my_settings, screen, nave, tiros)
        nave.update()
        gf.update_tiros(tiros,nave)
        gf.update_screen(my_settings, screen, nave, tiros)


run_game()
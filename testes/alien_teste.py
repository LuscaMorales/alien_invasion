import pygame
from settings_test import Settings
import game_funct as gf
from nave_teste import Nave
from pygame.sprite import Group
from star import Star
from gotas import Gota

def run_game():
    pygame.init()
    my_settings = Settings()
    screen = pygame.display.set_mode((my_settings.screen_widht,my_settings.screen_height))
    pygame.display.set_caption("Alien TESTE")
    nave = Nave(my_settings,screen)
    gota01 = Gota(my_settings, screen)
    tiros = Group()
    stars = Group()
    gotas = Group()
    gf.create_fleet(my_settings, screen, stars, nave)
    gf.create_todas_gota(my_settings, screen, gotas)
    while True:
        gf.check_events(my_settings, screen, nave, tiros)
        nave.update()
        gf.update_tiros(tiros,nave)
        gf.update_gota(gotas)
        gf.update_star(my_settings, screen, stars, nave)
        gf.update_screen(my_settings, screen, nave, stars, tiros, gotas)

run_game()
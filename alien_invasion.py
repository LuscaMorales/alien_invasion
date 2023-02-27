import game_fuction as gf
import pygame
from settings import Settings
from ship import Ship
from pygame.sprite import Group
from alien import Alien

def run_game():
    pygame.init()
    ai_settings = Settings()
    screen = pygame.display.set_mode((ai_settings.screen_widht,ai_settings.screen_height))
    pygame.display.set_caption("Alien Invasion")
    ship = Ship(ai_settings,screen)
    #Criacao de um grupo no qual serao armazenados os projeteis
    bullets = Group()
    aliens = Group()
    while True:
        gf.check_events(ai_settings, screen, ship, bullets)
        ship.update()
        gf.update_bullets(bullets)
        gf.create_fleet(ai_settings, screen, ship, aliens)
        gf.update_screen(ai_settings, screen, ship, aliens, bullets)


run_game()
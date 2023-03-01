import sys
import pygame
from tiros import Tiro
from star import Star

def check_events(my_settings, screen, nave, tiros):
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            check_keydown_events(event, my_settings, screen, nave, tiros)
        elif event.type == pygame.KEYUP:
            check_keyup_events(event,nave)

def update_screen(my_settings, screen, nave, stars, tiros):
    screen.fill(my_settings.bg_collor)
    for tiro in tiros.sprites():
        tiro.draw_tiro()
    nave.blitme()
    stars.draw(screen)
    pygame.display.flip()

def check_keydown_events(event, my_settings, screen, nave, tiros):
    if event.type == pygame.KEYDOWN:
        if event.key == pygame.K_UP:
            nave.moving_up = True
        # elif event.key == pygame.K_LEFT:
        # nave.moving_left = False
        elif event.key == pygame.K_DOWN:
            nave.moving_down = True
        # elif event.key == pygame.K_RIGHT:
        # nave.moving_right = False
        elif event.key == pygame.K_SPACE:
            fire_tiro(my_settings, screen, nave, tiros)
        elif event.key == pygame.K_q:
            sys.exit()

def check_keyup_events(event,nave):
    if event.type == pygame.KEYUP:
        if event.key == pygame.K_UP:
            nave.moving_up = False
        #elif event.key == pygame.K_LEFT:
            #nave.moving_left = False
        elif event.key == pygame.K_DOWN:
            nave.moving_down = False
        #elif event.key == pygame.K_RIGHT:
            #nave.moving_right = False

def fire_tiro(my_settings, screen, nave, tiros):
    if len(tiros) < my_settings.tiros_allowed:
        new_tiros = Tiro(my_settings, screen, nave)
        tiros.add(new_tiros)

def update_tiros(tiros,nave):
    tiros.update()
    for tiro in tiros.copy():
        if tiro.rect.left >= nave.screen_rect.right:
            tiros.remove(tiro)

def get_numbers_stars_y(my_settings, star_height):
    availible_space_y = my_settings.screen_height - (2 * star_height)
    numbers_stars_y = int(availible_space_y / (2 * star_height))
    return numbers_stars_y

def create_star(my_settings, screen, stars , star_number):
    star = Star(my_settings, screen)
    star_height = star.rect.height
    star.y = int(star_height + (2 * star_height * star_number))
    star.rect.y = star.y
    stars.add(star)

def create_fleet(my_settings, screen, stars):
    star = Star(my_settings, screen)
    number_stars_y = get_numbers_stars_y(my_settings, star.rect.height)
    for star_number in range(number_stars_y):
        create_star(my_settings, screen, stars,star_number)

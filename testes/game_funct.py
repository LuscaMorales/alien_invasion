import sys
import pygame
from tiros import Tiro
from star import Star
from gotas import Gota

def check_events(my_settings, screen, nave, tiros):
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            check_keydown_events(event, my_settings, screen, nave, tiros)
        elif event.type == pygame.KEYUP:
            check_keyup_events(event,nave)

def update_screen(my_settings, screen, nave, stars, tiros, gotas):
    screen.fill(my_settings.bg_collor)
    for tiro in tiros.sprites():
        tiro.draw_tiro()
    gotas.draw(screen)
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

def create_star(my_settings, screen, stars , star_number, row_number):
    star = Star(my_settings, screen)
    star_height = star.rect.height
    star.y = int(star_height + (2 * star_height * star_number))
    star.rect.y = star.y
    star.rect.x = my_settings.screen_widht - star.rect.width - 2 * star.rect.width * row_number
    stars.add(star)

def create_fleet(my_settings, screen, stars, nave):
    star = Star(my_settings, screen)
    number_stars_y = get_numbers_stars_y(my_settings, star.rect.height)
    number_rows = get_numbers_rows(my_settings, nave.rect.width, star.rect.width)
    for row_number in range(number_rows):
        for star_number in range(number_stars_y):
            create_star(my_settings, screen, stars, star_number, row_number)

def get_numbers_rows(my_settings, nave_width, star_width):
    available_space_x = (my_settings.screen_widht - (3 * star_width) - nave_width)
    number_rows = int(available_space_x  / (2 * star_width))
    return number_rows

def linha_da_gota(my_settings, gota_width):
    available_x_gota = my_settings.screen_widht
    numbers_gota = int(available_x_gota / (2 * gota_width))
    return numbers_gota

def create_gota(my_settings, screen, gotas, gota_numbers, gota_coluna):
    gota = Gota(my_settings, screen)
    gota_width = gota.rect.width
    gota_heigth = gota.rect.height
    gota.x = int(2 * gota_width * gota_numbers)
    gota.rect.x = gota.x
    gota.y = int(gota.screen_rect  2 * gota_heigth * gota_coluna)
    gota.rect.y = gota.y
    gotas.add(gota)

def create_todas_gota(my_settings, screen, gotas):
    gota = Gota(my_settings, screen)
    linha_gota =  linha_da_gota(my_settings, gota.rect.width)
    quantidade_add = 3
    linha_gota += quantidade_add
    numero_de_colunas_gota = numero_colunas_gota(my_settings, gota.rect.height)
    for gota_coluna in range(numero_de_colunas_gota):
        for gota_numbers in range(linha_gota):
            create_gota(my_settings, screen, gotas, gota_numbers, gota_coluna)

def numero_colunas_gota(my_settings, gota_height):
    available_y_gota = my_settings.screen_height
    numero_colunas = int(available_y_gota / (2 * gota_height))
    colunas_add = 2
    numero_colunas += colunas_add
    return numero_colunas

def update_gota(gotas):
    gotas.update()
import sys
import pygame

def check_events(nave):
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            check_keydown_events(event,nave)
        elif event.type == pygame.KEYUP:
            check_keyup_events(event,nave)

def update_screen(my_settings,screen,nave):
    screen.fill(my_settings.bg_collor)
    nave.blitme()
    pygame.display.flip()

def check_keydown_events(event,nave):
    if event.type == pygame.KEYDOWN:
        if event.key == pygame.K_RIGHT:
            nave.moving_right = True
        elif event.key == pygame.K_LEFT:
            nave.moving_left = True
        elif event.key == pygame.K_UP:
            nave.moving_up = True
        elif event.key == pygame.K_DOWN:
            nave.moving_down = True

def check_keyup_events(event,nave):
    if event.type == pygame.KEYUP:
        if event.key == pygame.K_RIGHT:
            nave.moving_right = False
        elif event.key == pygame.K_LEFT:
            nave.moving_left = False
        elif event.key == pygame.K_UP:
            nave.moving_up = False
        elif event.key == pygame.K_DOWN:
            nave.moving_down = False
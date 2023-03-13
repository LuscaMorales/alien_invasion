import sys
import pygame
from bullet import Bullet
from alien import Alien
from time import sleep

def check_keydown_events(event, ai_settings, screen, ship, bullets):
    """pressionamentos de tecla"""
    if event.type == pygame.KEYDOWN:
        if event.key == pygame.K_RIGHT:
            # move a espaconave para a direita
            ship.moving_right = True
        elif event.key == pygame.K_LEFT:
            ship.moving_left = True
        elif event.key == pygame.K_SPACE:
            #cria um novo projetil e o adiciona ao grupo de projeteis
            fire_bullet(ai_settings, screen, ship, bullets)
        elif event.key == pygame.K_q:
            sys.exit()

def fire_bullet(ai_settings, screen, ship, bullets):
    """Dispara projetil se o limite ainda nao foi alcancado"""
    #Cria um novo projetil e adiciona ao grupo de projeteis
    if len(bullets) < ai_settings.bullets_allowed:
        new_bullet = Bullet(ai_settings,screen,ship)
        bullets.add(new_bullet)

def check_keyup_events(event,ship):
    """Solturas de tecla"""
    if event.type == pygame.KEYUP:
        if event.key == pygame.K_RIGHT:
            ship.moving_right = False
        elif event.key == pygame.K_LEFT:
            ship.moving_left = False

def check_events(ai_settings, screen, ship, bullets):
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            check_keydown_events(event, ai_settings, screen, ship, bullets)
        elif event.type == pygame.KEYUP:
            check_keyup_events(event,ship)


def update_screen(ai_settings, screen, ship, aliens, bullets):
    screen.fill(ai_settings.bg_color)
    for bullet in bullets.sprites():
        bullet.draw_bullet()
    ship.blitme()
    aliens.draw(screen)
    pygame.display.flip()

def update_bullets(ai_settings, screen, ship, aliens, bullets):
    """Atualiza a posição dos projeteis e se livra dos projeteis antigos"""
    #Se livra dos projeteis antigos
    bullets.update()
    for bullet in bullets.copy():
        if bullet.rect.bottom <= 0:
            bullets.remove(bullet)
    check_bullet_alien_collisions(ai_settings, screen, ship, aliens, bullets)


def check_bullet_alien_collisions(ai_settings, screen, ship, aliens, bullets):
    """Responde a colisoes entre projeteis e alienigenas"""
    #Remove qualquer projetil e alienigena q tenha colidido
    collisions = pygame.sprite.groupcollide(bullets, aliens, True, True)
    # destrói os projéteis existentes e cria uma nova frota
    if len(aliens) == 0:
        bullets.empty()
        create_fleet(ai_settings, screen, ship, aliens)

def get_numbers_aliens_x(ai_settings, alien_width):
    """Determina a quantidade de alien que cabem em linha na tela"""
    available_space_x = ai_settings.screen_widht - (2 * alien_width)
    number_aliens_x = int(available_space_x / (2 * alien_width))
    return number_aliens_x

def create_alien(ai_settings, screen, aliens, alien_number, row_number):
    #Cria o alienigena e o posiciona em linha
    alien = Alien(ai_settings, screen)
    alien_width = alien.rect.width
    alien.x = alien_width + 2 * alien_width * alien_number
    alien.rect.x = alien.x
    alien.rect.y = alien.rect.height + 2 * alien.rect.height * row_number
    aliens.add(alien)

def create_fleet(ai_settings, screen, ship, aliens):
    """Cria uma frota completa de alienigenas"""
    alien = Alien(ai_settings,screen)
    number_aliens_x = get_numbers_aliens_x(ai_settings,alien.rect.width)
    number_rows = get_number_rows(ai_settings,ship.rect.height, alien.rect.height)
    for row_number in range(number_rows):
        for alien_number in range(number_aliens_x):
            create_alien(ai_settings,screen, aliens, alien_number,row_number)

def get_number_rows(ai_settings, ship_height, alien_height):
    """Determina o numero de linhas com alienigenas q cabem na tela"""
    available_space_y = (ai_settings.screen_height - (3 * alien_height) - ship_height)
    number_rows = int(available_space_y / (2 * alien_height))
    return number_rows

def update_aliens(ai_settings, stats, screen, ship, aliens, bullets):
    """Verifica se a frota esta em uma das bordas e entao atualiza as posicoes"""
    check_fleet_edges(ai_settings, aliens)
    #verifica se algum alienigena atingiu a parte inferior da tela
    check_aliens_bottom(ai_settings, stats, screen, ship, aliens, bullets)
    if pygame.sprite.spritecollideany(ship, aliens):
        ship_hit(ai_settings, stats, screen, ship, aliens, bullets)
    aliens.update()

def check_fleet_edges(ai_settings, aliens):
    """Responde apropriadamente se algum alienigena alcancou a borda"""
    for alien in aliens.sprites():
        if alien.check_edges():
            change_fleet_direction(ai_settings, aliens)
            break

def change_fleet_direction(ai_settings, aliens):
    """Faz toda a frota descer e muda sua direcao"""
    for alien in aliens.sprites():
        alien.rect.y += ai_settings.fleet_drop_speed
        ai_settings.fleet_direction *= -1

def check_aliens_bottom(ai_settings, stats, screen, ship, aliens, bullets):
    """Verifica se algum alienigena alcançou a parte inferior da tela"""
    screen_rect = screen.get_rect()
    for alien in aliens.sprites():
        if alien.rect.bottom >= screen_rect.bottom:
            #trata esse caso do mesmo modo que é feito quando a espaçonave é atingida
            ship_hit(ai_settings, stats, screen, ship, aliens, bullets)
            break

def ship_hit(ai_settings, stats, screen, ship, aliens, bullets):
    """Responde ao fato de a espaçonave ter sido atingida por um alienígena"""
    if stats.ships_left > 0:
        #Decrementa ships_left
        stats.ships_left -= 1
        #Esvazia a lista de alienígenas e de projéteis
        aliens.empty()
        bullets.empty()
        #Cria uma nova frota e centraliza a espaçonave
        create_fleet(ai_settings, screen, ship, aliens)
        ship.center_ship()
        #faz uma pausa
        sleep(1.5)
    else:
        stats.game_active = False

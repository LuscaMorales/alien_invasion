import pygame
from pygame.sprite import Sprite

class Bullet(Sprite):
    """Classe que administra projeteis disparados pela espaconave"""
    def __init__(self,ai_settings,screen,ship):
        super(Bullet,self).__init__()
        self.screen = screen
        #Cria um retangulo para o projetil em (0,0)
        self.rect = pygame.Rect(0, 0, ai_settings.bullet_widht, ai_settings.bullet_height)
        #Em seguida define a posicao certa
        self.rect.centerx = ship.rect.centerx
        self.rect.top = ship.rect.top
        self.y = float(self.rect.y)
        self.color = ai_settings.bullet_color
        self.speed_factor = ai_settings.bullet_speed_factor

    def update(self):
        """move o projetil para cima"""
        self.y -= self.speed_factor
        self.rect.y = self.y

    def draw_bullet(self):
        """desenha o projetil na tela"""
        pygame.draw.rect(self.screen, self.color, self.rect)

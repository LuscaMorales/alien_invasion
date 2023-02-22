import pygame
from pygame.sprite import Sprite


class Tiro(Sprite):
    def __init__(self,my_settings,screen,nave):
        super(Tiro,self).__init__()
        self.screen = screen
        self.rect = pygame.Rect(0, 0, my_settings.tiro_widht, my_settings.tiro_height)
        self.rect.centery = nave.rect.centery
        self.rect.top = nave.rect.top
        self.x = float(self.rect.x)
        self.color = my_settings.tiro_color
        self.speed_factor = my_settings.tiro_speed_factor

    def update(self):
        self.x += self.speed_factor
        self.rect.x = self.x

    def draw_tiro(self):
        pygame.draw.rect(self.screen, self.color, self.rect)

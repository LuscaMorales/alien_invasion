import pygame
from pygame.sprite import Sprite

class Gota(Sprite):
    def __init__(self, my_settings, screen):
        super(Gota, self).__init__()
        self.screen = screen
        self.screen_rect = screen.get_rect()
        self.my_settings = my_settings
        self.image = pygame.image.load("images/gota.png")
        self.image = pygame.transform.scale(self.image, (25, 30))
       #self.image = pygame.transform.rotate(self.image, -45)
        self.rect = self.image.get_rect()
        self.rect.x = self.rect.width
        self.rect.y = self.screen_rect.top
        self.x = float(self.rect.x)
        self.y = float(self.rect.y)

    def blitme(self):
        self.screen.blit(self.image, self.rect)

    def update(self):
        self.y += self.my_settings.gota_speed
        self.rect.y = self.y

    def check_bottom(self):
        screen_rect = self.screen.get_rect()
        if self.rect.y > screen_rect.bottom:
            return True

    def go_to_up(self):
        self.y = -10
        self.rect.y = self.y

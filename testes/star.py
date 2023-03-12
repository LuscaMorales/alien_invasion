import pygame
from pygame.sprite import Sprite


class Star(Sprite):
    def __init__(self, my_settigs, screen):
        super(Star,self).__init__()
        self.screen = screen
        self.screen_rect = screen.get_rect()
        self.my_settings = my_settigs
        self.image = pygame.image.load("images/star_picture.bmp")
        self.image = pygame.transform.scale(self.image,(80,80))
        self.rect = self.image.get_rect()
        self.rect.x = self.screen_rect.right - (2 * self.rect.width)
        self.rect.y = self.rect.height
        self.x = float(self.rect.x)
        self.y = float(self.rect.y)

    def blitme(self):
        self.screen.blit(self.image,self.rect)

    def update(self):
        self.x -= self.my_settings.star_speed
        self.rect.x = self.x
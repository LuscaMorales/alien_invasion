import pygame.image
import settings

class Nave():
    def __init__(self,my_settings,screen):
        self.screen = screen
        self.my_settings = my_settings
        self.image = pygame.image.load("images/missile-40387.bmp")
        self.image = pygame.transform.scale(self.image,my_settings.nave_size)
        self.image = pygame.transform.rotate(self.image, -90)
        self.rect = self.image.get_rect()
        self.screen_rect = screen.get_rect()
        self.rect.centerx = self.screen_rect.centerx
        self.rect.centery = self.screen_rect.centery
        self.centerx = float(self.rect.centerx)
        self.centery = float(self.rect.centery)
        #Flag de movimento
        self.moving_right = False
        self.moving_left = False
        self.moving_up = False
        self.moving_down = False

    def update(self):
        if self.moving_right and self.rect.right < self.screen_rect.right:
            self.centerx += self.my_settings.nave_speed
        if self.moving_left and self.rect.left > 0:
            self.centerx -= self.my_settings.nave_speed
        self.rect.centerx = self.centerx
        if self.moving_up and self.rect.top > 2:
            self.centery -= self.my_settings.nave_speed
        if self.moving_down and self.rect.bottom < self.screen_rect.bottom:
            self.centery += self.my_settings.nave_speed
        self.rect.centery = self.centery




    def blitme(self):
        self.screen.blit(self.image,self.rect)
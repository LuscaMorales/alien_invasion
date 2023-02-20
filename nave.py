import pygame

class Nave():
    def __init__(self,screen):
        size = (100,220)
        self.screen = screen
        self.image1 = pygame.image.load("images/missile-40387.bmp")
        self.image1 = pygame.transform.scale(self.image1,size)
        self.rect1 = self.image1.get_rect()
        self.screen_rect = screen.get_rect()
        self.rect1.centerx = self.screen_rect.centerx
        self.rect1.centery = self.screen_rect.centery


    def blitme1(self):
        self.screen.blit(self.image1,self.rect1)
import pygame
from pygame.locals import *

class Brick(pygame.sprite.Sprite):
    def __init__(self,x,y):
        self.image = pygame.image.load("data/brick1.png").convert()
        self.x = x
        self.y = y
        pygame.sprite.Sprite.__init__(self)
        self.rect = self.image.get_rect()
        self.rect.topleft = [self.x,self.y]

class Platform(pygame.sprite.Sprite):
    def __init__(self,x,y):
        self.image = pygame.image.load("data/platform-top.png").convert()
        self.x = x
        self.y = y
        pygame.sprite.Sprite.__init__(self)
        self.rect = self.image.get_rect()
        self.rect.topleft = [self.x,self.y]

class Cloud(pygame.sprite.Sprite):
    def __init__(self,x,y):
        self.image = pygame.image.load("data/cloud.png").convert()
        self.x = x
        self.y = y
        pygame.sprite.Sprite.__init__(self)
        self.rect = self.image.get_rect()
        self.rect.topleft = [self.x,self.y]




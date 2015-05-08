import pygame
from pygame.locals import *

class Brick(pygame.sprite.Sprite):
    def __init__(self,x,y):
        self.image = pygame.image.load("data/brick1.png").convert_alpha()
        self.x = x
        self.y = y
        pygame.sprite.Sprite.__init__(self)
        self.rect = self.image.get_rect()
        self.rect.topleft = [self.x,self.y]
    def update(self,screen,direction):
        pass
class Platform(pygame.sprite.Sprite):
    def __init__(self,x,y):
        self.image = pygame.image.load("data/platform-top.png").convert_alpha()
        self.x = x
        self.y = y
        pygame.sprite.Sprite.__init__(self)
        self.rect = self.image.get_rect()
        self.rect.topleft = [self.x,self.y]
    def update(self,screen,direction):
        pass
class Cloud(pygame.sprite.Sprite):
    def __init__(self,x,y):
        self.image = pygame.image.load("data/cloud.png").convert_alpha()
        self.x = x
        self.y = y
        pygame.sprite.Sprite.__init__(self)
        self.rect = self.image.get_rect()
        self.rect.topleft = [self.x,self.y]
    def update(self,screen,direction):
        pass
class Bush(pygame.sprite.Sprite):
    def __init__(self,x,y):
        self.image = pygame.image.load("data/bush-3.png").convert_alpha()
        self.x = x
        self.y = y
        pygame.sprite.Sprite.__init__(self)
        self.rect = self.image.get_rect()
        self.rect.topleft = [self.x,self.y]
    def update(self,screen,direction):
        pass
class DobbelCloud(pygame.sprite.Sprite):
    def __init__(self,x,y):
        self.image = pygame.image.load("data/dobbelclouds.png").convert_alpha()
        self.x = x
        self.y = y
        pygame.sprite.Sprite.__init__(self)
        self.rect = self.image.get_rect()
        self.rect.topleft = [self.x,self.y]
    def update(self,screen,direction):
        pass
class Pipe(pygame.sprite.Sprite):
    def __init__(self,x,y):
        self.image = pygame.image.load("data/pipe_green.png").convert_alpha()
        self.x = x
        self.y = y
        pygame.sprite.Sprite.__init__(self)
        self.rect = self.image.get_rect()
        self.rect.topleft = [self.x,self.y]
    def update(self,screen,direction):
        pass

class Mario(pygame.sprite.Sprite):
    def __init__(self,x,y):
        pygame.sprite.Sprite.__init__(self)
        self.x = x
        self.y = y
        self.image = pygame.image.load("data/mario1.png").convert_alpha()
        self.rect = self.image.get_rect()
        self.rect.topleft = [self.x,self.y]
        self.left_images = ["data/mario1-left.png","data/mario2-left.png",
                            "data/mario3-left.png","data/mario4-left.png"]
        self.right_images = ["data/mario1.png","data/mario2.png",
                             "data/mario3.png", "data/mario4.png"]
        self.frame = 0
    def update(self,screen,direction):
        if direction == "right":
            self.x += 3
            self.rect.left += 3
            self.frame += 1
            if self.frame == 16:
                self.frame = 0
            self.image = pygame.image.load(self.right_images[self.frame//4]).convert_alpha()
            screen.blit(self.image,self.rect)


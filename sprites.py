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
class Platform(pygame.sprite.Sprite):
    def __init__(self,x,y):
        self.image = pygame.image.load("data/platform-top.png").convert_alpha()
        self.x = x
        self.y = y
        pygame.sprite.Sprite.__init__(self)
        self.rect = self.image.get_rect()
        self.rect.topleft = [self.x,self.y]
        self.rect.h += 10
class Cloud(pygame.sprite.Sprite):
    def __init__(self,x,y):
        self.image = pygame.image.load("data/cloud.png").convert_alpha()
        self.x = x
        self.y = y
        pygame.sprite.Sprite.__init__(self)
        self.rect = self.image.get_rect()
        self.rect.topleft = [self.x,self.y]
class Bush(pygame.sprite.Sprite):
    def __init__(self,x,y):
        self.image = pygame.image.load("data/bush-3.png").convert_alpha()
        self.x = x
        self.y = y
        pygame.sprite.Sprite.__init__(self)
        self.rect = self.image.get_rect()
        self.rect.topleft = [self.x,self.y]
class DobbelCloud(pygame.sprite.Sprite):
    def __init__(self,x,y):
        self.image = pygame.image.load("data/dobbelclouds.png").convert_alpha()
        self.x = x
        self.y = y
        pygame.sprite.Sprite.__init__(self)
        self.rect = self.image.get_rect()
        self.rect.topleft = [self.x,self.y]
class Pipe(pygame.sprite.Sprite):
    def __init__(self,x,y):
        self.image = pygame.image.load("data/pipe_green.png").convert_alpha()
        self.x = x
        self.y = y
        pygame.sprite.Sprite.__init__(self)
        self.rect = self.image.get_rect()
        self.rect.topleft = [self.x,self.y]

class Mario(pygame.sprite.Sprite):
    def __init__(self,x,y):
        pygame.sprite.Sprite.__init__(self)
        self.dx = 0
        self.dy = 0
        self.x = x
        self.y = y
        self.image = pygame.image.load("data/mario1.png").convert_alpha()
        self.rect = self.image.get_rect()
        self.rect.topleft = [self.x,self.y]
        self.rect.w -= 2
        self.rect.h -= 2
        self.left_images = ["data/mario1-left.png","data/mario2-left.png",
                            "data/mario3-left.png","data/mario4-left.png"]
        self.right_images = ["data/mario1.png","data/mario2.png",
                             "data/mario3.png", "data/mario4.png"]
        self.frame = 0
        self.on_ground = True
        self.jumping = False
        self.jump_speed = -5
        self.gravity = .45
        self.face = "right"
    def update(self,screen,left,right,up,sprites):
        if right :
            self.dx = 3
            self.face = "right"
            self.x +=  self.dx
            self.rect.x += self.dx
            self.frame += 1
            if self.frame == 16:
                self.frame = 0
            self.image = pygame.image.load(self.right_images[self.frame//4]).convert_alpha()
            self.collide(sprites,left)
        if left:
            self.dx = -3
            self.face = "left"
            self.x += self.dx
            self.rect.x += self.dx
            self.frame += 1
            if self.frame == 16:
                self.frame = 0
            self.image = pygame.image.load(self.left_images[self.frame//4]).convert_alpha()
            self.collide(sprites,left)
        if up:
            self.y += self.dy
            if self.face == "left" and not self.on_ground:
                self.image = pygame.image.load("data/mario5-left.png").convert_alpha()
            elif self.face == "right" and not self.on_ground:
                self.image = pygame.image.load("data/mario5.png").convert_alpha()
            self.rect.y += self.dy
            self.dy += self.gravity
            if self.dy >= 16:
                self.dy = 0
                self.jumping = False
            self.collide(sprites,left)
        if not (left or right):
            self.dx = 0
            self.frame = 0
        if not self.jumping:
            self.dy += self.gravity
            self.y += self.gravity
            self.rect.y += self.dy
            self.collide(sprites,left)
    def collide(self,sprites,left):
        for s in sprites:
            if self.rect.colliderect(s):
                if s.rect.collidepoint(self.rect.bottomright) and not s.rect.collidepoint(self.rect.bottomleft) and self.dx > 0 and not self.on_ground:
                    self.rect.right = s.rect.left
                    self.dx = 0
                elif s.rect.collidepoint(self.rect.bottomleft) and not s.rect.collidepoint(self.rect.bottomright) and self.dx < 0 and not self.on_ground:
                    self.rect.left = s.rect.right
                    self.dx = 0
                elif s.rect.collidepoint(self.rect.topright) and not s.rect.collidepoint(self.rect.topleft) and self.dx > 0:
                    self.rect.right = s.rect.left
                    self.dx = 0
                    print("collide right")
                elif s.rect.collidepoint(self.rect.topleft) and not s.rect.collidepoint(self.rect.topright)  and self.dx < 0:
                    self.rect.left = s.rect.right
                    self.dx = 0
                    print("collide left")
                elif self.dy < 0:
                    self.rect.top = s.rect.bottom
                    self.dy = 0
                    print("collide top")
                elif self.dy > 0:
                    self.on_ground = True
                    self.rect.bottom = s.rect.top
                    self.dy = 0
                    if self.face == "left":
                        self.image = pygame.image.load("data/mario1-left.png").convert_alpha()
                    elif self.face == "right":
                        self.image = pygame.image.load("data/mario1.png").convert_alpha()

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
class Goomba(pygame.sprite.Sprite):
    def __init__(self,x,y):
        self.max_x = x + 48 #For animation purposes, the minimum and maximum x values the Goomba goes. Not the best idea if I wanted Goomba to act like real mario game.
        self.min_x = x - 48
        self.left = False #Direction the Goomba is moving
        self.image = pygame.image.load("data/slub1.png").convert_alpha()
        self.animate = ['data/slub1.png','data/slub2.png']
        self.rect = self.image.get_rect()
        self.rect.topleft = [x,y]
        self.rect.w -= 2
        self.rect.h -= 2
        pygame.sprite.Sprite.__init__(self)
        self.frame = 0
        self.squish_frame = 0
        self.dead = False
    def update(self):
        if self.dead:
            self.image = pygame.image.load('data/slub3.png').convert_alpha()
            self.rect.y = self.rect.y - 8 #Slub3 is 16x8 and not 16x16 so rect needs to be smaller
            self.squish_frame += 1
        else:
            self.frame += 1
            if self.frame > 9:
                self.frame = 0
            if self.left:
                self.rect.x -= 4
                if self.rect.x < self.min_x:
                    self.rect.x = self.min_x
                    self.left = False
            else:
                self.rect.x += 4
                if self.rect.x > self.max_x:
                    self.rect.x = self.max_x
                    self.left = True
            self.image = pygame.image.load(self.animate[self.frame//5]).convert_alpha()

class Mario(pygame.sprite.Sprite):
    def __init__(self,x,y):
        pygame.sprite.Sprite.__init__(self)
        self.dx = 0 #Distance moving X-axis
        self.dy = 0 #Distance moving Y-Axis
        self.x = x
        self.y = y
        self.image = pygame.image.load("data/mario1.png").convert_alpha()
        self.rect = self.image.get_rect()
        self.rect.topleft = [self.x,self.y]
        self.rect.w -= 2 #Hitbox needs to be smaller or collison acts weird
        self.rect.h -= 2
        self.left_images = ["data/mario1-left.png","data/mario2-left.png",
                            "data/mario3-left.png","data/mario4-left.png"]
        self.right_images = ["data/mario1.png","data/mario2.png",
                             "data/mario3.png", "data/mario4.png"]
        self.frame = 0
        self.on_ground = True
        self.jumping = False
        self.jump_speed = -8
        self.gravity = .48
        self.face = "right"
        self.dead = False
        self.jump_sound = pygame.mixer.Sound('data/sound/jump.ogg')
        self.collide_sound = pygame.mixer.Sound('data/sound/jump2.ogg')
        self.stomp_sound = pygame.mixer.Sound('data/sound/stomp.ogg')
        self.play_jump = False
    def update(self,screen,left,right,up,sprites,enemies):
        if self.rect.top >= screen.get_height(): #If you fall of bottom edge, Mario dies
            self.dead = True
            self.dy = -8
            return
        if right :
            self.dx = 3
            self.face = "right"
            self.frame += 1
            self.rect.x += self.dx
            if self.frame == 16:
                self.frame = 0
            if not self.on_ground:
                self.image = pygame.image.load("data/mario5.png").convert_alpha()
            else:
                self.image = pygame.image.load(self.right_images[self.frame//4]).convert_alpha()
            self.collide(sprites,enemies)
        if left:
            self.dx = -3
            self.face = "left"
            self.frame += 1
            self.rect.x += self.dx
            if self.frame == 16:
                self.frame = 0
            if not self.on_ground:
                self.image = pygame.image.load("data/mario5-left.png").convert_alpha()
            else:
                self.image = pygame.image.load(self.left_images[self.frame//4]).convert_alpha()
            self.collide(sprites,enemies)
        if up:
            if self.play_jump:
                self.jump_sound.stop()
                self.jump_sound.play()
                self.play_jump = False
            if self.face == "left" and not self.on_ground:
                self.image = pygame.image.load("data/mario5-left.png").convert_alpha()
            elif self.face == "right" and not self.on_ground:
                self.image = pygame.image.load("data/mario5.png").convert_alpha()
            self.rect.y += self.dy
            self.dy += self.gravity
            if self.dy >= 16:
                self.dy = 0
                self.jumping = False
            self.collide(sprites,enemies)

        if not (left or right):
            self.dx = 0
            self.frame = 0
        if not self.jumping: #Simulates gravity. Always falling unless Mario jumps or collides with something under him
            self.dy += self.gravity
            self.rect.y += self.dy
            self.collide(sprites,enemies)
        if self.rect.left < 0: #Prevents going off screen to the left
            self.rect.left = 0
        if self.rect.right > screen.get_width(): #Prevent going off screen to the right
            self.rect.right = screen.get_width()
    def death(self): #Death animation calculations
        self.rect.y += self.dy
        self.dy += self.gravity/2
    def collide(self,sprites,enemies):
        #Environment collision
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
                elif s.rect.collidepoint(self.rect.topleft) and not s.rect.collidepoint(self.rect.topright)  and self.dx < 0:
                    self.rect.left = s.rect.right
                    self.dx = 0
                elif self.dy < 0:
                    self.play_jump = False
                    self.jump_sound.stop()
                    self.collide_sound.play()
                    self.rect.top = s.rect.bottom
                    self.dy = 0
                elif self.dy > 0:
                    self.on_ground = True
                    self.rect.bottom = s.rect.top
                    self.dy = 0
                    if self.face == "left":
                        self.image = pygame.image.load("data/mario1-left.png").convert_alpha()
                    elif self.face == "right":
                        self.image = pygame.image.load("data/mario1.png").convert_alpha()
        #Enemy collision
        for e in enemies:
            if not e.dead: #For animation purposes, enemies aren't deleted until a few frames later
                if self.rect.colliderect(e):
                    if e.rect.collidepoint(self.rect.bottomright) and e.rect.collidepoint(self.rect.midbottom):
                        self.jump_sound.stop()
                        self.stomp_sound.play()
                        e.dead = True
                        self.dy = -2
                    elif e.rect.collidepoint(self.rect.bottomleft) and e.rect.collidepoint(self.rect.midbottom):
                        self.jump_sound.stop()
                        self.stomp_sound.play()
                        e.dead = True
                        self.dy = -2
                    else:
                        self.dead = True
                        self.dy = -6

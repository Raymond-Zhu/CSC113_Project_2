import pygame
from pygame.locals import *
from sprites import *

class Level():
    def __init__(self):
        self.level = []
        self.tilemap = open("data/level","r")
        self.world = []
        self.collidable = pygame.sprite.Group()

    def create(self,x,y):
        for tile in self.tilemap:
            self.level.append(tile)
        for row in self.level:
            for col in row:
                if col == "C":
                    cloud = Cloud(x,y)
                    self.world.append(cloud)
                if col == "B":
                    brick = Brick(x,y)
                    self.world.append(brick)
                    self.collidable.add(brick)
                if col == "P":
                    platform = Platform(x,y)
                    self.world.append(platform)
                    self.collidable.add(platform)
                if col == "U":
                    bush = Bush(x,y)
                    self.world.append(bush)
                if col == "G":
                    pipe = Pipe(x,y)
                    self.world.append(pipe)
                    self.collidable.add(pipe)
                if col == "D":
                    dcloud = DobbelCloud(x,y)
                    self.world.append(dcloud)
                if col == "M":
                    mario = Mario(x,y)
                    self.mario = mario
                x += 16
            y += 16
            x = 0
    def draw(self,surface):
        color = (0,128,255)
        for s in self.world:
           # pygame.draw.rect(surface,color,s.rect)
            surface.blit(s.image,s.rect.topleft)
        surface.blit(self.mario.image,self.mario.rect)
       # pygame.draw.rect(surface,color,self.mario.rect)




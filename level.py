import pygame
from pygame.locals import *
from sprites import *

class Level():
    def __init__(self):
        self.level = []
        self.tilemap = open("data/level","r")
        self.world = []
        self.sprites = pygame.sprite.Group()

    def create(self,x,y):
        for tile in self.tilemap:
            self.level.append(tile)
        for row in self.level:
            for col in row:
                if col == "C":
                    cloud = Cloud(x,y)
                    self.world.append(cloud)
                    self.sprites.add(cloud)
                if col == "B":
                    brick = Brick(x,y)
                    self.world.append(brick)
                    self.sprites.add(brick)
                if col == "P":
                    platform = Platform(x,y)
                    self.world.append(platform)
                    self.sprites.add(platform)
                if col == "U":
                    bush = Bush(x,y)
                    self.world.append(bush)
                    self.sprites.add(bush)
                if col == "G":
                    pipe = Pipe(x,y)
                    self.world.append(pipe)
                    self.sprites.add(pipe)
                if col == "D":
                    dcloud = DobbelCloud(x,y)
                    self.world.append(dcloud)
                    self.sprites.add(dcloud)
                if col == "M":
                    mario = Mario(x,y)
                    self.mario = mario
                    self.world.append(mario)
                    self.sprites.add(mario)
                x += 16
            y += 16
            x = 0
    def draw(self,surface):
        for s in self.sprites:
            surface.blit(s.image,s.rect.topleft)





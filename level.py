import pygame
from pygame.locals import *
from sprites import Brick, Platform, Cloud

class Level(self):
    def __init__(self):
        self.level = []
        self.tilemap = open("level","r")
        self.world = []
        self.sprites = pygame.sprite.Group()

    def create(self,x,y):
        for tile in tilemap:
            self.level.append(tile)
        for row in level:
            for col in row:
                if col = "C":
                    cloud = Cloud(x,y)
                    self.world.append(cloud)
                    self.sprites.add(cloud)
                if col = "B":
                    brick = Brick(x,y)
                    self.world.append(brick)
                    self.sprites.add(brick)
                if col = "P":
                    platform = Platform(x,y)
                    self.world.append(Platform)
                    self.sprites.add(Platform)
                x += 16
            y += 16
            x = 0


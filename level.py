import pygame
from pygame.locals import *
from sprites import *

class Level():
    def __init__(self):
        self.level = []
        self.tilemap = open("data/level","r")
        self.world = []
        self.collidable = pygame.sprite.Group()
        self.game_over = False
        self.font = pygame.font.Font("data/font.ttf",24)
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
        if self.game_over:
            surface.fill((0,0,0))
            text = self.font.render("GAME OVER",1,(255,255,255))
            surface.blit(text, (200,240))
        else:
            for s in self.world:
                surface.blit(s.image,s.rect.topleft)
            surface.blit(self.mario.image,self.mario.rect)




import pygame, sys
from pygame.locals import *
from level import Level

clock = pygame.time.Clock()
pygame.init()
SCREEN_SIZE = (640,480)
screen = pygame.display.set_mode(SCREEN_SIZE)
bg = pygame.image.load("data/background-2.png").convert()
#Rects are used for calculating how many times we need to blit background
bg_rect = bg.get_rect()
level = Level()
level.create(0,0)
pygame.mouse.set_visible(0)
up=left=right=False

while True:
    if level.mario.dead:
        level.mario.image = pygame.image.load("data/mariodie.png").convert_alpha()
        level.mario.death()
        if level.mario.rect.y > screen.get_height():
            pygame.quit()
            sys.exit()
    else:
        #Blits background according to screen size
        for event in pygame.event.get():
            if event.type == KEYDOWN and event.key == K_ESCAPE:
                pygame.quit()
                sys.exit()
            if event.type == KEYDOWN and event.key == K_RIGHT:
                right = True
            if event.type == KEYDOWN and event.key == K_LEFT:
                left = True
            if event.type == KEYDOWN and event.key == K_UP:
                if level.mario.on_ground:
                    up = True
                    level.mario.jumping = True
                    level.mario.dy = level.mario.jump_speed
                    level.mario.on_ground = False

            if event.type == KEYUP and event.key == K_RIGHT:
                level.mario.image = pygame.image.load("data/mario1.png").convert_alpha()
                right = False
            if event.type == KEYUP and event.key == K_LEFT:
                level.mario.image = pygame.image.load("data/mario1-left.png").convert_alpha()
                left = False
            if event.type == KEYUP and event.key == K_UP:
                if level.mario.on_ground:
                    level.mario.jump_speed = -5
                level.mario.jumping = False
                up = False
        level.mario.update(screen,left,right,up,level.collidable)
    for x in range(0,screen.get_width(),bg_rect.w):
        for y in range(0,screen.get_height(),bg_rect.h):
            screen.blit(bg,(x,y))
    level.draw(screen)
    pygame.display.flip()
    clock.tick(30)

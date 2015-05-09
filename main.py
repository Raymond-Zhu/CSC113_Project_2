import pygame, sys
from pygame.locals import *
from level import Level

clock = pygame.time.Clock()
pygame.init()
SCREEN_SIZE = (640,480)
screen = pygame.display.set_mode(SCREEN_SIZE)
bg = pygame.image.load("data/background-2.png").convert()
#Rects are used for calculating how many times we need to blit background
screen_rect = screen.get_rect()
bg_rect = bg.get_rect()
level = Level()
level.create(0,0)
pygame.mouse.set_visible(0)
up=left=right=False

#In case the size of the size is not evenly divisible by the size of the background, Blits one more background to "cover up" Temporarily not needed. Leaving for now  since background is 320 * 240.
#size = ((screen_rect.w // bg_rect.w + 1) * background_rect.w , (screen_rect.h // background_rect.h+1) * background_rect.h)

while True:
    #Blits background according to screen size
    for event in pygame.event.get():
        if event.type == KEYDOWN and event.key == K_ESCAPE:
            pygame.quit()
            sys.exit()
        if event.type == KEYDOWN and event.key == K_RIGHT:
            right = True
            level.mario.dx = 3
        if event.type == KEYDOWN and event.key == K_LEFT:
            left = True
            level.mario.dx = -3
        if event.type == KEYDOWN and event.key == K_UP:
            up = True
            level.mario.dy = level.mario.jump_speed

        if event.type == KEYUP and event.key == K_RIGHT:
            level.mario.image = pygame.image.load("data/mario1.png").convert_alpha()
            level.mario.frame = 0
            level.mario.dx = 0
            right = False
        if event.type == KEYUP and event.key == K_LEFT:
            level.mario.image = pygame.image.load("data/mario1-left.png").convert_alpha()
            level.mario.frame = 0
            level.mario.dx = 0
            left = False
        if event.type == KEYUP and event.key == K_UP:
            level.mario.jump_speed = -16
            up = False
            level.mario.dy = 0
    for x in range(0,screen_rect.w,bg_rect.w):
        for y in range(0,screen_rect.h,bg_rect.h):
            screen.blit(bg,(x,y))
    level.draw(screen)
    #for s in level.collidable:
        #pygame.draw.rect(screen,(255,255,255),s.rect)
    level.mario.update(screen,left,right,up,level.collidable)
    pygame.display.flip()
    clock.tick(15)

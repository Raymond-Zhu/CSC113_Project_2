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
direction = ""

#In case the size of the size is not evenly divisible by the size of the background, Blits one more background to "cover up" Temporarily not needed. Leaving for now  since background is 320 * 240.
#size = ((screen_rect.w // bg_rect.w + 1) * background_rect.w , (screen_rect.h // background_rect.h+1) * background_rect.h)

while True:
    #Blits background according to screen size
    for event in pygame.event.get():
        if event.type == KEYDOWN and event.key == K_ESCAPE:
            pygame.quit()
            sys.exit()
        if event.type == KEYDOWN and event.key == K_RIGHT:
            direction = "right"

        if event.type == KEYUP and event.key == K_RIGHT:
            if direction == "right":
                level.mario.image = pygame.image.load("data/mario1.png").convert_alpha()
            direction = ""
    for x in range(0,screen_rect.w,bg_rect.w):
        for y in range(0,screen_rect.h,bg_rect.h):
            screen.blit(bg,(x,y))
    level.draw(screen)
    level.mario.update(screen,direction)
    pygame.display.flip()
    clock.tick(30)

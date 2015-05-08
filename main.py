import pygame, sys
from pygame.locals import *

pygame.init()
SCREEN_SIZE = (640,480)
screen = pygame.display.set_mode(SCREEN_SIZE)
bg = pygame.image.load("data/background-2.png").convert()
#Rects are used for calculating how many times we need to blit background
screen_rect = screen.get_rect()
bg_rect = bg.get_rect()

#In case the size of the size is not evenly divisible by the size of the background, Blits one more background to "cover up" Temporarily not needed. Leaving for now  since background is 320 * 240.
#size = ((screen_rect.w // bg_rect.w + 1) * background_rect.w , (screen_rect.h // background_rect.h+1) * background_rect.h)

while True:

    #Blits background according to screen size
    for x in range(0,screen_rect.w,bg_rect.w):
        for y in range(0,screen_rect.h,bg_rect.h):
            screen.blit(bg,(x,y))

    pygame.display.flip()


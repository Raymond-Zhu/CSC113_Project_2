import pygame, sys
from pygame.locals import *

pygame.init()
SCREEN_SIZE(640,480)
screen = pygame.display.set_mode(SCREEN_SIZE)
screen_rect = screen.get_rect()
bg = pygame.image.load("data/background-.png").convert()
bg_rect = background.get_rect()






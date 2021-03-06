import pygame, sys
from pygame.locals import *
from level import Level

clock = pygame.time.Clock()
pygame.init()
SCREEN_SIZE = (640,480)
screen = pygame.display.set_mode(SCREEN_SIZE)
bg = pygame.image.load("data/background-2.png").convert()
bg_rect = bg.get_rect()
level = Level()
level.create(0,0)
pygame.mouse.set_visible(0)
up=left=right=False
pygame.mixer.init()
bg_music = pygame.mixer.Sound('data/sound/maintheme.ogg')
play_die_music = True
bg_music.play(-1)

while True:
    if level.mario.dead: #Deals with death animation and sounds. Also "freezes" the display except for mario so Goombas don't move.
        level.mario.image = pygame.image.load("data/mariodie.png").convert_alpha()
        if play_die_music:
            bg_music.stop()
            pygame.mixer.music.load('data/sound/death.ogg')
            pygame.mixer.music.queue('data/sound/gameover.ogg') #Queue seems to not work. Not sure why.
            pygame.mixer.music.play()
            play_die_music = False
        level.mario.death()
        if level.mario.rect.y > screen.get_height():
            level.game_over = True
            for event in pygame.event.get():
                if event.type == KEYDOWN and event.key == K_ESCAPE:
                    pygame.quit()
                    sys.exit()
    else:
        for event in pygame.event.get():
            if event.type == KEYDOWN and event.key == K_ESCAPE:
                pygame.quit()
                sys.exit()
            if event.type == KEYDOWN and event.key == K_RIGHT:
                right = True
                level.mario.dx = level.mario.velocity
            if event.type == KEYDOWN and event.key == K_LEFT:
                left = True
                level.mario.dx = -level.mario.velocity
            if event.type == KEYDOWN and event.key == K_UP:
                if level.mario.on_ground:
                    up = True
                    level.mario.jumping = True
                    level.mario.dy = level.mario.jump_speed
                    level.mario.on_ground = False
                    level.mario.play_jump = True

            if event.type == KEYUP and event.key == K_RIGHT:
                level.mario.image = pygame.image.load("data/mario1.png").convert_alpha()
                right = False
            if event.type == KEYUP and event.key == K_LEFT:
                level.mario.image = pygame.image.load("data/mario1-left.png").convert_alpha()
                left = False
            if event.type == KEYUP and event.key == K_UP:
                if level.mario.on_ground:
                    level.mario.jump_speed = -8
                level.mario.jumping = False
                up = False
        level.mario.update(screen,left,right,up,level.collidable,level.enemies)
        level.qblock.update(level.mario)
    for x in range(0,screen.get_width(),bg_rect.w):
        for y in range(0,screen.get_height(),bg_rect.h):
            screen.blit(bg,(x,y))
    level.update(screen)
    pygame.display.flip()
    clock.tick(30)

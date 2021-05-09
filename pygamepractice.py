#ok let's go
background_image_filename='psc.jpg'
mouse_image_filename='nnn.png'

import pygame
from pygame.locals import *
from sys import exit

pygame.init()

screen = pygame.display.set_mode((4000,2250),0,32)

background = pygame.image.load(background_image_filename).convert()
mouse_cursor = pygame.image.load(mouse_image_filename).convert_alpha()

while 1:
    for event in pygame.event.get():
        if event.type == QUIT:
            exit()

    screen.blit(background,(0,0))
    x,y = pygame.mouse.get_pos()
#    x-= mouse_cursor.get_width()/2
#    y-= mouse_cursor.get_height()/2
    screen.blit(mouse_cursor,(x-26,y-24))

    pygame.display.update()

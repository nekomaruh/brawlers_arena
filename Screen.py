# -*- coding: utf-8 -*-

import pygame
from pygame.locals import *
pygame.init()
Fullscreen=False
Resize=True

pygame.mouse.set_visible(False)

info = pygame.display.Info()
X= info.current_w
Y= info.current_h

if Fullscreen==True:
    screen= pygame.display.set_mode((800,600),pygame.HWSURFACE|pygame.DOUBLEBUF|pygame.RESIZABLE|pygame.FULLSCREEN)
else:
    screen = pygame.display.set_mode((800,600),pygame.HWSURFACE|pygame.DOUBLEBUF|pygame.RESIZABLE)

#if Resize == True:
#    screen = pygame.display.set_mode((400,300),pygame.RESIZABLE)
    

#pygame.display.toggle_fullscreen()
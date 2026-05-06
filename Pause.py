# -*- coding: utf-8 -*-
import pygame, glob, random
from pygame.locals import *
import sys
from Load_images import*
from Sprites import Animacion_rules_1
from Variables import break_main, joy_on
from Screen import *

class Pause:
    def __init__(self):
        pygame.init()
        pygame.sprite.Sprite.__init__(self)
        self.screen_size = (800, 600)
        self.screen = screen
        
        # Cargamos joysticks
        if joy_on:
            self.p1 = pygame.joystick.Joystick(0) 
            self.p2 = pygame.joystick.Joystick(1)
            self.p1.init()
            self.p2.init()
        
        # Fondo
        self.fondo = load_image("backgrounds/pause1.jpg",IMG_DIR,alpha=False)
        self.vineta = load_image("symbols/vineta.png",IMG_DIR,alpha=True)
        
        # Titulo
        self.font_title = pygame.font.Font("fonts/MotionControl-BoldItalic.otf", 100)
        self.text_title = self.font_title.render("PAUSED", True, (255,255,255))
        self.font_back = pygame.font.Font("fonts/MotionControl-BoldItalic.otf", 35)
        self.text_back = self.font_back.render("Continue", True, (255,255,255))
        self.text_exit = self.font_back.render("Exit", True, (255,255,255))
        self.text_main = self.font_back.render("Main menu", True, (255,255,255))
        
        # Botones
        self.triangle = load_image("symbols/triangle32_b.png",IMG_DIR,alpha=True)
        self.cross = load_image("symbols/cross32_b.png",IMG_DIR,alpha=True)
        self.circle = load_image("symbols/circle32_b.png",IMG_DIR,alpha=True)
        
        # Importamos animacion
        self.entities = pygame.sprite.Group()
        self.animaciones=[]
        for x in range(random.randint(0,20)):
            self.anim = self.animaciones.append(Animacion_rules_1(random.randint(10,750),random.randint(10,550)))
        
    def render(self):
        self.screen.blit(self.fondo,(0,0))
        
        self.entities.draw(self.screen)
        for x in range(len(self.animaciones)):
            self.entities.add(self.animaciones[x])
            self.animaciones[x].update()
        
        self.screen.blit(self.vineta,(0,0))
        self.screen.blit(self.text_title,(290,220))
        self.screen.blit(self.text_back,(670,550))
        self.screen.blit(self.text_exit,(570,550))
        self.screen.blit(self.text_main,(400,550))
        
        self.screen.blit(self.triangle,(530,550))
        self.screen.blit(self.cross,(630,550))
        self.screen.blit(self.circle,(360,550))
        pygame.display.flip()
        
        
    def pause_loop(self):
        self.fps = pygame.time.Clock()
        self.key = pygame.key.get_pressed()
        paused=True
        
        
        while paused:
            self.fps.tick(60) 
            
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_RETURN:
                        paused=False
                    if event.key == pygame.K_ESCAPE:
                        pygame.quit()
                        sys.exit()
                
                if joy_on:
                    if event.type == pygame.JOYBUTTONDOWN:
                        # Para el P1
                        if event.joy ==0:
                            if event.button==0:
                                paused=False
                            elif event.button==1:
                                break_main[0]=True
                                paused=False
                            elif event.button==3:
                                pygame.quit()
                                quit()
                        # Para el P2
                        if event.joy ==1:
                            if event.button==0:
                                paused=False
                            elif event.button==1:
                                break_main[0]=True
                                paused=False
                            elif event.button==3:
                                pygame.quit()
                                quit()

            self.render()
    

if __name__ == '__main__':
    P = Pause()
    P.pause_loop()
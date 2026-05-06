# -*- coding: utf-8 -*-
import pygame, glob, random
from pygame.locals import *
import sys
from Load_images import*
from Sprites import Animacion_rules_1
from Variables import break_main, joy_on
from Controls import *
from Volume import *
from Sound import *
from Screen import *

class Options:
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
        self.fondo = load_image("backgrounds/controller.jpg",IMG_DIR,alpha=False)
        
        # Titulo
        self.font_title = pygame.font.Font("fonts/MotionControl-BoldItalic.otf", 80)
        self.text_controls = self.font_title.render("Controls", True, (255,255,255))
        self.text_volume = self.font_title.render("Volume", True, (255,255,255))
        self.text_sounds = self.font_title.render("Sounds", True, (255,255,255))
        
        # Back
        self.font_back = pygame.font.Font("fonts/MotionControl-BoldItalic.otf", 35)
        self.text_back = self.font_back.render("Back", True, (255,255,255))
        
        # Botones
        self.triangle = load_image("symbols/triangle32_b.png",IMG_DIR,alpha=True)
        self.circle = load_image("symbols/cross32_a.png",IMG_DIR,alpha=True)
        self.square = load_image("symbols/circle32_a.png",IMG_DIR,alpha=True)
        self.cross = load_image("symbols/square32_a.png",IMG_DIR,alpha=True)
        
    def render(self):
        self.screen.blit(self.fondo,(0,0))
        
        self.screen.blit(self.text_controls,(310,150))
        self.screen.blit(self.text_volume,(310,250))
        self.screen.blit(self.text_sounds,(310,350))
        self.screen.blit(self.text_back,(690,548))
        
        self.screen.blit(self.triangle,(650,550))
        self.screen.blit(self.circle,(260,175))
        self.screen.blit(self.square,(260,275))
        self.screen.blit(self.cross,(260,375))
        
        pygame.display.flip() 
        
    def handle_event(self):
        self.fps = pygame.time.Clock()
        self.key = pygame.key.get_pressed()
        opciones=True
        delay=False
        
        while opciones:
            self.fps.tick(60) 
            
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_RETURN:
                        paused=False
                    if event.key == pygame.K_ESCAPE:
                        delay=True
                        
                if joy_on:
                    if event.type == pygame.JOYBUTTONDOWN:
                        # Para el P1
                        if event.joy ==0:
                            if event.button==0:
                                C = Controls()
                                C.controls_loop()
                            elif event.button==1:
                                V = Volume()
                                V.volume_loop()
                            elif event.button==2:
                                S = Sound()
                                S.sound_loop()
                            elif event.button==3:
                                opciones=False
                                delay=True
                        # Para el P2
                        if event.joy ==1:
                            if event.button==0:
                                C = Controls()
                                C.controls_loop()
                            elif event.button==1:
                                V = Volume()
                                V.volume_loop()
                            elif event.button==2:
                                S = Sound()
                                S.sound_loop()
                            elif event.button==3:
                                opciones=False
                                delay=True
            if delay == True:
                pygame.time.delay(400)
                break

            self.render()


if __name__ == '__main__':
    o = Options()
    o.handle_event()
    
    
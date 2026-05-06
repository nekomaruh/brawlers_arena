# -*- coding: utf-8 -*-
import pygame, sys
from pygame import *
from pygame.locals import *
from Load_images import*
from Main_menu import*
from Music_sounds import button_A
from Screen import *
from Variables import joy_on

class Controls:
    def __init__(self):
        pygame.init()
        pygame.sprite.Sprite.__init__(self)
        self.screen_size = (800, 600)
        self.screen = screen
        self.background = load_image("backgrounds/controller.jpg",IMG_DIR,alpha=False)
        self.joystick = load_image("symbols/joy_buttons.png",IMG_DIR,alpha=True)
        self.triangle = load_image("symbols/triangle32_b.png",IMG_DIR,alpha=True)
            
        self.r_background = self.background.get_rect()
        self.r_background.left=0
        self.r_background.top=0
        self.vx=1
        self.vy=1
        
        # Back
        self.font_back = pygame.font.Font("fonts/MotionControl-BoldItalic.otf", 35)
        self.text_back = self.font_back.render("Back", True, (255,255,255))
        # Titulo
        self.font_title = pygame.font.Font("fonts/MotionControl-BoldItalic.otf", 50)
        self.text_title = self.font_title.render("How to Play", True, (255,255,255))
        
        if joy_on == True:
            self.p1 = pygame.joystick.Joystick(0) 
            self.p1.init()
        
        
    def handle_input(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
                
    def render(self):
        self.key = pygame.key.get_pressed()
        self.screen.blit(self.background,self.r_background)
        self.screen.blit(self.triangle,(650,550))
        self.screen.blit(self.joystick,(-100,20))
        self.screen.blit(self.text_back,(690,548))
        self.screen.blit(self.text_title,(300,40))
        pygame.display.flip()
        
    def controls_loop(self):
        self.fps = pygame.time.Clock()
        self.key = pygame.key.get_pressed()
        delay = False
        
        while True:
            
            self.fps.tick(60)
            self.handle_input()
            
            self.r_background.left+=self.vx
            self.r_background.top+=self.vy
            
            if self.r_background.left>1:
                self.r_background.left=0
            if self.r_background.top>1:
                self.r_background.top=0
                
            if joy_on:
                b3_1=self.p1.get_button(3)
                if b3_1==1:
                    self.triangle = load_image("symbols/triangle32_a.png",IMG_DIR,alpha=True)
                    button_A.play()
                    delay = True
            if not joy_on:
                if self.key [K_ESCAPE]:
                    self.triangle = load_image("symbols/triangle32_a.png",IMG_DIR,alpha=True)
                    button_A.play()
                    delay = True
            
            self.render()
            
            if delay == True:
                pygame.time.delay(400)
                break
            pygame.time.delay(100)



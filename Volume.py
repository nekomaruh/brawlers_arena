# -*- coding: utf-8 -*-
import pygame, sys
from pygame import *
from pygame.locals import *
from Load_images import*
from Main_menu import*
from Music_sounds import button_A
from colores import GREEN
from Variables import vol_bar, vol, sou, joy_on
from Screen import *

class Volume:
    def __init__(self):
        pygame.init()
        pygame.sprite.Sprite.__init__(self)
        self.screen_size = (800, 600)
        self.screen = screen
        self.background = load_image("backgrounds/controller.jpg",IMG_DIR,alpha=False)
        #self.joystick = load_image("symbols/joy_buttons.png",IMG_DIR,alpha=True)
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
        self.font_title = pygame.font.Font("fonts/MotionControl-BoldItalic.otf", 80)
        self.text_title = self.font_title.render("Volume", True, (255,255,255))
        #Barra de volumen
        self.img_vol = pygame.transform.scale(load_image("symbols/vol_bar.png",IMG_DIR,alpha=True),(350,110))
        
        if joy_on:
            self.p1 = pygame.joystick.Joystick(0) 
            self.p1.init()
        
    def handle_input(self):
        if joy_on:
            hx_1=self.p1.get_hat(0)[0]
            a_1=self.p1.get_axis(0)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if joy_on:
                if event.type == pygame.JOYHATMOTION:
                    if event.joy==0:
                        if hx_1 ==1:
                            if vol_bar[0]>=0 and vol_bar[0]<=270:
                                vol_bar[0]+=30
                            else:
                                vol_bar[0]=vol_bar[0]
                        elif hx_1 ==-1:
                            if vol_bar[0]>=30 and vol_bar[0]<=300:
                                vol_bar[0]-=30
                            else:
                                vol_bar[0]=vol_bar[0]
                        elif hx_1==0:
                            vol_bar[0]=vol_bar[0]
                if event.type == pygame.JOYAXISMOTION:
                    if event.joy==0:
                        if a_1>0.5:
                            if vol_bar[0]>=300:
                                vol_bar[0]=vol_bar[0]
                            else:
                                vol_bar[0]+=3
                        if a_1<-0.5:
                            if vol_bar[0]<=0:
                                vol_bar[0]=vol_bar[0]
                            else:
                                vol_bar[0]-=3
                
    def render(self):
        self.screen.blit(self.background,self.r_background)
        self.screen.blit(self.img_vol,(227,270))
        self.screen.blit(self.triangle,(650,550))
        self.screen.blit(self.text_back,(690,548))
        self.screen.blit(self.text_title,(310,180))
        self.porcentaje = self.font_back.render(str(int(vol_bar[0]/3))+"%", True, (255,255,255))
        self.show_vol_bar(vol_bar[0])
        self.screen.blit(self.porcentaje,(260,300))
        
        
    def show_vol_bar(self,volume):
        if volume>=0 and volume<=300:
            vol_color = GREEN
        pygame.draw.rect(screen,vol_color,(250,300,volume,40))
        
    def volume_loop(self):
        self.fps = pygame.time.Clock()
        delay = False
        
        while True:
            self.key = pygame.key.get_pressed()
            self.handle_input()
            # Obtiene los botones
            if joy_on:
                b3_1=self.p1.get_button(3)
                if b3_1==1:
                    self.triangle = load_image("symbols/triangle32_a.png",IMG_DIR,alpha=True)
                    button_A.set_volume(sou[0])
                    button_A.play()    
                    delay = True
            if self.key [K_ESCAPE]:
                self.triangle = load_image("symbols/triangle32_a.png",IMG_DIR,alpha=True)
                button_A.set_volume(sou[0])
                button_A.play()    
                delay = True
            self.render()
            vol[0]=vol_bar[0]/300
            if delay == True:
                pygame.time.delay(400)
                break
            pygame.display.flip()
            pygame.mixer.music.set_volume(vol[0])
            self.fps.tick(60)

if __name__ == '__main__':
    vola = Volume()
    vola.volume_loop()

# -*- coding: utf-8 -*-
import pygame, sys
from pygame import *
from pygame.locals import *
from Load_images import*
from Music_sounds import button_A
from colores import GREEN
from Variables import *
from Screen import *

import numpy as np

class Scores:
    def __init__(self):
        pygame.init()
        pygame.sprite.Sprite.__init__(self)
        self.screen_size = (800, 600)
        self.screen = screen
        self.background = load_image("backgrounds/controller.jpg",IMG_DIR,alpha=False)
        #self.joystick = load_image("symbols/joy_buttons.png",IMG_DIR,alpha=True)
        self.triangle = load_image("symbols/triangle32_b.png",IMG_DIR,alpha=True)

        # Back
        self.font_back = pygame.font.Font("fonts/MotionControl-BoldItalic.otf", 35)
        self.text_back = self.font_back.render("Back", True, (255,255,255))
   
        # Titulo
        self.font_title = pygame.font.Font("fonts/MotionControl-BoldItalic.otf", 80)
        self.text_title = self.font_title.render("Highscore", True, (255,255,255))
        
        if joy_on:
            self.p1 = pygame.joystick.Joystick(0) 
            self.p1.init()
        
    def handle_input(self):
        if joy_on:
            hx_1=self.p1.get_hat(0)[0]
            a_1=self.p1.get_axis(0)
        for e in pygame.event.get():
            if e.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if joy_on:
                if e.type == pygame.JOYBUTTONDOWN:
                    if e.button==3:
                        break                  
                
    def render(self):
        self.screen.blit(self.background,(0,0))
        self.screen.blit(self.triangle,(650,550))
        self.screen.blit(self.text_back,(690,548))
        self.screen.blit(self.text_title,(280,50))
    
    def obtener_puntuacion_mas_alta():
        # Puntuación más alta por defecto
        puntuacion_mas_alta = 0
        try:
            archivo_puntuacion_mas_alta = open("high_score.txt", "r")
            puntuacion_mas_alta = int(archivo_puntuacion_mas_alta.read())
            archivo_puntuacion_mas_alta.close()
  
        except IOError:
            print("No existe puntuación mas alta")
        except ValueError:
            print("Error en las variables")
 
        return puntuacion_mas_alta
        
    def mostrar_puntajes(self):
        archivo_puntuacion_mas_alta = open("high_score.txt", "r")
        puntuacion_mas_alta = int(archivo_puntuacion_mas_alta.read())
        archivo_puntuacion_mas_alta.close()
        maximo = self.font_title.render("Best: "+ str(puntuacion_mas_alta)+"pts.", True, (255,255,255))
        arch_tiempo = open("time.txt","r")
        tiempo= str(arch_tiempo.read())
        arch_tiempo.close()
        timex = self.font_title.render("Time: " + str(tiempo),True,(255,255,255))
        screen.blit(maximo,(200,200))
        screen.blit(timex,(200,300))
            
    def guardar_puntuacion_mas_alta(nueva_puntuacion_mas_alta,tiempo):
        try:
            archivo_puntuacion_mas_alta = open("high_score.txt", "w")
            archivo_puntuacion_mas_alta.write(str(nueva_puntuacion_mas_alta))
            ae_tiempo = open("time.txt","w")
            ae_tiempo.write(str(tiempo))
            archivo_puntuacion_mas_alta.close()
            ae_tiempo.close()
        except IOError:
            print("No se puede guardar puntuacion mas alta")
            
    def loop(self):
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
                    button_A.play()
                    button_A.set_volume(sou[0])
                    delay = True

            if self.key [K_ESCAPE]:
                self.triangle = load_image("symbols/triangle32_a.png",IMG_DIR,alpha=True)
                button_A.play()
                button_A.set_volume(sou[0])
                delay = True

            self.render()

            if delay == True:
                pygame.time.delay(400)
                break
            
            self.mostrar_puntajes()
            
            pygame.display.flip()
            self.fps.tick(60)

if __name__ == '__main__':
    pt = Scores()
    pt.loop()

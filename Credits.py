# -*- coding: utf-8 -*-

import pygame
from pygame.locals import *
from Screen import *
from Load_images import *
from Load_joysticks import *
from Music_sounds import button_A
from Variables import sou, joy_on

class Creditos:
    def __init__(self):
        pygame.init()
        pygame.display.set_caption('End Credits')
        self.screen = screen
        self.screen_r = self.screen.get_rect()
        self.font = pygame.font.SysFont("Arial", 40)
        self.font_exit = pygame.font.Font("fonts/MotionControl-BoldItalic.otf", 35)
        self.text_exit = self.font_exit.render("Exit", True, (255,255,255))
        self.b_exit = load_image("symbols/triangle32_a.png",IMG_DIR,alpha=True)
        self.clock = pygame.time.Clock()
        if joy_on:
            Load_joy(self)

    def credits_loop(self):

        credit_list = ["CREDITS - Brawler's Arena"," ","Programmers","Catherine Alegría", "Johan Ordenes", "Pablo Arias"," ","Designers","Constanza Castro","Patricia Carrasco"]

        texts = []
        # Recorremos la credit_list
        for i, line in enumerate(credit_list):
            s = self.font.render(line, 1, (255, 255, 255))
            # Creamos un Rect para cada Surface. 
            # Le damos a cada Rect la posición en donde van a aparecer
            r = s.get_rect(centerx=self.screen_r.centerx, y=self.screen_r.bottom + i * 45)
            texts.append((r, s))
        delay=False

        while True:
            for e in pygame.event.get():
                if e.type == QUIT or e.type == KEYDOWN and e.key == pygame.K_ESCAPE:
                    return

            self.screen.fill((0, 0, 0))

            for r, s in texts:
                # Movemos cada Rect en 1 pixel en cada frame
                r.move_ip(0, -1)
                # Dibujamos
                screen.blit(s, r)

            # Si todos los Rect salieron de la pantalla, cerramos la ventana
            if not self.screen_r.collidelistall([r for (r, _) in texts]):
                return
            
            screen.blit(self.b_exit,(750,550))
            screen.blit(self.text_exit,(700,548))
            
            self.key = pygame.key.get_pressed()
            # Obtiene los botones
            if joy_on:
                b3_1=self.p1.get_button(3)
                if b3_1==1:
                    self.b_exite = load_image("symbols/triangle32_a.png",IMG_DIR,alpha=True)
                    button_A.play()
                    button_A.set_volume(sou[0])
                    delay = True
                    
                
            
            if self.key [K_ESCAPE]:
                self.b_exite = load_image("symbols/triangle32_a.png",IMG_DIR,alpha=True)
                button_A.play()
                button_A.set_volume(sou[0])
                delay = True
                
            if delay == True:
                pygame.time.delay(400)
                break

            # Hacemos flip a la pantalla
            pygame.display.update()

            # FPS en 60
            self.clock.tick(60)

if __name__ == '__main__': 
    C = Creditos()
    C.credits_loop()
# -*- coding: utf-8 -*-
from Variables import mapas, personajes_p1, personajes_p2, break_main, sou
from Load_images import load_image, IMG_DIR
from Sprites import *
from Music_sounds import countdown
import pygame
from Map_all import *
from Screen import *

pygame.init()

class Countdown:
    def __init__(self):
        #BOSQUE
        if mapas[0]==1:
            self.fondo=load_image("backgrounds/map1/map.png",IMG_DIR,alpha=False)
            self.plataformas=load_image("backgrounds/map1/platforms.png",IMG_DIR,alpha=True)
        #KAWAI
        elif mapas[1]==1:
            self.fondo=load_image("backgrounds/map3/map.jpg",IMG_DIR,alpha=False)
            self.plataformas=load_image("backgrounds/map3/platforms.png",IMG_DIR,alpha=True)
        #CIUDAD
        elif mapas[2]==1:
            self.fondo=load_image("backgrounds/map4/map.jpg",IMG_DIR,alpha=False)
            self.plataformas=load_image("backgrounds/map4/platforms.png",IMG_DIR,alpha=True)
        #DESIERTO
        elif mapas[3]==1:
            self.fondo=load_image("backgrounds/map2/map.jpg",IMG_DIR,alpha=False)
            self.plataformas=load_image("backgrounds/map2/platforms.png",IMG_DIR,alpha=True)
        #PLANETAS
        elif mapas[4]==1:
            self.fondo=load_image("backgrounds/map5/map.png",IMG_DIR,alpha=False)
            self.plataformas=load_image("backgrounds/map5/platforms.png",IMG_DIR,alpha=True)
        # Carga el player 1
        if personajes_p1[0]==1:
            self.jugador_1 = load_image("sprites/anubis/0.png",IMG_DIR,alpha=True)
        elif personajes_p1[1]==1:
            self.jugador_1 = load_image("sprites/astro/1.png",IMG_DIR,alpha=True)
        elif personajes_p1[2]==1:
            self.jugador_1 = load_image("sprites/robot/1.png",IMG_DIR,alpha=True)
        elif personajes_p1[3]==1:
            self.jugador_1 = load_image("sprites/soldier/0.png",IMG_DIR,alpha=True)
        elif personajes_p1[4]==1:
            self.jugador_1 = load_image("sprites/thing/2.png",IMG_DIR,alpha=True)
        # Carga el player 2
        if personajes_p2[0]==1:
            self.jugador_2 = load_image("sprites/anubis/7.png",IMG_DIR,alpha=True)
        elif personajes_p2[1]==1:
            self.jugador_2 = load_image("sprites/astro/9.png",IMG_DIR,alpha=True)
        elif personajes_p2[2]==1:
            self.jugador_2 = load_image("sprites/robot/10.png",IMG_DIR,alpha=True)
        elif personajes_p2[3]==1:
            self.jugador_2 = load_image("sprites/soldier/8.png",IMG_DIR,alpha=True)
        elif personajes_p2[4]==1:
            self.jugador_2 = load_image("sprites/thing/10.png",IMG_DIR,alpha=True)
        # Carga las letras del menu
        self.font = pygame.font.Font("fonts/MotionControl-BoldItalic.otf", 400)
        self.font_2 = pygame.font.Font("fonts/MotionControl-BoldItalic.otf", 430)
            
    def show_screen(self):
        screen.blit(self.fondo,(0,0))
        screen.blit(self.plataformas,(0,0))
        screen.blit(self.jugador_1,(350,350))
        screen.blit(self.jugador_2,(420,350))
        
    def handle_event(self):
        game=True
        transition=Countdown()
        self.fps = pygame.time.Clock()
        c=0
        counter=3
        countdown.play()
        countdown.set_volume(sou[0])
        while game:
            k = pygame.key.get_pressed()
            c+=1
            self.fps.tick(60)
            if c==60:
                counter-=1
                countdown.play()
            if c==120:
                counter-=1
                countdown.play()
            if c==180:
                counter=1           
            if c==200:
                g = Game_screen()
                g.handle_event()
            if k[K_ESCAPE]:
                game=False
            for e in pygame.event.get():
                if e.type == pygame.QUIT:
                    sys.exit(0)
                if e.type == pygame.KEYDOWN:
                    if e.key == pygame.K_ESCAPE:
                        game=False
            if break_main[0]==True:
                game=False
            show_321= self.font.render(str(counter), True, (255,255,255))
            show_321b= self.font_2.render(str(counter), True, (0,0,0))
            transition.show_screen()
            screen.blit(show_321b,(335,18))
            screen.blit(show_321,(330,20))
            pygame.display.update()
            
if __name__ == "__main__":
    T = Countdown()
    T.handle_event()
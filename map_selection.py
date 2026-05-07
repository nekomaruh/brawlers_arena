# -*- coding: utf-8 -*-
__author__ = "TeamFlammers"
import pygame, random
from colores import *
from pygame.locals import *
from Music_sounds import button_X, button_A
from Cursors import Manito
from Variables import mapas, personajes_p1, personajes_p2, break_main, joy_on
from Transitions import *
from Map_all import *
from Screen import *
from Load_joysticks import Load_joys

pygame.init()

class Maps:
    def __init__(self):
        # Dimensiones
        self.gameDisplay = screen
        # Font para los textos
        self.font = pygame.font.Font("fonts/MotionControl-BoldItalic.otf", 50)
        # Texto "Map Selection"
        self.text1 = self.font.render("Map Selection", True, BLACK)
        # Texto "Random"
        self.text2 = self.font.render("Random", True, WHITE)
        # Imagen de fondo
        self.backImg=load_image("backgrounds/Background.png",IMG_DIR,alpha=False)

        # Back
        self.font_back = pygame.font.Font("fonts/MotionControl-BoldItalic.otf", 35)
        self.text_back = self.font_back.render("Back", True, (0,0,0))
        self.triangle = load_image("symbols/triangle32_b.png",IMG_DIR,alpha=True)
        
        # Select
        self.text_select = self.font_back.render("Select", True, (0,0,0))
        self.cross = load_image("symbols/cross32_b.png",IMG_DIR,alpha=True)

        # Instancia las manos
        self.mano1=Manito(400,270,1)
        
        # Carga Joysticks     
        if joy_on:
            Load_joys(self)
        #self.p1 = pygame.joystick.Joystick(0) 
        #self.p1.init()
    # Función boton(pos x, pos y, ancho, alto, color1 cuando el cursor no está dentro del rect, color2 cuando está dentro del rect)
    def boton(self,x,y,ancho,alto,color1,color2):    
        self.mano1.vel=10
        self.k = pygame.key.get_pressed()
        if joy_on:
            b0_1=self.p1.get_button(0)

        if (x + ancho > self.mano1.rect.left > x) and (y + alto > self.mano1.rect.top > y): # Si está dentro del rectángulo, cambia de color
            pygame.draw.rect(self.gameDisplay, color2, (x, y, ancho, alto))
            
            if self.mano1.rect.left>40 and self.mano1.rect.top>90 and self.mano1.rect.left<260 and self.mano1.rect.top<260:
                if joy_on and b0_1:
                    for i in range(5):
                        mapas[i]=0
                    mapas[0]=1
                    button_X.play()
                    pygame.mixer.music.set_volume(1.0)
                    pygame.mixer.music.stop()
                    T = Countdown()
                    T.handle_event()
                    self.mano1=Manito(400,270,1)
                    
                if self.k[K_RETURN]:
                    #print("mapa bosque")
                    for i in range(5):
                        mapas[i]=0
                    mapas[0]=1
                    button_X.play()
                    pygame.mixer.music.set_volume(1.0)
                    pygame.mixer.music.stop()
                    T = Countdown()
                    T.handle_event()
                    self.mano1=Manito(400,270,1)
                    
            elif self.mano1.rect.left>290 and self.mano1.rect.top>90 and self.mano1.rect.left<510 and self.mano1.rect.top<260:
                if joy_on and b0_1:
                    #print("mapa kawai") 
                    for i in range(5):
                        mapas[i]=0
                    mapas[1]=1
                    button_X.play()
                    pygame.mixer.music.set_volume(1.0)
                    pygame.mixer.music.stop()
                    T = Countdown()
                    T.handle_event()
                    self.mano1=Manito(400,270,1)
                    
                if self.k[K_RETURN]:
                    #print("mapa kawai") 
                    for i in range(5):
                        mapas[i]=0
                    mapas[1]=1
                    button_X.play()
                    pygame.mixer.music.set_volume(1.0)
                    pygame.mixer.music.stop()
                    T = Countdown()
                    T.handle_event()
                    self.mano1=Manito(400,270,1)
                    
            elif self.mano1.rect.left>540 and self.mano1.rect.top>90 and self.mano1.rect.left<760 and self.mano1.rect.top<260:
                if joy_on and b0_1:
                    for i in range(5):
                        mapas[i]=0
                    mapas[2]=1
                    button_X.play()
                    pygame.mixer.music.set_volume(1.0)
                    pygame.mixer.music.stop()
                    T = Countdown()
                    T.handle_event()
                    self.mano1=Manito(400,270,1)
                    
                if self.k[K_RETURN]:
                    #print("mapa ciudad")
                    for i in range(5):
                        mapas[i]=0
                    mapas[2]=1
                    button_X.play()
                    pygame.mixer.music.set_volume(1.0)
                    pygame.mixer.music.stop()
                    T = Countdown()
                    T.handle_event()
                    self.mano1=Manito(400,270,1)
            ###
            elif self.mano1.rect.left>40 and self.mano1.rect.top>340 and self.mano1.rect.left<260 and self.mano1.rect.top<510:
                if joy_on and b0_1:
                    for i in range(5):
                        mapas[i]=0
                    mapas[3]=1
                    button_X.play()
                    pygame.mixer.music.set_volume(1.0)
                    pygame.mixer.music.stop()
                    T = Countdown()
                    T.handle_event()
                    self.mano1=Manito(400,270,1)
                    
                if self.k[K_RETURN]:
                    #print("mapa desierto")
                    for i in range(5):
                        mapas[i]=0
                    mapas[3]=1
                    button_X.play()
                    pygame.mixer.music.set_volume(1.0)
                    pygame.mixer.music.stop()
                    T = Countdown()
                    T.handle_event()
                    self.mano1=Manito(400,270,1)
            
            elif self.mano1.rect.left>290 and self.mano1.rect.top>340 and self.mano1.rect.left<510 and self.mano1.rect.top<510:
                if joy_on and b0_1:          
                    for i in range(5):
                        mapas[i]=0
                    mapas[4]=1
                    button_X.play()
                    pygame.mixer.music.set_volume(1.0)
                    pygame.mixer.music.stop()
                    T = Countdown()
                    T.handle_event()
                    self.mano1=Manito(400,270,1)
                    
                if self.k[K_RETURN]:
                    #print("mapa planetas")
                    for i in range(5):
                        mapas[i]=0
                    mapas[4]=1
                    button_X.play()
                    pygame.mixer.music.set_volume(1.0)
                    pygame.mixer.music.stop()
                    T = Countdown()
                    T.handle_event()
                    self.mano1=Manito(400,270,1)
            
            elif self.mano1.rect.left>540 and self.mano1.rect.top>340 and self.mano1.rect.left<760 and self.mano1.rect.top<510:
                if joy_on and b0_1:   
                    for i in range(5):
                        mapas[i]=0
                    mapas[5]=1
                    self.mano1=Manito(400,270,1)
                    
                if self.k[K_RETURN]:
                    #print("mapa random")
                    for i in range(5):
                        mapas[i]=0
                    mapas[5]=1
                    self.mano1=Manito(400,270,1)
                     
        # Si no está dentro del rectángulo, no cambia de color            
        else:
            pygame.draw.rect(self.gameDisplay, color1, (x, y, ancho, alto))
        
    # Función mapa(imagen del mapa, pos x, pos y)        
    def mapa(self,img, x, y):
        mapaImg = pygame.image.load(img)
        self.gameDisplay.blit(mapaImg, (x,y))
    
    def map_select(self):
        loop_map = True
        boton=Maps.boton
        mapa=Maps.mapa
        clock = pygame.time.Clock()
        up=down=left=right=cruz=circulo=False

        while loop_map:
            mapa_random=random.randint(0,4)
            for e in pygame.event.get():
                if e.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                    
                if joy_on:
                    if e.type == pygame.JOYAXISMOTION:
                        a_1=self.p1.get_axis(0)
                        a_1y=self.p1.get_axis(1)
                        # Para el p1
                        if e.joy==0:
                            if a_1>0.5:
                                right=True
                            elif a_1<-0.5:
                                left=True
                            else:
                                left=right=False
                            if a_1y>0.5:
                                down=True
                            elif a_1y<-0.5:
                                up=True
                            else:
                                up=down=False
                    if e.type == pygame.JOYBUTTONDOWN:
                        # Para el P1
                        if e.joy ==0:
                            if e.button==3:
                                for i in range(len(personajes_p1)):
                                    personajes_p1[i]=0
                                for i in range(len(personajes_p2)):
                                    personajes_p2[i]=0
                                loop_map=False
                        
                if e.type == pygame.KEYDOWN:
                    if e.key == pygame.K_ESCAPE:
                        button_A.play()
                        for i in range(len(personajes_p1)):
                            personajes_p1[i]=0
                            personajes_p2[i]=0
                        loop_map=False

                    if e.key == K_UP:
                        up=True
                    elif e.key == K_DOWN:
                        down=True
                    elif e.key == K_LEFT:
                        left=True
                    elif e.key == K_RIGHT:
                        right=True
                    elif e.key == K_RETURN:
                        cruz=True
                        suma1=1
                    elif e.key == K_BACKSPACE:
                        circulo=True
                        for i in range(len(mapas)):
                            mapas[i]=0
                        suma1=0
                if e.type==pygame.KEYUP:
                    if e.key == K_UP:
                        up=False
                    if e.key == K_DOWN:
                        down=False
                    if e.key == K_LEFT:
                        left=False
                    if e.key==K_RIGHT:
                        right=False
                    if e.key == K_RETURN:
                        cruz=False
                    if e.key == K_BACKSPACE:
                        circulo=False
                        
            # Se dibuja el fondo
            self.gameDisplay.blit(self.backImg, (0, 0))
    
            # Función boton con sus parámetros
            boton(self,40, 90, 220, 170, BLACK, GREEN)
            boton(self,290, 90, 220, 170, BLACK, GREEN)
            boton(self,540, 90, 220, 170, BLACK, GREEN)
            boton(self,40, 340, 220, 170, BLACK, GREEN)
            boton(self,290, 340, 220, 170, BLACK, GREEN)
            boton(self,540, 340, 220, 170, BLACK, PURPLE)
    
            # Función mapa con sus parámetros
            mapa(self,'images/symbols/Bosque_v3.png',50,100)
            mapa(self,'images/symbols/Kawai.png',300,100)
            mapa(self,'images/symbols/Zombie.png',550,100)
            mapa(self,'images/symbols/Desierto.png',50,350)
            mapa(self,'images/symbols/Space.png',300,350)
    
            # Se dibujan los textos "Map Selection" y "Random"
            self.gameDisplay.blit(self.text1,(280, 25))     
            self.gameDisplay.blit(self.text2,(590, 400))
            
            # Se dibuja el triangulo back y su texto
            self.gameDisplay.blit(self.triangle,(650,550))
            self.gameDisplay.blit(self.text_back,(690,548))
            self.gameDisplay.blit(self.cross,(510,550))
            self.gameDisplay.blit(self.text_select,(550,548))
            
            self.mano1.movimiento(up,down,left,right,cruz,circulo)

            # Para la carga del mapa random (carga el mapa automaticamente y se salta el countdown)
            if mapas[5]==1:
                up=down=left=right=False
                mapas[5]=0
                if mapa_random==0:
                    mapas[0]=1
                elif mapa_random==1:
                    mapas[1]=1
                elif mapa_random==2:
                    mapas[2]=1
                elif mapa_random==3:
                    mapas[3]=1
                elif mapa_random==4:
                    mapas[4]=1
                self.mano1.volver()
                button_X.play()
                pygame.mixer.music.set_volume(1.0)
                pygame.mixer.music.stop()
                g = Game_screen()
                g.handle_event()
                
            if break_main[0]==True:
                loop_map=False

            # Update
            pygame.display.update()
            clock.tick(60)
            

if __name__ == "__main__":
    M = Maps()
    M.map_select()
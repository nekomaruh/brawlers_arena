# -*- coding: utf-8 -*-
__author__ = "TeamFlammers"
import pygame
from colores import *
from pygame.locals import *
from map_selection import Maps
from Load_images import *
from Music_sounds import button_A, button_X, menu_select
from Variables import personajes_p1, personajes_p2, break_main, sou, joy_on
from Cursors import Manito_1, Manito_2
from Screen import *
from Load_joysticks import Load_joys

#pygame.init()

class Character:
    def __init__(self):
        self.gameDisplay=screen
        #self.font=pygame.font.SysFont("BinnerD",50)
        self.font = pygame.font.Font("fonts/MotionControl-BoldItalic.otf", 50)
        self.text1=self.font.render("Character Selection",True,BLACK)
        self.backImg=load_image("backgrounds/Background.png",IMG_DIR,alpha=False)
        
        # Back
        self.font_back = pygame.font.Font("fonts/MotionControl-BoldItalic.otf", 35)
        self.text_back = self.font_back.render("Back", True, (0,0,0))
        self.triangle = load_image("symbols/triangle32_b.png",IMG_DIR,alpha=True)
        
        # Change
        self.font_change = pygame.font.Font("fonts/MotionControl-BoldItalic.otf", 35)
        self.text_change = self.font_change.render("Change", True, (0,0,0))
        self.circle = load_image("symbols/circle32_b.png",IMG_DIR,alpha=True)
        
        # Select
        self.font_select = pygame.font.Font("fonts/MotionControl-BoldItalic.otf", 35)
        self.text_select = self.font_change.render("Select", True, (0,0,0))
        self.cross = load_image("symbols/cross32_b.png",IMG_DIR,alpha=True)
        
        # Instancia las manos
        self.mano1=Manito_1(340,270)
        self.mano2=Manito_2(400,270)
        
        # Carga Joysticks      
        if joy_on:
            self.p1 = pygame.joystick.Joystick(0) 
            self.p2 = pygame.joystick.Joystick(1)
            self.p1.init()
            self.p2.init()
        
        self.suma1=self.suma2=0

    def boton(self,x,y,ancho,alto,color1,color2):
        #self.mouse = pygame.mouse.get_pos() # Obtiene la posición del cursor del mouse
        #self.click = pygame.mouse.get_pressed() # Obtiene si se ha hecho click
        self.k = pygame.key.get_pressed()
        
        if joy_on:
            b0_1=self.p1.get_button(0)
            b0_2=self.p2.get_button(0)     
        
         # Si está dentro del rectángulo, cambia de color
        if (x + ancho > self.mano1.rect.left > x) and (y + alto > self.mano1.rect.top > y) or (x + ancho > self.mano2.rect.left > x) and (y + alto > self.mano2.rect.top > y):
            pygame.draw.rect(self.gameDisplay, color2, (x, y, ancho, alto))

            if self.mano1.rect.left>50 and self.mano1.rect.top>100 and self.mano1.rect.left<230 and self.mano1.rect.top<270:
                if joy_on:
                    if b0_1:
                        for i in range(5):
                            personajes_p1[i]=0
                        personajes_p1[0]=1
                        self.suma1=1
                        self.mano1.mano=load_image("symbols/hand_p1_t.png",IMG_DIR,alpha=True)
                        self.mano1.vel=0
                if self.k[K_RETURN]:
                    for i in range(5):
                        personajes_p1[i]=0
                    personajes_p1[0]=1
                    self.suma1=1
                    self.mano1.mano=load_image("symbols/hand_p1_t.png",IMG_DIR,alpha=True)
                    self.mano1.vel=0
                    
            elif self.mano1.rect.left>300 and self.mano1.rect.top>100 and self.mano1.rect.left<480 and self.mano1.rect.top<270:
                if joy_on:
                    if b0_1:
                        for i in range(5):
                            personajes_p1[i]=0
                        personajes_p1[1]=1
                        self.suma1=1
                        self.mano1.mano=load_image("symbols/hand_p1_t.png",IMG_DIR,alpha=True)
                        self.mano1.vel=0
                if self.k[K_RETURN]:
                    for i in range(5):
                        personajes_p1[i]=0
                    personajes_p1[1]=1
                    self.suma1=1
                    self.mano1.mano=load_image("symbols/hand_p1_t.png",IMG_DIR,alpha=True)
                    self.mano1.vel=0
                  
            elif self.mano1.rect.left>550 and self.mano1.rect.top>100 and self.mano1.rect.left<730 and self.mano1.rect.top<270:
                if joy_on:
                    if b0_1:
                        for i in range(5):
                            personajes_p1[i]=0
                        personajes_p1[2]=1
                        self.suma1=1
                        self.mano1.mano=load_image("symbols/hand_p1_t.png",IMG_DIR,alpha=True)
                        self.mano1.vel=0
                if self.k[K_RETURN]:
                    for i in range(5):
                        personajes_p1[i]=0
                    personajes_p1[2]=1
                    self.suma1=1
                    self.mano1.mano=load_image("symbols/hand_p1_t.png",IMG_DIR,alpha=True)
                    self.mano1.vel=0

                    
            elif self.mano1.rect.left>171 and self.mano1.rect.top>330 and self.mano1.rect.left<351 and self.mano1.rect.top<500:
                if joy_on:
                    if b0_1:
                        for i in range(5):
                            personajes_p1[i]=0
                        personajes_p1[3]=1
                        self.suma1=1
                        self.mano1.mano=load_image("symbols/hand_p1_t.png",IMG_DIR,alpha=True)
                        self.mano1.vel=0
                if self.k[K_RETURN]:
                    for i in range(5):
                        personajes_p1[i]=0
                    personajes_p1[3]=1
                    self.suma1=1
                    self.mano1.mano=load_image("symbols/hand_p1_t.png",IMG_DIR,alpha=True)
                    self.mano1.vel=0

            
            elif self.mano1.rect.left>425 and self.mano1.rect.top>330 and self.mano1.rect.left<605 and self.mano1.rect.top<500:
                if joy_on:
                    if b0_1:
                        for i in range(5):
                            personajes_p1[i]=0
                        personajes_p1[4]=1
                        self.suma1=1
                        self.mano1.mano=load_image("symbols/hand_p1_t.png",IMG_DIR,alpha=True)
                        self.mano1.vel=0
                if self.k[K_RETURN]:
                    for i in range(5):
                        personajes_p1[i]=0
                    personajes_p1[4]=1
                    self.suma1=1
                    self.mano1.mano=load_image("symbols/hand_p1_t.png",IMG_DIR,alpha=True)
                    self.mano1.vel=0

            
            
            
            ####################### MANO 2 #############################
            if self.mano2.rect.left>50 and self.mano2.rect.top>100 and self.mano2.rect.left<230 and self.mano2.rect.top<270:
                if joy_on:
                    if b0_2:
                        for i in range(5):
                            personajes_p2[i]=0
                        personajes_p2[0]=1
                        self.suma2=1
                        self.mano2.mano=load_image("symbols/hand_p2_t.png",IMG_DIR,alpha=True)
                        self.mano2.vel=0
                if self.k[K_1]:
                    for i in range(5):
                        personajes_p2[i]=0
                    personajes_p2[0]=1
                    self.suma2=1
                    self.mano2.mano=load_image("symbols/hand_p2_t.png",IMG_DIR,alpha=True)
                    self.mano2.vel=0
                    
            elif self.mano2.rect.left>300 and self.mano2.rect.top>100 and self.mano2.rect.left<480 and self.mano2.rect.top<270:
                if joy_on:
                    if b0_2:
                        for i in range(5):
                            personajes_p2[i]=0
                        personajes_p2[1]=1
                        self.suma2=1
                        self.mano2.mano=load_image("symbols/hand_p2_t.png",IMG_DIR,alpha=True)
                        self.mano2.vel=0
                if self.k[K_1]: 
                    for i in range(5):
                        personajes_p2[i]=0
                    personajes_p2[1]=1
                    self.suma2=1
                    self.mano2.mano=load_image("symbols/hand_p2_t.png",IMG_DIR,alpha=True)
                    self.mano2.vel=0
                    
            elif self.mano2.rect.left>550 and self.mano2.rect.top>100 and self.mano2.rect.left<730 and self.mano2.rect.top<270:
                if joy_on:
                    if b0_2:  
                        for i in range(5):
                            personajes_p2[i]=0
                        personajes_p2[2]=1
                        self.suma2=1
                        self.mano2.mano=load_image("symbols/hand_p2_t.png",IMG_DIR,alpha=True)
                        self.mano2.vel=0
                if self.k[K_1]:
                    for i in range(5):
                        personajes_p2[i]=0
                    personajes_p2[2]=1
                    self.suma2=1
                    self.mano2.mano=load_image("symbols/hand_p2_t.png",IMG_DIR,alpha=True)
                    self.mano2.vel=0
            
            elif self.mano2.rect.left>171 and self.mano2.rect.top>330 and self.mano2.rect.left<351 and self.mano2.rect.top<500:
                if joy_on:
                    if b0_2:   
                        for i in range(5):
                            personajes_p2[i]=0
                        personajes_p2[3]=1
                        self.suma2=1
                        self.mano2.mano=load_image("symbols/hand_p2_t.png",IMG_DIR,alpha=True)
                        self.mano2.vel=0
                if self.k[K_1]:
                    for i in range(5):
                        personajes_p2[i]=0
                    personajes_p2[3]=1
                    self.suma2=1
                    self.mano2.mano=load_image("symbols/hand_p2_t.png",IMG_DIR,alpha=True)
                    self.mano2.vel=0
            
            elif self.mano2.rect.left>425 and self.mano2.rect.top>330 and self.mano2.rect.left<605 and self.mano2.rect.top<500:
                if joy_on:
                    if b0_2:
                        for i in range(5):
                            personajes_p2[i]=0
                        personajes_p2[4]=1
                        self.suma2=1
                        self.mano2.mano=load_image("symbols/hand_p2_t.png",IMG_DIR,alpha=True)
                        self.mano2.vel=0
                if self.k[K_1]:
                    for i in range(5):
                        personajes_p2[i]=0
                    personajes_p2[4]=1
                    self.suma2=1
                    self.mano2.mano=load_image("symbols/hand_p2_t.png",IMG_DIR,alpha=True)
                    self.mano2.vel=0

        # Si no está dentro del rectángulo, no cambia de color
        else:
            pygame.draw.rect(self.gameDisplay, color1, (x, y, ancho, alto))
    
    def personaje(self,img, x, y):
        mapaImg = pygame.image.load(img)
        self.gameDisplay.blit(mapaImg, (x,y))
    
    def char_select(self):
        boton=Character.boton
        personaje=Character.personaje
        loop_char = True
        clock = pygame.time.Clock()
        up=down=left=right=cruz=circulo=False
        ar=ab=iz=de=x=o=False

        while loop_char:
                    
            for e in pygame.event.get():
                if e.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                
                if joy_on:
                    if e.type == pygame.JOYAXISMOTION:
                        a_1=self.p1.get_axis(0)
                        a_1y=self.p1.get_axis(1)
                        a_2=self.p2.get_axis(0)
                        a_2y=self.p2.get_axis(1)
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

                        # Para el p2
                        if e.joy==1:
                            if a_2>0.5:
                                de=True
                            elif a_2<-0.5: 
                                iz=True
                            else:
                                de=iz=False
                            if a_2y>0.5:
                                ab=True
                            elif a_2y<-0.5:
                                ar=True
                            else:
                                ar=ab=False
                            
                    if e.type == pygame.JOYBUTTONDOWN:
                        # Para el P1
                        if e.joy ==0:
                            if e.button==1:
                                circulo=True
                                for i in range(len(personajes_p1)):
                                    personajes_p1[i]=0
                                self.suma1=0
                                self.mano1.vel=8
                            if e.button==3:
                                loop_char=False
                       # Para el P2
                        if e.joy ==1: 
                            if e.button==1:
                                o=True
                                for i in range(len(personajes_p2)):
                                    personajes_p2[i]=0
                                self.suma2=0
                                self.mano2.vel=8
                            if e.button==3:
                                loop_char=False
                        
                    if e.type == pygame.JOYBUTTONUP:
                        if e.joy==0:
                            if e.button==0:
                                cruz=False
                            if e.button==1:
                                circulo=False
                        if e.joy==1:
                            if e.button==0:
                                x=False
                            if e.button==1:
                                o=False
                    
                if e.type == pygame.KEYDOWN:
                    if e.key == pygame.K_RETURN:
                        print("personaje seleccionado")
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
                    elif e.key == K_BACKSPACE:
                        circulo=True
                        for i in range(len(personajes_p1)):
                            personajes_p1[i]=0
                        self.suma1=0
                        
                    if e.key == K_w:
                        ar=True
                    elif e.key == K_s:
                        ab=True
                    elif e.key == K_a:
                        iz=True
                    elif e.key == K_d:
                        de=True
                    elif e.key == K_1:
                        x=True
                    elif e.key == K_2:
                        o=True
                        for i in range(len(personajes_p2)):
                            personajes_p2[i]=0
                        self.suma2=0
                        
                    elif e.key == K_ESCAPE:
                        button_A.play()
                        loop_char=False
                
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
                        
                    if e.key == K_w:
                        ar=False
                    if e.key == K_s:
                        ab=False
                    if e.key == K_a:
                        iz=False
                    if e.key == K_d:
                        de=False
                    elif e.key == K_1:
                        x=False
                    elif e.key == K_2:
                        o=False
            
            # Se dibuja el fondo
            self.gameDisplay.blit(self.backImg, (0, 0))
    
            # Función boton con sus parámetros    
            boton(self,50, 100, 180, 170, STEELBLUE, RED)
            boton(self,300, 100, 180, 170, STEELBLUE, RED)
            boton(self,550, 100, 180, 170, STEELBLUE, RED)
            boton(self,171, 330, 180, 170, STEELBLUE, RED)
            boton(self,425, 330, 180, 170, STEELBLUE, RED)
            
            # Función personaje con sus parámetros    
            personaje(self,'images/symbols/Anubis.png', 83, 130)
            personaje(self,'images/symbols/Astronaut.png', 335, 110)
            personaje(self,'images/symbols/Robot.png', 585, 115)
            personaje(self,'images/symbols/Soldier.png', 211, 350)
            personaje(self,'images/symbols/Thing.png', 458, 345)
    
            # Se dibuja el texto "Character Selection"
            self.gameDisplay.blit(self.text1,(230, 30))
            
            # Se dibuja el triangulo back y su texto
            self.gameDisplay.blit(self.triangle,(650,550))
            self.gameDisplay.blit(self.text_back,(690,548))
            self.gameDisplay.blit(self.circle,(500,550))
            self.gameDisplay.blit(self.text_change,(540,548))
            self.gameDisplay.blit(self.cross,(360,550))
            self.gameDisplay.blit(self.text_select,(400,548))
            
            self.mano1.movimiento(up,down,left,right,cruz,circulo)
            self.mano2.movimiento(ar,ab,iz,de,x,o)
            
            # Si la suma de ambos personajes es 2, carga seleccion de mapas
            suma_personajes=self.suma1+self.suma2
            if suma_personajes==2:
                up=down=left=right=cruz=circulo=False
                ar=ab=iz=de=x=o=False
                self.mano1.volver()
                self.mano2.volver()
                self.mano1=Manito_1(340,270)
                self.mano2=Manito_2(400,270)
                self.mano1.vel=8
                self.mano2.vel=8
                self.suma1=0
                self.suma2=0
                button_X.play()
                M = Maps()
                M.map_select()
                
            if break_main[0]==True:
                loop_char=False

            # Update
            pygame.display.update()
            clock.tick(60)
            
if __name__ == "__main__":
    C = Character()
    C.char_select()
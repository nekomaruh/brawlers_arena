# -*- coding: utf-8 -*-

import pygame, glob
from pygame import *
from Load_images import load_image, IMG_DIR
from Animations import *
from Variables import mov_E1, mov_E2, personajes_p1
from colores import GREEN, RED
from Screen import *

class Entity(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)     

class Platform(Entity):
    def __init__(self, x, y):
        Entity.__init__(self)
        self.image = Surface((0, 0))#tamaño color de los cuadrados
        self.image.convert()
        self.image.fill(Color("#00FF00"))
        self.rect = Rect(x, y, 3, 3)#tamaño del rectangulo de los cuadrados

    def update(self):
        pass

class ExitBlock(Platform):
    def __init__(self, x, y):
        Platform.__init__(self, x, y)
        self.image.fill(Color("#0033FF"))

############################ JUGADORES ################################

class Player1(Entity):
    def __init__(self,x,y):
        pygame.sprite.Sprite.__init__(self)
        self.x = x
        self.y = y
        
        if personajes_p1[1]==1:
            self.ani_speed_init=15 #velocidad inicial
        else:
            self.ani_speed_init=8 #velocidad inicial
        self.ani_speed=self.ani_speed_init
        # Cambiar con un if si es que se ingresa una variable (ani)
        if personajes_p1[0]==1:
            self.ani = glob.glob("images/sprites/anubis/walk/*.png")
            self.rect = Rect(x, y, 35, 55)
        elif personajes_p1[1]==1:
            self.ani = glob.glob("images/sprites/astro/walk/*.png")
            self.rect = Rect(x, y, 35, 45)
        elif personajes_p1[2]==1:
            self.ani = glob.glob("images/sprites/robot/walk/*.png")
            self.rect = Rect(x, y, 35, 45)
        elif personajes_p1[3]==1:
            self.ani = glob.glob("images/sprites/soldier/walk/*.png")
            self.rect = Rect(x, y, 35, 45)
        elif personajes_p1[4]==1:
            self.ani = glob.glob("images/sprites/thing/walk/*.png")
            self.rect = Rect(x, y, 35, 49)
        self.ani_pos=0
        self.ani_max=len(self.ani)-1
        self.image = pygame.image.load(self.ani[0])   
        self.gravity=0.9
        self.xvel=0
        self.yvel=0
        self.onGround = False
        self.doble = True
        self.pos_x = self.rect.left
        self.pos_y = self.rect.top

        self.arrow=load_image("symbols/arrow_p1.png",IMG_DIR,alpha=True)
    
    # Cambiar con un if si es que se ingresa una variable
    def update(self,pos,up,down,left,right,running,platforms,objetivo,attack,kick,bot):
        if personajes_p1[0]==1:
            handle_anubis.update1(self,pos,up,down,left,right,running,platforms,objetivo,attack,kick,bot)
        elif personajes_p1[1]==1:
            handle_astro.update1(self,pos,up,down,left,right,running,platforms,objetivo,attack,kick,bot)    
        elif personajes_p1[2]==1:
            handle_robot.update1(self,pos,up,down,left,right,running,platforms,objetivo,attack,kick,bot)  
        elif personajes_p1[3]==1:
            handle_soldado.update1(self,pos,up,down,left,right,running,platforms,objetivo,attack,kick,bot)
        elif personajes_p1[4]==1:
            handle_thing.update1(self,pos,up,down,left,right,running,platforms,objetivo,attack,kick,bot)
        screen.blit(self.arrow,(self.rect.left+6,self.rect.top-35))
        
            
    def collide(self, xvel, yvel, platforms):
        for p in platforms:
            if pygame.sprite.collide_rect(self, p):
                if isinstance(p, ExitBlock):
                    pygame.event.post(pygame.event.Event(QUIT))
                if xvel > 0:
                    # Colisiona a la derecha
                    self.rect.right = p.rect.left
                if xvel < 0:
                    # Colisiona a la izquierda
                    self.rect.left = p.rect.right
                if yvel > 0:
                    self.rect.bottom = p.rect.top
                    self.onGround = True
                    self.yvel = 0
                if yvel < 0:
                    self.rect.top = p.rect.bottom 
                
    def colision(self, xvel, yvel, objetivo):
        if pygame.sprite.collide_rect(self,objetivo):
            if isinstance(objetivo, ExitBlock):
                pygame.event.post(pygame.event.Event(QUIT))
            if xvel>0:
                self.rect.right = objetivo.rect.left
            elif xvel<0:
                self.rect.left = objetivo.rect.right
                xvel=0
            elif yvel >0:
                self.rect.bottom = objetivo.rect.top
                self.onGround = True
                self.yvel=0
            elif yvel<0:
                self.rect.top=objetivo.rect.bottom
                self.yvel=0
    def get_pos_x(self):
        return self.rect.left
    def get_pos_y(self):
        return self.rect.top
    
class Player2(Entity):
    def __init__(self,x,y):
        pygame.sprite.Sprite.__init__(self)
        self.x = x
        self.y = y
        if personajes_p2[1]==1:
            self.ani_speed_init=15 #velocidad inicial
        else:
            self.ani_speed_init=8 #velocidad inicial
        self.ani_speed=self.ani_speed_init
        self.ani_speed=self.ani_speed_init
        # Cambiar con un if si es que se ingresa una variable (ani)
        if personajes_p2[0]==1:
            self.ani = glob.glob("images/sprites/anubis/walk/*.png")
            self.rect = Rect(x, y, 35, 55)
        elif personajes_p2[1]==1:
            self.ani = glob.glob("images/sprites/astro/walk/*.png")
            self.rect = Rect(x, y, 35, 45)
        elif personajes_p2[2]==1:
            self.ani = glob.glob("images/sprites/robot/walk/*.png")
            self.rect = Rect(x, y, 35, 45)
        elif personajes_p2[3]==1:
            self.ani = glob.glob("images/sprites/soldier/walk/*.png")
            self.rect = Rect(x, y, 35, 45)
        elif personajes_p2[4]==1:
            self.ani = glob.glob("images/sprites/thing/walk/*.png")
            self.rect = Rect(x, y, 35, 49)
        self.ani_pos=0
        self.ani_max=len(self.ani)-1
        self.image = pygame.image.load(self.ani[0])   
        self.gravity=0.9
        self.xvel=0
        self.yvel=0
        self.onGround = False
        self.doble = True
        self.arrow=load_image("symbols/arrow_p2.png",IMG_DIR,alpha=True)
    
    # Cambiar con un if si es que se ingresa una variable
    def update(self,pos,up,down,left,right,running,platforms,objetivo,attack,kick,bot):
        if personajes_p2[0]==1:
            handle_anubis.update1(self,pos,up,down,left,right,running,platforms,objetivo,attack,kick,bot)  
        elif personajes_p2[1]==1:
            handle_astro.update1(self,pos,up,down,left,right,running,platforms,objetivo,attack,kick,bot)    
        elif personajes_p2[2]==1:
            handle_robot.update1(self,pos,up,down,left,right,running,platforms,objetivo,attack,kick,bot) 
        elif personajes_p2[3]==1:
            handle_soldado.update1(self,pos,up,down,left,right,running,platforms,objetivo,attack,kick,bot)
        elif personajes_p2[4]==1:
            handle_thing.update1(self,pos,up,down,left,right,running,platforms,objetivo,attack,kick,bot)
        screen.blit(self.arrow,(self.rect.left+6,self.rect.top-35))
            
    def collide(self, xvel, yvel, platforms):
        for p in platforms:
            if pygame.sprite.collide_rect(self, p):
                if isinstance(p, ExitBlock):
                    pygame.event.post(pygame.event.Event(QUIT))
                if xvel > 0:
                    # Colisiona a la derecha
                    self.rect.right = p.rect.left
                if xvel < 0:
                    # Colisiona a la izquierda
                    self.rect.left = p.rect.right
                if yvel > 0:
                    self.rect.bottom = p.rect.top
                    self.onGround = True
                    self.yvel = 0
                if yvel < 0:
                    self.rect.top = p.rect.bottom 
                
    def colision(self, xvel, yvel, objetivo):
        if pygame.sprite.collide_rect(self,objetivo):
            if isinstance(objetivo, ExitBlock):
                pygame.event.post(pygame.event.Event(QUIT))
            if xvel>0:
                self.rect.right = objetivo.rect.left
            elif xvel<0:
                self.rect.left = objetivo.rect.right
                xvel=0
            elif yvel >0:
                self.rect.bottom = objetivo.rect.top
                self.onGround = True
                self.yvel=0
            elif yvel<0:
                self.rect.top=objetivo.rect.bottom
                self.yvel=0
    def get_pos_x(self):
        return self.rect.left
    def get_pos_y(self):
        return self.rect.top
############################### ENEMIGOS ######################################


class Power(Entity):
    def __init__(self,x,y):
        pygame.sprite.Sprite.__init__(self)
        self.x = x
        self.y = y
        self.ani_speed_init=8 #velocidad inicial
        self.ani_speed=self.ani_speed_init
        # Cambiar con un if si es que se ingresa una variable (ani)
        self.ani = glob.glob("images/sprites/boost_time/walk/*.png")
        self.ani_pos=0
        self.ani_max=len(self.ani)-1
        self.image = pygame.image.load(self.ani[0])
        self.gravity=0.9
        self.rect = Rect(x, y, 40, 45)
        self.xvel=0
        self.yvel=0
        self.onGround = False
        self.doble = True
    
    # Cambiar con un if si es que se ingresa una variable      
    def update(self):
        pos=0
        pos+=1
        self.ani_speed-=1
        self.x+=pos
        if self.ani_speed==0:
            self.image=pygame.image.load(self.ani[self.ani_pos])
            self.ani_speed=self.ani_speed_init
            if self.ani_pos==self.ani_max:
                self.ani_pos=0
            else:
                self.ani_pos+=1
        self.r=self.image
    def get_pos_x(self):
        return self.rect.left
    def get_pos_y(self):
        return self.rect.top

class Animacion_rules_1(Entity):
    def __init__(self,x,y):
        pygame.sprite.Sprite.__init__(self)
        self.x = x
        self.y = y
        self.ani_speed_init=8 #velocidad inicial
        self.ani_speed=self.ani_speed_init
        # Cambiar con un if si es que se ingresa una variable (ani)
        self.ani = glob.glob("images/sprites/all/walk/*.png")
        self.ani_pos=0
        self.ani_max=len(self.ani)-1
        self.image = pygame.image.load(self.ani[0])
        self.gravity=0.9
        self.rect = Rect(x, y, 40, 45)
        self.xvel=0
        self.yvel=0
        self.onGround = False
        self.doble = True
    
    # Cambiar con un if si es que se ingresa una variable      
    def update(self):
        pos=1
        pos+=pos
        self.ani_speed-=1
        self.x+=pos
        if self.ani_speed==0:
            self.image=pygame.image.load(self.ani[self.ani_pos])
            self.ani_speed=self.ani_speed_init
            if self.ani_pos==self.ani_max:
                self.ani_pos=0
            else:
                self.ani_pos+=1
        self.r=self.image
    def get_rect(self):
        return rect

class E1(Entity):
    def __init__(self,x,y):
        pygame.sprite.Sprite.__init__(self)
        self.x = x
        self.y = y
        self.ani_speed_init=10 #velocidad inicial
        self.ani_speed=self.ani_speed_init
        # Cambiar con un if si es que se ingresa una variable (ani)
        if mapas[0]==1:
            self.ani = glob.glob("images/sprites/ghost/walk/*.png")
            self.rect = Rect(x, y, 26, 36) # BOSQUE
        elif mapas[1]==1:
            self.ani = glob.glob("images/sprites/duck/walk/*.png")
            self.rect = Rect(x, y, 32, 36) # KAWAI
        elif mapas[2]==1:
            self.ani = glob.glob("images/sprites/prototype/walk/*.png")
            self.rect = Rect(x, y, 48, 48) # CIUDAD
        elif mapas[3]==1:
            self.ani = glob.glob("images/sprites/mummy/walk/*.png")
            self.rect = Rect(x, y, 26, 48) # DESIERTO
        elif mapas[4]==1:
            self.ani = glob.glob("images/sprites/ufo/walk/*.png")
            self.rect = Rect(x, y, 35, 48) # PLANETAS
        self.ani_pos=0
        self.ani_max=len(self.ani)-1
        self.image = pygame.image.load(self.ani[0])   
        self.gravity=0.9
        self.xvel=1
        self.yvel=1
        self.onGround = False
        self.doble = True
        self.move=1
        self.life=30
        self.eliminado=False
        self.saltar=False
        self.c_saltar=0
        self.estado=1
        self.punio=False
        
    def life_bar(self,health):
        health=self.life
        if self.eliminado == False:
            if health >8:
                health_color = GREEN
            else:
                health_color= RED
            pygame.draw.rect(screen,health_color,(self.rect.left-8,self.rect.top-10,health,5))
        
    # Cambiar con un if si es que se ingresa una variable
    def update(self,pos,jump,down,move,platforms,objetivo,attack,punio,enemigo):
        punio=self.punio
        if self.eliminado==False:        
            if mapas[0]==1:
                if self.estado==1:
                    handle_ghost.state_1(self,pos,jump,down,move,platforms,objetivo,attack,punio,enemigo) 
                elif self.estado==2:
                    handle_ghost.state_2(self,pos,jump,down,move,platforms,objetivo,attack,punio,enemigo) 
                elif self.estado==3:
                    handle_ghost.state_3(self,pos,jump,down,move,platforms,objetivo,attack,punio,enemigo)
                
            elif mapas[1]==1:
                if self.estado==1:
                    handle_duck.state_1(self,pos,jump,down,move,platforms,objetivo,attack,punio,enemigo) 
                elif self.estado==2:
                    handle_duck.state_2(self,pos,jump,down,move,platforms,objetivo,attack,punio,enemigo) 
                elif self.estado==3:
                    handle_duck.state_3(self,pos,jump,down,move,platforms,objetivo,attack,punio,enemigo) 
                
            elif mapas[2]==1:
                if self.estado==1:
                    handle_prototype.state_1(self,pos,jump,down,move,platforms,objetivo,attack,punio,enemigo)
                elif self.estado==2:
                    handle_prototype.state_2(self,pos,jump,down,move,platforms,objetivo,attack,punio,enemigo)
                elif self.estado==3:
                    handle_prototype.state_3(self,pos,jump,down,move,platforms,objetivo,attack,punio,enemigo)
                
            elif mapas[3]==1:
                if self.estado==1:
                    handle_mummy.state_1(self,pos,jump,down,move,platforms,objetivo,attack,punio,enemigo)
                elif self.estado==2:
                    handle_mummy.state_2(self,pos,jump,down,move,platforms,objetivo,attack,punio,enemigo)
                elif self.estado==3:
                    handle_mummy.state_3(self,pos,jump,down,move,platforms,objetivo,attack,punio,enemigo)
            
            elif mapas[4]==1:
                if self.estado==1:
                    handle_ufo.state_1(self,pos,jump,down,move,platforms,objetivo,attack,punio,enemigo)
                elif self.estado==2:
                    handle_ufo.state_2(self,pos,jump,down,move,platforms,objetivo,attack,punio,enemigo) 
                elif self.estado==3:
                    handle_ufo.state_3(self,pos,jump,down,move,platforms,objetivo,attack,punio,enemigo) 
            
    def collide(self, xvel, yvel, platforms):
        for p in platforms:
            if pygame.sprite.collide_rect(self, p):
                if isinstance(p, ExitBlock):
                    pygame.event.post(pygame.event.Event(QUIT))
                if xvel > 0:
                    # Colisiona a la derecha
                    self.rect.right = p.rect.left
                    self.move=-1
                if xvel < 0:
                    # Colisiona a la izquierda
                    self.rect.left = p.rect.right
                    self.move=1
                if yvel > 0:
                    self.rect.bottom = p.rect.top
                    self.onGround = True
                    self.yvel = 0
                if yvel < 0:
                    self.rect.top = p.rect.bottom 
                
    def colision(self, xvel, yvel, objetivo):
        if pygame.sprite.collide_rect(self,objetivo):

            if isinstance(objetivo, ExitBlock):
                pygame.event.post(pygame.event.Event(QUIT))
            
            if xvel>0:
                self.rect.right = objetivo.rect.left
                xvel=0
                
            elif xvel<0:
                self.rect.left = objetivo.rect.right
                xvel=0
            elif yvel >0:
                self.rect.bottom = objetivo.rect.top
                self.onGround = True
                #self.yvel=0
            elif yvel<0:
                self.rect.top=objetivo.rect.bottom
                #self.yvel=0
                

    def get_pos_x(self):
        return self.rect.left
    def get_pos_y(self):
        return self.rect.top
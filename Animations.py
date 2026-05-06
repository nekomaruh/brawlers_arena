# -*- coding: utf-8 -*-
import pygame
from Load_images import load_image, IMG_DIR
from Music_sounds import *
import random
from Variables import *
from Panel import Score1

###### ATAQUES MELEE #####
kr_sold=[load_image("sprites/soldier/7.png", IMG_DIR, alpha=True),
           load_image("sprites/soldier/melee/0.png", IMG_DIR, alpha=True),
           load_image("sprites/soldier/melee/1.png", IMG_DIR, alpha=True)]        
           
kl_sold=[load_image("sprites/soldier/15.png", IMG_DIR, alpha=True),
           load_image("sprites/soldier/melee/2.png", IMG_DIR, alpha=True),
           load_image("sprites/soldier/melee/3.png", IMG_DIR, alpha=True)]
           
kr_robo=[load_image("sprites/robot/6.png", IMG_DIR, alpha=True),
           load_image("sprites/robot/melee/0.png", IMG_DIR, alpha=True),
           load_image("sprites/robot/melee/1.png", IMG_DIR, alpha=True)]  
           
kl_robo=[load_image("sprites/robot/7.png", IMG_DIR, alpha=True),
           load_image("sprites/robot/melee/2.png", IMG_DIR, alpha=True),
           load_image("sprites/robot/melee/3.png", IMG_DIR, alpha=True)]
           
kr_thin=[load_image("sprites/thing/7.png", IMG_DIR, alpha=True),
           load_image("sprites/thing/melee/0.png", IMG_DIR, alpha=True),
           load_image("sprites/thing/melee/1.png", IMG_DIR, alpha=True)]  
           
kl_thin=[load_image("sprites/thing/15.png", IMG_DIR, alpha=True),
           load_image("sprites/thing/melee/2.png", IMG_DIR, alpha=True),
           load_image("sprites/thing/melee/3.png", IMG_DIR, alpha=True)]
           
kr_astr=[load_image("sprites/astro/7.png", IMG_DIR, alpha=True),
           load_image("sprites/astro/melee/0.png", IMG_DIR, alpha=True),
           load_image("sprites/astro/melee/1.png", IMG_DIR, alpha=True)]  
           
kl_astr=[load_image("sprites/astro/15.png", IMG_DIR, alpha=True),
           load_image("sprites/astro/melee/2.png", IMG_DIR, alpha=True),
           load_image("sprites/astro/melee/3.png", IMG_DIR, alpha=True)]
           
kr_anub=[load_image("sprites/anubis/6.png", IMG_DIR, alpha=True),
           load_image("sprites/anubis/melee/0.png", IMG_DIR, alpha=True),
           load_image("sprites/anubis/melee/1.png", IMG_DIR, alpha=True)] 
           
kl_anub=[load_image("sprites/anubis/13.png", IMG_DIR, alpha=True),
           load_image("sprites/anubis/melee/2.png", IMG_DIR, alpha=True),
           load_image("sprites/anubis/melee/3.png", IMG_DIR, alpha=True)]

kr_ufo=[load_image("sprites/ufo/melee/0.png", IMG_DIR, alpha=True),
        load_image("sprites/ufo/melee/2.png", IMG_DIR, alpha=True),
        load_image("sprites/ufo/melee/2.png", IMG_DIR, alpha=True)]
           
kl_ufo=[load_image("sprites/ufo/melee/4.png", IMG_DIR, alpha=True),
        load_image("sprites/ufo/melee/5.png", IMG_DIR, alpha=True),
        load_image("sprites/ufo/melee/5.png", IMG_DIR, alpha=True)]

kr_duck=[load_image("sprites/duck/3.png", IMG_DIR, alpha=True)]
           
kl_duck=[load_image("sprites/duck/6.png", IMG_DIR, alpha=True)]

kr_mummy=[load_image("sprites/mummy/1.png", IMG_DIR, alpha=True)]
kl_mummy=[load_image("sprites/mummy/4.png", IMG_DIR, alpha=True)]

kr_prot=[load_image("sprites/prototype/melee/2.png", IMG_DIR, alpha=True)]
kl_prot=[load_image("sprites/prototype/melee/3.png", IMG_DIR, alpha=True)]
    

class handle_soldado:
    def update1(self,pos,up,down,left,right,running,platforms,objetivo,attack,kick,bot):
        if right:
            if kick:
                kick_right=random.randint(0,2)
                self.image=kr_sold[kick_right]
                button_kick.play()
                button_kick.set_volume(sou[0])
            self.xvel = 4
            if running:
                self.xvel+=4
            pos=1
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

        if left:
            if kick:
                kick_left=random.randint(0,2)
                self.image=kl_sold[kick_left]
                button_kick.play()
                button_kick.set_volume(sou[0])
            self.xvel = -4
            if running:
                self.xvel-=4
            pos=-1
            self.ani_speed-=1
            self.x+=pos
            if self.ani_speed==0:
                self.image=pygame.image.load(self.ani[self.ani_pos])
                self.image = pygame.transform.flip(self.image,True,False)
                self.ani_speed=self.ani_speed_init
                if self.ani_pos==self.ani_max:
                    self.ani_pos=0
                else:
                    self.ani_pos+=1
            self.l=self.image
        
        elif pos == 0:
                self.image=pygame.image.load("images/sprites/soldier/0.png")
                
        if self.onGround:
            if up:
                self.yvel -= 13
                self.doble=True
        
        else:
            # Solo acelera con gravedad si esta en el aire
            self.yvel += self.gravity
            
            if self.yvel>0 and self.doble==True:               
                if up:
                    self.yvel -= 12
                    self.doble=False
                    if left:
                        self.image=load_image("sprites/soldier/12.png", IMG_DIR, alpha=True)
                    if right:
                        self.image=load_image("sprites/soldier/4.png", IMG_DIR, alpha=True)
        
        if not(left or right):
            pos=0
            self.xvel = 0
            
        # Incrementa en x
        self.rect.left += self.xvel
        # Colisiones en x
        self.collide(self.xvel, 0, platforms)
        self.colision(self.xvel,0,objetivo)
        self.colision(self.xvel,0,bot)
        # Incrementa en y
        self.rect.top += self.yvel
        # Se asume que esta en el aire
        self.onGround = False;
        # Colisiones en y
        self.collide(0, self.yvel, platforms)
        self.colision(0, self.yvel, objetivo)
        self.colision(0,self.yvel,bot)

        
class handle_robot:
    def update1(self,pos,up,down,left,right,running,platforms,objetivo,attack,kick,bot):
        if right:
            if kick:
                kick_right=random.randint(0,2)
                self.image=kr_robo[kick_right]
                button_kick.play()
                button_kick.set_volume(sou[0])
            self.xvel = 5
            if running:
                self.xvel+=4
            pos=1
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

        if left:
            if kick:
                kick_left=random.randint(0,2)
                self.image=kl_robo[kick_left]
                button_kick.play()
                button_kick.set_volume(sou[0])
            self.xvel = -5
            if running:
                self.xvel-=4
            pos=-1
            self.ani_speed-=1
            self.x+=pos
            if self.ani_speed==0:
                self.image=pygame.image.load(self.ani[self.ani_pos])
                self.image = pygame.transform.flip(self.image,True,False)
                self.ani_speed=self.ani_speed_init
                if self.ani_pos==self.ani_max:
                    self.ani_pos=0
                else:
                    self.ani_pos+=1
            self.l=self.image
        
        elif pos == 0:
                self.image=pygame.image.load("images/sprites/robot/1.png")
        
        if self.onGround:
            if up:
                self.yvel -= 13
                self.doble=True
        
        else:
            # Solo acelera con gravedad si esta en el aire
            self.yvel += self.gravity
            
            if self.yvel>0 and self.doble==True:               
                if up:
                    self.yvel -= 10
                    self.doble=False
                    if left:
                        self.image=load_image("sprites/robot/9.png", IMG_DIR, alpha=True)
                    if right:
                        self.image=load_image("sprites/robot/8.png", IMG_DIR, alpha=True)
        
        if not(left or right):
            pos=0
            self.xvel = 0
            
        # Incrementa en x
        self.rect.left += self.xvel
        # Colisiones en x
        self.collide(self.xvel, 0, platforms)
        self.colision(self.xvel,0,objetivo)
        # Incrementa en y
        self.rect.top += self.yvel
        # Se asume que esta en el aire
        self.onGround = False;
        # Colisiones en y
        self.collide(0, self.yvel, platforms)
        self.colision(0, self.yvel, objetivo)
        
        self.colision(self.xvel,0,bot)
        self.colision(0,self.yvel,bot)
        
class handle_thing:
    def update1(self,pos,up,down,left,right,running,platforms,objetivo,attack,kick,bot):
        if right:
            if kick:
                kick_right=random.randint(0,2)
                self.image=kr_thin[kick_right]
                button_kick.play()
                button_kick.set_volume(sou[0])
            self.xvel = 4
            if running:
                self.xvel+=4
            pos=1
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

        if left:
            if kick:
                kick_left=random.randint(0,2)
                self.image=kl_thin[kick_left]
                button_kick.play()
                button_kick.set_volume(sou[0])
            self.xvel = -4
            if running:
                self.xvel-=4
            pos=-1
            self.ani_speed-=1
            self.x+=pos
            if self.ani_speed==0:
                self.image=pygame.image.load(self.ani[self.ani_pos])
                self.image = pygame.transform.flip(self.image,True,False)
                self.ani_speed=self.ani_speed_init
                if self.ani_pos==self.ani_max:
                    self.ani_pos=0
                else:
                    self.ani_pos+=1
            self.l=self.image
        
        elif pos == 0:
                self.image=pygame.image.load("images/sprites/thing/2.png")
        
        if self.onGround:
            if up:
                self.yvel -= 13
                self.doble=True
        
        else:
            # Solo acelera con gravedad si esta en el aire
            self.yvel += self.gravity
            
            if self.yvel>0 and self.doble==True:               
                if up:
                    self.yvel -= 12
                    self.doble=False
                    if left:
                        self.image=load_image("sprites/thing/12.png", IMG_DIR, alpha=True)
                    if right:
                        self.image=load_image("sprites/thing/4.png", IMG_DIR, alpha=True)
        
        if not(left or right):
            pos=0
            self.xvel = 0
            
        # Incrementa en x
        self.rect.left += self.xvel
        # Colisiones en x
        self.collide(self.xvel, 0, platforms)
        self.colision(self.xvel,0,objetivo)
        # Incrementa en y
        self.rect.top += self.yvel
        # Se asume que esta en el aire
        self.onGround = False;
        # Colisiones en y
        self.collide(0, self.yvel, platforms)
        self.colision(0, self.yvel, objetivo)
        
        self.colision(self.xvel,0,bot)
        self.colision(0,self.yvel,bot)

class handle_astro:
    def update1(self,pos,up,down,left,right,running,platforms,objetivo,attack,kick,bot):
        if right:
            if kick:
                kick_right=random.randint(0,2)
                self.image=kr_astr[kick_right]
                button_kick.play()
                button_kick.set_volume(sou[0])
            self.xvel = 3
            if running:
                self.xvel+=4
            pos=1
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

        if left:
            if kick:
                kick_left=random.randint(0,2)
                self.image=kl_astr[kick_left]
                button_kick.play()
                button_kick.set_volume(sou[0])
            self.xvel = -3
            if running:
                self.xvel-=4
            pos=-1
            self.ani_speed-=1
            self.x+=pos
            if self.ani_speed==0:
                self.image=pygame.image.load(self.ani[self.ani_pos])
                self.image = pygame.transform.flip(self.image,True,False)
                self.ani_speed=self.ani_speed_init
                if self.ani_pos==self.ani_max:
                    self.ani_pos=0
                else:
                    self.ani_pos+=1
            self.l=self.image
        
        elif pos == 0:
                self.image=pygame.image.load("images/sprites/astro/1.png")
        
        if self.onGround:
            if up:
                self.yvel -= 13
                self.doble=True
        
        else:
            # Solo acelera con gravedad si esta en el aire
            self.yvel += 0.5
            
            if self.yvel>0 and self.doble==True:               
                if up:
                    self.yvel -= 10
                    self.doble=False
                    if left:
                        self.image=load_image("sprites/astro/12.png", IMG_DIR, alpha=True)
                    if right:
                        self.image=load_image("sprites/astro/4.png", IMG_DIR, alpha=True)
        
        if not(left or right):
            pos=0
            self.xvel = 0
            
        # Incrementa en x
        self.rect.left += self.xvel
        # Colisiones en x
        self.collide(self.xvel, 0, platforms)
        self.colision(self.xvel,0,objetivo)
        # Incrementa en y
        self.rect.top += self.yvel
        # Se asume que esta en el aire
        self.onGround = False;
        # Colisiones en y
        self.collide(0, self.yvel, platforms)
        self.colision(0, self.yvel, objetivo)
        
        self.colision(self.xvel,0,bot)
        self.colision(0,self.yvel,bot)

        
class handle_anubis:
    def update1(self,pos,up,down,left,right,running,platforms,objetivo,attack,kick,bot):
        if right:
            if kick:
                kick_right=random.randint(0,2)
                self.image=kr_anub[kick_right]
                button_kick.play()
                button_kick.set_volume(sou[0])
            self.xvel = 4
            if running:
                self.xvel+=4
            pos=1
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

        if left:
            if kick:
                kick_left=random.randint(0,2)
                self.image=kl_anub[kick_left]
                button_kick.play()
                button_kick.set_volume(sou[0])
            self.xvel = -4
            if running:
                self.xvel-=4
            pos=-1
            self.ani_speed-=1
            self.x+=pos
            if self.ani_speed==0:
                self.image=pygame.image.load(self.ani[self.ani_pos])
                self.image = pygame.transform.flip(self.image,True,False)
                self.ani_speed=self.ani_speed_init
                if self.ani_pos==self.ani_max:
                    self.ani_pos=0
                else:
                    self.ani_pos+=1
            self.l=self.image
        
        elif pos == 0:
                self.image=pygame.image.load("images/sprites/anubis/0.png")
        
        if self.onGround:
            if up:
                self.yvel -= 13
                self.doble=True
        
        else:
            # Solo acelera con gravedad si esta en el aire
            self.yvel += self.gravity
            
            if self.yvel>0 and self.doble==True:               
                if up:
                    self.yvel -= 12
                    self.doble=False
                    if left:
                        self.image=load_image("sprites/anubis/15.png", IMG_DIR, alpha=True)
                    if right:
                        self.image=load_image("sprites/anubis/14.png", IMG_DIR, alpha=True)
        
        if not(left or right):
            pos=0
            self.xvel = 0
            
        # Incrementa en x
        self.rect.left += self.xvel
        # Colisiones en x
        self.collide(self.xvel, 0, platforms)
        self.colision(self.xvel,0,objetivo)
        # Incrementa en y
        self.rect.top += self.yvel
        # Se asume que esta en el aire
        self.onGround = False;
        # Colisiones en y
        self.collide(0, self.yvel, platforms)
        self.colision(0, self.yvel, objetivo)
        
        self.colision(self.xvel,0,bot)
        self.colision(0,self.yvel,bot)

class handle_ufo:
    def state_1(self,pos,jump,down,move,platforms,objetivo,attack,punio,enemigo):
        #move=mov_E1[0]
        if self.move==1:
            self.xvel = 2
            pos=1
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

        if self.move==-1:
            self.xvel = -2
            pos=-1
            self.ani_speed-=1
            self.x+=pos
            if self.ani_speed==0:
                self.image=pygame.image.load(self.ani[self.ani_pos])
                self.image = pygame.transform.flip(self.image,True,False)
                self.ani_speed=self.ani_speed_init
                if self.ani_pos==self.ani_max:
                    self.ani_pos=0
                else:
                    self.ani_pos+=1
            self.l=self.image     
        
        if self.onGround:
            if jump:
                self.yvel -= 15
                self.doble=True
        
        
        else:
            # Solo acelera con gravedad si esta en el aire
            self.yvel += self.gravity
            
            if self.yvel>0 and self.doble==True:               
                if jump:
                    self.yvel -= 15
                    self.doble=False
            
        # Incrementa en x
        self.rect.left += self.xvel
        # Colisiones en x
        self.collide(self.xvel, 0,platforms)
        self.colision(self.xvel,0,objetivo)
        self.colision(self.xvel,0,enemigo)
        # Incrementa en y
        self.rect.top += self.yvel
        # Se asume que esta en el aire
        self.onGround = False;
        # Colisiones en y
        self.collide(0, self.yvel, platforms)
        self.colision(0, self.yvel, objetivo)
        self.colision(0, self.yvel, enemigo)
        
    def state_2(self,pos,jump,down,move,platforms,objetivo,attack,punio,enemigo):
        #move=mov_E1[0]
        if self.move==1:
            if punio:
                kick_right=random.randint(0,2)
                self.image=kr_ufo[kick_right]
                ufo_golpe.play()
                ufo_golpe.set_volume(sou[0])
            self.xvel = 2
            pos=1
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

        if self.move==-1:
            if punio:
                kick_left=random.randint(0,2)
                self.image=kl_ufo[kick_left]
                ufo_golpe.play()
                ufo_golpe.set_volume(sou[0])
            self.xvel = -2
            pos=-1
            self.ani_speed-=1
            self.x+=pos
            if self.ani_speed==0:
                self.image=pygame.image.load(self.ani[self.ani_pos])
                self.image = pygame.transform.flip(self.image,True,False)
                self.ani_speed=self.ani_speed_init
                if self.ani_pos==self.ani_max:
                    self.ani_pos=0
                else:
                    self.ani_pos+=1
            self.l=self.image     
        
        if self.onGround:
            if jump:
                self.yvel -= 15
                self.doble=True
        
        
        else:
            # Solo acelera con gravedad si esta en el aire
            self.yvel += self.gravity
            
            if self.yvel>0 and self.doble==True:               
                if jump:
                    self.yvel -= 15
                    self.doble=False
            
        # Incrementa en x
        self.rect.left += self.xvel
        # Colisiones en x
        self.collide(self.xvel, 0,platforms)
        self.colision(self.xvel,0,objetivo)
        self.colision(self.xvel,0,enemigo)
        # Incrementa en y
        self.rect.top += self.yvel
        # Se asume que esta en el aire
        self.onGround = False;
        # Colisiones en y
        self.collide(0, self.yvel, platforms)
        self.colision(0, self.yvel, objetivo)
        self.colision(0, self.yvel, enemigo)
        
    def state_3(self,pos,jump,down,move,platforms,objetivo,attack,punio,enemigo):
        #move=mov_E1[0]
        if self.move==1:
            if punio:
                kick_right=random.randint(0,2)
                self.image=kr_ufo[kick_right]
                ufo_golpe.play()
                ufo_golpe.set_volume(sou[0])
            self.xvel = 3
            pos=1
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

        if self.move==-1:
            if punio:
                kick_left=random.randint(0,2)
                self.image=kl_ufo[kick_left]
                ufo_golpe.play()
                ufo_golpe.set_volume(sou[0])
            self.xvel = -3
            pos=-1
            self.ani_speed-=1
            self.x+=pos
            if self.ani_speed==0:
                self.image=pygame.image.load(self.ani[self.ani_pos])
                self.image = pygame.transform.flip(self.image,True,False)
                self.ani_speed=self.ani_speed_init
                if self.ani_pos==self.ani_max:
                    self.ani_pos=0
                else:
                    self.ani_pos+=1
            self.l=self.image     
        
        if self.onGround:
            if jump:
                self.yvel -= 15
                self.doble=True
        
        
        else:
            # Solo acelera con gravedad si esta en el aire
            self.yvel += self.gravity
            
            if self.yvel>0 and self.doble==True:               
                if jump:
                    self.yvel -= 15
                    self.doble=False
            
        # Incrementa en x
        self.rect.left += self.xvel
        # Colisiones en x
        self.collide(self.xvel, 0,platforms)
        self.colision(self.xvel,0,objetivo)
        self.colision(self.xvel,0,enemigo)
        # Incrementa en y
        self.rect.top += self.yvel
        # Se asume que esta en el aire
        self.onGround = False;
        # Colisiones en y
        self.collide(0, self.yvel, platforms)
        self.colision(0, self.yvel, objetivo)
        self.colision(0, self.yvel, enemigo)

class handle_duck:
    def state_1(self,pos,jump,down,move,platforms,objetivo,attack,punio,enemigo):

        if self.move==1:
            self.xvel = 2
            pos=1
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

        if self.move==-1:
            self.xvel = -2
            pos=-1
            self.ani_speed-=1
            self.x+=pos
            if self.ani_speed==0:
                self.image=pygame.image.load(self.ani[self.ani_pos])
                self.image = pygame.transform.flip(self.image,True,False)
                self.ani_speed=self.ani_speed_init
                if self.ani_pos==self.ani_max:
                    self.ani_pos=0
                else:
                    self.ani_pos+=1
            self.l=self.image     
        
        if self.onGround:
            if jump:
                self.yvel -= 15
                self.doble=True
                
        else:
            # Solo acelera con gravedad si esta en el aire
            self.yvel += self.gravity
            
            if self.yvel>0 and self.doble==True:               
                if jump:
                    self.yvel -= 15
                    self.doble=False
            
        # Incrementa en x
        self.rect.left += self.xvel
        # Colisiones en x
        self.collide(self.xvel, 0,platforms)
        self.colision(self.xvel,0,objetivo)
        self.colision(self.xvel,0,enemigo)
        # Incrementa en y
        self.rect.top += self.yvel
        # Se asume que esta en el aire
        self.onGround = False;
        # Colisiones en y
        self.collide(0, self.yvel, platforms)
        self.colision(0, self.yvel, objetivo)
        self.colision(0, self.yvel, enemigo)
        
    def state_2(self,pos,jump,down,move,platforms,objetivo,attack,punio,enemigo):
        
        if self.move==1:
            if punio:
                kick_right=0
                self.image=kr_duck[kick_right]
                cuack_golpe.play()
                cuack_golpe.set_volume(sou[0])
            self.xvel = 2
            pos=1
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

        if self.move==-1:
            if punio:
                kick_left=0
                self.image=kl_duck[kick_left]
                cuack_golpe.play()
                cuack_golpe.set_volume(sou[0])
            self.xvel = -2
            pos=-1
            self.ani_speed-=1
            self.x+=pos
            if self.ani_speed==0:
                self.image=pygame.image.load(self.ani[self.ani_pos])
                self.image = pygame.transform.flip(self.image,True,False)
                self.ani_speed=self.ani_speed_init
                if self.ani_pos==self.ani_max:
                    self.ani_pos=0
                else:
                    self.ani_pos+=1
            self.l=self.image     
        
        if self.onGround:
            if jump:
                self.yvel -= 15
                self.doble=True
                
        else:
            # Solo acelera con gravedad si esta en el aire
            self.yvel += self.gravity
            
            if self.yvel>0 and self.doble==True:               
                if jump:
                    self.yvel -= 15
                    self.doble=False
            
        # Incrementa en x
        self.rect.left += self.xvel
        # Colisiones en x
        self.collide(self.xvel, 0,platforms)
        self.colision(self.xvel,0,objetivo)
        self.colision(self.xvel,0,enemigo)
        # Incrementa en y
        self.rect.top += self.yvel
        # Se asume que esta en el aire
        self.onGround = False;
        # Colisiones en y
        self.collide(0, self.yvel, platforms)
        self.colision(0, self.yvel, objetivo)
        self.colision(0, self.yvel, enemigo)
        
    def state_3(self,pos,jump,down,move,platforms,objetivo,attack,punio,enemigo):
        
        if self.move==1:
            if punio:
                kick_right=0
                self.image=kr_duck[kick_right]
                cuack_golpe.play()
                cuack_golpe.set_volume(sou[0])
            self.xvel = 3
            pos=1
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

        if self.move==-1:
            if punio:
                kick_left=0
                self.image=kl_duck[kick_left]
                cuack_golpe.play()
                cuack_golpe.set_volume(sou[0])
            self.xvel = -3
            pos=-1
            self.ani_speed-=1
            self.x+=pos
            if self.ani_speed==0:
                self.image=pygame.image.load(self.ani[self.ani_pos])
                self.image = pygame.transform.flip(self.image,True,False)
                self.ani_speed=self.ani_speed_init
                if self.ani_pos==self.ani_max:
                    self.ani_pos=0
                else:
                    self.ani_pos+=1
            self.l=self.image     
        
        if self.onGround:
            if jump:
                self.yvel -= 15
                self.doble=True
                
        else:
            # Solo acelera con gravedad si esta en el aire
            self.yvel += self.gravity
            
            if self.yvel>0 and self.doble==True:               
                if jump:
                    self.yvel -= 15
                    self.doble=False
            
        # Incrementa en x
        self.rect.left += self.xvel
        # Colisiones en x
        self.collide(self.xvel, 0,platforms)
        self.colision(self.xvel,0,objetivo)
        self.colision(self.xvel,0,enemigo)
        # Incrementa en y
        self.rect.top += self.yvel
        # Se asume que esta en el aire
        self.onGround = False;
        # Colisiones en y
        self.collide(0, self.yvel, platforms)
        self.colision(0, self.yvel, objetivo)
        self.colision(0, self.yvel, enemigo)

class handle_mummy:
    def state_1(self,pos,jump,down,move,platforms,objetivo,attack,punio,enemigo):

        if self.move==1:
            self.xvel = 2
            pos=1
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

        if self.move==-1:
            self.xvel = -2
            pos=-1
            self.ani_speed-=1
            self.x+=pos
            if self.ani_speed==0:
                self.image=pygame.image.load(self.ani[self.ani_pos])
                self.image = pygame.transform.flip(self.image,True,False)
                self.ani_speed=self.ani_speed_init
                if self.ani_pos==self.ani_max:
                    self.ani_pos=0
                else:
                    self.ani_pos+=1
            self.l=self.image     
        
        if self.onGround:
            if jump:
                self.yvel -= 15
                self.doble=True
                
        else:
            # Solo acelera con gravedad si esta en el aire
            self.yvel += self.gravity
            
            if self.yvel>0 and self.doble==True:               
                if jump:
                    self.yvel -= 15
                    self.doble=False
            
        # Incrementa en x
        self.rect.left += self.xvel
        # Colisiones en x
        self.collide(self.xvel, 0,platforms)
        self.colision(self.xvel,0,objetivo)
        self.colision(self.xvel,0,enemigo)
        # Incrementa en y
        self.rect.top += self.yvel
        # Se asume que esta en el aire
        self.onGround = False;
        # Colisiones en y
        self.collide(0, self.yvel, platforms)
        self.colision(0, self.yvel, objetivo)
        self.colision(0, self.yvel, enemigo)
        
    def state_2(self,pos,jump,down,move,platforms,objetivo,attack,punio,enemigo):
        
        if self.move==1:
            if punio:
                kick_right=0
                self.image=kr_mummy[kick_right]
                momia_golpe.play()
                momia_golpe.set_volume(sou[0])
            self.xvel = 2
            pos=1
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

        if self.move==-1:
            if punio:
                kick_left=0
                self.image=kl_mummy[kick_left]
                momia_golpe.play()
                momia_golpe.set_volume(sou[0])
            self.xvel = -2
            pos=-1
            self.ani_speed-=1
            self.x+=pos
            if self.ani_speed==0:
                self.image=pygame.image.load(self.ani[self.ani_pos])
                self.image = pygame.transform.flip(self.image,True,False)
                self.ani_speed=self.ani_speed_init
                if self.ani_pos==self.ani_max:
                    self.ani_pos=0
                else:
                    self.ani_pos+=1
            self.l=self.image     
        
        if self.onGround:
            if jump:
                self.yvel -= 15
                self.doble=True
                
        else:
            # Solo acelera con gravedad si esta en el aire
            self.yvel += self.gravity
            
            if self.yvel>0 and self.doble==True:               
                if jump:
                    self.yvel -= 15
                    self.doble=False
            
        # Incrementa en x
        self.rect.left += self.xvel
        # Colisiones en x
        self.collide(self.xvel, 0,platforms)
        self.colision(self.xvel,0,objetivo)
        self.colision(self.xvel,0,enemigo)
        # Incrementa en y
        self.rect.top += self.yvel
        # Se asume que esta en el aire
        self.onGround = False;
        # Colisiones en y
        self.collide(0, self.yvel, platforms)
        self.colision(0, self.yvel, objetivo)
        self.colision(0, self.yvel, enemigo)
        
    def state_3(self,pos,jump,down,move,platforms,objetivo,attack,punio,enemigo):
        
        if self.move==1:
            if punio:
                #kick_right=0
                #self.image=kr_duck[kick_right]
                momia_golpe.play()
                momia_golpe.set_volume(sou[0])
            self.xvel = 3
            pos=1
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

        if self.move==-1:
            if punio:
                #kick_left=0
                #self.image=kl_duck[kick_left]
                momia_golpe.play()
                momia_golpe.set_volume(sou[0])
            self.xvel = -3
            pos=-1
            self.ani_speed-=1
            self.x+=pos
            if self.ani_speed==0:
                self.image=pygame.image.load(self.ani[self.ani_pos])
                self.image = pygame.transform.flip(self.image,True,False)
                self.ani_speed=self.ani_speed_init
                if self.ani_pos==self.ani_max:
                    self.ani_pos=0
                else:
                    self.ani_pos+=1
            self.l=self.image     
        
        if self.onGround:
            if jump:
                self.yvel -= 15
                self.doble=True
                
        else:
            # Solo acelera con gravedad si esta en el aire
            self.yvel += self.gravity
            
            if self.yvel>0 and self.doble==True:               
                if jump:
                    self.yvel -= 15
                    self.doble=False
            
        # Incrementa en x
        self.rect.left += self.xvel
        # Colisiones en x
        self.collide(self.xvel, 0,platforms)
        self.colision(self.xvel,0,objetivo)
        self.colision(self.xvel,0,enemigo)
        # Incrementa en y
        self.rect.top += self.yvel
        # Se asume que esta en el aire
        self.onGround = False;
        # Colisiones en y
        self.collide(0, self.yvel, platforms)
        self.colision(0, self.yvel, objetivo)
        self.colision(0, self.yvel, enemigo)

class handle_ghost:
    def state_1(self,pos,jump,down,move,platforms,objetivo,attack,punio,enemigo):
        if self.move==1:
            self.xvel = 2
            pos=1
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

        if self.move==-1:
            self.xvel = -2
            pos=-1
            self.ani_speed-=1
            self.x+=pos
            if self.ani_speed==0:
                self.image=pygame.image.load(self.ani[self.ani_pos])
                self.image = pygame.transform.flip(self.image,True,False)
                self.ani_speed=self.ani_speed_init
                if self.ani_pos==self.ani_max:
                    self.ani_pos=0
                else:
                    self.ani_pos+=1
            self.l=self.image     
        
        if self.onGround:
            if jump:
                self.yvel -= 15
                self.doble=True
                
        else:
            # Solo acelera con gravedad si esta en el aire
            self.yvel += self.gravity
            
            if self.yvel>0 and self.doble==True:               
                if jump:
                    self.yvel -= 15
                    self.doble=False
            
        # Incrementa en x
        self.rect.left += self.xvel
        # Colisiones en x
        self.collide(self.xvel, 0,platforms)
        self.colision(self.xvel,0,objetivo)
        self.colision(self.xvel,0,enemigo)
        # Incrementa en y
        self.rect.top += self.yvel
        # Se asume que esta en el aire
        self.onGround = False;
        # Colisiones en y
        self.collide(0, self.yvel, platforms)
        self.colision(0, self.yvel, objetivo)
        self.colision(0, self.yvel, enemigo)
        
    def state_2(self,pos,jump,down,move,platforms,objetivo,attack,punio,enemigo):
        
        if self.move==1:
            if punio:
                #kick_right=0
                #self.image=kr_duck[kick_right]
                ghost_golpe.play()
                ghost_golpe.set_volume(sou[0])
            self.xvel = 2
            pos=1
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

        if self.move==-1:
            if punio:
                #kick_left=0
                #self.image=kl_duck[kick_left]
                ghost_golpe.play()
                ghost_golpe.set_volume(sou[0])
            self.xvel = -2
            pos=-1
            self.ani_speed-=1
            self.x+=pos
            if self.ani_speed==0:
                self.image=pygame.image.load(self.ani[self.ani_pos])
                self.image = pygame.transform.flip(self.image,True,False)
                self.ani_speed=self.ani_speed_init
                if self.ani_pos==self.ani_max:
                    self.ani_pos=0
                else:
                    self.ani_pos+=1
            self.l=self.image     
        
        if self.onGround:
            if jump:
                self.yvel -= 15
                self.doble=True
                
        else:
            # Solo acelera con gravedad si esta en el aire
            self.yvel += self.gravity
            
            if self.yvel>0 and self.doble==True:               
                if jump:
                    self.yvel -= 15
                    self.doble=False
            
        # Incrementa en x
        self.rect.left += self.xvel
        # Colisiones en x
        self.collide(self.xvel, 0,platforms)
        self.colision(self.xvel,0,objetivo)
        self.colision(self.xvel,0,enemigo)
        # Incrementa en y
        self.rect.top += self.yvel
        # Se asume que esta en el aire
        self.onGround = False;
        # Colisiones en y
        self.collide(0, self.yvel, platforms)
        self.colision(0, self.yvel, objetivo)
        self.colision(0, self.yvel, enemigo)
        
    def state_3(self,pos,jump,down,move,platforms,objetivo,attack,punio,enemigo):
        
        if self.move==1:
            if punio:
                #kick_right=0
                #self.image=kr_duck[kick_right]
                ghost_golpe.play()
                ghost_golpe.set_volume(sou[0])
            self.xvel = 3
            pos=1
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

        if self.move==-1:
            if punio:
                #kick_left=0
                #self.image=kl_duck[kick_left]
                ghost_golpe.play()
                ghost_golpe.set_volume(sou[0])
            self.xvel = -3
            pos=-1
            self.ani_speed-=1
            self.x+=pos
            if self.ani_speed==0:
                self.image=pygame.image.load(self.ani[self.ani_pos])
                self.image = pygame.transform.flip(self.image,True,False)
                self.ani_speed=self.ani_speed_init
                if self.ani_pos==self.ani_max:
                    self.ani_pos=0
                else:
                    self.ani_pos+=1
            self.l=self.image     
        
        if self.onGround:
            if jump:
                self.yvel -= 15
                self.doble=True
                
        else:
            # Solo acelera con gravedad si esta en el aire
            self.yvel += self.gravity
            
            if self.yvel>0 and self.doble==True:               
                if jump:
                    self.yvel -= 15
                    self.doble=False
            
        # Incrementa en x
        self.rect.left += self.xvel
        # Colisiones en x
        self.collide(self.xvel, 0,platforms)
        self.colision(self.xvel,0,objetivo)
        self.colision(self.xvel,0,enemigo)
        # Incrementa en y
        self.rect.top += self.yvel
        # Se asume que esta en el aire
        self.onGround = False;
        # Colisiones en y
        self.collide(0, self.yvel, platforms)
        self.colision(0, self.yvel, objetivo)
        self.colision(0, self.yvel, enemigo)

class handle_prototype:
    def state_1(self,pos,jump,down,move,platforms,objetivo,attack,punio,enemigo):
        if self.move==1:
            self.xvel = 2
            pos=1
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

        if self.move==-1:
            self.xvel = -2
            pos=-1
            self.ani_speed-=1
            self.x+=pos
            if self.ani_speed==0:
                self.image=pygame.image.load(self.ani[self.ani_pos])
                self.image = pygame.transform.flip(self.image,True,False)
                self.ani_speed=self.ani_speed_init
                if self.ani_pos==self.ani_max:
                    self.ani_pos=0
                else:
                    self.ani_pos+=1
            self.l=self.image     
        
        if self.onGround:
            if jump:
                self.yvel -= 15
                self.doble=True
                
        else:
            # Solo acelera con gravedad si esta en el aire
            self.yvel += self.gravity
            
            if self.yvel>0 and self.doble==True:               
                if jump:
                    self.yvel -= 15
                    self.doble=False
            
        # Incrementa en x
        self.rect.left += self.xvel
        # Colisiones en x
        self.collide(self.xvel, 0,platforms)
        self.colision(self.xvel,0,objetivo)
        self.colision(self.xvel,0,enemigo)
        # Incrementa en y
        self.rect.top += self.yvel
        # Se asume que esta en el aire
        self.onGround = False;
        # Colisiones en y
        self.collide(0, self.yvel, platforms)
        self.colision(0, self.yvel, objetivo)
        self.colision(0, self.yvel, enemigo)
        
    def state_2(self,pos,jump,down,move,platforms,objetivo,attack,punio,enemigo):
        
        if self.move==1:
            if punio:
                kick_right=0
                self.image=kr_prot[kick_right]
                robot_golpe.play()
                robot_golpe.set_volume(sou[0])
            self.xvel = 2
            pos=1
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

        if self.move==-1:
            if punio:
                kick_left=0
                self.image=kl_prot[kick_left]
                robot_golpe.play()
                robot_golpe.set_volume(sou[0])
            self.xvel = -2
            pos=-1
            self.ani_speed-=1
            self.x+=pos
            if self.ani_speed==0:
                self.image=pygame.image.load(self.ani[self.ani_pos])
                self.image = pygame.transform.flip(self.image,True,False)
                self.ani_speed=self.ani_speed_init
                if self.ani_pos==self.ani_max:
                    self.ani_pos=0
                else:
                    self.ani_pos+=1
            self.l=self.image     
        
        if self.onGround:
            if jump:
                self.yvel -= 15
                self.doble=True
                
        else:
            # Solo acelera con gravedad si esta en el aire
            self.yvel += self.gravity
            
            if self.yvel>0 and self.doble==True:               
                if jump:
                    self.yvel -= 15
                    self.doble=False
            
        # Incrementa en x
        self.rect.left += self.xvel
        # Colisiones en x
        self.collide(self.xvel, 0,platforms)
        self.colision(self.xvel,0,objetivo)
        self.colision(self.xvel,0,enemigo)
        # Incrementa en y
        self.rect.top += self.yvel
        # Se asume que esta en el aire
        self.onGround = False;
        # Colisiones en y
        self.collide(0, self.yvel, platforms)
        self.colision(0, self.yvel, objetivo)
        self.colision(0, self.yvel, enemigo)
        
    def state_3(self,pos,jump,down,move,platforms,objetivo,attack,punio,enemigo):
        if self.move==1:
            if punio:
                kick_right=0
                self.image=kr_prot[kick_right]
                robot_golpe.play()
                robot_golpe.set_volume(sou[0])
            self.xvel = 3
            pos=1
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

        if self.move==-1:
            if punio:
                kick_left=0
                self.image=kl_prot[kick_left]
                robot_golpe.play()
                robot_golpe.set_volume(sou[0])
            self.xvel = -3
            pos=-1
            self.ani_speed-=1
            self.x+=pos
            if self.ani_speed==0:
                self.image=pygame.image.load(self.ani[self.ani_pos])
                self.image = pygame.transform.flip(self.image,True,False)
                self.ani_speed=self.ani_speed_init
                if self.ani_pos==self.ani_max:
                    self.ani_pos=0
                else:
                    self.ani_pos+=1
            self.l=self.image     
        
        if self.onGround:
            if jump:
                self.yvel -= 15
                self.doble=True
                
        else:
            # Solo acelera con gravedad si esta en el aire
            self.yvel += self.gravity
            
            if self.yvel>0 and self.doble==True:               
                if jump:
                    self.yvel -= 15
                    self.doble=False
            
        # Incrementa en x
        self.rect.left += self.xvel
        # Colisiones en x
        self.collide(self.xvel, 0,platforms)
        self.colision(self.xvel,0,objetivo)
        self.colision(self.xvel,0,enemigo)
        # Incrementa en y
        self.rect.top += self.yvel
        # Se asume que esta en el aire
        self.onGround = False;
        # Colisiones en y
        self.collide(0, self.yvel, platforms)
        self.colision(0, self.yvel, objetivo)
        self.colision(0, self.yvel, enemigo)
        
        
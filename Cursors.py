# -*- coding: utf-8 -*-
from Load_images import *
from Screen import *

ancho=800
alto=600

class Manito_1:
    def __init__(self,x,y):
        self.mano = load_image("symbols/hand_p1.png",IMG_DIR,alpha=True)
        self.rect = self.mano.get_rect()
        self.vel=8
        self.rect.left=x
        self.rect.top=y
        
    def movimiento(self,up,down,left,right,cross,circle):
        if up:
            if self.rect.top<0:
                self.rect.top=self.rect.top
            else:
                self.rect.top-=self.vel
        if down:
            if self.rect.bottom>alto:
                self.rect.bottom=self.rect.bottom
            else:
                self.rect.bottom+=self.vel
        if left:
            if self.rect.left<0:
                self.rect.left=self.rect.left
            else:
                self.rect.left-=self.vel
        if right:
            if self.rect.right>ancho:
                self.rect.right=self.rect.right
            else:
                self.rect.right+=self.vel
        if circle:
            self.mano = load_image("symbols/hand_p1.png",IMG_DIR,alpha=True)
        screen.blit(self.mano,self.rect)
    
    def volver(self):
        self.mano = load_image("symbols/hand_p1.png",IMG_DIR,alpha=True)

class Manito_2:
    def __init__(self,x,y):
        self.mano = load_image("symbols/hand_p2.png",IMG_DIR,alpha=True)
        self.rect = self.mano.get_rect()
        self.vel=8
        self.rect.left=x
        self.rect.top=y
        
    def movimiento(self,up,down,left,right,cross,circle):
        if up:
            if self.rect.top<0:
                self.rect.top=self.rect.top
            else:
                self.rect.top-=self.vel
        if down:
            if self.rect.bottom>alto:
                self.rect.bottom=self.rect.bottom
            else:
                self.rect.bottom+=self.vel
        if left:
            if self.rect.left<0:
                self.rect.left=self.rect.left
            else:
                self.rect.left-=self.vel
        if right:
            if self.rect.right>ancho:
                self.rect.right=self.rect.right
            else:
                self.rect.right+=self.vel
        if circle:
            self.mano = load_image("symbols/hand_p2.png",IMG_DIR,alpha=True)
        screen.blit(self.mano,self.rect)
            
    def volver(self):
        self.mano = load_image("symbols/hand_p2.png",IMG_DIR,alpha=True)

            

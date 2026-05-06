# -*- coding: utf-8 -*-
import pygame
from Variables import personajes_p1, personajes_p2, life_bar
from colores import GREEN, YELLOW, RED, LIME, ORANGE
from Load_images import *
from Screen import *

class Time:
    def __init__(self):
        self.font = pygame.font.Font("fonts/MotionControl-BoldItalic.otf", 50)
        self.font2 = pygame.font.Font("fonts/MotionControl-BoldItalic.otf", 60)
        self.s = 0
        self.m = 0
                        
    def show_time(self):
        tiempo = [int(self.m),int(self.s)]
        self.s += 1/60
        if int(self.s) == 60:
            self.s = 0
            self.m +=1
        show_text_time = self.font.render("TIME", True, (255,255,255))
        show_tiempo = self.font2.render(str(tiempo[0]).zfill(2)+":"+str(tiempo[1]).zfill(2), True, (255,255,255))
        screen.blit(show_text_time,(370,500))
        screen.blit(show_tiempo,(350,530))
        
    def get_minutos(self):
        return int(self.m)
    
    def get_segundos(self):
        return int(self.s)


class Score1:
    def __init__(self):
        self.font = pygame.font.Font("fonts/MotionControl-BoldItalic.otf", 30)
        self.score = 0
        
    def show_score(self):
        show_score = self.font.render("SCORE - "+str(self.score).zfill(10), True, (255,255,255))
        screen.blit(show_score,(80,560))
    
    def get_score(self):
        return self.score
        
    def set_score(self,score):
        self.score+=score
    
class Score2:
    def __init__(self):
        self.font = pygame.font.Font("fonts/MotionControl-BoldItalic.otf", 30)
        self.score = 0
        
    def show_score(self):
        show_score = self.font.render("SCORE - "+str(self.score).zfill(10), True, (255,255,255))
        screen.blit(show_score,(530,560))
    
    def get_score(self):
        return self.score
    
    def set_score(self,score):
        self.score+=score

class Caratula:
    def __init__(self):
        self.c_anu=load_image("sprites/anubis/0.png", IMG_DIR, alpha=True)
        self.c_ast=load_image("sprites/astro/0.png", IMG_DIR, alpha=True)
        self.c_rob=load_image("sprites/robot/0.png", IMG_DIR, alpha=True)
        self.c_sol=load_image("sprites/soldier/1.png", IMG_DIR, alpha=True)
        self.c_thi=load_image("sprites/thing/0.png", IMG_DIR, alpha=True)

    def obtener_personaje_1():
        for i in range(len(personajes_p1)):
            if personajes_p1[i] == 1:
                return i
                
    def obtener_personaje_2():
        for i in range(len(personajes_p2)):
            if personajes_p2[i] == 1:
                return i          
                
    def show_caratula_p1(self):
        cara = Caratula.obtener_personaje_1()
        if cara ==0:
            screen.blit(self.c_anu,(30,510))
        elif cara ==1:
            screen.blit(self.c_ast,(30,510))
        elif cara ==2:
            screen.blit(self.c_rob,(30,510))
        elif cara ==3:
            screen.blit(self.c_sol,(30,510))
        elif cara ==4:
            screen.blit(self.c_thi,(30,510))
            
    def show_caratula_p2(self):
        cara = Caratula.obtener_personaje_2()
        if cara ==0:
            screen.blit(pygame.transform.flip(self.c_anu,True,False),(740,510))
        elif cara ==1:
            screen.blit(pygame.transform.flip(self.c_ast,True,False),(740,510))
        elif cara ==2:
            screen.blit(pygame.transform.flip(self.c_rob,True,False),(740,510))
        elif cara ==3:
            screen.blit(pygame.transform.flip(self.c_sol,True,False),(740,510))
        elif cara ==4:
            screen.blit(pygame.transform.flip(self.c_thi,True,False),(740,510))

class Lifebar:
    def __init__(self):
        self.bar=pygame.transform.scale(load_image("symbols/lifebar_frame.png", IMG_DIR, alpha=True),(220,30))
        self.vin=load_image("symbols/vineta.png", IMG_DIR, alpha=True)
    
    def show_rectangle(self):
        screen.blit(self.bar,(80,515))
        screen.blit(self.bar,(510,515))
    
    def show_life_bar(self,player1_health,player2_health):
        if player1_health >120:
            player1_health_color = GREEN
        elif player1_health >90:
            player1_health_color = LIME
        elif player1_health>60:
            player1_health_color= YELLOW
        elif player1_health>30:
            player1_health_color= ORANGE
        else:
            player1_health_color= RED
        if player2_health >120:
            player2_health_color = GREEN
        elif player2_health>90:
            player2_health_color = LIME
        elif player2_health>60:
            player2_health_color= YELLOW
        elif player2_health>30:
            player2_health_color= ORANGE
        else:
            player2_health_color = RED
            
        pygame.draw.rect(screen,player1_health_color,(520,520,player1_health,20))
        pygame.draw.rect(screen,player2_health_color,(90,520,player2_health,20))
    def show_vin(self):
        screen.blit(self.vin,(0,0))
        
    
    
        
    
        
        
            
    



    
	


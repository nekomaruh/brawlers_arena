# -*- coding: utf-8 -*-

import pygame

def load_joy_1(j1):  
    try:
        pygame.joystick.Joystick(j1)  
    except pygame.error as message:   
        print("No hay joystick conectados")
        raise SystemExit(message)  
        pygame.exit()
        quit()
def load_joy_2(j2):  
    try:
        pygame.joystick.Joystick(j2)  
    except pygame.error as message:   
        print("Conecte el joystick 2")
        raise SystemExit(message) 
        pygame.exit()
        quit()

def Load_joy(self):
    self.p1 = pygame.joystick.Joystick(0)
    self.p1.init()

def Load_joys(self):
    self.p1 = pygame.joystick.Joystick(0) 
    self.p2 = pygame.joystick.Joystick(1)
    self.p1.init()
    self.p2.init()
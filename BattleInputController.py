# -*- coding: utf-8 -*-
import pygame
from pygame.locals import *

class BattleInputController:
    """
    Clase para manejar y abstraer la lógica de entrada de botones y joysticks
    para los jugadores en la pantalla de batalla.
    """
    def __init__(self, joy_on=False, p1=None, p2=None):
        self.joy_on = joy_on
        self.p1 = p1
        self.p2 = p2
        self.reset_inputs()

    def reset_inputs(self):
        self.inputs = {
            'up': False, 'down': False, 'left': False, 'right': False, 'running': False,
            'kick': False, 'attack': False,
            'arriba': False, 'abajo': False, 'izquierda': False, 'derecha': False, 'correr': False,
            'golpe': False, 'ataque': False
        }

    def process_event(self, e):
        # Joystick events
        if self.joy_on:
            if e.type == pygame.JOYAXISMOTION:
                if self.p1 and e.joy == 0:
                    a_1 = self.p1.get_axis(0)
                    self.inputs['right'] = a_1 > 0.5
                    self.inputs['left'] = a_1 < -0.5
                if self.p2 and e.joy == 1:
                    a_2 = self.p2.get_axis(0)
                    self.inputs['derecha'] = a_2 > 0.5
                    self.inputs['izquierda'] = a_2 < -0.5
            if e.type == pygame.JOYBUTTONDOWN:
                if e.joy == 0:
                    if e.button == 0:
                        self.inputs['up'] = True
                    if e.button == 2:
                        self.inputs['kick'] = True
                    if e.button == 3:
                        self.inputs['attack'] = True
                    if e.button == 5:
                        self.inputs['running'] = True
                if e.joy == 1:
                    if e.button == 0:
                        self.inputs['arriba'] = True
                    if e.button == 2:
                        self.inputs['golpe'] = True
                    if e.button == 3:
                        self.inputs['ataque'] = True
                    if e.button == 5:
                        self.inputs['correr'] = True
            if e.type == pygame.JOYBUTTONUP:
                if e.joy == 0:
                    if e.button == 0:
                        self.inputs['up'] = False
                    if e.button == 2:
                        self.inputs['kick'] = False
                    if e.button == 3:
                        self.inputs['attack'] = False
                    if e.button == 5:
                        self.inputs['running'] = False
                if e.joy == 1:
                    if e.button == 0:
                        self.inputs['arriba'] = False
                    if e.button == 2:
                        self.inputs['golpe'] = False
                    if e.button == 3:
                        self.inputs['ataque'] = False
                    if e.button == 5:
                        self.inputs['correr'] = False
        # Keyboard events
        if e.type == pygame.KEYDOWN:
            if e.key == K_UP:
                self.inputs['up'] = True
            if e.key == K_DOWN:
                self.inputs['down'] = True
            if e.key == K_LEFT:
                self.inputs['left'] = True
            if e.key == K_RIGHT:
                self.inputs['right'] = True
            if e.key == K_SPACE:
                self.inputs['running'] = True
            if e.key == K_k:
                self.inputs['kick'] = True
            if e.key == K_l:
                self.inputs['attack'] = True
            if e.key == K_w:
                self.inputs['arriba'] = True
            if e.key == K_d:
                self.inputs['derecha'] = True
            if e.key == K_a:
                self.inputs['izquierda'] = True
            if e.key == K_s:
                self.inputs['abajo'] = True
            if e.key == K_g:
                self.inputs['correr'] = True
            if e.key == K_g:
                self.inputs['correr'] = True
        if e.type == pygame.KEYUP:
            if e.key == K_UP:
                self.inputs['up'] = False
            if e.key == K_DOWN:
                self.inputs['down'] = False
            if e.key == K_LEFT:
                self.inputs['left'] = False
            if e.key == K_RIGHT:
                self.inputs['right'] = False
            if e.key == K_SPACE:
                self.inputs['running'] = False
            if e.key == K_k:
                self.inputs['kick'] = False
            if e.key == K_l:
                self.inputs['attack'] = False
            if e.key == K_w:
                self.inputs['arriba'] = False
            if e.key == K_d:
                self.inputs['derecha'] = False
            if e.key == K_a:
                self.inputs['izquierda'] = False
            if e.key == K_s:
                self.inputs['abajo'] = False
            if e.key == K_g:
                self.inputs['correr'] = False

    def get_inputs(self):
        return self.inputs.copy()

    def clear(self):
        self.reset_inputs()

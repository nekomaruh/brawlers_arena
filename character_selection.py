# -*- coding: utf-8 -*-
__author__ = "TeamFlammers"
import sys
import pygame
from colores import *
from pygame.locals import *
from map_selection import Maps
from Load_images import *
from Music_sounds import button_A, button_X, menu_select
from Variables import personajes_p1, personajes_p2, break_main, sou, joy_on
from Cursors import Manito
from Screen import *
from Load_joysticks import Load_joys

class Character:
    def __init__(self):
        self.gameDisplay = screen
        
        # 1. OPTIMIZACIÓN: Cargar fuentes una sola vez
        self.font_title = pygame.font.Font("fonts/MotionControl-BoldItalic.otf", 50)
        self.font_ui = pygame.font.Font("fonts/MotionControl-BoldItalic.otf", 35)
        
        self.text1 = self.font_title.render("Character Selection", True, BLACK)
        self.text_back = self.font_ui.render("Back", True, BLACK)
        self.text_change = self.font_ui.render("Change", True, BLACK)
        self.text_select = self.font_ui.render("Select", True, BLACK)
        
        # 2. OPTIMIZACIÓN: Cargar imágenes de la UI una sola vez
        self.backImg = load_image("backgrounds/Background.png", IMG_DIR, alpha=False)
        self.triangle = load_image("symbols/triangle32_b.png", IMG_DIR, alpha=True)
        self.circle = load_image("symbols/circle32_b.png", IMG_DIR, alpha=True)
        self.cross = load_image("symbols/cross32_b.png", IMG_DIR, alpha=True)
        
        # 3. OPTIMIZACIÓN: Cargar imágenes de personajes UNA SOLA VEZ
        self.img_anubis = pygame.image.load('images/symbols/Anubis.png')
        self.img_astro = pygame.image.load('images/symbols/Astronaut.png')
        self.img_robot = pygame.image.load('images/symbols/Robot.png')
        self.img_soldier = pygame.image.load('images/symbols/Soldier.png')
        self.img_thing = pygame.image.load('images/symbols/Thing.png')
        
        # 4. OPTIMIZACIÓN DRY: Unificar las posiciones y dimensiones en una lista
        self.ancho_btn = 180
        self.alto_btn = 170
        self.char_slots = [
            {'id': 0, 'x': 50,  'y': 100, 'img': self.img_anubis,  'px': 83,  'py': 130},
            {'id': 1, 'x': 300, 'y': 100, 'img': self.img_astro,   'px': 335, 'py': 110},
            {'id': 2, 'x': 550, 'y': 100, 'img': self.img_robot,   'px': 585, 'py': 115},
            {'id': 3, 'x': 171, 'y': 330, 'img': self.img_soldier, 'px': 211, 'py': 350},
            {'id': 4, 'x': 425, 'y': 330, 'img': self.img_thing,   'px': 458, 'py': 345}
        ]

        # Instancia de las manos
        self.mano1 = Manito(340, 270, 1)
        self.mano2 = Manito(400, 270, 2)
        
        if joy_on:
            self.p1 = pygame.joystick.Joystick(0) 
            self.p2 = pygame.joystick.Joystick(1)
            self.p1.init()
            self.p2.init()
        
        self.suma1 = 0
        self.suma2 = 0

    def esta_adentro(self, mano, x, y):
        """Tu lógica matemática original EXACTA para evitar autoselecciones"""
        return (x + self.ancho_btn > mano.rect.left > x) and (y + self.alto_btn > mano.rect.top > y)

    def dibujar_y_seleccionar(self, p1_confirm, p2_confirm):
        """Dibuja todos los recuadros y evalúa las selecciones en un solo ciclo"""
        for slot in self.char_slots:
            x, y = slot['x'], slot['y']
            
            hover_p1 = self.esta_adentro(self.mano1, x, y)
            hover_p2 = self.esta_adentro(self.mano2, x, y)
            
            # Dibujar el recuadro (Rojo si hay hover, Azul si no)
            if hover_p1 or hover_p2:
                pygame.draw.rect(self.gameDisplay, RED, (x, y, self.ancho_btn, self.alto_btn))
            else:
                pygame.draw.rect(self.gameDisplay, STEELBLUE, (x, y, self.ancho_btn, self.alto_btn))
            
            # Dibujar el personaje
            self.gameDisplay.blit(slot['img'], (slot['px'], slot['py']))

            # Selección Jugador 1
            if hover_p1 and p1_confirm and self.suma1 == 0:
                for i in range(5): personajes_p1[i] = 0
                personajes_p1[slot['id']] = 1
                self.suma1 = 1
                self.mano1.mano = load_image("symbols/hand_p1_t.png", IMG_DIR, alpha=True)
                self.mano1.vel = 0

            # Selección Jugador 2
            if hover_p2 and p2_confirm and self.suma2 == 0:
                for i in range(5): personajes_p2[i] = 0
                personajes_p2[slot['id']] = 1
                self.suma2 = 1
                self.mano2.mano = load_image("symbols/hand_p2_t.png", IMG_DIR, alpha=True)
                self.mano2.vel = 0

    def char_select(self):
        loop_char = True
        clock = pygame.time.Clock()
        up = down = left = right = cruz = circulo = False
        ar = ab = iz = de = x = o = False

        while loop_char:
            self.k = pygame.key.get_pressed()
            
            # Centralizamos la acción de "Confirmar"
            p1_confirm = self.k[K_RETURN]
            p2_confirm = self.k[K_1]
            if joy_on:
                p1_confirm = p1_confirm or self.p1.get_button(0)
                p2_confirm = p2_confirm or self.p2.get_button(0)
                    
            for e in pygame.event.get():
                if e.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                
                if joy_on:
                    if e.type == pygame.JOYAXISMOTION:
                        a_1 = self.p1.get_axis(0)
                        a_1y = self.p1.get_axis(1)
                        a_2 = self.p2.get_axis(0)
                        a_2y = self.p2.get_axis(1)
                        
                        # Para el p1
                        if e.joy == 0:
                            if a_1 > 0.5: right = True
                            elif a_1 < -0.5: left = True
                            else: left = right = False
                            
                            if a_1y > 0.5: down = True
                            elif a_1y < -0.5: up = True
                            else: up = down = False

                        # Para el p2
                        if e.joy == 1:
                            if a_2 > 0.5: de = True
                            elif a_2 < -0.5: iz = True
                            else: de = iz = False
                            
                            if a_2y > 0.5: ab = True
                            elif a_2y < -0.5: ar = True
                            else: ar = ab = False
                            
                    if e.type == pygame.JOYBUTTONDOWN:
                        # Para el P1
                        if e.joy == 0:
                            if e.button == 1:
                                circulo = True
                                for i in range(len(personajes_p1)): personajes_p1[i] = 0
                                self.suma1 = 0
                                self.mano1.vel = 8
                                self.mano1.volver()
                            if e.button == 3: loop_char = False
                            
                        # Para el P2
                        if e.joy == 1: 
                            if e.button == 1:
                                o = True
                                for i in range(len(personajes_p2)): personajes_p2[i] = 0
                                self.suma2 = 0
                                self.mano2.vel = 8
                                self.mano2.volver()
                            if e.button == 3: loop_char = False
                        
                    if e.type == pygame.JOYBUTTONUP:
                        if e.joy == 0:
                            if e.button == 0: cruz = False
                            if e.button == 1: circulo = False
                        if e.joy == 1:
                            if e.button == 0: x = False
                            if e.button == 1: o = False
                    
                if e.type == pygame.KEYDOWN:
                    if e.key == K_UP: up = True
                    elif e.key == K_DOWN: down = True
                    elif e.key == K_LEFT: left = True
                    elif e.key == K_RIGHT: right = True
                    elif e.key == K_RETURN: cruz = True
                    elif e.key == K_BACKSPACE:
                        circulo = True
                        for i in range(len(personajes_p1)): personajes_p1[i] = 0
                        self.suma1 = 0
                        self.mano1.vel = 8
                        self.mano1.volver()
                        
                    if e.key == K_w: ar = True
                    elif e.key == K_s: ab = True
                    elif e.key == K_a: iz = True
                    elif e.key == K_d: de = True
                    elif e.key == K_1: x = True
                    elif e.key == K_2:
                        o = True
                        for i in range(len(personajes_p2)): personajes_p2[i] = 0
                        self.suma2 = 0
                        self.mano2.vel = 8
                        self.mano2.volver()
                        
                    elif e.key == K_ESCAPE:
                        button_A.play()
                        loop_char = False
                
                if e.type == pygame.KEYUP:
                    if e.key == K_UP: up = False
                    if e.key == K_DOWN: down = False
                    if e.key == K_LEFT: left = False
                    if e.key == K_RIGHT: right = False
                    if e.key == K_RETURN: cruz = False
                    if e.key == K_BACKSPACE: circulo = False
                        
                    if e.key == K_w: ar = False
                    if e.key == K_s: ab = False
                    if e.key == K_a: iz = False
                    if e.key == K_d: de = False
                    elif e.key == K_1: x = False
                    elif e.key == K_2: o = False
            
            # --- RENDERIZADO ---
            self.gameDisplay.blit(self.backImg, (0, 0))
    
            # Evaluamos y dibujamos las 5 áreas con sus personajes en un solo llamado
            self.dibujar_y_seleccionar(p1_confirm, p2_confirm)
    
            # Se dibuja la UI
            self.gameDisplay.blit(self.text1, (230, 30))
            self.gameDisplay.blit(self.triangle, (650, 550))
            self.gameDisplay.blit(self.text_back, (690, 548))
            self.gameDisplay.blit(self.circle, (500, 550))
            self.gameDisplay.blit(self.text_change, (540, 548))
            self.gameDisplay.blit(self.cross, (360, 550))
            self.gameDisplay.blit(self.text_select, (400, 548))
            
            self.mano1.movimiento(up, down, left, right, cruz, circulo)
            self.mano2.movimiento(ar, ab, iz, de, x, o)
            
            # Transición de pantalla
            suma_personajes = self.suma1 + self.suma2
            if suma_personajes == 2:
                up = down = left = right = cruz = circulo = False
                ar = ab = iz = de = x = o = False
                self.mano1.volver()
                self.mano2.volver()
                self.mano1 = Manito(340, 270, 1)
                self.mano2 = Manito(400, 270, 2)
                self.mano1.vel = 8
                self.mano2.vel = 8
                self.suma1 = 0
                self.suma2 = 0
                button_X.play()
                M = Maps()
                M.map_select()
                
            if break_main[0]:
                loop_char = False

            pygame.display.update()
            clock.tick(60)
            
if __name__ == "__main__":
    C = Character()
    C.char_select()
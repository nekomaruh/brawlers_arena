# -*- coding: utf-8 -*-
__author__ = "TeamFlammers"
import pygame, random
import sys
from colores import *
from pygame.locals import *
from Music_sounds import button_X, button_A
from Cursors import Manito
from Variables import mapas, personajes_p1, personajes_p2, break_main, joy_on
from Transitions import *
from Game_screen import *
from Screen import *
from Load_joysticks import Load_joys

pygame.init()

class Maps:
    def __init__(self):
        self.gameDisplay = screen
        
        # 1. OPTIMIZACIÓN: Cargar fuentes y textos una sola vez
        self.font = pygame.font.Font("fonts/MotionControl-BoldItalic.otf", 50)
        self.font_ui = pygame.font.Font("fonts/MotionControl-BoldItalic.otf", 35)
        
        self.text1 = self.font.render("Map Selection", True, BLACK)
        self.text2 = self.font.render("Random", True, WHITE)
        self.text_back = self.font_ui.render("Back", True, BLACK)
        self.text_select = self.font_ui.render("Select", True, BLACK)
        
        # 2. OPTIMIZACIÓN: Cargar imágenes base
        self.backImg = load_image("backgrounds/Background.png", IMG_DIR, alpha=False)
        self.triangle = load_image("symbols/triangle32_b.png", IMG_DIR, alpha=True)
        self.cross = load_image("symbols/cross32_b.png", IMG_DIR, alpha=True)

        # 3. OPTIMIZACIÓN: Cargar imágenes de mapas una SOLA vez (Evita caída de FPS)
        self.img_bosque = pygame.image.load('images/symbols/Bosque_v3.png')
        self.img_kawai = pygame.image.load('images/symbols/Kawai.png')
        self.img_zombie = pygame.image.load('images/symbols/Zombie.png')
        self.img_desierto = pygame.image.load('images/symbols/Desierto.png')
        self.img_space = pygame.image.load('images/symbols/Space.png')

        # 4. OPTIMIZACIÓN DRY: Definir áreas y datos de mapas en una lista
        self.ancho_btn = 220
        self.alto_btn = 170
        self.map_slots = [
            {'id': 0, 'x': 40,  'y': 90,  'img': self.img_bosque,   'px': 50,  'py': 100, 'hover_color': GREEN},
            {'id': 1, 'x': 290, 'y': 90,  'img': self.img_kawai,    'px': 300, 'py': 100, 'hover_color': GREEN},
            {'id': 2, 'x': 540, 'y': 90,  'img': self.img_zombie,   'px': 550, 'py': 100, 'hover_color': GREEN},
            {'id': 3, 'x': 40,  'y': 340, 'img': self.img_desierto, 'px': 50,  'py': 350, 'hover_color': GREEN},
            {'id': 4, 'x': 290, 'y': 340, 'img': self.img_space,    'px': 300, 'py': 350, 'hover_color': GREEN},
            {'id': 5, 'x': 540, 'y': 340, 'img': None,              'px': 0,   'py': 0,   'hover_color': PURPLE} # Slot Random
        ]

        self.mano1 = Manito(400, 270, 1)
        self.mano1.vel = 10
        
        if joy_on:
            Load_joys(self)
            
    def esta_adentro(self, mano, x, y):
        """Lógica exacta de colisión manual para evitar selección automática en los bordes"""
        return (x + self.ancho_btn > mano.rect.left > x) and (y + self.alto_btn > mano.rect.top > y)

    def dibujar_y_seleccionar(self, p1_confirm):
        """Unifica el render de botones, mapas y la detección de selección"""
        mapa_seleccionado = None
        
        for slot in self.map_slots:
            x, y = slot['x'], slot['y']
            hover = self.esta_adentro(self.mano1, x, y)
            
            # Dibujar el rectángulo de fondo
            if hover:
                pygame.draw.rect(self.gameDisplay, slot['hover_color'], (x, y, self.ancho_btn, self.alto_btn))
            else:
                pygame.draw.rect(self.gameDisplay, BLACK, (x, y, self.ancho_btn, self.alto_btn))
            
            # Dibujar imagen del mapa o texto si es Random
            if slot['img']:
                self.gameDisplay.blit(slot['img'], (slot['px'], slot['py']))
            else:
                self.gameDisplay.blit(self.text2, (590, 400)) # Dibuja "Random"
                
            # Registrar selección
            if hover and p1_confirm:
                mapa_seleccionado = slot['id']
                
        return mapa_seleccionado

    def iniciar_transicion_mapa(self, id_mapa, es_random=False):
        """Ejecuta los sonidos, limpia arrays y lanza el juego o countdown"""
        for i in range(len(mapas)):
            mapas[i] = 0
            
        mapas[id_mapa] = 1
        button_X.play()
        pygame.mixer.music.set_volume(1.0)
        pygame.mixer.music.stop()
        
        if es_random:
            self.mano1.volver()
            g = Game_screen()
            g.handle_event()
        else:
            T = Countdown()
            T.handle_event()
            self.mano1 = Manito(400, 270, 1)

    def map_select(self):
        loop_map = True
        clock = pygame.time.Clock()
        up = down = left = right = cruz = circulo = False

        while loop_map:
            mapa_random = random.randint(0, 4)
            
            self.k = pygame.key.get_pressed()
            p1_confirm = self.k[K_RETURN]
            
            if joy_on:
                try:
                    p1_confirm = p1_confirm or self.p1.get_button(0)
                except AttributeError:
                    pass

            for e in pygame.event.get():
                if e.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                    
                if joy_on:
                    if e.type == pygame.JOYAXISMOTION:
                        # Control P1
                        if e.joy == 0:
                            a_1 = self.p1.get_axis(0)
                            a_1y = self.p1.get_axis(1)
                            
                            if a_1 > 0.5: right = True
                            elif a_1 < -0.5: left = True
                            else: left = right = False
                            
                            if a_1y > 0.5: down = True
                            elif a_1y < -0.5: up = True
                            else: up = down = False
                            
                    if e.type == pygame.JOYBUTTONDOWN:
                        if e.joy == 0:
                            if e.button == 3:
                                for i in range(len(personajes_p1)): personajes_p1[i] = 0
                                for i in range(len(personajes_p2)): personajes_p2[i] = 0
                                loop_map = False
                        
                if e.type == pygame.KEYDOWN:
                    if e.key == pygame.K_ESCAPE:
                        button_A.play()
                        for i in range(len(personajes_p1)):
                            personajes_p1[i] = 0
                            personajes_p2[i] = 0
                        loop_map = False

                    if e.key == K_UP: up = True
                    elif e.key == K_DOWN: down = True
                    elif e.key == K_LEFT: left = True
                    elif e.key == K_RIGHT: right = True
                    elif e.key == K_RETURN: cruz = True
                    elif e.key == K_BACKSPACE:
                        circulo = True
                        for i in range(len(mapas)): mapas[i] = 0
                        
                if e.type == pygame.KEYUP:
                    if e.key == K_UP: up = False
                    if e.key == K_DOWN: down = False
                    if e.key == K_LEFT: left = False
                    if e.key == K_RIGHT: right = False
                    if e.key == K_RETURN: cruz = False
                    if e.key == K_BACKSPACE: circulo = False
                        
            # --- RENDERIZADO ---
            self.gameDisplay.blit(self.backImg, (0, 0))
    
            # Dibujar slots y detectar si se presionó alguno
            mapa_sel = self.dibujar_y_seleccionar(p1_confirm)
            
            # Ejecutar acción si se seleccionó un mapa
            if mapa_sel is not None:
                if mapa_sel == 5:
                    self.iniciar_transicion_mapa(mapa_random, es_random=True)
                else:
                    self.iniciar_transicion_mapa(mapa_sel, es_random=False)
    
            # Dibujar UI
            self.gameDisplay.blit(self.text1, (280, 25))     
            self.gameDisplay.blit(self.triangle, (650, 550))
            self.gameDisplay.blit(self.text_back, (690, 548))
            self.gameDisplay.blit(self.cross, (510, 550))
            self.gameDisplay.blit(self.text_select, (550, 548))
            
            self.mano1.movimiento(up, down, left, right, cruz, circulo)
                
            if break_main[0]:
                loop_map = False

            pygame.display.update()
            clock.tick(60)

if __name__ == "__main__":
    M = Maps()
    M.map_select()
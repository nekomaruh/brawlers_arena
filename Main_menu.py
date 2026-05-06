# -*- coding: utf-8 -*-
import pygame, sys
from pygame.locals import *
from pygame import*
from Credits import*
from character_selection import *
from Music_sounds import *
from Load_joysticks import load_joy_1, load_joy_2
from Variables import break_main, vol, sou, joy_on
from Options import *
from Load_images import *
from Scores import *
from Screen import *

# Carga joysticks - lanza error si no hay conectados
if joy_on==True:
    load_joy_1(0)
    load_joy_2(1)

class Opcion:
    def __init__(self, fuente, titulo, x, y, paridad, funcion_asignada):
        self.imagen_normal = fuente.render(titulo, 1, (0, 0, 0))
        self.imagen_destacada = fuente.render(titulo, 10, (200, 0, 0))
        self.image = self.imagen_normal
        self.rect = self.image.get_rect()
        self.rect.x = 9999 * paridad
        self.rect.y = y
        self.funcion_asignada = funcion_asignada
        self.x = float(self.rect.x)

    def actualizar(self):
        destino_x = 105
        self.x += (destino_x - self.x) / 15.0
        self.rect.x = int(self.x)

    def imprimir(self, screen):
        screen.blit(self.image, self.rect)

    def destacar(self, estado):
        if estado:
            self.image = self.imagen_destacada
        else:
            self.image = self.imagen_normal

    def activar(self):
        self.funcion_asignada()


class Cursor:
    def __init__(self, x, y, dy):
        self.image = pygame.image.load('images/symbols/s3.png').convert_alpha()
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.y_inicial = y
        self.dy = dy
        self.y = 0
        self.seleccionar(0)

    def actualizar(self):
        self.y += (self.to_y - self.y) / 20
        self.rect.y = int(self.y)

    def seleccionar(self, indice):
        self.to_y = self.y_inicial + indice * self.dy

    def imprimir(self, screen):
        screen.blit(self.image, self.rect)


class Menu:
    def __init__(self, opciones):
        self.opciones = []
        fuente = pygame.font.Font("fonts/MotionControl-BoldItalic.otf", 35)
        x = 320
        y = 350
        paridad = 5
        if joy_on == True:
            self.p1 = pygame.joystick.Joystick(0) 
            self.p1.init()

        self.cursor = Cursor(x - 30, y, 38)

        for titulo, funcion in opciones:
            self.opciones.append(Opcion(fuente, titulo, x, y, paridad, funcion))
            y += 40
            if paridad == 1:
                paridad = -1
            else:
                paridad = 1

        self.seleccionado = 0
        self.total = len(self.opciones)
        self.mantiene_pulsado = False

    def actualizar(self):
        k = pygame.key.get_pressed()
        
        if joy_on ==True:
            hy_1=self.p1.get_hat(0)[1]
            b0_1=self.p1.get_button(0)

        if not self.mantiene_pulsado:
            if joy_on == True:
                if hy_1==1:
                    self.seleccionado -= 1
                    menu_select.play()
                    menu_select.set_volume(sou[0])
                elif hy_1==-1:
                    menu_select.play()
                    self.seleccionado += 1
                    menu_select.set_volume(sou[0])
                elif b0_1==1:
                    self.opciones[self.seleccionado].activar()
            
            if k[K_UP]:
                self.seleccionado -= 1
                menu_select.play()
                menu_select.set_volume(sou[0])
            elif k[K_DOWN]:
                menu_select.play()
                self.seleccionado += 1
                menu_select.set_volume(sou[0])
            elif k[K_RETURN]:
                # Invoca a la función asociada a la opción.
                self.opciones[self.seleccionado].activar()
            

        # procura que el cursor esté entre las opciones permitidas
        if self.seleccionado < 0:
            self.seleccionado = 0
        elif self.seleccionado > self.total - 1:
            self.seleccionado = self.total - 1
        
        self.cursor.seleccionar(self.seleccionado)

        # indica si el usuario mantiene pulsada alguna tecla.
        if joy_on:
            self.mantiene_pulsado = hy_1
        self.mantiene_pulsado = k[K_UP] or k[K_DOWN] or k[K_RETURN]

        self.cursor.actualizar()
     
        for o in self.opciones:
            o.actualizar()

    def imprimir(self, screen):

        self.cursor.imprimir(screen)

        for opcion in self.opciones:
            opcion.imprimir(screen)
            
def start():
    button_X.play()
    button_X.set_volume(sou[0])
    C = Character()
    C.char_select()

def options():    
    button_X.play()
    button_X.set_volume(sou[0])
    o = Options()
    o.handle_event()

def scores():
    button_X.play()
    button_X.set_volume(sou[0])
    pt = Scores()
    pt.loop()

def credits():
    button_X.play()
    button_X.set_volume(sou[0])
    C = Creditos()
    C.credits_loop()

def exit():
    button_X.play()
    button_X.set_volume(sou[0])
    pygame.quit()
    quit()

FS = Fullscreen

class main:
    def __init__(self):    
        self.cross = pygame.image.load("images/symbols/cross32_b.png")
        font_select = pygame.font.Font("fonts/MotionControl-BoldItalic.otf", 35)
        self.logo = load_image("symbols/ba_logo.png",IMG_DIR,alpha=True)
        self.text_select = font_select.render("Select", True, (50,50,50))
        self.exit = load_image("symbols/exit.png",IMG_DIR,alpha=True)
    
        font = pygame.font.SysFont("Stencil",72)
        self.text = font.render("   ",True,(0,50,128))
        self.text1 = font.render("   ",True,(0,50,128))
        self.rText= self.text.get_rect()
        self.rText1=self.text1.get_rect()

        self.rText.left=200
        self.rText.top=100
        self.rText1.left=270
        self.rText1.top=170

        self.opciones = [
            ("                                    Start", start),
            ("                                    Options", options),
            ("                                    Highscore", scores),
            ("                                    Credits", credits),
            ("                                          Exit", exit)
            ]

        pygame.font.init()
        self.screen = screen #Añadir ,pygame.FULLSCREEN para pantalla completa (despues del parentesis (800,600))
        self.fondo = load_image("backgrounds/Background_2.jpg",IMG_DIR,alpha=False)
        #self.fondo = load_image("backgrounds/main.jpg",IMG_DIR,alpha=False)
        self.menu = Menu(self.opciones)
    
        pygame.mixer.music.load("music/wan1.mid") # carga musica
        pygame.mixer.music.play(-1, 0.0) # reproduce musica
        
    def main_loop(self):
        terminado = False
        while not terminado:
            for e in pygame.event.get():
                if e.type == QUIT:
                    terminado = True
                if e.type == pygame.KEYDOWN:
                    if e.key == K_f:
                        print("Con FS")
                    elif e.key == K_g:
                        print("Sin FS")
                if e.type == pygame.KEYUP:
                    if e.key == K_f:
                        FS=True
                    elif e.key == K_g:
                        FS=False
                    
            self.screen.blit(self.fondo, (0, 0))
            self.menu.actualizar()
            self.menu.imprimir(self.screen)
            self.screen.blit(self.text,self.rText)
            self.screen.blit(self.text1,self.rText1)
            self.screen.blit(self.text_select,(690,548))
            self.screen.blit(self.cross,(650,550))
            self.screen.blit(self.logo,(350,150))
            self.screen.blit(self.exit,(355,510))
            pygame.display.flip()
            pygame.time.delay(8)
            break_main[0]=False  


        


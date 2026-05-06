# -*- coding: utf-8 -*-
from Variables import mapas
from Load_images import *
from Map_limits import *

def Load_map(self):
    if mapas[0]==1:
        self.mapa = load_image("backgrounds/map1/map.png",IMG_DIR,alpha=False)
        self.plataforma = load_image("backgrounds/map1/platforms.png",IMG_DIR,alpha=True)
        self.level=lista_bosque #importa la lista de las plataformas
        pygame.mixer.music.load("music/tema_bosque.ogg")
    elif mapas[1]==1:
        self.mapa = load_image("backgrounds/map3/map.jpg",IMG_DIR,alpha=False)
        self.plataforma = load_image("backgrounds/map3/platforms.png",IMG_DIR,alpha=True)
        self.level=lista_kawai #importa la lista de las plataformas
        pygame.mixer.music.load("music/tema_kawai.ogg")
    elif mapas[2]==1:
        self.mapa = load_image("backgrounds/map4/map.jpg",IMG_DIR,alpha=False)
        self.plataforma = load_image("backgrounds/map4/platforms.png",IMG_DIR,alpha=True)
        self.level=lista_ciudad #importa la lista de las plataformas
        pygame.mixer.music.load("music/tema_ciudad.ogg")
    elif mapas[3]==1:
        self.mapa = load_image("backgrounds/map2/map.jpg",IMG_DIR,alpha=False)
        self.plataforma = load_image("backgrounds/map2/platforms.png",IMG_DIR,alpha=True)
        self.level=lista_desierto #importa la lista de las plataformas
        pygame.mixer.music.load("music/tema_desierto.ogg")
    elif mapas[4]==1:
        self.mapa = load_image("backgrounds/map5/map.png",IMG_DIR,alpha=False)
        self.plataforma = load_image("backgrounds/map5/platforms.png",IMG_DIR,alpha=True)
        self.level=lista_planetas #importa la lista de las plataformas
        pygame.mixer.music.load("music/tema_planetas.ogg")  


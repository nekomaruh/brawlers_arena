# -*- coding: utf-8 -*-
"""
Created on Fri Apr 21 20:10:33 2017

@author: Neko
"""
import os
import sys
import pygame

IMG_DIR="images"

def load_image(name, IMG_DIR, alpha=False):
    ruta = os.path.join(IMG_DIR, name)
    try:
        image = pygame.image.load(ruta)
    except:
        print("Error, no se puede cargar la imagen: " + ruta)
        sys.exit(1)
    if alpha is True:
        image = image.convert_alpha()
    else:
        image = image.convert()
    return image

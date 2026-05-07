# -*- coding: utf-8 -*-
from math import sqrt

def enemy_attack(d1, d2, vida_enemigo, vida_p2, vida_p1, kick, right, left, golpe, izquierda, derecha, punio):
    """
    Lógica de ataque enemigo. Modifica las vidas según la distancia y acciones.
    """
    if d1 <= 50:
        punio = True
        vida_p2 -= 0.5
        if kick and (right or left):
            vida_enemigo -= 0.5
    elif d2 <= 50:
        punio = True
        vida_p1 -= 0.5
        if golpe and (izquierda or derecha):
            vida_enemigo -= 0.5
    else:
        punio = False
    return vida_enemigo, vida_p2, vida_p1, punio

def distance(x1, y1, x2, y2):
    """
    Calcula la distancia euclidiana entre dos puntos.
    """
    return int(sqrt((y2 - y1) ** 2 + (x2 - x1) ** 2))

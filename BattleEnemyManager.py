# -*- coding: utf-8 -*-
import random
from Sprites import E1

class EnemyManager:

    def __init__(self):
        self.e1=E1(random.randint(10,700),random.randint(10,450))
        self.e2=E1(random.randint(10,700),random.randint(10,450))
        self.e3=E1(random.randint(10,700),random.randint(10,450))

        self.e4=E1(800,600)
        self.e5=E1(800,600)

        self.enemies=[
            self.e1,
            self.e2,
            self.e3
        ]

        self.bot=self.e4
        self.bot2=self.e5

    def add_to_entities(self,entities):
        for enemy in self.enemies:
            entities.add(enemy)

    def reset_enemy_position(self,enemy):
        enemy.rect.left=random.randint(10,700)
        enemy.rect.top=random.randint(10,450)

    def respawn_all(self,life,estado):
        for enemy in self.enemies:
            enemy.eliminado=False
            enemy.life=life
            enemy.estado=estado
            self.reset_enemy_position(enemy)

    def all_dead(self):
        for enemy in self.enemies:
            if enemy.eliminado==False:
                return False
        return True
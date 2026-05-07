# -*- coding: utf-8 -*-
from math import sqrt
import pygame, sys, random, shelve
from pygame import *
from Load_images import load_image, IMG_DIR
from Pause import Pause
from Panel import Time, Score1, Score2, Caratula, Lifebar
from Variables import personajes_p1, personajes_p2, life_bar, break_main, vol, mapas, mov_E1, jump_E1, pun_E1
from BattleInputController import BattleInputController
from Music_sounds import button_kick_2, new_surge
from Sprites import *
from Screen import *
from Load_map import *
from Load_joysticks import Load_joys
from Scores import *
from BattleUtils import distance, enemy_attack
from BattleEnemyManager import EnemyManager

# Enemy states
EASY = 1
MEDIUM = 2
HARD = 3

# Enemy damage values based on difficulty
enemy_damage = {
    EASY: 0.001,
    MEDIUM: 0.01,
    HARD: 0.1
}

class Game_screen:
    def __init__(self):
        self.screen = screen
        self.timer = pygame.time.Clock()
        self.entities = pygame.sprite.RenderUpdates()

        # Carga los players
        self.jugador1 = Player(350,350,1)
        self.jugador2 = Player(420,350,2)
            
        self.platforms = []
        
        pygame.mixer.music.set_volume(vol[0])
        
        # Carga mapas
        Load_map(self)
        pygame.mixer.music.play(-1, 0.0) # reproduce musica

        # Carga imágenes
        self.vine_image = load_image(
            "symbols/blood.png",
            IMG_DIR,
            alpha=True
        )

        self.tomb_images = [
            load_image("sprites/tomb/1.png", IMG_DIR, alpha=True),
            load_image("sprites/tomb/2.png", IMG_DIR, alpha=True),
            load_image("sprites/tomb/3.png", IMG_DIR, alpha=True)
        ]

        self.player_tomb = load_image(
            "sprites/tomb/tumba.png",
            IMG_DIR,
            alpha=True
        )
        
        # Carga enemigo
        self.enemy_manager=EnemyManager()
        self.e1=self.enemy_manager.e1
        self.e2=self.enemy_manager.e2
        self.e3=self.enemy_manager.e3
        self.e4=self.enemy_manager.e4
        self.e5=self.enemy_manager.e5
    
        self.font = pygame.font.Font("fonts/MotionControl-BoldItalic.otf", 50)
        
        # Letra de % de vida
        self.font_vida = pygame.font.Font("fonts/MotionControl-BoldItalic.otf", 20)
    
        self.poder = Power(random.randint(40,600),random.randint(40,550))

        # Carga Joysticks        
        if joy_on:   
            Load_joys(self)

        # Construye el level
        self.x = self.y = 0
        for row in self.level:
            for col in row:
                if col == "P":
                    p = Platform(self.x, self.y)
                    self.platforms.append(p)
                    self.entities.add(p)
                if col == "E":
                    e = ExitBlock(self.x, self.y)
                    self.platforms.append(e)
                    self.entities.add(e)
                self.x += 10.55
            self.y += 10.35
            self.x = 2.5
        
        # Checkquear colisiones con enemigos
        self.entities_to_check = [
            self.jugador1,
            self.jugador2,
            *self.enemy_manager.enemies
        ]

    def handle_event(self):
        self.entities.add(self.jugador1)
        self.entities.add(self.jugador2)
        self.enemy_manager.add_to_entities(self.entities)

        # Controlador de entradas
        try:
            from Variables import joy_on
        except ImportError:
            joy_on = False
        input_controller = BattleInputController(joy_on=joy_on, p1=getattr(self, 'p1', None), p2=getattr(self, 'p2', None))

        # Movimientos del enemigo 1
        move = True
        jump = punio = False
        c_jump_E1 = 0
        pos = 0
        objetivo = self.jugador2
        enemigo = self.jugador1
        chronus = Time()
        cronometro = chronus.get_segundos()
        puntaje1 = Score1()
        puntaje2 = Score2()
        cara = Caratula()
        game = True
        c_breaker = 0
        c_scores = 0
        c_state = 0
        state = 0
        maxima = False
        vida = Lifebar()
        vida_p1 = life_bar[0]
        vida_p2 = life_bar[1]
        bot = self.enemy_manager.bot
        bot2 = self.enemy_manager.bot2
        surge = 0

        while game:
            c_jump_E1 += 1 / 60
            if state == 0:
                if int(c_jump_E1) == 4:
                    jump = True
                    c_jump_E1 = 0
            elif state == 1:
                if int(c_jump_E1) == 3:
                    jump = True
                    c_jump_E1 = 0
            elif state == 2:
                if int(c_jump_E1) == 2:
                    jump = True
                    c_jump_E1 = 0
            elif state == 3:
                if int(c_jump_E1) == 1:
                    jump = True
                    c_jump_E1 = 0

            if self.enemy_manager.all_dead():
                bot = self.e4
                bot2 = self.e5
                c_state += 1 / 60
                surge += 1

            if surge == 60:
                new_surge.play()
                new_surge.set_volume(sou[0])

            if int(c_state) == 5:
                surge = 0
                if state == 0:
                    self.enemy_manager.respawn_all(50, 2)
                    c_state = 0
                    state += 1
                elif state == 1:
                    self.enemy_manager.respawn_all(60, 3)
                    c_state = 0
                    state += 1
                elif state == 2:
                    self.enemy_manager.respawn_all(75, 3)
                    c_state = 0
                    state += 1
                elif state == 3:
                    self.enemy_manager.respawn_all(100, 3)
                    c_state = 0
                    state += 1

            self.timer.tick(60)
            cronometro += 1

            # Procesar eventos de entrada
            for e in pygame.event.get():
                if e.type == pygame.QUIT:
                    sys.exit(0)
                # Pausa universal
                if (e.type == pygame.KEYDOWN and e.key == K_RETURN) or (input_controller.joy_on and e.type in [pygame.JOYBUTTONDOWN] and (getattr(e, 'button', -1) in [7, 9])):
                    input_controller.reset_inputs()
                    P = Pause()
                    P.pause_loop()
                    continue
                if e.type == pygame.KEYDOWN and e.key == K_ESCAPE:
                    game = False
                    continue
                input_controller.process_event(e)

            inputs = input_controller.get_inputs()
            up = inputs['up']
            down = inputs['down']
            left = inputs['left']
            right = inputs['right']
            running = inputs['running']
            kick = inputs['kick']
            attack = inputs['attack']
            arriba = inputs['arriba']
            abajo = inputs['abajo']
            izquierda = inputs['izquierda']
            derecha = inputs['derecha']
            correr = inputs['correr']
            golpe = inputs['golpe']
            ataque = inputs['ataque']

            # Reduce la vida mientras no esté en movimiento (p1,p2)
            if left or right or up:
                if vida_p2 <= 0:
                    vida_p2 = 0
            elif not left and not right and not up:
                vida_p2 -= 0.05
                if vida_p2 <= 0:
                    vida_p2 = 0
            if izquierda or derecha or arriba:
                if vida_p1 <= 0:
                    vida_p1 = 0
            elif not izquierda and not derecha and not arriba:
                vida_p1 -= 0.05
                if vida_p1 <= 0:
                    vida_p1 = 0

            # Limitar que la vida no baje a (-) cuando ambos pegan
            if kick and golpe:
                if vida_p1 <= 0:
                    vida_p1 = 0
                if vida_p2 <= 0:
                    vida_p2 = 0
            # Limitar que la vida no suba a (+) cuando peguen
            if kick or golpe:
                if vida_p1 > 200:
                    vida_p1 = 200
                if vida_p2 > 200:
                    vida_p2 = 200

            p1x = self.jugador1.get_pos_x()
            p1y = self.jugador1.get_pos_y()
            p2x = self.jugador2.get_pos_x()
            p2y = self.jugador2.get_pos_y()
            distance_p1_p2 = distance(p1x, p1y, p2x, p2y)

            # Obtiene las distancias entre el enemigo y el jugador
            for enemy in self.enemy_manager.enemies:
                d1 = distance(p1x, p1y, enemy.get_pos_x(), enemy.get_pos_y())
                d2 = distance(p2x, p2y, enemy.get_pos_x(), enemy.get_pos_y())
                if d1 <= 50:
                    if enemy.eliminado:
                        bot = self.e4
                    else:
                        bot = enemy
                        enemy.punio = enemy.estado >= MEDIUM
                        vida_p2 -= enemy_damage[enemy.estado]
                    if not enemy.eliminado and kick and (right or left):
                        enemy.life -= 0.2
                        puntaje1.set_score(5)
                elif d2 <= 50:
                    if enemy.eliminado:
                        bot2 = self.e5
                    else:
                        bot2 = enemy
                        enemy.punio = True
                        vida_p1 -= enemy_damage[enemy.estado]
                    if not enemy.eliminado and golpe and (izquierda or derecha):
                        enemy.life -= 0.2
                        puntaje2.set_score(5)
                else:
                    enemy.punio = False

            for index, enemy in enumerate(self.enemy_manager.enemies):
                if enemy.life <= 1:
                    enemy.image = self.tomb_images[index]
                    enemy.eliminado = True

            # Setea el score mientras el jugador este cerca y este pegando
            if distance_p1_p2 <= 36 and kick and (right or left):
                vida_p2 += 0.05
                puntaje1.set_score(10)
                vida_p1 -= 0.2
                button_kick_2.play()
                button_kick_2.set_volume(sou[0])
            if distance_p1_p2 <= 36 and golpe and (izquierda or derecha):
                vida_p1 += 0.05
                puntaje2.set_score(10)
                vida_p2 -= 0.2
                button_kick_2.play()
                button_kick_2.set_volume(sou[0])

            # Si se buguea, se reinica a la posicion 300,300
            if self.jugador1.rect.left > 800 or self.jugador1.rect.left == 0 or self.jugador1.rect.top > 600 or self.jugador1.rect.top == 0:
                self.jugador1.rect.left = 300
                self.jugador1.rect.top = 300
            if self.jugador2.rect.left > 800 or self.jugador2.rect.left == 0 or self.jugador2.rect.top > 600 or self.jugador2.rect.top == 0:
                self.jugador2.rect.left = 300
                self.jugador2.rect.top = 300

            for entity in self.entities_to_check:
                if (
                    entity.rect.left > 800
                    or entity.rect.left == 0
                    or entity.rect.top > 600
                    or entity.rect.top == 0
                ):
                    entity.rect.left = 300
                    entity.rect.top = 300

            # Muestra el mapa y las plataformas
            self.screen.blit(self.mapa, (0, 0))
            self.screen.blit(self.plataforma, (0, 0))

            # Dibuja al jugador y sus caracteristicas
            self.entities.draw(self.screen)
            self.jugador1.update(pos, up, down, left, right, running, self.platforms, objetivo, attack, kick, bot)
            self.jugador2.update(pos, arriba, abajo, izquierda, derecha, correr, self.platforms, enemigo, ataque, golpe, bot2)

            for enemy in self.enemy_manager.enemies:
                if not enemy.eliminado:
                    enemy.update(
                        pos,
                        jump,
                        down,
                        move,
                        self.platforms,
                        objetivo,
                        attack,
                        punio,
                        enemigo
                    )
                    enemy.life_bar(enemy.life)

            # Reinicia el salto del enemigo
            if c_jump_E1 == 0:
                jump = False

            # Muestra el conometro por pantalla
            chronus.show_time()
            # Muestra los puntajes por pantalla
            puntaje1.show_score()
            puntaje2.show_score()
            # Muestra las caras por pantalla
            cara.show_caratula_p1()
            cara.show_caratula_p2()
            #vida.show_vida_p1()
            vida.show_life_bar(vida_p1, vida_p2)
            vida.show_rectangle()
            show_por_vida_1 = self.font_vida.render(str(int(vida_p2 / 2)) + "%", True, (255, 255, 255))
            show_por_vida_2 = self.font_vida.render(str(int(vida_p1 / 2)) + "%", True, (255, 255, 255))
            self.screen.blit(show_por_vida_1, (310, 520))
            self.screen.blit(show_por_vida_2, (470, 520))

            if break_main[0] == True:
                game = False

            if int(vida_p1) == 0:
                self.screen.blit(self.vine_image, (170, 200))
                imp_vida1 = self.font.render("  Player 2 has lost", True, (255, 255, 255))
                self.screen.blit(imp_vida1, (250, 250))
                self.jugador2.image = self.player_tomb
                vida.show_vin()
                c_breaker += 1
                c_scores += 1
                if c_breaker == 300:
                    break_main[0] = True
            elif int(vida_p2) == 0:
                self.screen.blit(self.vine_image, (170, 200))
                imp_vida2 = self.font.render("  Player 1 has lost", True, (255, 255, 255))
                self.screen.blit(imp_vida2, (250, 250))
                self.jugador1.image = self.player_tomb
                vida.show_vin()
                c_scores += 1
                c_breaker += 1
                if c_breaker == 300:
                    break_main[0] = True

            if c_scores == 1:
                score1 = puntaje1.get_score()
                score2 = puntaje2.get_score()
                minx = chronus.get_minutos()
                secx = chronus.get_segundos()
                t_final = str(minx) + ":" + str(secx)
                if score1 > score2:
                    p_final = score1
                elif score2 > score1:
                    p_final = score2
                elif score2 == score1:
                    p_final = 0
                puntuacion_mas_alta = Scores.obtener_puntuacion_mas_alta()
                try:
                    puntuacion_actual = p_final
                except ValueError:
                    print("ERROR")
                if puntuacion_actual > puntuacion_mas_alta:
                    maxima = True
                    Scores.guardar_puntuacion_mas_alta(puntuacion_actual, t_final)
                else:
                    print("Mejor suerte la próxima vez!")

            if maxima == True:
                highx = self.font.render("¡New Highscore!", True, (255, 255, 255))
                self.screen.blit(highx, (285, 300))

            pygame.display.update()

if __name__ == "__main__":
    g = Game_screen()
    g.handle_event()

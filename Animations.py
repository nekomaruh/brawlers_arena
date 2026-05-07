# -*- coding: utf-8 -*-
import pygame
from typing import Any
from Load_images import load_image, IMG_DIR
from Music_sounds import *
import random
from Variables import *
from Panel import Score1

# =====================================================================
# CONFIGURACIÓN DE PERSONAJES Y ENEMIGOS (Data-Driven)
# =====================================================================
# Aquí centralizamos todos los sprites y sonidos para no repetir código.
# Si en el futuro quieres añadir más personajes, solo agregas un bloque aquí.

FIGHTER_CONFIG = {
    # --- JUGADORES ---
    "soldier": {
        "speed": 4,
        "run_bonus": 4,
        "jump_power": 13,
        "double_jump": 12,
        "gravity": 1, # Ajusta según tu Variables.py si es diferente
        "sound_kick": button_kick,
        "idle_img": "images/sprites/soldier/0.png",
        "jump_l": "sprites/soldier/12.png",
        "jump_r": "sprites/soldier/4.png",
        "melee_r": ["sprites/soldier/7.png", "sprites/soldier/melee/0.png", "sprites/soldier/melee/1.png"],
        "melee_l": ["sprites/soldier/15.png", "sprites/soldier/melee/2.png", "sprites/soldier/melee/3.png"]
    },
    "robot": {
        "speed": 5,
        "run_bonus": 4,
        "jump_power": 13,
        "double_jump": 10,
        "gravity": 1,
        "sound_kick": button_kick,
        "idle_img": "images/sprites/robot/1.png",
        "jump_l": "sprites/robot/9.png",
        "jump_r": "sprites/robot/8.png",
        "melee_r": ["sprites/robot/6.png", "sprites/robot/melee/0.png", "sprites/robot/melee/1.png"],
        "melee_l": ["sprites/robot/7.png", "sprites/robot/melee/2.png", "sprites/robot/melee/3.png"]
    },
    "thing": {
        "speed": 4,
        "run_bonus": 4,
        "jump_power": 13,
        "double_jump": 12,
        "gravity": 1,
        "sound_kick": button_kick,
        "idle_img": "images/sprites/thing/2.png",
        "jump_l": "sprites/thing/12.png",
        "jump_r": "sprites/thing/4.png",
        "melee_r": ["sprites/thing/7.png", "sprites/thing/melee/0.png", "sprites/thing/melee/1.png"],
        "melee_l": ["sprites/thing/15.png", "sprites/thing/melee/2.png", "sprites/thing/melee/3.png"]
    },
    "astro": {
        "speed": 3,
        "run_bonus": 4,
        "jump_power": 13,
        "double_jump": 10,
        "gravity": 0.5, # Gravedad lunar
        "sound_kick": button_kick,
        "idle_img": "images/sprites/astro/1.png",
        "jump_l": "sprites/astro/12.png",
        "jump_r": "sprites/astro/4.png",
        "melee_r": ["sprites/astro/7.png", "sprites/astro/melee/0.png", "sprites/astro/melee/1.png"],
        "melee_l": ["sprites/astro/15.png", "sprites/astro/melee/2.png", "sprites/astro/melee/3.png"]
    },
    "anubis": {
        "speed": 4,
        "run_bonus": 4,
        "jump_power": 13,
        "double_jump": 12,
        "gravity": 1,
        "sound_kick": button_kick,
        "idle_img": "images/sprites/anubis/0.png",
        "jump_l": "sprites/anubis/15.png",
        "jump_r": "sprites/anubis/14.png",
        "melee_r": ["sprites/anubis/6.png", "sprites/anubis/melee/0.png", "sprites/anubis/melee/1.png"],
        "melee_l": ["sprites/anubis/13.png", "sprites/anubis/melee/2.png", "sprites/anubis/melee/3.png"]
    },
    
    # --- ENEMIGOS (UFO, DUCK, MUMMY, GHOST, PROTOTYPE) ---
    # Tienen velocidades variables según su estado (1, 2, 3), manejado en la lógica.
    "ufo": {
        "jump_power": 15,
        "gravity": 1,
        "sound_kick": ufo_golpe,
        "melee_r": ["sprites/ufo/melee/0.png", "sprites/ufo/melee/2.png", "sprites/ufo/melee/2.png"],
        "melee_l": ["sprites/ufo/melee/4.png", "sprites/ufo/melee/5.png", "sprites/ufo/melee/5.png"]
    },
    "duck": {
        "jump_power": 15,
        "gravity": 1,
        "sound_kick": cuack_golpe,
        "melee_r": ["sprites/duck/3.png"],
        "melee_l": ["sprites/duck/6.png"]
    },
    "mummy": {
        "jump_power": 15,
        "gravity": 1,
        "sound_kick": momia_golpe,
        "melee_r": ["sprites/mummy/1.png"],
        "melee_l": ["sprites/mummy/4.png"]
    },
    "ghost": {
        "jump_power": 15,
        "gravity": 1,
        "sound_kick": ghost_golpe,
        "melee_r": [], # Ghost no tenía sprites de ataque en el código original, usa animación base
        "melee_l": []
    },
    "prototype": {
        "jump_power": 15,
        "gravity": 1,
        "sound_kick": robot_golpe,
        "melee_r": ["sprites/prototype/melee/2.png"],
        "melee_l": ["sprites/prototype/melee/3.png"]
    }
}

# =====================================================================
# LÓGICA CENTRALIZADA (Base Entity / Mixin)
# =====================================================================

class BaseFighter:
    def _ensure_config(self, fighter_type: str) -> None:
        """Inicializa las variables del personaje de forma perezosa (Lazy Init)."""
        if not hasattr(self, 'config') or getattr(self, '_fighter_type', None) != fighter_type:
            self.config = FIGHTER_CONFIG.get(fighter_type, {})
            self._fighter_type = fighter_type
            
            # Cargar estadísticas desde el diccionario
            self.base_speed = self.config.get("speed", 4)
            self.run_bonus = self.config.get("run_bonus", 4)
            self.jump_power = self.config.get("jump_power", 13)
            self.double_jump_power = self.config.get("double_jump", 12)
            self.gravity = self.config.get("gravity", 1)
            
            # Inicializar variables de estado requeridas por la lógica si no existen
            if not hasattr(self, 'ataque'): self.ataque = 0
            if not hasattr(self, 'doble'): self.doble = False
            if not hasattr(self, 'xvel'): self.xvel = 0
            if not hasattr(self, 'yvel'): self.yvel = 0

    def _base_update(self, fighter_type: str, up: bool, left: bool, right: bool, running: bool, 
               platforms: list, objetivo: Any, attack: bool, kick: bool, 
               enemigo_o_bot: Any, state_speed_override: int = 0) -> None:
        
        # 1. Asegurar configuración
        BaseFighter._ensure_config(self, fighter_type)
        
        # 2. Determinar velocidad actual
        current_speed = state_speed_override if state_speed_override > 0 else self.base_speed
        
        # 3. Lógica Horizontal y Animación
        if right:
            if kick:
                self.ataque += 1
                melee_list = self.config.get("melee_r", [])
                if melee_list:
                    if self.ataque >= len(melee_list) * 2:
                        self.ataque = 0
                    self.image = load_image(melee_list[self.ataque // 2], IMG_DIR, alpha=True)
                
                sound = self.config.get("sound_kick")
                if sound:
                    sound.play()
                    try: sound.set_volume(sou[0])
                    except: pass
                    
            self.xvel = current_speed + (self.run_bonus if running else 0)
            self.x += 1 # RESTAURADO: Necesario para el cálculo de distancia de la IA
            
            # Animación de caminar original
            if hasattr(self, 'ani_speed'):
                self.ani_speed -= 1
                if self.ani_speed <= 0:
                    self.image = pygame.image.load(self.ani[self.ani_pos])
                    self.ani_speed = self.ani_speed_init
                    if self.ani_pos >= self.ani_max:
                        self.ani_pos = 0
                    else:
                        self.ani_pos += 1
            self.r = self.image # RESTAURADO: El motor de IA lo puede estar leyendo

        elif left:
            if kick:
                self.ataque += 1
                melee_list = self.config.get("melee_l", [])
                if melee_list:
                    if self.ataque >= len(melee_list) * 2:
                        self.ataque = 0
                    self.image = load_image(melee_list[self.ataque // 2], IMG_DIR, alpha=True)
                
                sound = self.config.get("sound_kick")
                if sound:
                    sound.play()
                    try: sound.set_volume(sou[0])
                    except: pass

            self.xvel = -current_speed - (self.run_bonus if running else 0)
            self.x -= 1 # RESTAURADO: Necesario para el cálculo de distancia de la IA
            
            # Animación de caminar original (espejada)
            if hasattr(self, 'ani_speed'):
                self.ani_speed -= 1
                if self.ani_speed <= 0:
                    self.image = pygame.image.load(self.ani[self.ani_pos])
                    self.image = pygame.transform.flip(self.image, True, False)
                    self.ani_speed = self.ani_speed_init
                    if self.ani_pos >= self.ani_max:
                        self.ani_pos = 0
                    else:
                        self.ani_pos += 1
            self.l = self.image # RESTAURADO: El motor de IA lo puede estar leyendo
        else:
            self.xvel = 0
            if "idle_img" in self.config:
                self.image = pygame.image.load(self.config["idle_img"]).convert_alpha()

        # 4. Lógica Vertical (Saltos y Gravedad)
        if self.onGround:
            if up:
                self.yvel -= self.jump_power
                self.doble = True
        else:
            self.yvel += self.gravity
            
            if self.yvel > 0 and getattr(self, 'doble', False):               
                if up:
                    self.yvel -= self.double_jump_power
                    self.doble = False
                    if left and "jump_l" in self.config:
                        self.image = load_image(self.config["jump_l"], IMG_DIR, alpha=True)
                    elif right and "jump_r" in self.config:
                        self.image = load_image(self.config["jump_r"], IMG_DIR, alpha=True)

        # 5. Aplicar físicas X y evaluar colisiones
        self.rect.left += self.xvel
        self.collide(self.xvel, 0, platforms)
        
        if objetivo: 
            self.colision(self.xvel, 0, objetivo)
        if enemigo_o_bot: 
            self.colision(self.xvel, 0, enemigo_o_bot)

        # 6. Aplicar físicas Y y evaluar colisiones
        self.rect.top += self.yvel
        self.onGround = False
        
        self.collide(0, self.yvel, platforms)
        
        if objetivo: 
            self.colision(0, self.yvel, objetivo)
        if enemigo_o_bot: 
            self.colision(0, self.yvel, enemigo_o_bot)

# =====================================================================
# WRAPPERS DE COMPATIBILIDAD: JUGADORES
# =====================================================================

class handle_soldado:
    def update1(self, pos, up, down, left, right, running, platforms, objetivo, attack, kick, bot):
        BaseFighter._base_update(self, "soldier", up, left, right, running, platforms, objetivo, attack, kick, bot)

class handle_robot:
    def update1(self, pos, up, down, left, right, running, platforms, objetivo, attack, kick, bot):
        BaseFighter._base_update(self, "robot", up, left, right, running, platforms, objetivo, attack, kick, bot)

class handle_thing:
    def update1(self, pos, up, down, left, right, running, platforms, objetivo, attack, kick, bot):
        BaseFighter._base_update(self, "thing", up, left, right, running, platforms, objetivo, attack, kick, bot)

class handle_astro:
    def update1(self, pos, up, down, left, right, running, platforms, objetivo, attack, kick, bot):
        BaseFighter._base_update(self, "astro", up, left, right, running, platforms, objetivo, attack, kick, bot)

class handle_anubis:
    def update1(self, pos, up, down, left, right, running, platforms, objetivo, attack, kick, bot):
        BaseFighter._base_update(self, "anubis", up, left, right, running, platforms, objetivo, attack, kick, bot)


# =====================================================================
# WRAPPERS DE COMPATIBILIDAD: ENEMIGOS
# =====================================================================
# CAMBIO: Usamos `getattr(self, 'move', 0)` porque la IA altera `self.move`, NO el argumento `move`.

class handle_ufo:
    def state_1(self, pos, jump, down, move, platforms, objetivo, attack, punio, enemigo):
        c_move = getattr(self, 'move', 0)
        BaseFighter._base_update(self, "ufo", jump, c_move==-1, c_move==1, False, platforms, objetivo, attack, False, enemigo, 2)

    def state_2(self, pos, jump, down, move, platforms, objetivo, attack, punio, enemigo):
        c_move = getattr(self, 'move', 0)
        BaseFighter._base_update(self, "ufo", jump, c_move==-1, c_move==1, False, platforms, objetivo, attack, punio, enemigo, 2)

    def state_3(self, pos, jump, down, move, platforms, objetivo, attack, punio, enemigo):
        c_move = getattr(self, 'move', 0)
        BaseFighter._base_update(self, "ufo", jump, c_move==-1, c_move==1, False, platforms, objetivo, attack, punio, enemigo, 3)

class handle_duck:
    def state_1(self, pos, jump, down, move, platforms, objetivo, attack, punio, enemigo):
        c_move = getattr(self, 'move', 0)
        BaseFighter._base_update(self, "duck", jump, c_move==-1, c_move==1, False, platforms, objetivo, attack, False, enemigo, 2)

    def state_2(self, pos, jump, down, move, platforms, objetivo, attack, punio, enemigo):
        c_move = getattr(self, 'move', 0)
        BaseFighter._base_update(self, "duck", jump, c_move==-1, c_move==1, False, platforms, objetivo, attack, punio, enemigo, 2)

    def state_3(self, pos, jump, down, move, platforms, objetivo, attack, punio, enemigo):
        c_move = getattr(self, 'move', 0)
        BaseFighter._base_update(self, "duck", jump, c_move==-1, c_move==1, False, platforms, objetivo, attack, punio, enemigo, 3)

class handle_mummy:
    def state_1(self, pos, jump, down, move, platforms, objetivo, attack, punio, enemigo):
        c_move = getattr(self, 'move', 0)
        BaseFighter._base_update(self, "mummy", jump, c_move==-1, c_move==1, False, platforms, objetivo, attack, False, enemigo, 2)

    def state_2(self, pos, jump, down, move, platforms, objetivo, attack, punio, enemigo):
        c_move = getattr(self, 'move', 0)
        BaseFighter._base_update(self, "mummy", jump, c_move==-1, c_move==1, False, platforms, objetivo, attack, punio, enemigo, 2)

    def state_3(self, pos, jump, down, move, platforms, objetivo, attack, punio, enemigo):
        c_move = getattr(self, 'move', 0)
        BaseFighter._base_update(self, "mummy", jump, c_move==-1, c_move==1, False, platforms, objetivo, attack, punio, enemigo, 3)

class handle_ghost:
    def state_1(self, pos, jump, down, move, platforms, objetivo, attack, punio, enemigo):
        c_move = getattr(self, 'move', 0)
        BaseFighter._base_update(self, "ghost", jump, c_move==-1, c_move==1, False, platforms, objetivo, attack, False, enemigo, 2)

    def state_2(self, pos, jump, down, move, platforms, objetivo, attack, punio, enemigo):
        c_move = getattr(self, 'move', 0)
        BaseFighter._base_update(self, "ghost", jump, c_move==-1, c_move==1, False, platforms, objetivo, attack, punio, enemigo, 2)

    def state_3(self, pos, jump, down, move, platforms, objetivo, attack, punio, enemigo):
        c_move = getattr(self, 'move', 0)
        BaseFighter._base_update(self, "ghost", jump, c_move==-1, c_move==1, False, platforms, objetivo, attack, punio, enemigo, 3)

class handle_prototype:
    def state_1(self, pos, jump, down, move, platforms, objetivo, attack, punio, enemigo):
        c_move = getattr(self, 'move', 0)
        BaseFighter._base_update(self, "prototype", jump, c_move==-1, c_move==1, False, platforms, objetivo, attack, False, enemigo, 2)

    def state_2(self, pos, jump, down, move, platforms, objetivo, attack, punio, enemigo):
        c_move = getattr(self, 'move', 0)
        BaseFighter._base_update(self, "prototype", jump, c_move==-1, c_move==1, False, platforms, objetivo, attack, punio, enemigo, 2)

    def state_3(self, pos, jump, down, move, platforms, objetivo, attack, punio, enemigo):
        c_move = getattr(self, 'move', 0)
        BaseFighter._base_update(self, "prototype", jump, c_move==-1, c_move==1, False, platforms, objetivo, attack, punio, enemigo, 3)
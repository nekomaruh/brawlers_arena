# -*- coding: utf-8 -*-
from math import sqrt
import pygame, sys, random, shelve
from pygame import *
from Load_images import load_image, IMG_DIR
from Pause import Pause
from Panel import Time, Score1, Score2, Caratula, Lifebar
from Variables import personajes_p1, personajes_p2, life_bar, break_main, vol, mapas, mov_E1, jump_E1, pun_E1
from Music_sounds import button_kick_2, new_surge
from Sprites import *
from Screen import *
from Load_map import *
from Load_joysticks import Load_joys
from Scores import *

def enemy_attack(d1,d2,vida_enemigo,vida_p2,vida_p1,kick,right,left,golpe,izquierda,derecha,punio):
    if d1 <=50:
        punio=True
        vida_p2-=0.5
        if kick==True and(right or left)==True:
            vida_enemigo-=0.5
    elif d2 <=50:
        punio=True
        vida_p1-=0.5
        if golpe==True and(izquierda or derecha)==True:
            vida_enemigo-=0.5
    else:
        punio=False

def distance(x1,y1,x2,y2):
    d=int(sqrt((y2-y1)**2+(x2-x1)**2))
    return d


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
        
       
        # Carga enemigo
        self.e1=E1(random.randint(10,700),random.randint(10,450))
        self.e2=E1(random.randint(10,700),random.randint(10,450))
        self.e3=E1(random.randint(10,700),random.randint(10,450))
        self.e4=E1(800,600)
        self.e5=E1(800,600)

    
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
        

    def handle_event(self):
        self.entities.add(self.jugador1)
        self.entities.add(self.jugador2)
        self.entities.add(self.e1)
        self.entities.add(self.e2)
        self.entities.add(self.e3)
        #self.entities.add(self.e4)
        #self.entities.add(self.e5)
        up=down=left=right=running=arriba=abajo=izquierda=derecha=correr=attack=kick=ataque=golpe=False
        
        # Movimientos del enemigo 1
        move=True
        jump=punio=False
        c_jump_E1=0
        
        pos=0
        objetivo=self.jugador2
        enemigo=self.jugador1
        
        chronus = Time()
        cronometro=chronus.get_segundos()
        puntaje1 = Score1()
        puntaje2 = Score2()
        cara = Caratula()
        game = True

        c_breaker=0
        c_scores=0
        c_state=0
        state=0
        maxima=False

        vida = Lifebar()
        
        # Carga la vida de los jugadores
        vida_p1=life_bar[0]
        vida_p2=life_bar[1]
        
        bot=self.e4
        bot2=self.e5
        
        surge=0
        
        while game:
            c_jump_E1+=1/60
            
            if state==0:
                if int(c_jump_E1)==4:
                    jump=True
                    c_jump_E1=0
            elif state==1:
                if int(c_jump_E1)==3:
                    jump=True
                    c_jump_E1=0
            elif state==2:
                if int(c_jump_E1)==2:
                    jump=True
                    c_jump_E1=0
            elif state==3:
                if int(c_jump_E1)==1:
                    jump=True
                    c_jump_E1=0
            
            if self.e1.eliminado==True and self.e2.eliminado==True and self.e3.eliminado==True:
                bot=self.e4
                bot2=self.e5
                c_state+=1/60     
                surge+=1
            
            if surge==60:
                new_surge.play()
                new_surge.set_volume(sou[0])
                
            if int(c_state)==5:
                surge=0
                if state==0:
                    self.e1.eliminado=False
                    self.e2.eliminado=False
                    self.e3.eliminado=False
                    self.e1.life=50
                    self.e2.life=50
                    self.e3.life=50
                    self.e1.estado=2
                    self.e2.estado=2
                    self.e3.estado=2
                    self.e1.rect.left=random.randint(10,700)
                    self.e1.rect.top=random.randint(10,450)
                    self.e2.rect.left=random.randint(10,700)
                    self.e2.rect.top=random.randint(10,450)
                    self.e3.rect.left=random.randint(10,700)
                    self.e3.rect.top=random.randint(10,450)
                    c_state=0
                    state+=1
                elif state==1:
                    self.e1.eliminado=False
                    self.e2.eliminado=False
                    self.e3.eliminado=False
                    self.e1.life=60
                    self.e2.life=60
                    self.e3.life=60
                    self.e1.estado=3
                    self.e2.estado=3
                    self.e3.estado=3
                    self.e1.rect.left=random.randint(10,700)
                    self.e1.rect.top=random.randint(10,450)
                    self.e2.rect.left=random.randint(10,700)
                    self.e2.rect.top=random.randint(10,450)
                    self.e3.rect.left=random.randint(10,700)
                    self.e3.rect.top=random.randint(10,450)
                    c_state=0
                    state+=1
                elif state==2:
                    self.e1.eliminado=False
                    self.e2.eliminado=False
                    self.e3.eliminado=False
                    self.e1.life=75
                    self.e2.life=75
                    self.e3.life=75
                    self.e1.estado=3
                    self.e2.estado=3
                    self.e3.estado=3
                    self.e1.rect.left=random.randint(10,700)
                    self.e1.rect.top=random.randint(10,450)
                    self.e2.rect.left=random.randint(10,700)
                    self.e2.rect.top=random.randint(10,450)
                    self.e3.rect.left=random.randint(10,700)
                    self.e3.rect.top=random.randint(10,450)
                    c_state=0
                    state+=1
                elif state==3:
                    self.e1.eliminado=False
                    self.e2.eliminado=False
                    self.e3.eliminado=False
                    self.e1.life=100
                    self.e2.life=100
                    self.e3.life=100
                    self.e1.estado=3
                    self.e2.estado=3
                    self.e3.estado=3
                    self.e1.rect.left=random.randint(10,700)
                    self.e1.rect.top=random.randint(10,450)
                    self.e2.rect.left=random.randint(10,700)
                    self.e2.rect.top=random.randint(10,450)
                    self.e3.rect.left=random.randint(10,700)
                    self.e3.rect.top=random.randint(10,450)
                    c_state=0
                    state+=1

            self.timer.tick(60)
            cronometro+=1
            

            # Reduce la vida mientras no esté en movimiento (p1,p2)
            if left==True or right==True or up==True:
                vida_p2=vida_p2
                if vida_p2<=0:
                    vida_p2=0
                
            elif left==False and right==False and up==False:
                vida_p2-=0.05
                if vida_p2<=0:
                    vida_p2=0
                    
            if izquierda==True or derecha==True or arriba==True: 
                vida_p1=vida_p1
                if vida_p1<=0:
                    vida_p1=0
                    
            elif izquierda==False or derecha==False or arriba==False:
                vida_p1-=0.05
                if vida_p1<=0:
                    vida_p1=0            
            
            # Limitar que la vida no baje a (-) cuando ambos pegan
            if kick==True and golpe==True:
                if vida_p1<=0:
                    vida_p1=0
                if vida_p2<=0:
                    vida_p2=0
            
            # Limitar que la vida no suba a (+) cuando peguen
            if kick==True or golpe==True:
                if vida_p1>200:
                    vida_p1=200
                if vida_p2>200:
                    vida_p2=200
            
            distance_p1_p2=distance(self.jugador1.get_pos_x(),self.jugador1.get_pos_y(),self.jugador2.get_pos_x(),self.jugador2.get_pos_y())
            
            # Obtiene las distancias entre el enemigo y el jugador
            d1_e1=distance(self.jugador1.get_pos_x(),self.jugador1.get_pos_y(),self.e1.get_pos_x(),self.e1.get_pos_y())
            d2_e1=distance(self.jugador2.get_pos_x(),self.jugador2.get_pos_y(),self.e1.get_pos_x(),self.e1.get_pos_y())
            
            d1_e2=distance(self.jugador1.get_pos_x(),self.jugador1.get_pos_y(),self.e2.get_pos_x(),self.e2.get_pos_y())
            d2_e2=distance(self.jugador2.get_pos_x(),self.jugador2.get_pos_y(),self.e2.get_pos_x(),self.e2.get_pos_y())
            
            d1_e3=distance(self.jugador1.get_pos_x(),self.jugador1.get_pos_y(),self.e3.get_pos_x(),self.e3.get_pos_y())
            d2_e3=distance(self.jugador2.get_pos_x(),self.jugador2.get_pos_y(),self.e3.get_pos_x(),self.e3.get_pos_y())            
            
            # Ataque enemigo 1
            
            if d1_e1 <=50:
                if self.e1.eliminado==True:
                    bot=self.e4
                if self.e1.eliminado==False:
                    bot=self.e1
                    self.e1.punio=True
                    #punio=True
                    if self.e1.estado==1:
                        vida_p2-=0.001
                    elif self.e1.estado==2:
                        vida_p2-=0.01
                    elif self.e1.estado==3:
                        vida_p2-=0.1
                if kick==True and(right or left)==True:
                    if self.e1.eliminado==False:
                        self.e1.life-=0.2
                        puntaje1.set_score(5)
                   
            elif d2_e1 <=50:
                if self.e1.eliminado==True:
                    bot2=self.e5
                if self.e1.eliminado==False:
                    bot2=self.e1
                    self.e1.punio=True
                    #punio=True
                    if self.e1.estado==1:
                        vida_p1-=0.001
                    elif self.e1.estado==2:
                        vida_p1-=0.01
                    elif self.e1.estado==3:
                        vida_p1-=0.1
                if golpe==True and(izquierda or derecha)==True:
                    if self.e1.eliminado==False:
                        self.e1.life-=0.2
                        puntaje2.set_score(5)
            else:
                self.e1.punio=False
            # Ataque enemigo 2
            if d1_e2 <=50:
                if self.e2.eliminado==True:
                    bot=self.e4
                if self.e2.eliminado==False:
                    bot=self.e2
                    self.e2.punio=True
                    #punio=True
                    if self.e2.estado==1:
                        vida_p2-=0.001
                    elif self.e2.estado==2:
                        vida_p2-=0.01
                    elif self.e2.estado==3:
                        vida_p2-=0.1
                if kick==True and(right or left)==True:
                    if self.e2.eliminado==False:
                        self.e2.life-=0.2
                        puntaje1.set_score(5)
            elif d2_e2 <=50:
                if self.e2.eliminado==True:
                    bot2=self.e5
                if self.e2.eliminado==False:
                    bot2=self.e2
                    self.e2.punio=True
                    #punio=True
                    if self.e2.estado==1:
                        vida_p1-=0.001
                    elif self.e2.estado==2:
                        vida_p1-=0.01
                    elif self.e2.estado==3:
                        vida_p1-=0.1
                if golpe==True and(izquierda or derecha)==True:
                    if self.e2.eliminado==False:
                        self.e2.life-=0.2
                        puntaje2.set_score(5)
            else:
                self.e2.punio=False
            # ENEMI 3
            if d1_e3 <=50:
                if self.e3.eliminado==True:
                    bot=self.e4
                if self.e3.eliminado==False:
                    bot=self.e3
                    self.e3.punio=True
                    #punio=True
                    if self.e3.estado==1:
                        vida_p2-=0.001
                    elif self.e3.estado==2:
                        vida_p2-=0.01
                    elif self.e3.estado==3:
                        vida_p2-=0.1
                if kick==True and(right or left)==True:
                    if self.e3.eliminado==False:
                        self.e3.life-=0.2
                        puntaje1.set_score(5)
            elif d2_e3 <=50:
                if self.e3.eliminado==True:
                    bot2=self.e5
                if self.e3.eliminado==False:
                    bot2=self.e3
                    self.e3.punio=True
                    #punio=True
                    if self.e3.estado==1:
                        vida_p1-=0.001
                    elif self.e3.estado==2:
                        vida_p1-=0.01
                    elif self.e3.estado==3:
                        vida_p1-=0.1
                if golpe==True and(izquierda or derecha)==True:
                    if self.e3.eliminado==False:
                        self.e3.life-=0.2
                        puntaje2.set_score(5)
            else:
                self.e3.punio=False
            
            if self.e1.life<=1:
                self.e1.image=load_image("sprites/tomb/1.png",IMG_DIR,alpha=True)
                self.e1.eliminado=True
            
            if self.e2.life<=1:
                self.e2.image=load_image("sprites/tomb/2.png",IMG_DIR,alpha=True)
                self.e2.eliminado=True
                
            if self.e3.life<=1:
                self.e3.image=load_image("sprites/tomb/3.png",IMG_DIR,alpha=True)
                self.e3.eliminado=True
            
            # Setea el score mientras el jugador este cerca y este pegando
            if distance_p1_p2 <= 36 and kick==True and (right or left)==True:
                vida_p2+=0.05
                puntaje1.set_score(10)
                vida_p1-=0.2
                button_kick_2.play()
                button_kick_2.set_volume(sou[0])
            if distance_p1_p2 <= 36 and golpe==True and (izquierda or derecha)==True:
                vida_p1+=0.05
                puntaje2.set_score(10)
                vida_p2-=0.2
                button_kick_2.play()
                button_kick_2.set_volume(sou[0])
            
            for e in pygame.event.get():
                if e.type == pygame.QUIT:
                    sys.exit(0)
                
                if joy_on:
                    if e.type == pygame.JOYAXISMOTION:
                        a_1=self.p1.get_axis(0)
                        a_2=self.p2.get_axis(0)
                        # Para el p1
                        if e.joy==0:
                            if a_1>0.5:
                                right=True
                            elif a_1<-0.5:
                                left=True
                            else:
                                left=right=False
                        # Para el p2
                        if e.joy==1:
                            if a_2>0.5:
                                derecha=True
                            elif a_2<-0.5: 
                                izquierda=True
                            else:
                                izquierda=derecha=False

                    if e.type == pygame.JOYBUTTONDOWN:
                        # Para el P1
                        if e.joy ==0:
                            if e.button==0:
                                up=True
                            if e.button==2:
                                kick=True
                            if e.button==3:
                                attack=True
                            if e.button==5:
                                running=True
                            if e.button==7 or e.button==9:
                                up=down=left=right=arriba=abajo=izquierda=derecha=correr=running=attack=kick=ataque=golpe=False
                                P = Pause()
                                P.pause_loop()
                        
                        # Para el P2
                        if e.joy==1:
                            if e.button==0:
                                arriba=True
                            if e.button==2:
                                golpe=True
                            if e.button==3:
                                ataque=True
                            if e.button==5:
                                correr=True
                            if e.button==7 or e.button==9:
                                up=down=left=right=arriba=abajo=izquierda=derecha=correr=running=attack=kick=ataque=golpe=False
                                P = Pause()
                                P.pause_loop()
            
                    if e.type == pygame.JOYBUTTONUP:
                        if e.joy==0:
                            if e.button==0:
                                up=False
                            if e.button==2:
                                kick=False
                            if e.button==3:
                                attack=False
                            if e.button==5:
                                running=False
                        if e.joy==1:
                            if e.button==0:
                                arriba=False
                            if e.button==2:
                                golpe=False
                            if e.button==3:
                                ataque=False
                            if e.button==5:
                                correr=False
                
                if e.type == KEYDOWN:
                    # Para el jugador 1
                    if e.key == K_ESCAPE:
                        game = False
                    if e.key == K_UP:
                        up = True
                    if e.key == K_DOWN:
                        down = True
                    if e.key == K_LEFT:
                        left = True
                    if e.key == K_RIGHT:
                        right = True
                    if e.key == K_SPACE:
                        running = True
                    if e.key == K_RETURN:
                        up=down=left=right=arriba=abajo=izquierda=derecha=correr=running=attack=kick=ataque=golpe=False
                        P = Pause()
                        P.pause_loop()
                        
                    # Para el jugador 2
                    if e.key == K_w:
                        arriba=True
                    if e.key == K_d:
                        derecha=True
                    if e.key == K_a:
                        izquierda=True
                    if e.key == K_s:
                        abajo=True
                    if e.key == K_g:
                        correr = True

                if e.type == KEYUP:
                    # Para el jugador 1
                    if e.key == K_UP:
                        up = False
                    if e.key == K_DOWN:
                        down = False
                    if e.key == K_RIGHT:
                        right = False
                        pos=0
                    if e.key == K_LEFT:
                        left = False
                        pos=0
                    if e.key == K_SPACE:
                        running = False
                    
                    # Para el jugador 2
                    if e.key == K_w:
                        arriba = False
                    if e.key == K_s:
                        abajo = False
                    if e.key == K_d:
                        derecha = False
                        pos=0
                    if e.key == K_a:
                        izquierda = False
                        pos=0
                    if e.key == K_g:
                        correr = False
                        
            
            # Si se buguea, se reinica a la posicion 300,300
            if self.jugador1.rect.left>800 or self.jugador1.rect.left==0 or self.jugador1.rect.top>600 or self.jugador1.rect.top==0:
                self.jugador1.rect.left=300
                self.jugador1.rect.top=300
            if self.jugador2.rect.left>800 or self.jugador2.rect.left==0 or self.jugador2.rect.top>600 or self.jugador2.rect.top==0:
                self.jugador2.rect.left=300
                self.jugador2.rect.top=300
            if self.e1.rect.left>800 or self.e1.rect.left==0 or self.e1.rect.top>600 or self.e1.rect.top==0:
                self.e1.rect.left=300
                self.e1.rect.top=300
            if self.e2.rect.left>800 or self.e2.rect.left==0 or self.e2.rect.top>600 or self.e2.rect.top==0:
                self.e2.rect.left=300
                self.e2.rect.top=300
            if self.e3.rect.left>800 or self.e3.rect.left==0 or self.e3.rect.top>600 or self.e3.rect.top==0:
                self.e3.rect.left=300
                self.e3.rect.top=300
            
            # Muestra el mapa y las plataformas
            self.screen.blit(self.mapa,(0,0))
            self.screen.blit(self.plataforma,(0,0))
            
            # Dibuja al jugador y sus caracteristicas
            self.entities.draw(self.screen)
            self.jugador1.update(pos,up,down,left,right,running,self.platforms,objetivo,attack,kick,bot)
            self.jugador2.update(pos,arriba,abajo,izquierda,derecha,correr,self.platforms,enemigo,ataque,golpe,bot2)
            
            if self.e1.eliminado==False:
                self.e1.update(pos,jump,down,move,self.platforms,objetivo,attack,punio,enemigo)
                self.e1.life_bar(self.e1.life)
                
            if self.e2.eliminado==False:
                self.e2.update(pos,jump,down,move,self.platforms,objetivo,attack,punio,enemigo)
                self.e2.life_bar(self.e2.life)
            
            if self.e3.eliminado==False:
                self.e3.update(pos,jump,down,move,self.platforms,objetivo,attack,punio,enemigo)
                self.e3.life_bar(self.e3.life)        
            
            # Reinicia el salto del enemigo
            if c_jump_E1==0:
                jump=False
                        
            # Muestra el conometro por pantalla
            chronus.show_time()
            
            # Muestra los puntajes por pantalla
            puntaje1.show_score()
            puntaje2.show_score()
            
            # Muestra las caras por pantalla
            cara.show_caratula_p1()
            cara.show_caratula_p2()
            
            #vida.show_vida_p1()
            vida.show_life_bar(vida_p1,vida_p2)
            vida.show_rectangle()
            show_por_vida_1= self.font_vida.render(str(int(vida_p2/2))+"%", True, (255,255,255))
            show_por_vida_2= self.font_vida.render(str(int(vida_p1/2))+"%", True, (255,255,255))
            self.screen.blit(show_por_vida_1,(310,520))
            self.screen.blit(show_por_vida_2,(470,520))
            

            if break_main[0]==True:
                game=False
            
            if int(vida_p1)==0:
                #imp_vida1=self.font.render("Jugador 2 ha perdido", True, (255,255,255))
                vine=load_image("symbols/blood.png", IMG_DIR, alpha=True)
                self.screen.blit(vine,(170,200))
                imp_vida1=self.font.render("  Player 2 has lost", True, (255,255,255))
                self.screen.blit(imp_vida1,(250,250))
                self.jugador2.image=load_image("sprites/tomb/tumba.png", IMG_DIR, alpha=True)
                vida.show_vin()
                c_breaker+=1
                c_scores+=1

                if c_breaker==300:
                    break_main[0]=True
            elif int(vida_p2)==0:
                #imp_vida2=self.font.render("Jugador 1 ha perdido", True, (255,255,255))
                vine=load_image("symbols/blood.png", IMG_DIR, alpha=True)
                self.screen.blit(vine,(170,200))
                imp_vida2=self.font.render("  Player 1 has lost", True, (255,255,255))
                self.screen.blit(imp_vida2,(250,250))
                self.jugador1.image=load_image("sprites/tomb/tumba.png", IMG_DIR, alpha=True)
                vida.show_vin()
                c_scores+=1
                c_breaker+=1
                if c_breaker==300:
                    break_main[0]=True
            
            if c_scores==1:
                score1 = puntaje1.get_score()
                score2 = puntaje2.get_score()
                
                minx=chronus.get_minutos()
                secx=chronus.get_segundos()
                
                t_final=str(minx)+":"+str(secx)
                
                if score1 > score2:
                    p_final=score1
                elif score2 > score1:
                    p_final=score2
                elif score2==score1:
                    p_final=0

                puntuacion_mas_alta = Scores.obtener_puntuacion_mas_alta()
                
                try:
                    puntuacion_actual = p_final
                except ValueError:
                    print("ERROR")
                
                if puntuacion_actual > puntuacion_mas_alta:
                    maxima=True
                    Scores.guardar_puntuacion_mas_alta(puntuacion_actual,t_final)
                else:
                    print("Mejor suerte la próxima vez!") 
                    
            if maxima==True:
                highx=self.font.render("¡New Highscore!", True, (255,255,255))
                self.screen.blit(highx,(285,300))
    
                
            pygame.display.update()

if __name__ == "__main__":
    g = Game_screen()
    g.handle_event()



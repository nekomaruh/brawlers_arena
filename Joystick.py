# -*- coding: utf-8 -*-
import pygame

class Input:
    def __init__(self):
        self.p1 = pygame.joystick.Joystick(0) 
        self.p2 = pygame.joystick.Joystick(1)
        self.p1.init()
        self.p2.init()
    
    def joy(self):     
        # Possible joystick actions: JOYAXISMOTION JOYBALLMOTION JOYBUTTONDOWN JOYBUTTONUP JOYHATMOTION
        if e.type == pygame.JOYAXISMOTION:
            a_1=self.p1.get_axis(0)
            a_2=self.p2.get_axis(0)
            # Para el p1
            if e.joy==0:
                if a_1>0.5:
                    print("derecha1")
                elif a_1<-0.5:
                    print("izquierda1")
            # Para el p2
            if e.joy==1:
                if a_2>0.5:
                    print("derecha")
                elif a_2<-0.5:
                    print("izquierda")  

        if e.type == pygame.JOYBUTTONDOWN:
            # Para el P1
            if e.button==0 and e.joy ==0:
                up=True
            elif e.button==1 and e.joy ==0:
                print("o")
            elif e.button==2 and e.joy ==0:
                print("■")
            elif e.button==3 and e.joy ==0:
                print("▲")
            elif e.button==5 and e.joy ==0:
                print("run")
            elif e.button==7 and e.joy ==0:
                print("start")
            # Para el P2
            if e.button==0 and e.joy ==1:
                arriba=True
            elif e.button==1 and e.joy ==1:
                print("o")
            elif e.button==2 and e.joy ==1:
                print("■")
            elif e.button==3 and e.joy ==1:
                print("▲")
            elif e.button==5 and e.joy ==1:
                print("run")
            elif e.button==7 and e.joy ==1:
                print("start")
            
        if e.type == pygame.JOYBUTTONUP:
            if e.joy==0:
                if e.button==0:
                    up=False
            if e.joy==1:
                if e.button==0:
                    arriba=False
                
        if e.type == pygame.JOYHATMOTION:
            hx_1=self.p1.get_hat(0)[0]
            hy_1=self.p1.get_hat(0)[1]
            hx_2=self.p2.get_hat(0)[0]
            hy_2=self.p2.get_hat(0)[1]
            # Para el player 1
            if e.joy==0:
                if hx_1 ==1:
                    print("d")
                elif hx_1 ==-1:
                    print("i")
                elif hy_1 ==1:
                    print("a")
                elif hy_1==-1:
                    print("ab")
            # Para el player 2
            if e.joy ==1:
                if hx_2 ==1:
                    print("2d")
                elif hx_2 ==-1:
                    print("2i")
                elif hy_2 ==1:
                    print("2a")
                elif hy_2==-1:
                    print("2ab")
    def key(self):
        if e.type == KEYDOWN:
            # Para el jugador 1
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
                up=down=left=right=arriba=abajo=izquierda=derecha=False
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

                
                
        
    
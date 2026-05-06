__author__ = 'TeamFlammers'

import pygame, time, random
from Load_images import *
from Main_menu import *

pygame.init()
black=(0,0,0)
green=(0,255,0)
blue=(0,0,255)
small_font=pygame.font.SysFont("comicsansms",25)
ancho=800
largo=600
size=(ancho,largo)
screen=pygame.display.set_mode(size)
clock=pygame.time.Clock()
progress=0



logo=load_image("symbols/team_logo.png",IMG_DIR,alpha=True)

def text_objects(text,color,size):
    if size=="small":
        text_surface=small_font.tender(text,True,color)
    return text_surface,text_surface.get_rect()

def loading(progress):
    if progress < 100:
        text = small_font.render("Loading "+str(int(progress))+"%",True,green)
    else:
        text = small_font.render("Loading "+str(100)+"%",True,green)
    screen.blit(text,(335,423))

def message_to_screen(msg,color,y_displace=0,size="small"):
    text_surface,textRect=text_objects(msg,color,size)
    textRect.center = (ancho/2),(largo/2)
    screen.blit(text_surface,textRect.center)

time_count=1/15
launch=True
while(progress/2)<100:
    clock.tick(60)
    for e in pygame.event.get():
        if e.type == pygame.QUIT:
            sys.exit(0)
    increase = random.randint(1,5)
    progress += increase
    screen.fill(black)
    pygame.draw.rect(screen,blue,(310,373,204,49))
    pygame.draw.rect(screen,black,(311,374,202,47))
    if progress/2 >100:
        pygame.draw.rect(screen,green,(312,375,200,45))
    elif progress/2>95:
        run = main()
        run.main_loop()
    else:
        pygame.draw.rect(screen,green,(312,375,progress,45))
    loading(progress/2)
    screen.blit(logo,(260,50))
    pygame.display.flip()
    time.sleep(time_count)

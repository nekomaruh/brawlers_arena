import pygame, time, random
from pygame.locals import *
from Load_images import *
from Main_menu import main
from colores import BLACK,GREEN,BLUE
from Screen import *

pygame.init()
size=(800,600)
pygame.display.set_caption("Brawler's Arena")
Surface=pygame.image.load('images/surface/logo.png')
pygame.display.set_icon(Surface)

def loading(progress):
    if progress < 100:
        text = small_font.render("Loading "+str(int(progress))+"%",True,GREEN)
    else:
        text = small_font.render("Loading "+str(100)+"%",True,GREEN)
    screen.blit(text,(372,423))

small_font = pygame.font.Font("fonts/MotionControl-BoldItalic.otf", 20)
time_count=1/15
progress=0
logo=load_image("symbols/team_logo.png",IMG_DIR,alpha=True)
clock=pygame.time.Clock()

while(progress/2)<101:
    clock.tick(60)
    for e in pygame.event.get():
        if e.type == pygame.QUIT:
            sys.exit(0)
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

    increase = random.randint(1,30)
    progress += increase
    screen.fill(BLACK)
    pygame.draw.rect(screen,BLUE,(310,373,204,49))
    pygame.draw.rect(screen,BLACK,(311,374,202,47))
    if progress/2>100:
        run = main()
        run.main_loop()
    else:
        pygame.draw.rect(screen,GREEN,(312,375,progress,45))
    loading(progress/2)
    screen.blit(logo,(260,50))
    pygame.display.flip()
    time.sleep(time_count)


    
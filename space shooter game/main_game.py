import pygame as pg
import random
pg.init()
width=1000
height=600
win=pg.display.set_mode((width,height))
run=True
sx=width/2
sy=height-100
fire=False
clock=pg.time.Clock()
bullet_pos=[]
ey=0
#loading images
bg=pg.image.load("background.webp")
bg=pg.transform.scale(bg,(width,height))

space_ship=pg.image.load("spaceship.png")
space_ship=pg.transform.scale(space_ship,(100,100))

bullet=pg.image.load("bullet.png")
bullet=pg.transform.scale(bullet,(50,50))

enemy=pg.image.load("enemy.png")
enemy=pg.transform.scale(enemy,(100,100))


    

#controlling user input
def action():
    global fire
    global sx,sy
    button=pg.key.get_pressed()
    if button[pg.K_LEFT]:
            sx-=20
    if button[pg.K_RIGHT]:
            sx+=20


while run:
    for event in pg.event.get():
        if event.type==pg.QUIT:
            run=False
        if event.type==pg.KEYDOWN:
            if event.key==pg.K_SPACE:
                fire=True
                bullet_pos.append((sx,sy))
                
    win.blit(bg,(0,0))
    win.blit(enemy,(random.randint(0,width-100),ey))
    win.blit(space_ship,(sx,sy))
    for i in range(len(bullet_pos)):
        x, y = bullet_pos[i]
        bullet_pos[i] = (x, y - 10)
        win.blit(bullet, (x, y))
    action()
        
            
            
    clock.tick(40)
    ey+=1
    pg.display.update()

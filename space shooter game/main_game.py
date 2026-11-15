import pygame as pg
import random
import numpy as np
import math
pg.init()
width=1000
height=600
arr = np.empty((0, 2))
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
#collision detection
def collision():
    global arr
    global bullet_pos
    for bx,by in bullet_pos[:]:
        for ex,ey in arr: 
            print(ex,ey)
            distance=math.sqrt((bx-ex)**2+(by-ey)**2)
            if distance<100:
                arr = arr[~np.all(arr == [ex, ey], axis=1)]
                bullet_pos.remove((bx,by))
                break 


while run:
    for event in pg.event.get():
        if event.type==pg.QUIT:
            run=False
        if event.type==pg.KEYDOWN:
            if event.key==pg.K_SPACE:
                fire=True
                bullet_pos.append((sx,sy))
                
    win.blit(bg,(0,0))
    ex=random.randint(0,width-100)
    if len(arr)<6:
        arr=np.vstack((arr,[ex,ey]))
    for x,y in arr:
        win.blit(enemy,(x,y))
    arr[:,1]+=1
    win.blit(space_ship,(sx,sy))
    for i in range(len(bullet_pos) ):
        x, y = bullet_pos[i]
        bullet_pos[i] = (x, y - 10)
        win.blit(bullet, (x, y))
    action()
    collision()
        
            
            
    clock.tick(40)
    pg.display.update()

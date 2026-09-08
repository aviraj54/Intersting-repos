import pygame as pg
import numpy as np
import random
width=1000
height=500
e_y=0
win=pg.display.set_mode((width,height))
running=True
clock=pg.time.Clock()
bg=pg.image.load("background.webp")
bg=pg.transform.scale(bg,(width,height))
ship=pg.image.load("spaceship.png")
ship=pg.transform.scale(ship,(100,100))
bullet=pg.image.load("bullet.png")
bullet=pg.transform.scale(bullet,(30,20))
x=250
bullet_mode=False
bx=0
by=0
enemy_coords=np.empty((0,2))
shooter_timer=0
shooter_timerf=0
bullet_coords=np.empty((0,2))
enemy=pg.image.load('enemy.png')
enemy=pg.transform.scale(enemy,(100,50))
while running:
    e_x=random.randint(0,width)
    if len(enemy_coords)<=8:
        enemy_coords=np.append(enemy_coords,[[e_x,e_y]],axis=0)

    for event in pg.event.get():
        if event.type==pg.QUIT:
            running=False
    keys=pg.key.get_pressed()
    if keys[pg.K_LEFT]:
        x-=10
    if keys[pg.K_RIGHT]:
            x+=10
    if keys[pg.K_SPACE]:
        shooter_timerf+=1 
        if shooter_timerf>=5:
            bullet_mode=True
            bx=x
            by=height-100
            bullet_coords=np.append(bullet_coords,[[bx,by]],axis=0)#not default here so 
            #need to inilizate  to add rowise also make multidimensional by adding[[]]
            shooter_timerf=0
    win.blit(bg,(0,0))
    win.blit(ship,(x,height-100))
    for y,z in enemy_coords:
        win.blit(enemy,(y,z))
    if bullet_mode:
        for a,b in bullet_coords:
            win.blit(bullet,(a,b))
    bullet_coords=bullet_coords-[0,5]
    enemy_coords=enemy_coords+[0,0.5]
    clock.tick(60)
    pg.display.update()
pg.quit()
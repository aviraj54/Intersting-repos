import pygame as pg
import numpy as np
import math
import random
pg.init()
width=1000
height=500
px=width/4
step=0
py=height/2
multiple=250
y=0
b=0
clock=pg.time.Clock()
casted_rays=1
pov=60
target_x=270-30
target_y=270-30
win=pg.display.set_mode((width,height))
mapp=np.array([[1,1,1,1,1],
              [0,0,0,0,0],
              [1,1,0,1,1],
              [1,1,0,1,1],
              [1,1,1,1,1]])
run=True
def draw_map():
    for rows in range(len(mapp)):
        for cols in range(len(mapp[rows])):
            if mapp[rows][cols]==1:
                pg.draw.rect(win,'red',(cols*100,rows*100,100-1,100-1))
            if mapp[rows][cols]==0:
                pg.draw.rect(win,'white',(cols*100,rows*100,100-1,100-1))
while run:
    for event in pg.event.get():
        if event.type==pg.QUIT:
            run=False
    win.fill('black')
    draw_map()
    pg.draw.circle(win,'green',(px,py),5)
    keys=pg.key.get_pressed()
    if keys[pg.K_LEFT]:
            target_x-=1
            target_y-=1
    if keys[pg.K_RIGHT]:
            target_x+=1
            target_y+=1
    if keys[pg.K_UP]:
        px += math.cos(math.radians(target_x)) * 2
        py += math.sin(math.radians(target_y)) * 2
    if keys[pg.K_DOWN]:
            px += math.cos(math.radians(target_x+180)) * 2
            py += math.sin(math.radians(target_y+180)) * 2
    if mapp[int(py//100)][int(px//100)]==1:
        if keys[pg.K_UP]:
            px -= math.cos(math.radians(target_x)) * 2
            py -= math.sin(math.radians(target_y)) * 2
        if keys[pg.K_DOWN]:
            px -= math.cos(math.radians(target_x+180)) * 2
            py -= math.sin(math.radians(target_y+180)) * 2
    for i in range(60):
        for depth in range(500):
            if depth==0:
                depth+=1
            wall_height=40000/depth 
            end_x=px+math.cos(math.radians(target_x+i))*depth
            end_y=py+math.sin(math.radians(target_y+i))*depth
            if end_x%10==0 and end_y%10==0:
                 r=int(end_x//100 -1)
                 c=int(end_y//100 -1)
            else:
                r=int(end_x//100)
                c=int(end_y//100)
            if mapp[c][r]==1:
                pg.draw.rect(win,'purple',(r*100,c*100,100-1,100-1))
                pg.draw.line(win,'black',(px,py),(end_x,end_y))
                pg.draw.rect(win,'brown',(500+i*10,(height-wall_height)/2,10,wall_height))
                break
    clock.tick(60)
    pg.display.update()
            
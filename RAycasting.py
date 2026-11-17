import pygame as pg
import numpy as np
import math
pg.init()
width=1000
height=500
px=width/4
py=height/2
clock=pg.time.Clock()
casted_rays=60//2
pov=60
target_x=270
target_y=270
win=pg.display.set_mode((width,height))
mapp=np.array([[0,0,0,0,0],
              [0,0,0,1,0],
              [0,0,0,0,0],
              [0,0,1,0,0],
              [0,0,1,0,0]])
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
            target_x-=10
            target_y-=10
    if keys[pg.K_RIGHT]:
            target_x+=10
            target_y+=10
    if keys[pg.K_UP]:
        px += math.cos(math.radians(target_x)) * 5
        py += math.sin(math.radians(target_y)) * 5
    if keys[pg.K_DOWN]:
            px += math.cos(math.radians(target_x+180)) * 5
            py += math.sin(math.radians(target_y+180)) * 5
    for i in range(casted_rays):
        for j in range(pov//2):
            pg.draw.line(win,'blue',(px,py),(px+250*math.cos(math.radians(target_x+j)),py+250*math.sin(math.radians(target_y+j))),10)
            pg.draw.line(win,'blue',(px,py),(px+250*math.cos(math.radians(target_x-j)),py+250*math.sin(math.radians(target_y-j))),10)
    end_x=px+250*math.cos(math.radians(target_x))
    end_y=py+250*math.sin(math.radians(target_y))
    if end_x%10==0 and end_y%10==0:
        r=int(end_x//100 -1)
        c=int(end_y//100 -1)
    else:
        r=int(end_x//100)
        c=int(end_y//100)
    print(c,r)
    if mapp[c][r]==1:
        pg.draw.rect(win,'yellow',(r*100,c*100,100-1,100-1))
    clock.tick(60)
    pg.display.update()
            
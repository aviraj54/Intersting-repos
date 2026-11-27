import pygame as pg
import numpy as np
import math
import random
pg.init()
width=1600                                # CHANGED: 800 map + 800 for 3D view
height=800                                # CHANGED: 8 cells x 100
px=150                                    # CHANGED: start inside an open cell
step=0
py=150
multiple=250
y=0
b=0
clock=pg.time.Clock()
casted_rays=1
pov=60
target_x=270
target_y=270
rays=120                                  # more rays = more accurate (try 240, 480)
col_w=800/rays                            # CHANGED: 3D view is now 800px wide
win=pg.display.set_mode((width,height))
mapp=np.array([[1,1,1,1,1,1,1,1],        # CHANGED: 8x8 map
               [1,0,0,0,0,0,0,1],
               [1,0,1,1,0,1,0,1],
               [1,0,1,0,0,1,0,1],
               [1,0,0,0,1,1,0,1],
               [1,1,0,1,0,0,0,1],
               [1,0,0,0,0,1,0,1],
               [1,1,1,1,1,1,1,1]])
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
            target_x-=3
            target_y-=3
    if keys[pg.K_RIGHT]:
            target_x+=3
            target_y+=3
    if keys[pg.K_UP]:
        px += math.cos(math.radians(target_x)) * 5
        py += math.sin(math.radians(target_y)) * 5
    if keys[pg.K_DOWN]:
            px += math.cos(math.radians(target_x+180)) * 5
            py += math.sin(math.radians(target_y+180)) * 5
    if mapp[int(py//100)][int(px//100)]==1:
        if keys[pg.K_UP]:
            px -= math.cos(math.radians(target_x)) * 5
            py -= math.sin(math.radians(target_y)) * 5
        if keys[pg.K_DOWN]:
            px -= math.cos(math.radians(target_x+180)) * 5
            py -= math.sin(math.radians(target_y+180)) * 5
    for n in range(rays):
        i = -30 + n*(60/rays)             # spans -30 to +30, i=0 is the center ray
        for depth in range(800):          # CHANGED: longer rays for the bigger map
            if depth==0:
                depth+=1
            wall_height=30000/depth
            end_x=px+math.cos(math.radians(target_x+i))*depth
            end_y=py+math.sin(math.radians(target_y+i))*depth
            if end_x%10==0 and end_y%10==0:
                 r=int(end_x//100 -1)
                 c=int(end_y//100 -1)
            else:
                r=int(end_x//100)
                c=int(end_y//100)
            if not (0<=r<8 and 0<=c<8):   # CHANGED: 8x8 bounds
                break
            if mapp[c][r]==1:
                pg.draw.rect(win,'purple',(r*100,c*100,100-1,100-1))
                pg.draw.rect(win,'brown',(800+n*col_w,(height-wall_height)/2,col_w+1,wall_height))   # CHANGED: 3D view starts at x=800
                break
    clock.tick(90)
    pg.display.update()
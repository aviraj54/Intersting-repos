import pygame 
import time
import random
import math
pygame.init()
head=[]
width=1000
height=700
win=pygame.display.set_mode((width,height))
pygame.display.set_caption("snake game")
c=pygame.time.Clock()
fx=random.randrange(0,width)
fy=random.randrange(0,height)
length=1
def gameloop():
    sx=int(width/2)
    sy=int(height/2)
    zx=20
    zy=20
    class snake:
        def __init__(self,sx,sy,zx,zy,surface):
            self.sx=sx
            self.surface=surface
            self.sy=sy
            self.zx=zx
            self.zy=zy
        def draw_snake(self,surface,sx,sy,zx,zy):
            pygame.draw.rect(surface,'red',(sx,sy,zx,zy))
    Stop=False
    speed=0
    speedy=0
    run=False
    s=snake(sx,sy,zx,zy,win)
    class food:
        def __init__(self,fx,fy,zx,zy,surface):
            self.fx=fx
            self.surface=surface
            self.fy=fy
            self.zx=zx
            self.zy=zy
        def draw_food(self,surface,fx,fy,zx,zy):
            pygame.draw.rect(surface,'green',(fx,fy,zx,zy))
    f=food(fx,fy,zx,zy,win)
    def detect_collision():
        global length
        if ((sx-f.fx)**2+(sy-f.fy)**2)<=144:
            f.fx=random.randrange(0,width)
            f.fy=random.randrange(0,height)
            length+=1
    while  not Stop:
        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                Stop=True
            if event.type==pygame.KEYDOWN:
                if event.key==pygame.K_RIGHT:
                    speed+=10
                    speedy=0
                elif event.key==pygame.K_LEFT:
                   speed-=10
                   speedy=0
                elif event.key==pygame.K_UP:
                    speedy-=10
                    speed=0
                else:
                    speed=0
                    speedy+=10
        win.fill('black')
        sx+=speed
        sy+=speedy
        if sx>width:
            sx=0
        if sy>height:
            sy=0
        if sx<0:
            sx=width
        if sy<0:
            sy=height
        head.append((sx,sy))
        if len(head)>length:
            head.pop(0)
        print(head)
        for x,y in head:
            s.draw_snake(win,x,y,zx,zy)
        f.draw_food(win,f.fx,f.fy,zx,zy)
        detect_collision()
        c.tick(50)
        pygame.display.update()
gameloop()

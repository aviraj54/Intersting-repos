import pygame 
import time
pygame.init()
width=1000
height=700
win=pygame.display.set_mode((width,height))
pygame.display.set_caption("snake game")
c=pygame.time.Clock()
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
        s.draw_snake(win,sx,sy,zx,zy)
        c.tick(50)
        pygame.display.update()
gameloop()

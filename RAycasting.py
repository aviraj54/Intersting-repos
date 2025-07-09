import pygame
import math
import time
pygame.init()
width,height=1000,500
win=pygame.display.set_mode((width,height))
def gameloop():
    c=pygame.time.Clock()
    f=width/4
    g=height/2
    speed=0
    semihalf=math.radians(120)
    global win
    px,py=width/4,height/2
    player_angle=math.radians(90)
    def castrays():
        for rays in range(120):
            for depth in range(height):
                tx=px+math.cos(math.radians(player_angle+30-rays*1/2))*depth
                ty=px-math.sin(math.radians(player_angle+30-rays*1/2))*depth
                pygame.draw.line(win,'red',(px,py),(tx,ty))
                
    def draw_map():
        global win
        map_size=5
        map_width=width/2
        Map=['0','#','#','#','#',
             '#','#','0','#','#',
             '#','#','0','#','#',
             '#','#','#','#','#',
             '#','#','#','#','#']
        for col in range(map_size):
            for row in range(map_size):
                x=col*map_size+row
                if Map[x]=="#":
                    pygame.draw.rect(win,'green',((row*100),col*100,100-2,100-2))
                else:
                     pygame.draw.rect(win,'white',((row*100),col*100,100-2,100-2)) 

    def new_func(x):
        print(x)      
    run=True
    while run:
        global k
        k=pygame.key.get_pressed()
        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                run=False
        win.fill('black')
        draw_map()
        castrays()
        if k[pygame.K_UP]:
            py-=2
        if k[pygame.K_DOWN]:
            py+=2
        if k[pygame.K_RIGHT]:
            player_angle-=2
        if k[pygame.K_LEFT]:
            player_angle+=2
        pygame.draw.circle(win,'red',(px,py),10)
        c.tick(20)
        pygame.display.update()
    pygame.quit()
    
    
gameloop()
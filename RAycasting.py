import pygame
import math
pygame.init()
width,height=1000,500
win=pygame.display.set_mode((width,height))
def gameloop():
    semihalf=math.radians(120)
    global win
    px,py=width/4,height/2
    player_angle=math.radians(90)
    def castrays():
        for rays in range(60):
            tx=px+math.cos(math.radians(120-rays*1))*200
            ty=px-math.sin(math.radians(120-rays*1))*200

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
        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                run=False
        win.fill('black')
        draw_map()
        pygame.draw.circle(win,'red',(width/4,height/2),10)
        pygame.draw.line(win,'red',(px,py),(px+math.cos(player_angle)*200,py-math.sin(player_angle)*200))
        pygame.draw.line(win,'pink',(px,py),(px+math.cos(math.radians(60))*2000,py-math.sin(math.radians(60))*2000))
        pygame.draw.line(win,'yellow',(px,py),(px+math.cos(math.radians(120))*2000,py-math.sin(math.radians(120))*2000))
        castrays()
        pygame.display.update()
    pygame.quit()
    
    
gameloop()
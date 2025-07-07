import pygame
pygame.init()
width,height=1000,500
win=pygame.display.set_mode((width,height))
def gameloop():
    global win
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
        pygame.display.update()
    pygame.quit()
    
    
gameloop()
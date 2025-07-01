import pygame
pygame.init()
Width=1000
global win
Height=600
class Start_game:
    def __init__(self,width,height):
        self.width=width
        self.height=height
    def screen_feature(self):
        win=pygame.display.set_mode((self.width,self.height))
        pygame.display.set_caption("snake game")
        return win
        
def gameloop():
    run=True
    sg=Start_game(Width,Height)
    win=sg.screen_feature()
    while run:
        sg.screen_feature()
        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                run=False
        win.fill('black')
        pygame.display.update()
gameloop()
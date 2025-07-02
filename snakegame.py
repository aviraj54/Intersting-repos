import pygame
pygame.init()
Width=1000
global win
size_x=20
size_y=20
Height=600
sx=Width/2
sy=Height/2
class Start_game:
    def __init__(self,width,height):
        self.width=width
        self.height=height
    def screen_feature(self):
        win=pygame.display.set_mode((self.width,self.height))
        pygame.display.set_caption("snake game")
        return win
class snake:
    def __init__(self,sx,sy,size_x,size_y):
        self.sx=sx
        self.sy=sy
        self.szx=size_x
        self.szy=size_y
class inheritsnake(Start_game,snake):
    def __init__(self,width,height,sx,sy,size_x,size_y):
        Start_game.__init__(self,width,height)
        snake.__init__(self,sx,sy,size_x,size_y)
    def drawsnake(self):
        c=Start_game(Width,Height)
        win=c.screen_feature()
        s=snake(sx,sy,size_x,size_y)
        pygame.draw.rect(win, 'red', (int(s.sx), int(s.sy), int(s.szx), int(s.szy)))

def gameloop():
    run=True
    sarp=inheritsnake(Width,Height,sx,sy,size_x,size_y)
    sg=Start_game(Width,Height)
    win=sg.screen_feature()
    while run:
        sg.screen_feature()
        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                run=False
        win.fill('black')
        sarp.drawsnake()
        pygame.display.update()
gameloop()
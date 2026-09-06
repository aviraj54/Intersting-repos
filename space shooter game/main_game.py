import pygame as pg
width=1000
height=500
win=pg.display.set_mode((width,height))
running=True
clock=pg.time.Clock()
bg=pg.image.load("background.webp")
bg=pg.transform.scale(bg,(width,height))
ship=pg.image.load("spaceship.png")
ship=pg.transform.scale(ship,(100,100))
x=250
while running:
    for event in pg.event.get():
        if event.type==pg.QUIT:
            running=False
    keys=pg.key.get_pressed()
    if keys[pg.K_LEFT]:
        x-=10
    if keys[pg.K_RIGHT]:
            x+=10
    win.blit(bg,(0,0))
    win.blit(ship,(x,height-100))
    clock.tick(60)
    pg.display.update()
pg.quit()
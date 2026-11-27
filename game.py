import pygame as pg
import socket
client=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
client.connect(('127.0.0.1',8080))
win=pg.display.set_mode((500,500))
run =True
x,y=50,50
clock=pg.time.Clock()
while run:
    for event in pg.event.get():
        if event.type==pg.QUIT:
            run=False
    win.fill('black')
    keys=pg.key.get_pressed()
    if keys[pg.K_LEFT]:
        x-=5
    if keys[pg.K_RIGHT]:
        x+=5
    if keys[pg.K_UP]:
        y-=5
    if keys[pg.K_DOWN]:
        y+=5
    pos=str((x,y))
    client.sendall(pos.encode())
    pg.draw.rect(win,'red',(x,y,50,50))
    clock.tick(60)
    pg.display.flip()
pg.quit()
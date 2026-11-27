
import pygame as pg
import math

pg.init()

WIDTH, HEIGHT = 1000, 600
HALF = WIDTH // 2

win = pg.display.set_mode((WIDTH, HEIGHT))
pg.display.set_caption("2D Raycasting to 3D")

clock = pg.time.Clock()

# Map
TILE = 50

world_map = [
    [1,1,1,1,1,1,1,1,1,1],
    [1,0,0,0,0,0,0,0,0,1],
    [1,0,1,0,0,1,0,0,0,1],
    [1,0,1,0,0,1,0,1,0,1],
    [1,0,0,0,0,0,0,1,0,1],
    [1,0,1,1,0,0,0,0,0,1],
    [1,0,0,0,0,1,0,0,0,1],
    [1,0,0,1,0,0,0,1,0,1],
    [1,0,0,0,0,0,0,0,0,1],
    [1,1,1,1,1,1,1,1,1,1]
]

MAP_W = len(world_map[0])
MAP_H = len(world_map)

# Player
px = 75
py = 75
angle = 0

FOV = math.radians(60)
NUM_RAYS = 200
MAX_DEPTH = 600

def is_wall(x, y):
    mx = int(x // TILE)
    my = int(y // TILE)

    if mx < 0 or my < 0 or mx >= MAP_W or my >= MAP_H:
        return True

    return world_map[my][mx] == 1


def move_player(dx, dy):
    global px, py

    if not is_wall(px + dx, py):
        px += dx

    if not is_wall(px, py + dy):
        py += dy


def cast_rays():

    for ray in range(NUM_RAYS):

        ray_angle = angle - FOV/2 + ray * FOV/NUM_RAYS

        distance = 0
        hit_x = px
        hit_y = py

        while distance < MAX_DEPTH:

            hit_x = px + math.cos(ray_angle) * distance
            hit_y = py + math.sin(ray_angle) * distance

            if is_wall(hit_x, hit_y):
                break

            distance += 2

        # Fish-eye correction
        corrected_dist = distance * math.cos(ray_angle - angle)
        corrected_dist = max(corrected_dist, 1)

        # 3D wall height
        wall_height = min(HEIGHT, (TILE * 350) / corrected_dist)

        # Wall shading
        shade = max(25, 255 - int(corrected_dist * 0.4))

        # 3D screen coordinates
        column_width = HALF / NUM_RAYS

        x = HALF + ray * column_width
        y = HEIGHT/2 - wall_height/2

        pg.draw.rect(
            win,
            (shade, shade, shade),
            (int(x), int(y), math.ceil(column_width), int(wall_height))
        )

        # Draw rays on 2D map
        map_scale = 0.5

        pg.draw.line(
            win,
            (255, 220, 0),
            (int(px * map_scale), int(py * map_scale)),
            (int(hit_x * map_scale), int(hit_y * map_scale)),
            1
        )


def draw_map():

    scale = 0.5

    for y in range(MAP_H):
        for x in range(MAP_W):

            color = (100, 100, 100) if world_map[y][x] else (30, 30, 30)

            pg.draw.rect(
                win,
                color,
                (x*TILE*scale, y*TILE*scale,
                 TILE*scale, TILE*scale)
            )

            pg.draw.rect(
                win,
                (80, 80, 80),
                (x*TILE*scale, y*TILE*scale,
                 TILE*scale, TILE*scale), 1
            )

    # Player
    pg.draw.circle(
        win,
        (0, 255, 0),
        (int(px*scale), int(py*scale)),
        5
    )

    # Direction
    pg.draw.line(
        win,
        (255, 0, 0),
        (px*scale, py*scale),
        (px*scale + math.cos(angle)*30,
         py*scale + math.sin(angle)*30),
        3
    )


running = True

while running:

    dt = clock.tick(60) / 1000

    for event in pg.event.get():

        if event.type == pg.QUIT:
            running = False

    keys = pg.key.get_pressed()

    # Rotation
    if keys[pg.K_LEFT]:
        angle -= 2 * dt

    if keys[pg.K_RIGHT]:
        angle += 2 * dt

    # Movement
    speed = 150 * dt

    forward_x = math.cos(angle)
    forward_y = math.sin(angle)

    if keys[pg.K_w]:
        move_player(forward_x*speed, forward_y*speed)

    if keys[pg.K_s]:
        move_player(-forward_x*speed, -forward_y*speed)

    if keys[pg.K_a]:
        move_player(
            math.cos(angle-math.pi/2)*speed,
            math.sin(angle-math.pi/2)*speed
        )

    if keys[pg.K_d]:
        move_player(
            math.cos(angle+math.pi/2)*speed,
            math.sin(angle+math.pi/2)*speed
        )

    # Background
    win.fill((0, 0, 0))

    # 3D ceiling and floor
    pg.draw.rect(win, (40, 40, 55), (HALF, 0, HALF, HEIGHT//2))
    pg.draw.rect(win, (80, 80, 80), (HALF, HEIGHT//2, HALF, HEIGHT//2))

    # Render
    cast_rays()
    draw_map()

    # Screen divider
    pg.draw.line(win, (255,255,255), (HALF,0), (HALF,HEIGHT), 2)

    pg.display.flip()

pg.quit()

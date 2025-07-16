import pygame
import math

pygame.init()
w, h = 800, 600
screen = pygame.display.set_mode((w, h))
clock = pygame.time.Clock()

map_ = [
    "########",
    "#......#",
    "#.##...#",
    "#......#",
    "###.####",
    "#......#",
    "########"
]
map_w, map_h = len(map_[0]), len(map_)

block = 64
fov = math.pi / 3
num_rays = 120
max_depth = block * 8
half_h = h // 2
scale = w // num_rays

player_x, player_y = block + block//2, block + block//2
player_angle = 0
speed = 3

def cast_ray(px, py, angle):
    sin_a = math.sin(angle)
    cos_a = math.cos(angle)

    for depth in range(0, max_depth, 5):
        x = px + depth * cos_a
        y = py + depth * sin_a

        map_x = int(x // block)
        map_y = int(y // block)

        if 0 <= map_x < map_w and 0 <= map_y < map_h:
            if map_[map_y][map_x] == '#':
                return depth, x, y
    return max_depth, x, y

run = True
while run:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT]:
        player_angle -= 0.04
    if keys[pygame.K_RIGHT]:
        player_angle += 0.04
    if keys[pygame.K_UP]:
        nx = player_x + speed * math.cos(player_angle)
        ny = player_y + speed * math.sin(player_angle)
        if map_[int(ny // block)][int(nx // block)] == '.':
            player_x, player_y = nx, ny
    if keys[pygame.K_DOWN]:
        nx = player_x - speed * math.cos(player_angle)
        ny = player_y - speed * math.sin(player_angle)
        if map_[int(ny // block)][int(nx // block)] == '.':
            player_x, player_y = nx, ny

    screen.fill((0, 0, 0))

    start_angle = player_angle - fov / 2
    for ray in range(num_rays):
        angle = start_angle + ray * fov / num_rays
        depth, hit_x, hit_y = cast_ray(player_x, player_y, angle)
        depth *= math.cos(player_angle - angle)  # fishbowl fix
        if depth == 0:
            depth = 0.0001
        h_line = 21000 / depth
        color = 255 / (1 + depth * depth * 0.0001)
        pygame.draw.rect(screen, (color, color, color),
                         (ray * scale, half_h - h_line // 2, scale, h_line))

    pygame.display.flip()
    clock.tick(60)

pygame.quit()

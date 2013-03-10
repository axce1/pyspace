import invaders
import pygame
import sys

w = 800
h = 500

pygame.init()
screen = pygame.display.set_mode((w,h))

clock = pygame.time.Clock()

enemies = []

for x in range(5):
    enemies.append(invaders.Invaders(50*x+50, 50, 'boo', screen))
    enemies.append(invaders.Invaders(50*x+50, 100, 'kva', screen))
    enemies.append(invaders.Invaders(50*x+50, 150, 'boo', screen))

print (enemies)
pos = 0
enemyspeed = 0.5
while 1:

    screen.fill((0,0,0))
    clock.tick(60)

    for e in pygame.event.get():
        if e.type == pygame.QUIT:
            sys.exit()

    for i in range(len(enemies)):
        enemies[i].x += enemyspeed
        if pos == 0:
            enemies[i].update(screen,pos)
            pos = 1
        if pos == 1:
            enemies[i].update(screen,pos)
            pos = 0

        if enemies[len(enemies)-1].x > 500:
            enemyspeed = -2
        if enemies[0].x < 50:
            enemyspeed = 0.5

    pygame.display.update()

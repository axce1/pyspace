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
    enemies.append(invaders.Invaders(50*x+50, 50, 'boo'))
    enemies.append(invaders.Invaders(50*x+50, 100, 'kva'))

print (enemies)
enemyspeed = 15

while 1:

    ev = pygame.event.poll()
    if ev.type == pygame.QUIT:
        sys.exit()

    screen.fill((0,0,0))
    clock.tick(60)

    for i in range(len(enemies)):
        enemies[i].x += enemyspeed
        enemies[i].update(screen)

    if enemies[len(enemies)-1].x > 500:
        enemyspeed = -15

    if enemies[0].x < 100:
        enemyspeed = 15

    pygame.display.flip()


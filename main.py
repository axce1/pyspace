import invaders
import pygame
import sys

w = 850
h = 500

pygame.init()
screen = pygame.display.set_mode((w,h))

clock = pygame.time.Clock()

enemies = []

for x in range(5):
    enemies.append(invaders.Invaders(50*x+50, 50, 'boo'))
    enemies.append(invaders.Invaders(50*x+50, 100, 'kva'))


hero = pygame.image.load('spacy.png')
hero = pygame.transform.scale(hero, (50,30))

playtime = 0
enemyspeed = 2
x = 200
while 1:

    for ev in pygame.event.get():
        if ev.type == pygame.QUIT:
            sys.exit()
        if ev.type == pygame.KEYDOWN:
            if ev.key == pygame.K_RIGHT:
                x += 25
            if ev.key == pygame.K_LEFT:
                x -= 25


    screen.fill((0,0,0))
    m = clock.tick(50.00)
    playtime += m/1000.0

    for i in range(len(enemies)):
        enemies[i].x += enemyspeed
        enemies[i].update(screen)

    if enemies[len(enemies)-1].x > 750:
        enemyspeed = -2

    if enemies[0].x < 50:
        enemyspeed = 2

    screen.blit(hero, (x,450))
    pygame.display.set_caption('Space Invaders - %.2f fps - %.2f' %(clock.get_fps(), playtime))
    pygame.display.flip()

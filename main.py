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


hero = invaders.Player(w/2,450)

shots = pygame.sprite.Group()
all = pygame.sprite.RenderUpdates()
invaders.Shot.containers = shots, all

shot = invaders.Shot(w/2,500)
# repeat keydown
pygame.key.set_repeat(1,1)

playtime = 0
enemyspeed = 2
herospeed = 0
while 1:

    for ev in pygame.event.get():

        if ev.type == pygame.QUIT:
            sys.exit()

        elif ev.type == pygame.KEYDOWN:
            if ev.key == pygame.K_RIGHT and hero.px < 750:
                hero.px += 5

            if ev.key == pygame.K_LEFT  and hero.px > 50:
                hero.px -= 5

            if ev.key == pygame.K_SPACE:
                shot.px = hero.px
                shot.py = hero.py


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

    #if invaders.shot.py < 500 and invaders.shot.py > 0:
#    shot.update(screen)

    for i in range(len(enemies)):
        enemies[i].x += enemyspeed
        enemies[i].update(screen)

    if  shot.py < 479: # and shot.py > 0:
        shot.py -= 5
        shot.update(screen)
    all.update(screen)
    hero.update(screen)

    pygame.display.set_caption('Space Invaders - %.2f fps - %.2f' %(clock.get_fps(), playtime))
    pygame.display.flip()

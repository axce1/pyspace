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

# create sprite group for shots
shots_sprite = pygame.sprite.Group()
all = pygame.sprite.RenderUpdates()

# each shot sprite member both group
invaders.Shot.containers = shots_sprite, all

#create single sprite
shot = invaders.Shot(0,0)

# repeat keydown
pygame.key.set_repeat(1,1)

playtime = 0
enemyspeed = 2
herospeed = 0


while 1:

    all.clear(screen,screen)

    all.update(screen)

    for ev in pygame.event.get():

        if ev.type == pygame.QUIT:
            sys.exit()

        elif ev.type == pygame.KEYDOWN:
            if ev.key == pygame.K_RIGHT and hero.px < 750:
                hero.px += 5

            if ev.key == pygame.K_LEFT  and hero.px > 50:
                hero.px -= 5


    keystate = pygame.key.get_pressed()
    shoting = keystate[pygame.K_SPACE]
    if shoting:
        shot.kill()
        shot = invaders.Shot(hero.px, 450)

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

    for i in range(len(enemies)):
        enemies[i].x += enemyspeed
        enemies[i].update(screen)

    if  shot.py < 479: # and shot.py > 0:
        shot.py -= 5
        shot.update(screen)
    if shot.py < 100:
        shot.kill()

    shots_sprite.update(screen)
    shots_sprite.draw(screen)

    hero.update(screen)

    pygame.display.set_caption('Space Invaders - %.2f fps - %.2f' %(clock.get_fps(), playtime))
    pygame.display.flip()


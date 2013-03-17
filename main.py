import invaders
import pygame
import sys

w = 850
h = 500

pygame.init()

screen = pygame.display.set_mode((w,h))

clock = pygame.time.Clock()

enemies = []

#for x in range(5):
    #enemies.append(invaders.Monster(50*x+50, 50, 'boo'))
    #enemies.append(invaders.Monster(50*x+50, 100, 'kva'))



# create sprite group for shots
monsterS = pygame.sprite.Group()
shotsS = pygame.sprite.Group()
heroS = pygame.sprite.Group()
boomS = pygame.sprite.Group()
all = pygame.sprite.RenderUpdates()

# each shot sprite member both group
invaders.Monster.containers = monsterS, all
invaders.Shot.containers = shotsS, all
invaders.Hero.containers = all
invaders.Boom.containers = all

#create single sprite
for x in range(5):
    enemies.append(invaders.Monster(50*x+50, 50, 'boo'))
    enemies.append(invaders.Monster(50*x+50, 100, 'kva'))
shot = invaders.Shot(0,0)
hero = invaders.Hero(w/2,450)

# repeat keydown
pygame.key.set_repeat(1,1)

playtime = 0
enemyspeed = 2
herospeed = 0
killer = 0

while 1:

    all.clear(screen,screen)

    all.update()


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
        enemies[i].update()

    if enemies[len(enemies)-1].x > 750:
        enemyspeed = -2

    if enemies[0].x < 50:
        enemyspeed = 2

    for i in range(len(enemies)):
        enemies[i].x += enemyspeed
        enemies[i].update()

    if  shot.py < 479: # and shot.py > 0:
        shot.py -= 5
        shot.update()

 #   shotsS.update()
    #shotsS.draw(screen)

    #heroS.update()
    #heroS.draw(screen)

    #monsterS.update()
    #monsterS.draw(screen)


    for monster in  pygame.sprite.spritecollide(shot, monsterS, 1, pygame.sprite.collide_mask):
        shot.py = 0
        shot.kill()
        boom = invaders.Boom(monster)
        #boomS.update()
        #boomS.draw(screen)
        killer += 1
        #boom.kill()
        print 'Fuck U Spilberg %.1f' %killer
    print all

    dirty = all.draw(screen)
    pygame.display.set_caption('Space Invaders - %.2f fps - %.2f' %(clock.get_fps(), playtime))
    pygame.display.update(dirty)


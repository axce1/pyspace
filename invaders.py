import glob
import pygame

class Shot(pygame.sprite.Sprite):
    # class for working with player

    def __init__(self,px, py):
        """ init player """
        pygame.sprite.Sprite.__init__(self, self.containers)
        self.px    = px
        self.py    = py
        self.image = pygame.image.load('shot.png')
        self.rect  = self.image.get_rect()

    def update(self):

        self.rect.center = (self.px,self.py)
        if self.py <= -20:
            self.kill()

class Hero(pygame.sprite.Sprite):

    def __init__(self, px, py):
        pygame.sprite.Sprite.__init__(self, self.containers)
        self.px = px
        self.py = py
        self.image = pygame.image.load('spacy.png')
        self.rect = self.image.get_rect()

    def update(self):

        self.rect.center = (self.px, self.py)

class Boom(pygame.sprite.Sprite):
    defaultlite = 3
    def __init__(self, actor):
        pygame.sprite.Sprite.__init__(self, self.containers)
        self.image = pygame.image.load('explosion.png')
        self.image = pygame.transform.scale(self.image, (50,50))
        self.rect = self.image.get_rect(center=actor.rect.center)
        self.life = self.defaultlite

    def update(self):

        self.life = self.life - 1
        if self.life <= 0: self.kill()

class Monster(pygame.sprite.Sprite):

    frame = 0
    last_update = 0


    def __init__(self, x, y, name):
        pygame.sprite.Sprite.__init__(self, self.containers)
        self.x = x
        self.y = y
        self.m_speed_init = 10
        self.m_speed = self.m_speed_init
        if name == 'boo':
            self.m = glob.glob('boo*.png')
        elif name == 'kva':
            self.m = glob.glob('kva*.png')
        self.m.sort()
        self.m_pos = 0
        self.img = pygame.image.load(self.m[0])
        self.image = pygame.transform.scale(self.img, (50,50))
        self.rect = self.image.get_rect()

    def update(self):

        tick = pygame.time.get_ticks()
        self.seconds = tick / 100.0

        if tick - self.last_update > 350:
            self.frame += 1
            if self.frame >= len(self.m): self.frame = 0

            self.image = pygame.image.load(self.m[self.frame])
            self.last_update = tick

        self.image = pygame.transform.scale(self.image, (50,50))
        self.rect.center = (self.x, self.y)

class Fire(pygame.sprite.Sprite):

    speed = 5

    def __init__(self, monster):
        pygame.sprite.Sprite.__init__(self, self.containers)
        self.image = pygame.image.load('fire.png')
        self.image = pygame.transform.scale(self.image, (10,20))
        self.rect = self.image.get_rect(midbottom=
                    monster.rect.move(0,5).midbottom)
       # self.rect = self.image.get_rect(midbottom=
                    #monster.rect.move(0.5).midbottom)

    def update(self):
        self.rect.move_ip(0,self.speed)
        if self.rect.bottom >= 800:
            self.kill()

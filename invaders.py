import glob
import pygame

#class Invaders(pygame.sprite.Sprite):
    #'''class for working with monster's'''

    #def __init__(self, posX, posY, name):
        #'''
        #init monster
        #'''
        #self.x        = posX
        #self.y        = posY
        #if name       == 'boo':
            #self.m    = glob.glob('boo1.png')
        #elif name     == 'kva':
            #self.m    = glob.glob('kva1.png')
        #self.m.sort()
        #self.img      = pygame.image.load(self.m[0])
        #self.img      = pygame.transform.scale(self.img, (50,50))

    #def update(self, di):
        #'''
        #update/animated moster
        #'''

        #di.blit(self.img,(self.x,self.y))


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

    def __init__(self, actor):
        pygame.sprite.Sprite.__init__(self, self.containers)
        self.image = pygame.image.load('explosion.png')
        self.image = pygame.transform.scale(self.image, (50,50))
        self.rect = self.image.get_rect(center=actor.rect.center)

    #def update(self):

     #   self.rect.center = self.rect1

class Monster(pygame.sprite.Sprite):

    def __init__(self, x, y, name):
        pygame.sprite.Sprite.__init__(self, self.containers)
        self.x = x
        self.y = y
        if name == 'boo':
            self.m = glob.glob('boo1.png')
        elif name == 'kva':
            self.m = glob.glob('kva1.png')
        self.m.sort()
        self.img = pygame.image.load(self.m[0])
        self.image = pygame.transform.scale(self.img, (50,50))
        self.rect = self.image.get_rect()

    def update(self):
        self.rect.center = (self.x, self.y)

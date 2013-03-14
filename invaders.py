import glob
import pygame

class Invaders(pygame.sprite.Sprite):
    '''class for working with monster's'''

    def __init__(self, posX, posY, name):
        '''
        init monster
        '''
        self.x        = posX
        self.y        = posY
        if name       == 'boo':
            self.m    = glob.glob('boo1.png')
        elif name     == 'kva':
            self.m    = glob.glob('kva1.png')
        self.m.sort()
        self.img      = pygame.image.load(self.m[0])
        self.img      = pygame.transform.scale(self.img, (50,50))

    def update(self, di):
        '''
        update/animated moster
        '''

        di.blit(self.img,(self.x,self.y))


class Player(pygame.sprite.Sprite):
    # class for working with player

    def __init__(self, px, py):
        """ init player """
        self.px   = px
        self.py   = py
        self.hero = pygame.image.load('spacy.png')
        self.hero = pygame.transform.scale(self.hero, (50,30))

    def update(self, di):

        di.blit(self.hero, (self.px,self.py))


class Shot(pygame.sprite.Sprite):
    # class for working with player

    def __init__(self, px, py):
        """ init player """
        pygame.sprite.Sprite.__init__(self, self.containers)
        self.px   = px
        self.py   = py
        self.hero = pygame.image.load('shot.png')
        #self.hero = pygame.transform.scale(self.hero, (50,30))

    def update(self, di):

        di.blit(self.hero, (self.px,self.py))
        if self.py <= 400:
            self.kill()

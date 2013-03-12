import glob
import pygame

class Invaders():
    '''class for working with monster's'''

    def __init__(self, posX, posY, name):
        '''
        init monster
        '''
        self.x = posX
        self.y = posY
        if name == 'boo':
            self.m = glob.glob('boo1.png')
        elif name == 'kva':
            self.m = glob.glob('kva1.png')
        self.m.sort()
        self.img = pygame.image.load(self.m[0])
        self.img = pygame.transform.scale(self.img, (50,50))

    def update(self, di):
        '''
        update/animated moster
        '''

        di.blit(self.img,(self.x,self.y))

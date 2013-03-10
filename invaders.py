import glob
import pygame

class Invaders():
    '''class for working with monster's'''

    def __init__(self, posX, posY, name, di):
        '''
        init monster
        '''
        self.x = posX
        self.y = posY
        self.m_speed_init = 10
        self.m_speed = self.m_speed_init
        if name == 'boo':
            self.m = glob.glob('boo*png')
        elif name == 'kva':
            self.m = glob.glob('kva*png')
        self.m.sort()
        self.m_pos = 0
        self.m_max = len(self.m)-1
        self.img = pygame.image.load(self.m[0])
        self.img = pygame.transform.scale(self.img, (50,50))
        self.update(di,0)

    def update(self, di, pos):
        '''
        update/animated moster
        '''
        if pos != 0:
            self.m_speed -= 1
            self.x += pos
            if self.m_speed == 0:
                self.img = pygame.image.load(self.m[self.m_pos])
                self.img = pygame.transform.scale(self.img, (50,50))
                self.m_speed = self.m_speed_init
                if self.m_pos == self.m_max:
                    self.m_pos = 0
                else:
                    self.m_pos += 1
        di.blit(self.img,(self.x,self.y))

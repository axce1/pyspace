# -*- coding: utf-8 -*-
# тесте
import pygame
import sys
import glob
from pygame import *

h = 300
w = 800

screen = pygame.display.set_mode((w,h))

clock = pygame.time.Clock()

class Kva:

    def __init__(self):
        self.x = 200
        self.y = 300
        self.k_speed_init = 10
        self.k_speed = self.k_speed_init
        self.k = glob.glob("kva*.png")
        self.k.sort()
        self.k_pos = 0
        self.k_max = len(self.k)-1
        self.img = pygame.image.load(self.k[0])
        self.update(0)


    def update(self, pos):
        if pos != 0:
            self.k_speed -= 1
            self.x += pos
            if self.k_speed == 0:
                self.img = pygame.image.load(self.k[sekf.k_pos])
                self.k_speed = self.k_speed_init
                if self.k_pos == self.k_max:
                    self.k_pos = 0
                else:
                    self.k_pos += 1
        screen.blit(self.img,(self.x,self.y))


kva_kva = Kva()
pos = 0

while 1:
    screen.fill((0,0,0))
    clock.tick(60)

    for e in pygame.event.get():
        if e.type == pygame.QUIT:
            sys.exit()

    kva_kva.update(pos)

    pygame.display.update()

import pygame
from random import randint

class Apple:
    def __init__(self, surface, snakebody):
        while True:
            self.cords = (randint(0,35),randint(0,23))
            if not self.cords in snakebody:
                break
        self.surface = surface

    def draw(self):
        pygame.draw.rect(self.surface,(255,0,0),(self.cords[0]*25,self.cords[1]*25,25,25))


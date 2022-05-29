import pygame
from random import randint

class Apple:    # Klasa obsługująca jabłka
    def __init__(self, surface, snakebody):
        while True: # Generuje jebłko dopuki pojawi się poza ciałem węża
            self.cords = (randint(0,35),randint(0,23))
            if not self.cords in snakebody:
                break   # Po wygenerowaniu jabłka na własciwej pozycji przerywa pętle
        self.surface = surface

    def draw(self): # Rysuje jabłko na ekranie
        pygame.draw.rect(self.surface,(255,0,0),(self.cords[0]*25,self.cords[1]*25,25,25))


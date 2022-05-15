import pygame
from random import randint


class Snake:
    # Variables
    body = []
    # Constructor
    def __init__(self,surface, head = (18,12), lenght = 5, direction = "r", speed = 100):

        if direction == "r":
            for i in range(lenght):
                self.body.append((head[0]-i,head[1]))
        elif direction == "l":
            for i in range(lenght):
                self.body.append((head[0]+i,head[1]))
        elif direction == "u":
            for i in range(lenght):
                self.body.append((head[0],head[1]-i))
        elif direction == "d":
            for i in range(lenght):
                self.body.append((head[0],head[1]+i))
        self.speed = speed
        self.surface = surface
        self.time = self.speed
        self.direction = direction

    def printbody(self):
        print(type(self.body[1]))

    def drawBody(self):
        for i in self.body:
            pygame.draw.rect(self.surface,(0,255,0),(i[0]*25,i[1]*25,25,25))

    def ismove(self):
        self.time -= 1
        if self.time == 0:
            self.time = self.speed
            return True

    def move(self):
        for i in self.body:
            pass

    def eatapple(self):
        pass

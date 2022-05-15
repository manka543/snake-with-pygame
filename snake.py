import pygame
from random import randint

def sayhi():
    print("Witaj kretynie")


class Snake:
    # constructor
    body = []

    def __init__(self, head = (18,12), lenght = 3, direction = "r", speed = 100):

        if direction == "r":
            for i in range(lenght):
                self.body += (head[0]-i,head[1])
        elif direction == "l":
            for i in range(lenght):
                self.body += (head[0]+i,head[1])
        elif direction == "u":
            for i in range(lenght):
                self.body += (head[0],head[1]-i)
        elif direction == "d":
            for i in range(lenght):
                self.body += (head[0],head[1]+i)
        self.speed = speed

    def printbody(self):
        for i in range(len(self.body)):
            print(self.body[i])
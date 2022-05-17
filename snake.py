from nis import match
from operator import truediv
import pygame
from random import randint


class Snake:
    # Variables
    body = []
    # Constructor
    def __init__(self,surface, head = (18,12), lenght = 5, direction = "r",directionn = "r",directionc=False, directuoncc = False, speed = 100000):

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
        self.moves = []

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
        if len(self.moves)>0:
            self.direction = self.moves.pop(0)
        self.movepredictf()
        #if self.ismovepossible():
        self.body[0] = self.movepredict 
        for i in range(len(self.body)-1):
            self.body[len(self.body)-1-i]= self.body[len(self.body)-i-2]

    def ismovepossible(self):
        if not self.movepredict in self.body:   
            if self.direction == 'r' and self.movepredict[0]+1 > 36:
                return True
            elif self.direction == 'l' and self.movepredict[0]-1 < 0:
                return True
            elif self.direction == 'u' and self.movepredict[1]-1 < 0:
                return True
            elif self.direction == 'd' and self.movepredict[1]+1 > 24:
                return True
            else:
                return False
        else:
            return False
    def movepredictf(self):
        if self.direction == 'r':
            self.movepredict = (self.body[0][0]+1,self.body[0][1])
        elif self.direction == 'l':
            self.movepredict = (self.body[0][0]-1,self.body[0][1])
        elif self.direction == 'u':
            self.movepredict = (self.body[0][0],self.body[0][1]-1)
        elif self.direction == 'd':
            self.movepredict = (self.body[0][0],self.body[0][1]+1)

    def eatapple(self):
        pass

    def setdirection(self,key):
        if key == pygame.K_UP and len(self.moves) == 0 and not self.direction == 'd':
            self.moves += 'u'
        elif key == pygame.K_UP and len(self.moves) > 0:
            if self.moves[len(self.moves) -1] == 'd':
                self.moves += 'u'
        elif key == pygame.K_DOWN and len(self.moves) == 0 and not self.direction == 'u':
            self.moves += 'd'
        elif key == pygame.K_DOWN and len(self.moves) > 0:
            if self.moves[len(self.moves) -1] == 'u':
                self.moves += 'd'
        elif key == pygame.K_RIGHT and len(self.moves) == 0 and not self.direction == 'l':
            self.moves += 'r'
        elif key == pygame.K_RIGHT and len(self.moves) > 0:
            if self.moves[len(self.moves) -1] == 'l':
                self.moves += 'r'
        elif key == pygame.K_LEFT and len(self.moves) == 0 and not self.direction == 'r':
            self.moves += 'l'
        elif key == pygame.K_LEFT and len(self.moves) > 0:
            if self.moves[len(self.moves) -1] == 'r':
                self.moves += 'l'
    
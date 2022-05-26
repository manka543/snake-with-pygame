import pygame
from random import randint



# Klasa snake jest utwożona z oparciem o bibliotekę pygame i random
# Pozwala ona na stwożenie i obsługę węża z wykożystaniem kilku funkcji
class Snake:
    # Variables
     # Twoży listę żeby można było do niej dodać dane w formanie "tuple"; Bez tego do body dodawały się zmienne nie opakowane w tuple co nie jest zgodne z założeniem zmiennej
    # Constructor
    def __init__(self,surface, head = (18,12), lenght = 3, direction = "r", speed = 20000):
        print("snake init")
        # Używając zmiennej head i lenght generuje ciało węża w lini prostej zgodnej z kierunkiem podanym w direction
        self.body = []
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
        self.speed = speed # Szybkość kaltki
        self.surface = surface # Okno w którym działa wąż
        self.time = self.speed # Czas ruchu
        self.direction = direction # Kierunek poruszania się węża Legenda: 'l' - lewo, 'r' - prawo, 'u' - góra, 'd' - dół
        self.moves = []  # Lista z następnymi ruchami
        self.movesnumbers = 0
        self.alive = True
        self.points = 0
        self.font = pygame.font.Font('freesansbold.ttf',32)
        self.pointrender()
        

    def printbody(self): # Pomocnicza funkcja w debugowaniu ktróra wypisuje części ciała węża
        print(type(self.body[1]))

    def pointrender(self):
        self.pointsrend = self.font.render(str(self.points),True,(255,255,255))

    def drawBody(self): # Ta rysuje węża w okienku
        for i in self.body:
            pygame.draw.rect(self.surface,(0,255,0),(i[0]*25,i[1]*25,25,25))
        print('drawing')
        self.surface.blit(self.pointsrend,(750,50))

    def ismove(self): # Taki zegarek który wywołuje ruch co zmienną speed przy pomocy zmiennej time
        self.time -= 1
        if self.time == 0:
            self.time = self.speed
            self.movesnumbers += 1
            return True
        else:
            return False

    def move(self,apple): # Ta funkcja wykonuje ruch
        if len(self.moves)>0:
            self.direction = self.moves.pop(0)
        self.movepredictf()
        if self.ismovepossible() and self.alive:
            if not apple.cords in self.body:    
                self.body[0] = self.movepredict 
                for i in range(len(self.body)-1):
                    self.body[len(self.body)-1-i]= self.body[len(self.body)-i-2]
            else:
                self.body.append(self.body[-1])
                self.body[0] = self.movepredict 
                for i in range(len(self.body)-1):
                    self.body[len(self.body)-1-i]= self.body[len(self.body)-i-2]
                apple.__init__(self.surface, self.body)
                self.points += 1
                self.pointrender()
        else:
            self.alive = False
            return "end"


    def ismovepossible(self): # Ta funkcja sprawdza czy następny ruch jest legalny
        if not self.movepredict in self.body:   
            if -1 < self.movepredict[0] < 36 and -1 < self.movepredict[1] < 24:
                return True
        return False

    def movepredictf(self): # Tu sie dzieje przewidywanie ruchu i ustawianie go
        if self.direction == 'r':
            self.movepredict = (self.body[0][0]+1,self.body[0][1])
        elif self.direction == 'l':
            self.movepredict = (self.body[0][0]-1,self.body[0][1])
        elif self.direction == 'u':
            self.movepredict = (self.body[0][0],self.body[0][1]-1)
        elif self.direction == 'd':
            self.movepredict = (self.body[0][0],self.body[0][1]+1)

    def eatapple(self,apple): # Ta funkcja obsługuje jedzenie jabłek tako
        pass

    def setdirection(self,key): # To jest funkcja która robi tablice następnych ruchów
        if key == pygame.K_UP and len(self.moves) == 0 and not self.direction == 'd':
            self.moves += 'u'
        elif key == pygame.K_UP and len(self.moves) > 0:
            if not self.moves[len(self.moves) -1] == 'd':
                self.moves += 'u'
        elif key == pygame.K_DOWN and len(self.moves) == 0 and not self.direction == 'u':
            self.moves += 'd'
        elif key == pygame.K_DOWN and len(self.moves) > 0:
            if not self.moves[len(self.moves) -1] == 'u':
                self.moves += 'd'
        elif key == pygame.K_RIGHT and len(self.moves) == 0 and not self.direction == 'l':
            self.moves += 'r'
        elif key == pygame.K_RIGHT and len(self.moves) > 0:
            if not self.moves[len(self.moves) -1] == 'l':
                self.moves += 'r'
        elif key == pygame.K_LEFT and len(self.moves) == 0 and not self.direction == 'r':
            self.moves += 'l'
        elif key == pygame.K_LEFT and len(self.moves) > 0:
            if not self.moves[len(self.moves) -1] == 'r':
                self.moves += 'l'
        print(self.moves)

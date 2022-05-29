import apple
import snake
import pygame


class Game: # Klasa obsługująca gre

    def __init__(self):
        pygame.init()   # Inicjalizacja pygame
        self.font = pygame.font.Font('freesansbold.ttf', 72)    # Import czcionki
        self.endstr = self.font.render("Koniec, Przegrałeś!!!", True, (255,255,255))    # Render napisu końcowego

        self.screen = pygame.display.set_mode((900,600)) # Board 36x24[squares]; Square 25x25[px]
        self.snake = snake.Snake(self.screen)   # Twożenie obiektu węża
        self.apple = apple.Apple(self.screen,self.snake.body)   # Twożenie obiektu jabłka
    
    def end(self):  # Ekran końcowy
        self.screen.blit(self.endstr, (100, 250))

    def gameloop(self): # Pętla gry
        while self.running:
            for event in pygame.event.get():    # Obsługa wkładu gracza
                if event.type == pygame.QUIT:
                    break
                elif event.type == pygame.KEYDOWN:
                    if self.snake.alive:
                        self.snake.setdirection(event.key)
                    else:
                        self.snake.__init__(self.screen)
            if self.snake.ismove(): #Sprawdza czy minął odpowiedni czas żeby wygenerować klatke i wykonać ruch w grze
                self.screen.fill((0,0,0))
                if self.snake.move(self.apple) == "end":
                    self.end()
                else:
                    self.apple.draw()
                    self.snake.drawBody()
                    self.snake.printbody()
                print('move')
                len(self.snake.body)
                pygame.display.update()
            
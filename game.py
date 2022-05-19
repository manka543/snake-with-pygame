import apple
import snake
import pygame


class game:

    def __init__(self):
        pygame.init()
        self.font = pygame.font.Font('freesansbold.ttf', 72) #TODO: Przenieś do klasy snake i to niżej też
        self.endstr = self.font.render("Koniec, Przegrałeś!!!", True, (255,255,255))
        print('init')

        self.screen = pygame.display.set_mode((900,600)) # Board 36x24[squares]; Square 25x25[px]
        self.snake = snake.Snake(self.screen)
    
    def end(self):
        self.screen.blit(self.endstr, (400, 250))

    def gameloop(self):
        self.running = True
        print("running")
        while self.running:
            for event in pygame.event.get():
                print("running2")
                if event.type == pygame.QUIT:
                    self.running = False
                elif event.type == pygame.KEYDOWN:
                    self.snake.setdirection(event.key)
            if self.snake.ismove():
                print("move")
                print(snake.body)
                self.screen.fill((0,0,0))
                self.snake.move()
                self.snake.drawBody()
                print('move')
            pygame.display.update()
            
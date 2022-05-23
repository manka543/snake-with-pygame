import apple
import snake
import pygame


class Game:

    def __init__(self):
        pygame.init()
        self.font = pygame.font.Font('freesansbold.ttf', 72) 
        self.endstr = self.font.render("Koniec, Przegrałeś!!!", True, (255,255,255))
        print('init')

        self.screen = pygame.display.set_mode((900,600)) # Board 36x24[squares]; Square 25x25[px]
        self.snake = snake.Snake(self.screen)
        self.apple = apple.Apple(self.screen,self.snake.body)
    
    def end(self):
        self.screen.blit(self.endstr, (100, 250))

    def gameloop(self):
        self.running = True
        print("running")
        while self.running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.running = False
                elif event.type == pygame.KEYDOWN:
                    if self.snake.alive:
                        self.snake.setdirection(event.key)
                    else:
                        self.snake.__init__(self.screen)
            if self.snake.ismove():
                print("move")
                self.screen.fill((0,0,0))
                if self.snake.move(self.apple) == "end":
                    self.end()
                else:
                    self.apple.draw()
                    self.snake.drawBody()
                print('move')
                len(self.snake.body)
                pygame.display.update()
            
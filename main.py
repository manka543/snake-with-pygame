import pygame
import snake

pygame.init() # Inicjalizacja pygama

# Game variables
font = pygame.font.Font('freesansbold.ttf', 72) #TODO: Przenieś do klasy snake i to niżej też
endstr = font.render("Koniec, Przegrałeś!!!", True, (255,255,255))


screen = pygame.display.set_mode((900,600)) # Board 36x24[squares]; Square 25x25[px]

# TODO: Po dodaniu możliwości zginięcia dodaj to do klasy snake
def end():
    screen.blit(endstr, (400, 250))

snake = snake.Snake(screen) # Twożenie objektu klasy snake


# TODO: To wsumie też można zrobić klase game i tam przenieść prawie wszystko żeby jak ktoś to będzie przeglądać to nic nie bedzie wiedzieć
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            snake.setdirection(event.key)
    if snake.ismove():
        print("move")
        print(snake.body)
        screen.fill((0,0,0))
        snake.move()
        snake.drawBody()

        pygame.display.update()
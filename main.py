import pygame
from random import randint

pygame.init()

# Game variables
gameSpeed = 1000 # This int change game speed
gameClock = gameSpeed
font = pygame.font.Font('freesansbold.ttf', 72)
endstr = font.render("Koniec, Przegrałeś!!!", True, (255,255,255))


screen = pygame.display.set_mode((900,600)) # Board 36x24[squares]; Square 25x25[px]

def end():
    screen.blit(endstr, (400, 250))


running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        
    pygame.display.update()
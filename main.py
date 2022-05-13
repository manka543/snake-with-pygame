import pygame

pygame.init()

# Game variables
gameSpeed = 50 # This int change game speed
gameClock = gameSpeed
snakeX = [7,8,9,10] # List with snake elements on x axis
snakeY = [12,12,12,12] # List with snake elements on y axis
aplle = (2*25,5*25) # Tuple with apple cordinates
nextMove = "r"
nnextMove = "r"
nextMoveC = False
nnextMoveC = False
font = pygame.font.Font('freesansbold.ttf', 72)
endstr = font.render("Koniec, Przegrałeś!!!", True, (255,255,255))


screen = pygame.display.set_mode((900,600)) # Board 36x24[squares]; Square 25x25[px]

def end():
    screen.blit(endstr, (400, 250))

def graph(snakeXEl,snakeYEl,appleCor):
    for x in range(len(snakeXEl)):
        pygame.draw.rect(screen,(0,255,0),(snakeXEl[x]*25,snakeYEl[x]*25,25,25))
    pygame.draw.rect(screen,(255,0,0),(appleCor[0],appleCor[1],25,25))

def eatingapple():
    print("jabułko zjedzone")


def gameLogic(snakeXEl,snakeYEl,appleCor,nextMovel,nextMoveCl,nnextMovel,nnextMoveCl):
    if nextMovel == 'r' or nextMovel == 'l':
        if snakeXEl[0]-1 < 0 or snakeXEl[0]+1 >35:
            return end()
    elif nextMovel == 'u' or nextMove == 'd':
        if snakeYEl[0]-1 < 0 or snakeYEl[0]+1 >23:
            return end()
    if snakeXEl[0] == appleCor[0] and snakeYEl[0] == appleCor[1]:
        eatingapple()

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                if not nextMoveC and not nextMove == 'd' and not nextMove == 'u':
                    nextMove = 'u'
                    nextMoveC = True
                elif not nnextMoveC and not nextMove == 'd' and not nextMove == 'u':
                    nnextMove = 'u'
                    nnextMoveC = True
            elif event.key == pygame.K_DOWN:
                if not nextMoveC and not nextMove == 'u' and not nextMove == 'd':
                    nextMove = 'd'
                    nextMoveC = True
                elif not nnextMoveC and not nextMove == 'u' and not nextMove == 'd':
                    nnextMove = 'd'
                    nnextMoveC = True
            elif event.key == pygame.K_RIGHT:
                if not nextMoveC and not nextMove == 'l' and not nextMove == 'r':
                    nextMove = 'r'
                    nextMoveC = True
                elif not nnextMoveC and not nextMove == 'l' and not nextMove == 'r':
                    nnextMove = 'r'
                    nnextMoveC = True
            elif event.key == pygame.K_LEFT:
                if not nextMoveC and not nextMove == 'r' and not nextMove == 'l':
                    nextMove = 'l'
                    nextMoveC = True
                elif not nnextMoveC and not nextMove == 'r' and not nextMove == 'l':
                    nnextMove = 'l'
                    nnextMoveC = True
    gameClock -= 1
    if gameClock == 0:
        gameLogic(snakeX,snakeY,aplle,nextMove,nextMoveC,nnextMove,nnextMoveC)
        gameClock = gameSpeed
    graph(snakeX,snakeY,aplle)
    pygame.display.update()
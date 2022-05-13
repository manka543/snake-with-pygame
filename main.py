import pygame
from random import randint

pygame.init()

# Game variables
gameSpeed = 1000 # This int change game speed
gameClock = gameSpeed
snakeX = [14,13,12] # List with snake elements on x axis
snakeY = [15,15,15] # List with snake elements on y axis
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
    apple = (randint(0,35), randint(0,23))


def gameLogic(appleCor,nextMovel,nextMoveCl,nnextMovel,nnextMoveCl):
    global snakeX, snakeY
    if nextMovel == 'r':
        if snakeX[0]+1 > 35:
            return end()
    elif nextMovel == 'l':
        if snakeX[0]-1 < 0:
            return end()
    elif nextMovel == 'u':
        if snakeY[0]+1 >23:
            return end()
    elif nextMove == 'd':
        if snakeY[0]-1 < 0:
            return end()
    snakeX.pop(len(snakeX)-2)
    snakeY.pop(len(snakeY)-2)
    # Move
    if nextMovel == 'r':
        print('ruch w prawo')
        nextCords = (snakeX[0]+1,snakeY[0])
    elif nextMovel == 'l':
        print('ruch w lewo')
        nextCords = (snakeX[0]-1,snakeY[0])
    elif nextMovel == 'u':
        print('ruch w góre')
        nextCords = (snakeX[0],snakeY[0]-1)
    elif nextMovel == 'd':
        print('ruch w dól')
        nextCords = (snakeX[0]+1,snakeY[0]+1)
    for i in range(len(snakeX)):
        if i > 2:    
            snakeX[len(snakeX)-i-1] = snakeX[len(snakeX)-i-2]
            snakeY[len(snakeY)-i-1] = snakeY[len(snakeY)-i-2]
    snakeX[0] = nextCords[0]
    snakeY[0] = nextCords[1]
    
    if snakeX[0] == appleCor[0] and snakeY[0] == appleCor[1]:
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
        gameLogic(aplle,nextMove,nextMoveC,nnextMove,nnextMoveC)
        gameClock = gameSpeed
    graph(snakeX,snakeY,aplle)
    pygame.display.update()
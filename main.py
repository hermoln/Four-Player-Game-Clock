import pygame, time
import math

pygame.init()


SCREENWIDTH = 600
SCREENHEIGHT = 600
BLUE = (0,0,255)
BLACK = (0, 0, 0)
GRAY = (128,128,128)
GREEN = (0, 255, 0)
GRAY_HIGHLIGHT = (194,194,194)

screen = pygame.display.set_mode((SCREENWIDTH,SCREENHEIGHT))
screen.fill(GRAY)

turn = 1

def getTime():
    global playersTime, players, timePass

    players = []
    playersTime = []

    for i in range(0, int(input("How many players in the game?"))):
        players.append(i + 1)
    for i in range(len(players)):
        playersTime.append(input("How much time for player " + str(i + 1) + "?"))
    print(playersTime)

    timePass = time.time() + 1

def paintScreen():
    screen.fill(GRAY)
    for i in range(len(players)):
        if turn == players[i]:
            outlineColor = GREEN
        else:
            outlineColor = BLACK
        pygame.draw.rect(screen, outlineColor, (SCREENWIDTH/8, (i+1)*6/8*SCREENWIDTH/len(players) - (6/8*SCREENWIDTH/len(players))/2, SCREENWIDTH*6/8, 6/8*SCREENWIDTH/len(players)), 2)

def nextPlayer():
    global turn

    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                if turn == players[len(players)-1]:
                    turn = players[0]
                else:
                    turn += 1

def convert(seconds):
    minutes, seconds = divmod(int(seconds), 60)
    return "%d:%02d" % (minutes, int(seconds))

def countPlayerTime():
    global timePass

    if time.time() >= timePass:
        timePass = time.time() + 1
        playersTime[turn-1] = int(playersTime[turn-1]) - 1

def setPlayerTime():
    global playersDisplayTime

    playersDisplayTime = []

    for i in range(len(players)):
        playersDisplayTime.append(convert(playersTime[i]))

def displayTime():
    countPlayerTime()
    setPlayerTime()
    for i in range(len(players)):
        timeFont = pygame.font.SysFont('arial', round(6/8*SCREENWIDTH/len(players)/2))
        timeText = timeFont.render(str(playersDisplayTime[i]), True, BLACK)
        textRect = timeText.get_rect()
        textRect.center = (SCREENWIDTH/2, (i+1)*6/8*SCREENWIDTH/len(players))
        screen.blit(timeText, textRect)

def startClock():

    getTime()

    while True:
        pygame.display.update()
        nextPlayer()
        paintScreen()
        displayTime()

startClock()

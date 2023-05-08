import pygame, time
import math

pygame.init()


SCREENWIDTH = 600
SCREENHEIGHT = 600
BLUE = (0,0,255)
BLACK = (0, 0, 0)
GRAY = (128,128,128)
GRAY_HIGHLIGHT = (194,194,194)
#used to indicate which players turn it is
TIME_FONT = pygame.font.SysFont('arial', 30)

screen = pygame.display.set_mode((SCREENWIDTH,SCREENHEIGHT))
screen.fill(BLACK)

player = 1
playersRemaining = [1, 2, 3, 4]


def getTime():
    global playersTime

    print("Please input the following values in terms of seconds.")
    player1Time = input("Time for player one? ")
    player2Time = input("Time for player two? ")
    player3Time = input("Time for player three? ")
    player4Time = input("Time for player four? ")
    playersTime = [player1Time, player2Time, player3Time, player4Time]
		
def paintScreen():
	#creates the area for time to be displayed
    if player == 1:
        pygame.draw.rect(screen, GRAY_HIGHLIGHT, (1,1,SCREENWIDTH/2-1,SCREENHEIGHT/2-1), 0)
    else:
        pygame.draw.rect(screen, GRAY, (1,1,SCREENWIDTH/2-1,SCREENHEIGHT/2-1), 0)
    if player == 2:
        pygame.draw.rect(screen, GRAY_HIGHLIGHT, (SCREENWIDTH/2+1,1,SCREENWIDTH/2-1,SCREENHEIGHT/2-1), 0)
    else:
        pygame.draw.rect(screen, GRAY, (SCREENWIDTH/2+1,1,SCREENWIDTH/2-1,SCREENHEIGHT/2-1), 0)
    if player == 3:
        pygame.draw.rect(screen, GRAY_HIGHLIGHT, (1,SCREENWIDTH/2+1,SCREENHEIGHT/2-1,SCREENHEIGHT/2-1), 0)
    else:
        pygame.draw.rect(screen, GRAY, (1,SCREENWIDTH/2+1,SCREENHEIGHT/2-1,SCREENHEIGHT/2-1), 0)
    if player == 4:
        pygame.draw.rect(screen, GRAY_HIGHLIGHT, (SCREENWIDTH/2+1,SCREENHEIGHT/2+1,SCREENWIDTH/2-1,SCREENHEIGHT/2-1), 0)
    else:
        pygame.draw.rect(screen, GRAY, (SCREENWIDTH/2+1,SCREENHEIGHT/2+1,SCREENWIDTH/2-1,SCREENHEIGHT/2-1), 0)


def nextPlayer():
    global player

    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                if player == playersRemaining[len(playersRemaining)-1]:
                    player = playersRemaining[0]
                else:
                    player += 1

def convert(seconds):
    minutes, seconds = divmod(int(seconds), 60)
    return "%d:%02d" % (minutes, int(seconds))
		#changes seconds to normal clock display

def countPlayerTime():
    time.sleep(1)
    playersTime[player-1] = int(playersTime[player-1]) - 1

def setPlayerTime():
    global playersDisplayTime

    playersDisplayTime = []
    playersDisplayTime.append(convert(playersTime[0]))
    playersDisplayTime.append(convert(playersTime[1]))
    playersDisplayTime.append(convert(playersTime[2]))
    playersDisplayTime.append(convert(playersTime[3]))

def displayTime():
    countPlayerTime()
    setPlayerTime()
    player1Text = TIME_FONT.render(str(playersDisplayTime[0]), True, BLACK)
    player1TextRect = player1Text.get_rect()
    player1TextRect.center = (SCREENWIDTH/4, SCREENWIDTH/4)
    player2Text = TIME_FONT.render(str(playersDisplayTime[1]), True, BLACK)
    player2TextRect = player2Text.get_rect()
    player2TextRect.center = (SCREENWIDTH*(3/4), SCREENWIDTH/4)
    player3Text = TIME_FONT.render(str(playersDisplayTime[2]), True, BLACK)
    player3TextRect = player3Text.get_rect()
    player3TextRect.center = (SCREENWIDTH/4, SCREENWIDTH*(3/4))
    player4Text = TIME_FONT.render(str(playersDisplayTime[3]), True, BLACK)
    player4TextRect = player4Text.get_rect()
    player4TextRect.center = (SCREENWIDTH*(3/4), SCREENWIDTH*(3/4))

    screen.blit(player1Text, player1TextRect)
    screen.blit(player2Text, player2TextRect)
    screen.blit(player3Text, player3TextRect)
    screen.blit(player4Text, player4TextRect)

def startClock():

    getTime()

    while True:
        pygame.display.update()
        nextPlayer()
        paintScreen()
        displayTime()

startClock()

import pygame
import random
from pygame.locals import (
    K_UP,
    K_DOWN,
    K_LEFT,
    K_RIGHT,
    K_ESCAPE,
    KEYDOWN,
    QUIT,
    K_w,
    K_s
)
print("this is a test message")
pygame.init()
sWidth = 640
sHeight = 480
lPos = 50
rPos = 50
bPosX = sWidth/2
bPosY = sHeight/2
center = (sWidth/2,sHeight/2)
bSpeedY = 0.1
bSpeedX = 0.1
bRad = 12
lScore = 0
rScore = 0
color = 255
inc = False
screen = pygame.display.set_mode((sWidth, sHeight))
running = True
while running:
    '''
    if inc == True:
        if round(color,0) == 254:
            inc = False
        color = color + 1
    else:
        if round(color,0) == 1:
            inc = True
        color = color - 1
    ''' 
    for event in pygame.event.get():
        if event.type == KEYDOWN:
            if event.key == K_ESCAPE:
                running = False
            if event.key == K_w:
                lPos = lPos - 45
                if lPos < bPosY + 13 and 27 < bPosX < 73:
                    lPos = bPosY + 12
                if lPos < 20:
                    lPos = 20
            if event.key == K_s:
                lPos = lPos + 45
                if lPos < bPosY + 93 and 27 < bPosX < 73:
                    lPos = bPosY - 92
                if lPos > 380:
                    lPos = 380
            if event.key == K_UP:
                rPos = rPos - 45
                if rPos < bPosY + 13 and 573 < bPosX < 627:
                    rPos = bPosY + 12
                if rPos < 20:
                    rPos = 20
            if event.key == K_DOWN:
                rPos = rPos + 45
                if rPos < bPosY + 93 and 573 < bPosX < 627:
                    rPos = bPosY - 92
                if rPos > 380:
                    rPos = 380
        elif event.type == QUIT:
            running = False
    if bPosY < bRad:
        bSpeedY = bSpeedY * (-1.05)
    elif bPosY > sHeight-bRad:
        bSpeedY = bSpeedY * (-1.05)
    if bPosX < bRad:
        rScore = rScore + 1
        bSpeedX = 0.1
        bSpeedY = 0.1
        bPosX = center[0]
        bPosY = center[1]
        print(f"Left Player Score: {lScore}")
        print(f"Right Player Score: {rScore}")
    if bPosX > sWidth-bRad:
        lScore = lScore + 1
        bSpeedX = -0.1
        bSpeedY = 0.1
        bPosX = center[0]
        bPosY = center[1]
        print(f"Left Player Score: {lScore}")
        print(f"Right Player Score: {rScore}")
    if (bPosY > lPos) and (bPosY < lPos+80) and (70 < round(bPosX,1) < 72):
        bSpeedX = bSpeedX*(-1.1)
    elif (bPosY > lPos) and (bPosY < lPos+80) and (30 < round(bPosX,1) < 69):
        bSpeedX = bSpeedX*(-1.25)
        bSpeedY = bSpeedY*(-1.25)
    if (bPosY > rPos) and (bPosY < rPos+80) and (570 < round(bPosX,1) < 572):
        bSpeedX = bSpeedX*(-1.25)
    elif (bPosY > rPos) and (bPosY < rPos+80) and (620 > round(bPosX,1) > 573):
        bSpeedX = bSpeedX*(-1.25)
        bSpeedY = bSpeedY*(-1.25)
    if bSpeedX > .4:
        bSpeedX = .4
    if bSpeedY > .4:
        bSpeedY = .4
    bSpeedX = round(bSpeedX, 2)
    bSpeedY = round(bSpeedY, 2)
    bPosY = bPosY + bSpeedY
    bPosX = bPosX + bSpeedX
    screen.fill((0,0,0))
    pygame.draw.rect(screen,(255,255,255),(40,lPos,20,80))
    pygame.draw.rect(screen,(255,255,255),(580,rPos,20,80))
    pygame.draw.circle(screen,(color,color,color),(bPosX,bPosY), bRad)
    pygame.display.flip()
pygame.quit()


import pygame
import random
from pygame.locals import ( #Import the definitions of keys from pygame to make my life easier.
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
print("this is a test message") #Just make sure the import didn't bork itself.
pygame.init()
sWidth = 640 #Initialize a bunch of the game variables.
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
screen = pygame.display.set_mode((sWidth, sHeight)) #Make a window with the predefined w and h values
running = True
while running:
    #If active, this code makes the ball flash, because that's very funny. I don't think it works.
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
    for event in pygame.event.get(): #Whenever some input happens...
        if event.type == KEYDOWN: #Check if it was a keypress
            if event.key == K_ESCAPE: #Check what key it was
                running = False
            if event.key == K_w: 
                lPos = lPos - 45
                if lPos < bPosY + 13 and 27 < bPosX < 73: #For all the paddle movement keys, make sure that the next move wouldn't move the paddle inside the ball.
                    lPos = bPosY + 12 #If it would, only move it far enough to touch the ball.
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
        elif event.type == QUIT: #If they pressed the X button, quit the game.
            running = False
    if bPosY < bRad: #If the ball hits the top/bottom of the screen, give it a slight speed boost and make it bounce.
        bSpeedY = bSpeedY * (-1.05)
    elif bPosY > sHeight-bRad:
        bSpeedY = bSpeedY * (-1.05)
    if bPosX < bRad: #If the ball hits the left/right of the screen, reset its speed, center it, and update/print the score accordingly.
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
    if (bPosY > lPos-2) and (bPosY < lPos+82) and (70 < round(bPosX,1) < 72): #If the ball hits the left paddle's sides, bounce it and increase its speed by 1.1x.
        bSpeedX = bSpeedX*(-1.1)
    elif (bPosY > lPos-2) and (bPosY < lPos+82) and (30 < round(bPosX,1) < 69): #Do the same for the top edges, but with a speed boost, and bounce it in a different way.
        bSpeedX = bSpeedX*(-1.25)
        bSpeedY = bSpeedY*(-1.25)
    if (bPosY > rPos-2) and (bPosY < rPos+82) and (570 < round(bPosX,1) < 572): #Same stuff for the right paddle.
        bSpeedX = bSpeedX*(-1.25)
    elif (bPosY > rPos-2) and (bPosY < rPos+82) and (620 > round(bPosX,1) > 573):
        bSpeedX = bSpeedX*(-1.25)
        bSpeedY = bSpeedY*(-1.25)
    if bSpeedX > .4: #Don't let the speed go about .4 pixels per game loop.
        bSpeedX = .4
    if bSpeedY > .4:
        bSpeedY = .4
    bSpeedX = round(bSpeedX, 2) #Round the speed values so that they don't cause ugly floating-point madness.
    bSpeedY = round(bSpeedY, 2)
    bPosY = bPosY + bSpeedY #Add the speed values to the overall X and Y co-ords.
    bPosX = bPosX + bSpeedX
    screen.fill((0,0,0)) #Fill the screen with black.
    pygame.draw.rect(screen,(255,255,255),(40,lPos,20,80)) #Draw the two paddles and the ball to the screen.
    pygame.draw.rect(screen,(255,255,255),(580,rPos,20,80))
    pygame.draw.circle(screen,(color,color,color),(bPosX,bPosY), bRad)
    pygame.display.flip()
pygame.quit()


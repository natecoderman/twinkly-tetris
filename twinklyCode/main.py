""" code tasks:
    - print score/end screen
    

    for git readMe
    - having the twinkly app open while runnning program causes problems
    - which libraries have to be pip installed?
    - include python version, twinkly version (device.vers() or something)
    - include "this does not break, modify, or otherwise change your twinkly device. just use the app again to kick it back into normal"
    - flags available (Twinkly_D11F1D)
    - trouble shooting (wrong device connected? just keep trying) (try recalibrating your twinkly device by deleting and readding device)
    - how it works "we send a big list of bytes in format "/0x00/0xff ... for rgb vals .."
    - controls (left/right, down, rotate)
"""


import pygame
import sys
import xled
import threading
import random
import time

import os
import signal

DEFINE_HEIGHT = 8 #y axis, in pixels
DEFINE_WIDTH = 8 #x axis, in pixels
DEFINE_PANELS = 1 # number of panels
DEFINE_DEVICE = "Twinkly_D11F1D" 
DEFINE_ROTATE = 0 #rotate the screen, for 8x8 only
DEFINE_CLASSIC = False # classic colors 


#commandline args
executeRest = False
arglen = len(sys.argv) 


if (arglen == 5):
    # number of panels, rotate, classic mode, specify device
    executeRest = True
    DEFINE_DEVICE = sys.argv[4]

if (arglen == 4 or executeRest):
    #num panels, rotate, classic mode
    executeRest = True
    if (sys.argv[3] == "1"):
        print("playing in classic mode")
        DEFINE_CLASSIC = True
    else:
        print("playing in normal mode")

if (arglen == 3  or executeRest):
    # number of panels, rotate
    executeRest = True
    if (int(sys.argv[1]) > 1 and sys.argv[2] != "0"):
        print("can't rotate more than one panel (set rotate arg to 0 or panel arg to 1)")
        sys.exit(1)
    elif (int(sys.argv[2]) > -1 and int(sys.argv[2]) < 4):
        DEFINE_ROTATE = int(sys.argv[2])
    else:
        print("invalid rotate value")
        sys.exit(1)

if (arglen == 2 or executeRest):
    # number of panels
    if (sys.argv[1] == "1"): #1 panel, the default
        pass
    elif(sys.argv[1] == "2"):
        DEFINE_HEIGHT = 16
        DEFINE_PANELS = 2
    else:
        print("invalid number of panels")
        sys.exit(1)


#include other files

with open('endGame.py', 'r') as file: 
    exec(file.read())

with open('frameClass.py', 'r') as file:
    exec(file.read())

with open('blockClass.py', 'r') as file:
    exec(file.read())

with open('pieceClass.py', 'r') as file:
    exec(file.read())

with open('pieces.py', 'r') as file:
    exec(file.read())

with open('twinklyConnect.py', 'r') as file:
    exec(file.read())

# global functions



def createPiece():
    randPiece = random.randint(1, 7)
    if (randPiece == 1):
        if (DEFINE_CLASSIC):
            return Opiece((255, 255, 0))
        return Opiece((random.randint(1, 200), random.randint(1, 200), random.randint(1, 200)))
    elif (randPiece == 2):
        if (DEFINE_CLASSIC):
            return Ipiece((173, 216, 230))
        return Ipiece((random.randint(1, 200), random.randint(1, 200), random.randint(1, 200)))
    elif (randPiece == 3):
        if (DEFINE_CLASSIC):
            return Lpiece((255, 43, 0))
        return Lpiece((random.randint(1, 200), random.randint(1, 200), random.randint(1, 200)))
    elif (randPiece == 4):
        if (DEFINE_CLASSIC):
            return Jpiece((0, 0, 255))
        return Jpiece((random.randint(1, 200), random.randint(1, 200), random.randint(1, 200)))
    elif (randPiece == 5):
        if (DEFINE_CLASSIC):
            return Tpiece((128, 0, 128))
        return Tpiece((random.randint(1, 200), random.randint(1, 200), random.randint(1, 200)))
    elif (randPiece == 6):
        if (DEFINE_CLASSIC):
            return Spiece((0, 255, 0))
        return Spiece((random.randint(1, 200), random.randint(1, 200), random.randint(1, 200)))
    else:
        if (DEFINE_CLASSIC):
            return Zpiece((255, 0, 0))
        return Zpiece((random.randint(1, 200), random.randint(1, 200), random.randint(1, 200)))



#general setup

matTest = [[(0, 0, 0) for _ in range(DEFINE_HEIGHT)] for _ in range(DEFINE_WIDTH)] # initialize matrix of colors
matStore = [[None for _ in range(DEFINE_HEIGHT)] for _ in range(DEFINE_WIDTH)] # holds data of what spaces are already full of blocks

# EXAMPLE matTest layout for 8 x 8: 
#            [[(0, 0, 255), (0, 0, 255), (0, 0, 255), (0, 0, 255), (0, 0, 255), (0, 0, 255), (0, 0, 255), (0, 0, 255)], ## bottom right is here
#            [(0, 0, 255), (0, 0, 255), (0, 0, 255), (0, 0, 255), (0, 0, 255), (0, 0, 255), (0, 0, 255), (0, 0, 255)],
#            [(0, 0, 255), (0, 0, 255), (0, 0, 255), (0, 0, 255), (0, 0, 255), (0, 0, 255), (0, 0, 255), (0, 0, 255)],
#            [(0, 0, 255), (0, 0, 255), (0, 0, 255), (0, 0, 255), (0, 0, 255), (0, 0, 255), (0, 0, 255), (0, 0, 255)],
#            [(0, 0, 255), (0, 0, 255), (0, 0, 255), (0, 0, 255), (0, 0, 255), (0, 0, 255), (0, 0, 255), (0, 0, 255)],
#            [(0, 0, 255), (0, 0, 255), (0, 0, 255), (0, 0, 255), (0, 0, 255), (0, 0, 255), (0, 0, 255), (0, 0, 255)],
#            [(0, 0, 255), (0, 0, 255), (0, 0, 255), (0, 0, 255), (0, 0, 255), (0, 0, 255), (0, 0, 255), (0, 0, 255)],
#            [(0, 0, 255), (0, 0, 255), (0, 0, 255), (0, 0, 255), (0, 0, 255), (0, 0, 255), (0, 0, 255), (0, 0, 255)]] ## bottom left is here
#
# Notice indexes are essentially flipped, so yLoc = 0 is the top 
# xLoc = 0 is right

frameTest = Frame(matTest)
control.set_rt_frame_socket(frameTest, 2)

pygame.init()
display = pygame.display.set_mode((300, 300))
fallTime = 0
player = createPiece()
clock = pygame.time.Clock()
score = 0


while True:
    
    clock.tick(30)
    fallTime += clock.get_time()
    if (fallTime > 500): #block fall
        fallTime = 0
        if (player.checkFall()):
            player.delCurrent()
            player.fall()
            if((score >= (DEFINE_WIDTH * 5)) and player.checkFall()): #squares fall twice as fast
                player.delCurrent()
                player.fall()
                if((score >= (DEFINE_WIDTH * 8)) and DEFINE_PANELS == 1 and player.checkFall()): #squares fall thrice as fast
                    player.delCurrent()
                    player.fall()
                    if((score >= (DEFINE_WIDTH * 11)) and player.checkFall()): #squares fall 4x as fast
                        player.delCurrent()
                        player.fall()
        
        if (not player.checkFall()):
            if (player.checkLine()):
                score += DEFINE_WIDTH
            time.sleep(0.2)
            player = createPiece()

        control.set_rt_frame_socket(frameTest, 2) #screen refresh
        

    # creating a loop to check events that are occurring
    for event in pygame.event.get():
        control.set_rt_frame_socket(frameTest, 2) #screen refresh
        # checking if keydown event happened or not
        if event.type == pygame.KEYDOWN:
               
            if event.key == pygame.K_ESCAPE:
                print("exiting..")
                pygame.quit()
                sys.exit()
            
            if event.key == pygame.K_LEFT:
                if(player.checkMoveLeft()):
                    player.delCurrent()
                    player.moveLeft()

            if event.key == pygame.K_RIGHT:
                if(player.checkMoveRight()):
                    player.delCurrent()
                    player.moveRight()
            
            if event.key == pygame.K_r:
                if(player.rightRotateCheck()):
                    player.delCurrent()
                    player.rightRotate()


            if event.key == pygame.K_DOWN:
                if (player.checkFall()):
                    player.delCurrent()
                    player.fall()
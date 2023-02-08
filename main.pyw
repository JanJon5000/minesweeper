import pygame
import random
import boardClass
import sys
from random import randint
import aplicationWindows
import colorsRGB
import otherFunctions
import datetime
import webbrowser
#setting up a dictionary witch in the future will store coordinates of buttons created in menu() func
dictOfMenuButtons = dict()
dictOfLvLButtons = dict()
#setting up menu
pygame.init()
screen = pygame.display.set_mode((400, 400))
aplicationWindows.menu(screen, dictOfMenuButtons)
running = True
#setting up the variable which says wheather it is a menu or a game window
currentWindow = 'menu'
previousWindow = None
listOfLvls = ['beginner', 'normal', 'hard', 'impossible', 'game rules']
isItSecondClick = False
flagedButtons = []
allButtons = []
once = True
while running:    
    for event in pygame.event.get():
        # menu oriented events handling
        if currentWindow == 'menu':
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.MOUSEBUTTONDOWN:
                mousePosition = event.pos
                for lvl in listOfLvls:
                    if dictOfMenuButtons[lvl].collidepoint(mousePosition):
                        if lvl == 'game rules':
                            webbrowser.open("https://en.wikipedia.org/wiki/Minesweeper_(video_game)")
                            break
                        board = boardClass.boardClass(lvl)
                        aplicationWindows.lvl(screen, board, dictOfLvLButtons)
                        allButtons = [dictOfLvLButtons[key][num] for key in dictOfLvLButtons.keys() for num in range(len(dictOfLvLButtons[key]))]
                        previousWindow = currentWindow         
                        currentWindow = lvl
                        flagedButtons = []
                        otherFunctions.buttonsAlreadyFlipped = []
                        flagsLeft = board.minesRequired
                        beforeTheGame = datetime.datetime.now()

        #
        # minesweeper oriented event handling
        #
        if currentWindow in ['beginner', 'normal', 'hard', 'impossible']:
            if event.type == pygame.QUIT:
                aplicationWindows.menu(screen, dictOfMenuButtons)
                dictOfLvLButtons = dict()
                currentWindow = 'menu'
                isItSecondClick = False
                once = True
            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:
                    possibleButtons = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 'Flag', 'Mine', 'Nothing']
                    images = {key:f'img\\{key}.png' for key in possibleButtons}
                    if isItSecondClick == True:
                        mousePosition = event.pos
                        if once:
                            for item in dictOfLvLButtons.keys():
                                for button in dictOfLvLButtons[item]:
                                    if button.collidepoint(mousePosition):
                                        firslyClickedButton = button
                            while True:
                                dictOfLvLButtons = dict()
                                board = boardClass.boardClass(currentWindow)
                                aplicationWindows.lvl(screen, board, dictOfLvLButtons)
                                if firslyClickedButton in dictOfLvLButtons[0]:
                                    once = False
                                    otherFunctions.Chain0ButtonReaction(screen, images, 0, firslyClickedButton, dictOfLvLButtons, board)
                                    otherFunctions.lines(screen, board)
                                    flagedButtons = []
                                    otherFunctions.buttonsAlreadyFlipped = []
                                    allButtons = [dictOfLvLButtons[key][num] for key in dictOfLvLButtons.keys() for num in range(len(dictOfLvLButtons[key]))]
                                    flagsLeft = board.minesRequired
                                    beforeTheGame = datetime.datetime.now()
                                    break

                        for item in dictOfLvLButtons.keys():
                            for button in dictOfLvLButtons[item]:
                                if button.collidepoint(mousePosition):
                                    if item != 'Mine':
                                        if item == 0:
                                            if button not in flagedButtons:
                                                otherFunctions.Chain0ButtonReaction(screen, images, item, button, dictOfLvLButtons, board)
                                                otherFunctions.lines(screen, board)
                                            else:
                                                pass
                                        else:
                                            if button not in flagedButtons:
                                                otherFunctions.rectToImg(screen, images, item, button)
                                                otherFunctions.lines(screen, board)
                                            else:
                                                pass                
                                    else:
                                        if button not in flagedButtons:
                                            aplicationWindows.GameOverScreen(screen, images, dictOfLvLButtons, board)
                                            isItSecondClick = False
                                            currentWindow = 'GameOverScreen'
                                            once = True
                                        else:
                                            pass
                    else:
                        isItSecondClick = True
                
            
                if event.button == 3:
                    if isItSecondClick == True:
                        images = {'Flag':'img\\Flag.png', 'Nothing':'img\\Nothing.png'}
                        mousePosition = pygame.mouse.get_pos()
                        for item in dictOfLvLButtons.keys():
                            for button in dictOfLvLButtons[item]:
                                if button.collidepoint(mousePosition):
                                    if button not in otherFunctions.buttonsAlreadyFlipped:
                                        if button not in flagedButtons and flagsLeft > 0:
                                            otherFunctions.rectToImg(screen, images, 'Flag', button)
                                            otherFunctions.lines(screen, board)
                                            flagedButtons.append(button)
                                            difference = [item for item in allButtons + otherFunctions.buttonsAlreadyFlipped if item not in allButtons or item not in otherFunctions.buttonsAlreadyFlipped]   
                                            flagsLeft -= 1                               
                                        else:
                                            otherFunctions.rectToImg(screen, images, 'Nothing', button)
                                            otherFunctions.lines(screen, board)
                                            try:
                                                flagedButtons.remove(button)
                                                flagsLeft += 1
                                            except:
                                                pass
                                                                         
                    else:
                        isItSecondClick = True
            
            try:
                difference = [item for item in allButtons + otherFunctions.buttonsAlreadyFlipped if item not in allButtons or item not in otherFunctions.buttonsAlreadyFlipped]            
                if difference == dictOfLvLButtons['Mine'] or otherFunctions.compareTwoNotSortedLists(dictOfLvLButtons['Mine'], flagedButtons):
                    timeOfTheGame = datetime.datetime.now()-beforeTheGame
                    aplicationWindows.VictoryScreen(screen, board, timeOfTheGame)
                    currentWindow = 'VictoryScreen'
                    isItSecondClick = False                    
            except KeyError:
                pass
            

        if currentWindow == "GameOverScreen":
            dictOfLvLButtons = dict()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if isItSecondClick == True:
                    aplicationWindows.menu(screen, dictOfMenuButtons)
                    currentWindow = 'menu'
                    isItSecondClick = False
                else:
                    isItSecondClick = True
            if event.type == pygame.QUIT:
                running = False

        if currentWindow == "VictoryScreen":
            dictOfLvLButtons = dict()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if isItSecondClick == True:
                    aplicationWindows.menu(screen, dictOfMenuButtons)
                    currentWindow = 'menu'
                    isItSecondClick = False
                else:
                    isItSecondClick = True
            if event.type == pygame.QUIT:
                running = False
                
    pygame.display.update()
import pygame
import colorsRGB
from pprint import pprint
pygame.init()
buttonsAlreadyFlipped = []
def findKeyOfAButton(button, boardButtons, board):
    for key in boardButtons.keys():
        for element in boardButtons[key]:
            if element == button:
                return key

def ButtoNextToAnother(screen, images, coreButton, boardButtons: dict(), board, direction):
    for key in boardButtons.keys():
        for button in boardButtons[key]:
            if direction == 'up':
                if button.x == coreButton.x and button.y == coreButton.y - 50:
                    searchedButton = button
                    searchedKey = key
            elif direction == 'down':
                if button.x == coreButton.x and button.y == coreButton.y + 50:
                    searchedButton = button
                    searchedKey = key
            elif direction == 'left':
                if button.x == coreButton.x - 50 and button.y == coreButton.y:
                    searchedButton = button
                    searchedKey = key
            elif direction == 'right':
                if button.x == coreButton.x + 50 and button.y == coreButton.y:
                    searchedButton = button
                    searchedKey = key
            elif direction == 'top_left_diagonal':
                if button.x == coreButton.x - 50 and button.y == coreButton.y - 50:
                    searchedButton = button
                    searchedKey = key
            elif direction == 'bottom_left_diagonal':
                if button.x == coreButton.x  - 50 and button.y == coreButton.y + 50:
                    searchedButton = button
                    searchedKey = key
            elif direction == 'top_right_diagonal':
                if button.x == coreButton.x + 50 and button.y == coreButton.y + 50:
                    searchedButton = button
                    searchedKey = key
            elif direction == 'bottom_right_diagonal':
                if button.x == coreButton.x + 50 and button.y == coreButton.y - 50:
                    searchedButton = button
                    searchedKey = key
    try:
        return searchedButton, searchedKey
    except UnboundLocalError:
        return None, None

def rectToImg(screen, images, key, button):
    img = pygame.image.load(images[key])
    pygame.draw.rect(screen, colorsRGB.white, button)
    screen.blit(img, (button.centerx-25, button.centery-25))
    if key != 'Flag' and key != 'Nothing':
        buttonsAlreadyFlipped.append(button)
    else:
        pass

def lines(screen, board):
    for x in range(board.sizeX):        
        pygame.draw.line(screen, colorsRGB.black, (x*50+50, 0), (x*50+50, board.sizeX*50))
    for y in range(board.sizeY):
        pygame.draw.line(screen, colorsRGB.black, (0, y*50+50), (board.sizeX*50, y*50+50))
    
def Chain0ButtonReaction(screen, images, key, button, boardButtons, board):
    #needed lists
    listOfButtons = []
    finalEditedButtons = []
    listOfButtonsRemake = []
    #making button a rectangle itself
    rectToImg(screen, images, key, button)

    # FIRST PHASE   
    # checking whether there are empty buttons near - any direction
    # setting up the button that we started with so that we can come back to it when checking other buttons
    coreButton = button
    directions = ['up', 'down', 'left', 'right', 'bottom_left_diagonal', 'top_left_diagonal', 'top_right_diagonal', 'bottom_right_diagonal']
    for direction in directions:
        while True:
            button, key = ButtoNextToAnother(screen, images, button, boardButtons, board, direction)
            try:
                if key != 'Mine':
                    if direction in ['bottom_left_diagonal', 'top_left_diagonal', 'top_right_diagonal', 'bottom_right_diagonal']:
                        rectToImg(screen, images, key, button)
                        break
                    else:
                        if key == 0:
                            rectToImg(screen, images, key, button)
                        else:
                            rectToImg(screen, images, key, button)
                            break
                if (direction == 'up' or direction == 'down') and key == 0:
                    listOfButtons.append(button)
                    listOfButtonsRemake.append(button)
                elif (direction == 'left' or direction == 'right'):
                    listOfButtonsRemake.append(button)
                    if button == None:
                        listOfButtons.remove(button)
                        break
            except KeyError:
                break
            
            if key != 0:
                break
        button = coreButton

    directions = ['left', 'right', 'top_left_diagonal', 'top_right_diagonal', 'bottom_left_diagonal', 'bottom_right_diagonal']
    for button0 in listOfButtons:
        coreButton0 = button0
        for direction in directions:
            while True:
                button0, key = ButtoNextToAnother(screen, images, button0, boardButtons, board, direction)
                try:
                    if key != 'Mine':
                        if direction in ['bottom_left_diagonal', 'top_left_diagonal', 'top_right_diagonal', 'bottom_right_diagonal']:
                            rectToImg(screen, images, key, button0)
                            break
                        else:
                            rectToImg(screen, images, key, button0)
                        if key == 0 and button != None:
                            finalEditedButtons.append(button0)
                            listOfButtonsRemake.append(button0)
                except KeyError:
                    break
                if button0 == None:
                    break
                if key != 0:
                    break
            button0 = coreButton0
    directions = ['left', 'right', 'up', 'bottom', 'top_left_diagonal', 'top_right_diagonal', 'bottom_left_diagonal', 'bottom_right_diagonal']
    for buttonFinalEdited in finalEditedButtons:
        coreButton = buttonFinalEdited
        for direction in directions:
            buttonFinalEdited, key = ButtoNextToAnother(screen, images, buttonFinalEdited, boardButtons, board, direction)
            if key == 0 and buttonFinalEdited != None:
                listOfButtonsRemake.append(buttonFinalEdited)
            if key != 'Mine' and buttonFinalEdited != None:
                rectToImg(screen, images, key, buttonFinalEdited)
            buttonFinalEdited = coreButton
    
    directions = ['left', 'right', 'up', 'bottom', 'top_left_diagonal', 'top_right_diagonal', 'bottom_left_diagonal', 'bottom_right_diagonal']
    for buttonLast in listOfButtonsRemake:
        coreButton = buttonLast
        for direction in directions:
            buttonLast, key = ButtoNextToAnother(screen, images, buttonLast, boardButtons, board, direction)
            if key != 'Mine' and key != None:
                rectToImg(screen, images, key, buttonLast)
            buttonLast = coreButton

def compareTwoNotSortedLists(list1, list2):
    for element in list1:
        elementExistsInList2 = False
        for otherElement in list2:
            if element == otherElement:
                elementExistsInList2 = True
        if elementExistsInList2 == False:
            return False
    return True
        
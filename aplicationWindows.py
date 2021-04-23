import pygame
import colorsRGB
import boardClass
import otherFunctions
import datetime
def menu(screen, dictOfButtons: list):
    pygame.init()
    # general settings of a screen - icon, caption, size, background color
    pygame.display.set_icon(pygame.image.load('img\\MineIcon.png'))
    pygame.display.set_caption('Minesweeper')
    screen = pygame.display.set_mode((400, 400))
    screen.fill(colorsRGB.grey1)

    # fonts for title, and buttons
    buttonFont = pygame.font.SysFont('Helvetica', 25)
    titleFont = pygame.font.SysFont('Helvetica', 35)

    # a list of a button names
    buttonsList = ['beginner', 'normal', 'hard', 'impossible', 'game rules']
    # title creation
    titleSurface = titleFont.render('MINESWEEPER', False, colorsRGB.black)
    titleSurfaceRect = titleSurface.get_rect()
    screen.blit(titleSurface, (200-(titleSurfaceRect.centerx-titleSurfaceRect.x), 0))
    # a loop which creates buttons and text on them
    for x in range(len(buttonsList)):
        button = pygame.Rect(120, 60*x + 100, 160, 40)
        dictOfButtons[buttonsList[x]] = button
        textSurface = buttonFont.render(buttonsList[x], False, colorsRGB.black)
        pygame.draw.rect(screen, colorsRGB.yellow, button)
        textSurfaceRect = textSurface.get_rect()
        screen.blit(textSurface, (199-(textSurfaceRect.centerx-textSurfaceRect.x), 60*x + 100))
    

def lvl(screen, board: boardClass, boardButtons: dict):
    pygame.display.set_icon(pygame.image.load('img\\MineIcon.png'))
    pygame.display.set_caption('Sapper')
    screen = pygame.display.set_mode((board.sizeX*50, board.sizeY*50))
    screen.fill(colorsRGB.grey1)
    for y in range(board.sizeY):
        for x in range (board.sizeX):
            button = pygame.Rect(x*50, y*50, 50, 50)
            pygame.draw.rect(screen, colorsRGB.grey2, button)
            if board.boardModel[y][x] not in boardButtons.keys():
                boardButtons[board.boardModel[y][x]] = [button]
            elif board.boardModel[y][x] in boardButtons.keys():
                boardButtons[board.boardModel[y][x]].append(button)
            
    otherFunctions.lines(screen, board)


def GameOverScreen(screen, images, boardButtons: dict(), board):
    for key in boardButtons.keys():
        if key == 'Mine':
            for button in boardButtons[key]:
                otherFunctions.rectToImg(screen, images, 'Mine', button)
        else:
            pass
    otherFunctions.lines(screen, board)
    GameOverFont = pygame.font.SysFont('Helvetica', 40)
    GameOverSurface = GameOverFont.render('GAME OVER', False, colorsRGB.pureRed)
    GameOverSurfaceRect = GameOverSurface.get_rect()
    GameOverSurfaceRect.left = board.sizeX/2*50 - (GameOverSurfaceRect.centerx-GameOverSurfaceRect.x)
    GameOverSurfaceRect.top = board.sizeY/2*50 - (GameOverSurfaceRect.centery-GameOverSurfaceRect.y)-30
    pygame.draw.rect(screen, colorsRGB.grey1, GameOverSurfaceRect)
    screen.blit(GameOverSurface, (board.sizeX/2*50 - (GameOverSurfaceRect.centerx-GameOverSurfaceRect.x), board.sizeY/2*50 - (GameOverSurfaceRect.centery-GameOverSurfaceRect.y)-30))

def VictoryScreen(screen, board, timeOfTheGame):
    VictoryFont = pygame.font.SysFont('Helvetica', 40)
    timeFont = pygame.font.SysFont('Helvetica', 20)
    
    VictorySurface = VictoryFont.render('Victory!', False, colorsRGB.pureGreen)
    VictorySurfaceRect = VictorySurface.get_rect()
    VictorySurfaceRect.left = board.sizeX/2*50 - (VictorySurfaceRect.centerx-VictorySurfaceRect.x)
    VictorySurfaceRect.top = board.sizeY/2*50 - (VictorySurfaceRect.centery-VictorySurfaceRect.y)-40
    pygame.draw.rect(screen, colorsRGB.grey1, VictorySurfaceRect)
    screen.blit(VictorySurface, (board.sizeX/2*50 - (VictorySurfaceRect.centerx-VictorySurfaceRect.x), board.sizeY/2*50 - (VictorySurfaceRect.centery-VictorySurfaceRect.y)-40))

    timeSurface = timeFont.render(str(timeOfTheGame), False, colorsRGB.pureGreen)
    timeSurfaceRect = timeSurface.get_rect()
    timeSurfaceRect.left = board.sizeX/2*50 - (timeSurfaceRect.centerx-timeSurfaceRect.x)
    timeSurfaceRect.top = board.sizeY/2*50 - (timeSurfaceRect.centery-timeSurfaceRect.y)
    pygame.draw.rect(screen, colorsRGB.grey1, timeSurfaceRect)
    screen.blit(timeSurface, (board.sizeX/2*50 - (timeSurfaceRect.centerx-timeSurfaceRect.x), board.sizeY/2*50 - (timeSurfaceRect.centery-timeSurfaceRect.y)))
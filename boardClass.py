from random import choice, randint
from pprint import pprint
class boardClass:
    def __init__(self, hardnessLevel):
        if hardnessLevel == 'beginner':
            self.minesRequired = 10
            minesRequired = self.minesRequired
            self.sizeX = 8
            self.sizeY = 8
            self.boardModel = [ [0 for _ in range(self.sizeX)] for _ in range(self.sizeY) ]
        elif hardnessLevel == 'normal':
            self.minesRequired = 40
            minesRequired = self.minesRequired
            self.sizeX = 16
            self.sizeY = 16
            self.boardModel = [ [0 for _ in range(self.sizeX)] for _ in range(self.sizeY) ]
        elif hardnessLevel == 'hard':
            self.minesRequired = 99
            minesRequired = self.minesRequired
            self.sizeX = 30
            self.sizeY = 16
            self.boardModel = [ [0 for _ in range(self.sizeX)] for _ in range(self.sizeY) ]
        elif hardnessLevel == 'impossible':
            self.minesRequired = 200
            minesRequired = self.minesRequired
            self.sizeX = 30
            self.sizeY = 24
            self.boardModel = [ [0 for _ in range(self.sizeX)] for _ in range(self.sizeY) ]

        while minesRequired > 0:
            y = randint(0, self.sizeY-1)
            x = randint(0, self.sizeX-1)
            if self.boardModel[y][x] != 'Mine':
                self.boardModel[y][x] = 'Mine'
                minesRequired -= 1

                for y2 in range(y-1, y+2):
                    for x2 in range(x-1, x+2):
                        try:
                            if self.boardModel[y2][x2] != 'Mine' and x2>=0 and y2>=0:
                                self.boardModel[y2][x2] += 1
                        except IndexError:
                            continue
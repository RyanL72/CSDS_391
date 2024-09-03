import numpy as np

class Eight_Puzzle:
    
    def __init__(self, puzzleConfiguration=[[0,1,2],[3,4,5],[6,7,8]]):
        self.__puzzleConfiguration = puzzleConfiguration
        self.__x = None
        self.__y = None
        self.updateZeroPosition()
        self.checkZero()

    def checkZero(self):
        for i, row in enumerate(self.__puzzleConfiguration):
            for j, row in enumerate(row):
                if self.__puzzleConfiguration[i][j] == 0:
                    print(f"{i} {j}")
                    return
        raise ValueError("Invalid puzzle configuration: No zero value found.")
        
    def updateZeroPosition(self):
        for i, row in enumerate(self.__puzzleConfiguration):
            for j, row in enumerate(row):
                if self.__puzzleConfiguration[i][j] == 0:
                    self.__x = i
                    self.__y = j

    def getZeroPosition(self):
        return self.__x, self.__y

    def printPuzzleConfiguration(self):
        for row in self.__puzzleConfiguration:
            print(" ".join(map(str, row)))

    def setState(self, newPuzzleConfiguration):
        self.__puzzleConfiguration = newPuzzleConfiguration
        self.checkZero()

    def printState(self):
        for row in self.__puzzleConfiguration:
            formattedRow = [" " if element == 0 else str(element) for element in row]
            print(" ".join(formattedRow))
    
    def move(self, direction):
        pass

    def getValidMoves(self):
        position = self.getZeroPosition()
        if position == (0, 0):
            return ["Right", "Down"]
        elif position == (1, 0):
            return ["Right", "Down", "Up"]
        elif position == (2, 0):
            return ["Right", "Up"]
        elif position == (0, 1):
            return ["Right", "Down", "Left"]
        elif position == (1, 1):
            return ["Right", "Down", "Left", "Up"]
        elif position == (2, 1):
            return ["Right", "Left", "Up"]
        elif position == (0, 2):
            return ["Down", "Left"]
        elif position == (1, 2):
            return ["Down", "Left", "Up"]
        elif position == (2, 2):
            return ["Left", "Up"]


if __name__ == "__main__":

    newEightPuzzle = Eight_Puzzle()

    newEightPuzzle.printState()

    print(newEightPuzzle.getValidMoves())

    print(newEightPuzzle.getZeroPosition())

    newEightPuzzle.setState([[8,7,6], [5,4,3],[2,1,0]])

    newEightPuzzle.printState()



class Eight_Puzzle:
    
    def __init__(self, puzzleConfiguration=[[0,1,2],[3,4,5],[6,7,8]]):
        self.__puzzleConfiguration = puzzleConfiguration
        self.__x = None
        self.__y = None
        self.updateZeroPosition()
        self.checkZero()


    def setState(self, newPuzzleConfiguration):
        self.checkZero()
        self.__puzzleConfiguration = newPuzzleConfiguration
        self.updateZeroPosition()
        
        

    def printState(self):
        for row in self.__puzzleConfiguration:
            formattedRow = [" " if element == 0 else str(element) for element in row]
            print(" ".join(formattedRow))
    
   
    def move(self, direction):
        validMoves = self.getValidMoves()
        print(f"The valid moves are: {validMoves}")
        for x in validMoves:
            if direction == x:
                currentX = self.__x
                currentY = self.__y

                if direction == "Right":
                    print("Moving Right")
                    swapPosition = currentX + 1
                    newState = [row[:] for row in self.__puzzleConfiguration] 
                    swapPtr = newState[currentY][swapPosition]
                    newState[currentY][swapPosition] = newState[currentY][currentX]
                    newState[currentY][currentX] = swapPtr
                    self.setState(newState)

                elif direction == "Down":
                    print("Moving Down")
                    swapPosition = currentY + 1
                    newState = [row[:] for row in self.__puzzleConfiguration] 
                    swapPtr = newState[swapPosition][currentX]
                    newState[swapPosition][currentX] = newState[currentY][currentX]
                    newState[currentY][currentX] = swapPtr
                    print(self.getZeroPosition())
                    self.setState(newState)

                elif direction == "Left":
                    print("Moving Left")
                    swapPosition = currentX - 1
                    newState = [row[:] for row in self.__puzzleConfiguration]  
                    swapPtr = newState[currentY][swapPosition]
                    newState[currentY][swapPosition] = newState[currentY][currentX]
                    newState[currentY][currentX] = swapPtr
                    self.setState(newState)

                elif direction == "Up":
                    print("Moving Up")
                    swapPosition = currentY - 1
                    newState = [row[:] for row in self.__puzzleConfiguration]  
                    swapPtr = newState[swapPosition][currentX]
                    newState[swapPosition][currentX] = newState[currentY][currentX]
                    newState[currentY][currentX] = swapPtr
                    self.setState(newState)

                    

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
        
    # Helper Functions
    def checkZero(self):
        for i, row in enumerate(self.__puzzleConfiguration):
            for j, row in enumerate(row):
                if self.__puzzleConfiguration[i][j] == 0:
                    self.__x = i
                    self.__y = j
                    return
        raise ValueError("Invalid puzzle configuration: No zero value found.")
        
    def updateZeroPosition(self):
        for i, row in enumerate(self.__puzzleConfiguration):
            for j, row in enumerate(row):
                if self.__puzzleConfiguration[i][j] == 0:
                    self.__x = i
                    self.__y = j
                    print(f"The new Zero Position is {self.getZeroPosition()}")

    def getZeroPosition(self):
        return self.__x, self.__y

    def printPuzzleConfiguration(self):
        for row in self.__puzzleConfiguration:
            print(" ".join(map(str, row)))


if __name__ == "__main__":

    newEightPuzzle = Eight_Puzzle()
    newEightPuzzle.printState()


    newEightPuzzle.setState([[8,7,6], [5,4,3],[2,1,0]])
    newEightPuzzle.printState()


    print("---------")

    newEightPuzzle.setState([[0,1,2],[3,4,5],[6,7,8]])
    newEightPuzzle.printState()

    newEightPuzzle.move("Down")
    newEightPuzzle.printState()

    newEightPuzzle.move("Left")
    newEightPuzzle.printState()





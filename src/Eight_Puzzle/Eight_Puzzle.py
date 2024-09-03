import random

class Eight_Puzzle:
    
    def __init__(self, puzzleConfiguration=[[0,1,2],[3,4,5],[6,7,8]]):
        self.__puzzleConfiguration = puzzleConfiguration
        '''
        puzzleConfiguration[y][x]

        .------------------------> (X)
        |
        |
        |
        |
        |
        |
        |
        v
        (Y)

        '''
        self.__x = None
        self.__y = None
        self.updateZeroPosition()



    def setState(self, newPuzzleConfiguration):
        self.__puzzleConfiguration = newPuzzleConfiguration
        self.updateZeroPosition()
        #print(f"Set Zero to {self.__x} {self.__y}")
        
        

    def printState(self):
        for row in self.__puzzleConfiguration:
            formattedRow = [" " if element == 0 else str(element) for element in row]
            print(" ".join(formattedRow))
    
   
    def move(self, direction):
        validMoves = self.getValidMoves()
        #print(f"The valid moves are: {validMoves}")
        #print(f"Before this move, the current zero is at {self.__x} {self.__y}")
        if direction in validMoves:
                
                currentX = self.__x
                currentY = self.__y

                if direction == "Right":
                    #print("Moving Right")
                    swapPosition = currentX + 1
                    #print(f" -the position we are swapping is swapPosition {swapPosition} right")
                    newState = [row[:] for row in self.__puzzleConfiguration] 
                    #print(f" -copy of old array: {newState}")
                    swapPtr = newState[currentY][swapPosition]
                    #print(f" -The value we need to swap into blank: {swapPtr}")
                    newState[currentY][swapPosition] = newState[currentY][currentX]
                    #print(f" -The new configuration step 1: {newState}")
                    newState[currentY][currentX] = swapPtr
                    #print(f" -The new configuration step 2: {newState}")
                    self.setState(newState)
                    return

                elif direction == "Down":
                    #print("Moving Down")
                    swapPosition = currentY + 1
                    #print(f" -the position we are swapping is swapPosition {swapPosition} down")
                    newState = [row[:] for row in self.__puzzleConfiguration] 
                    #print(f" -copy of old array: {newState}")
                    swapPtr = newState[swapPosition][currentX]
                    #print(f" -The value we need to swap into blank: {swapPtr}")
                    newState[swapPosition][currentX] = newState[currentY][currentX]
                    #print(f" -The new configuration step 1: {newState}")
                    newState[currentY][currentX] = swapPtr
                    #print(f" -The new configuration step 2: {newState}")
                    self.setState(newState)
                    return

                elif direction == "Left":
                    #print("Moving Left")
                    swapPosition = currentX - 1
                    #print(f" -the position we are swapping is swapPosition {swapPosition} left")
                    newState = [row[:] for row in self.__puzzleConfiguration]  
                    #print(f" -copy of old array: {newState}")
                    swapPtr = newState[currentY][swapPosition]
                    #print(f" -The value we need to swap into blank: {swapPtr}")
                    newState[currentY][swapPosition] = newState[currentY][currentX]
                    #print(f" -The new configuration step 1: {newState}")
                    newState[currentY][currentX] = swapPtr
                    #print(f" -The new configuration step 2: {newState}")
                    self.setState(newState)
                    return

                elif direction == "Up":
                    #print("Moving Up")
                    #print(f" -the currentY: {currentY}")
                    swapPosition = currentY - 1
                    #print(f" -the position we are swapping is swapPosition {swapPosition} up")
                    newState = [row[:] for row in self.__puzzleConfiguration]  
                    #print(f" -copy of old array: {newState}")
                    swapPtr = newState[swapPosition][currentX]
                    #print(f" -The value we need to swap into blank: {swapPtr}")
                    newState[swapPosition][currentX] = newState[currentY][currentX]
                    #print(f" -The new configuration step 1: {newState}")
                    newState[currentY][currentX] = swapPtr
                    #print(f" -The new configuration step 2: {newState}")
                    self.setState(newState)
                    return

        raise ValueError(f"The Current Position is {self.getZeroPosition()} and we can't go {direction}")
                    

    def getValidMoves(self):
        position = self.getZeroPosition()
        #print(f"Our Zero Position is {position}")
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
        
    def scrambleState(self, n):
        self.setState([[0,1,2],[3,4,5],[6,7,8]])
        count=0
        while count < n:
            self.printState()
            print("-------")
            validMoves = self.getValidMoves()
            randomValidMoveNumber = random.randint(0,len(validMoves)-1)
            randomValidMove = validMoves[randomValidMoveNumber]
            self.move(randomValidMove)
            count = count + 1
        
    # Helper Functions
        
    def updateZeroPosition(self):
        for i, row in enumerate(self.__puzzleConfiguration):
            for j, element in enumerate(row):
                if element == 0:
                    self.__x = j
                    self.__y = i
                    return
        raise ValueError("No Zero Value")

    def getZeroPosition(self):
        return self.__y, self.__x

    def printPuzzleConfiguration(self):
        for row in self.__puzzleConfiguration:
            print(" ".join(map(str, row)))


if __name__ == "__main__":

    newEightPuzzle = Eight_Puzzle()
    newEightPuzzle.printState()
    
    print("-------")

    newEightPuzzle.scrambleState(100)
    






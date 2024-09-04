import random

class EightPuzzle:
    
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
        self.checkConfiguration(newPuzzleConfiguration)
        self.__puzzleConfiguration = newPuzzleConfiguration
        self.updateZeroPosition()
        #print(f"Set Zero to {self.__x} {self.__y}")
        
        

    def printState(self):
        for row in self.__puzzleConfiguration:
            formattedRow = [" " if element == 0 else str(element) for element in row]
            print(" ".join(formattedRow))
    
   
    def move(self, direction):
        directionLowerCase=direction.lower()
        #print(directionLowerCase)
        validMoves = self.getValidMoves()
        #print(f"The valid moves are: {validMoves}")
        #print(f"Before this move, the current zero is at {self.__x} {self.__y}")
        if directionLowerCase in validMoves:
                
                currentX = self.__x
                currentY = self.__y

                if directionLowerCase == "right":
                    #print("Moving right")
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

                elif directionLowerCase == "down":
                    #print("Moving down")
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

                elif directionLowerCase == "left":
                    #print("Moving left")
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

                elif directionLowerCase == "up":
                    #print("Moving up")
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

        raise ValueError(f"The Current Position is {self.getZeroPosition()} and we can't go {directionLowerCase}")
                    

    def getValidMoves(self):
        position = self.getZeroPosition()
        #print(f"Our Zero Position is {position}")
        if position == (0, 0):
            return ["right", "down"]
        elif position == (1, 0):
            return ["right", "down", "up"]
        elif position == (2, 0):
            return ["right", "up"]
        elif position == (0, 1):
            return ["right", "down", "left"]
        elif position == (1, 1):
            return ["right", "down", "left", "up"]
        elif position == (2, 1):
            return ["right", "left", "up"]
        elif position == (0, 2):
            return ["down", "left"]
        elif position == (1, 2):
            return ["down", "left", "up"]
        elif position == (2, 2):
            return ["left", "up"]
        
    def scrambleState(self, n):
        self.setState([[0,1,2],[3,4,5],[6,7,8]])
        count=0
        while count < n:
            #print(f"count: {count}" )
            #self.printState()
            #print("--------")
            validMoves = self.getValidMoves()
            randomValidMoveNumber = random.randint(0,len(validMoves)-1)
            randomValidMove = validMoves[randomValidMoveNumber]
            self.move(randomValidMove)
            count = count + 1
        #print(f"count: {count}")
        #self.printState()

    def cmd(self, command):
        parts = command.split()
        if not parts:
            print("Error: invalid command")
            return
        
        if parts[0] == "setState":
            try:
                newState = [list(map(int, parts[1:4])), list(map(int, parts[4:7])), list(map(int, parts[7:]))]
                self.setState(newState)
            except:
                print("Error: invalid puzzle state")
        elif parts[0] == "move":
            if parts[1].lower() in ["up", "down", "left", "right"]:
                try:
                    self.move(parts[1])
                except ValueError as e:
                    print(str(e))
            else:
                print("Error: invalid direction")
        elif parts[0] == "printState":
            self.printState()
        elif parts[0] == "scrambleState":
            try:
                self.scrambleState(int(parts[1]))
            except:
                print("Error: invalid scramble number")
        else:
            print(f"Error: invalid command: {command}")
            
    def cmdfile(self, filename):
        with open(filename, 'r') as file:
            for line in file:
                command = line.strip()
                if command.startswith('#') or command.startswith('//'):
                    continue
                self.cmd(command)
        
    # Helper Functions

    def checkConfiguration(self, configuration):
        requiredValues = set(range(9))
        flattenedConfiguration = [element for row in configuration for element in row]
        flattenedConfigurationSet = set(flattenedConfiguration)
        #print(f"configuration:{flattenedConfigurationSet}   requirement:{requiredValues}")
        if(set(flattenedConfigurationSet) == requiredValues):
            pass
        else:
            raise ValueError("Invalid Puzzle Configuration")

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
    pass
    

    
    






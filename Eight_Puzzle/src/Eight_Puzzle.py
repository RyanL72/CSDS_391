class Eight_Puzzle:
    
    def __init__(self, puzzleConfiguration=[[0,1,2],[3,4,5],[6,7,8]]):
        
        self.__puzzleConfiguration = puzzleConfiguration
        
        self.__x = None
        self.__y = None

        for i, row in enumerate(puzzleConfiguration):
            for j, row in enumerate(row):
                if puzzleConfiguration[i][j] == 0:
                    self.__x = i
                    self.__y = j

        # Check if x and y value for zero were found
        if self.__x is None or self.__y is None:
            raise ValueError("Invalid puzzle configuration: No zero value found.")

    def getZeroPosition(self):
        return self.__x, self.__y

    
    def printPuzzleConfiguration(self):
        for row in self.__puzzleConfiguration:
            print(" ".join(map(str, row)))

    def setState(self, newPuzzleConfiguration):
        self.__puzzleConfiguration = newPuzzleConfiguration

    def printState(self):
        for row in self.__puzzleConfiguration:
            formattedRow = [" " if element == 0 else str(element) for element in row]
            print(" ".join(formattedRow))
    

if __name__ == "__main__":

    newEightPuzzle = Eight_Puzzle()

    newEightPuzzle.printState()
    print(newEightPuzzle.getZeroPosition())

    newEightPuzzle.setState([[8,7,6], [5,4,3],[2,1,0]])

    newEightPuzzle.printState()
    print(newEightPuzzle.getZeroPosition())


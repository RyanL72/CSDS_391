class Eight_Puzzle:
    
    def __init__(self, puzzleConfiguration):
        
        self.__puzzleConfiguration = puzzleConfiguration
    
    def printPuzzleConfiguration(self):
        
        size = int(len(self.__puzzleConfiguration) ** 0.5)
        for i in range(size):
            row = self.__puzzleConfiguration[i * size:(i + 1) * size]
            print(" ".join(map(str, row)))
    
if __name__ == "__main__":
    array = [0, 1, 2, 3, 4, 5, 6, 7, 8]
    newEightPuzzle = Eight_Puzzle(array)
    newEightPuzzle.printPuzzleConfiguration()


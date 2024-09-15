import random
from collections import deque

class EightPuzzle:
    
    def __init__(self, puzzleConfiguration=[[0,1,2],[3,4,5],[6,7,8]]):
        self.__puzzleConfiguration = puzzleConfiguration
        '''
        Assignment 1

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

    '''
    Assignment 2 
    '''

    def solveDFS(self, max_nodes=1000):
        stack = [(self.copy(), [])]  
        nodes_explored = 0
        visited = set()

        while stack:
            current_state, path = stack.pop()
            nodes_explored += 1

            # Use Set to keep track of where I already visited
            state_key = tuple(tuple(row) for row in current_state.__puzzleConfiguration)
            str_cur_state = ' '.join(str(piece) for line in current_state.__puzzleConfiguration for piece in line)
            visited.add(str_cur_state)

            if current_state.isSolved():
                print(f"Nodes created during search: {nodes_explored}")
                print(f"Solution length: {len(path)}")
                print("Move sequence:")
                for move in path:
                    print(f"move {move}")
                return path

            if nodes_explored >= max_nodes:
                print(f"Node limit {max_nodes} reached, solution not found")
                return None

            valid_moves = current_state.getValidMoves()
            for move in valid_moves:
                new_state = current_state.copy()
                new_state.move(move)
                new_state_string = ' '.join(str(piece) for line in new_state.__puzzleConfiguration for piece in line)
                if new_state_string not in visited:
                    stack.append((new_state, path + [move]))

        print("No solution found")
        return None

    
    def solveBFS(self, max_nodes=1000):
        queue = deque([(self.copy(), [])])  # Queue with the initial state and empty path
        nodes_explored = 0
        visited = set()

        # Add the initial state's string representation to the visited set
        initial_state_str = ' '.join(str(piece) for line in self.__puzzleConfiguration for piece in line)
        visited.add(initial_state_str)

        while queue:
            current_state, path = queue.popleft()  # Get the current state and path from the queue
            nodes_explored += 1

            if current_state.isSolved():
                print(f"Nodes created during search: {nodes_explored}")
                print(f"Solution length: {len(path)}")
                print("Move sequence:")
                for move in path:
                    print(f"move {move}")
                return path

            if nodes_explored >= max_nodes:
                print(f"Node limit {max_nodes} reached, solution not found")
                return None

            valid_moves = current_state.getValidMoves()
            for move in valid_moves:
                new_state = current_state.copy()  # Create a copy of the current state
                new_state.move(move)  # Apply the move to the new state

                # Convert the new state to a string for the visited set
                new_state_str = ' '.join(str(piece) for line in new_state.__puzzleConfiguration for piece in line)

                # Check if this new state has been visited before
                if new_state_str not in visited:
                    visited.add(new_state_str)  
                    queue.append((new_state, path + [move]))

        print("No solution found")
        return None

    # Assignment 3
    
    def heuristicNumMismatch(self):
        solvedArray = [[0,1,2], [3,4,5],[6,7,8]]
        wrongCount = 0

        for i in range(len(self.__puzzleConfiguration)):
            for j in range(len(self.__puzzleConfiguration[i])):
                if self.__puzzleConfiguration[j][i] == 0:
                        continue
                if solvedArray[j][i] != self.__puzzleConfiguration[j][i]:
                    wrongCount+=1
        return wrongCount 
    
    def heuristicManhattan(self):
        # Figure out where it needs to go
        # calculate the distance
        manhattanTotal = 0
        for i in range(len(self.__puzzleConfiguration)):
            for j in range(len(self.__puzzleConfiguration[i])):
                value = self.__puzzleConfiguration[j][i]
                if value == 0:
                    continue
                goalPosition = self.goalPosition(value)
                xDeviation = abs(i - goalPosition[1])
                yDeviation = abs(j - goalPosition[0])
                manhattanTotal += xDeviation + yDeviation
        return manhattanTotal

    def goalPosition(self, number):
        if number == 0:
            return (0,0)
        elif number == 1:
            return (0,1)
        elif number == 2:
            return (0,2)
        elif number == 3:
            return (1,0)
        elif number == 4:
            return (1,1)
        elif number == 5:
            return (1,2)
        elif number == 6:
            return (2,0)
        elif number == 7:
            return (2,1)
        elif number == 8:
            return (2,2)
        else:
            raise ValueError(f"{number} is not a number 0 - 8")
        


    def cmd(self, command):

        command = command.strip()
        if not command or command.startswith('#') or command.startswith('//'):
            return  
        
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
        elif parts[0] == "solveDFS":
            max_nodes = int(parts[1]) if len(parts) > 1 else 1000  
            self.solveDFS(max_nodes=max_nodes)
        elif parts[0] == "solveBFS":
            max_nodes = int(parts[1]) if len(parts) > 1 else 1000  
            self.solveBFS(max_nodes=max_nodes)
        elif parts[0] == "heuristics":
            if parts[1] == "h1":
                print(self.heuristicNumMismatch())
            elif parts[1] == "h2":
                printvalue = self.heuristicManhattan()
                print(printvalue)
        else:
            print(f"Error: invalid command: {command}")
            
    def cmdfile(self, filename):
        with open(filename, 'r') as file:
            for line in file:
                command = line.strip()
                
                # Print the command to the terminal
                if command.startswith('#') or command.startswith('//'):
                    # If it's a comment, print it as a comment
                    print(f"Comment: {command}")
                elif command:  # Non-empty line (not a comment)
                    print(f"Running command: {command}")
                    self.cmd(command)  # Execute the command
                else:
                    # Skip empty lines but optionally you can print this
                    print("Skipping empty line")
                    command = line.strip()
                
        
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

    def isSolved(self):
        if self.__puzzleConfiguration == [[0,1,2], [3,4,5],[6,7,8]]:
            return True
        else:
            return False
    
    def copy(self):
        return EightPuzzle([row[:] for row in self.__puzzleConfiguration])


if __name__ == "__main__":
    # Create a new puzzle instance
    puzzle1 = EightPuzzle()
    puzzle2 = EightPuzzle()

    # Scramble the puzzle 
    scramble_moves = 20
    print(f"Scrambling the puzzle with {scramble_moves} random moves...")
    puzzle1.scrambleState(scramble_moves)
    puzzle2.scrambleState(scramble_moves)

    # Print the scrambled state
    print("Scrambled Puzzle State:")
    puzzle1.printState()
    print("------------")

    puzzle2.printState()
    print("------------")

    # Solve the puzzle using DFS
    print("\nSolving the puzzle using DFS with max nodes = 1000...")
    puzzle1.solveDFS(max_nodes=1000)
    print("------------")

    # Solve the puzzle using BFS
    print("\nSolving the puzzle using BFS with max nodes = 1000...")
    puzzle2.solveBFS(max_nodes=1000)
    
    

    
    






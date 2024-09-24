import random
from collections import deque
import heapq
import math

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
       
        self.__stateTracking = False
        self.__stateHistory = set()



    def setState(self, newPuzzleConfiguration):
        self.checkConfiguration(newPuzzleConfiguration)
        self.__puzzleConfiguration = newPuzzleConfiguration
        self.updateZeroPosition()
        
        

    def printState(self):
        for row in self.__puzzleConfiguration:
            formattedRow = [" " if element == 0 else str(element) for element in row]
            print(" ".join(formattedRow))
    
    # Store the current state in state history before moving
    def move(self, direction):
        if self.__stateTracking == True:
            self.updateHistory()

        directionLowerCase=direction.lower()
        validMoves = self.getValidMoves()
        if directionLowerCase in validMoves:
                
                currentX = self.__x
                currentY = self.__y

                if directionLowerCase == "right":
                    swapPosition = currentX + 1
                    newState = [row[:] for row in self.__puzzleConfiguration] 
                    swapPtr = newState[currentY][swapPosition]
                    newState[currentY][swapPosition] = newState[currentY][currentX]
                    newState[currentY][currentX] = swapPtr
                    self.setState(newState)
                    return

                elif directionLowerCase == "down":
                    swapPosition = currentY + 1
                    newState = [row[:] for row in self.__puzzleConfiguration] 
                    swapPtr = newState[swapPosition][currentX]
                    newState[swapPosition][currentX] = newState[currentY][currentX]
                    newState[currentY][currentX] = swapPtr
                    self.setState(newState)
                    return

                elif directionLowerCase == "left":
                    swapPosition = currentX - 1
                    newState = [row[:] for row in self.__puzzleConfiguration]  
                    swapPtr = newState[currentY][swapPosition]
                    newState[currentY][swapPosition] = newState[currentY][currentX]
                    newState[currentY][currentX] = swapPtr
                    self.setState(newState)
                    return

                elif directionLowerCase == "up":
                    swapPosition = currentY - 1
                    newState = [row[:] for row in self.__puzzleConfiguration]  
                    swapPtr = newState[swapPosition][currentX]
                    newState[swapPosition][currentX] = newState[currentY][currentX]
                    newState[currentY][currentX] = swapPtr
                    self.setState(newState)
                    return

        raise ValueError(f"The Current Position is {self.getZeroPosition()} and we can't go {directionLowerCase}")
                    

    def getValidMoves(self):
        position = self.getZeroPosition()
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
            validMoves = self.getValidMoves()
            randomValidMoveNumber = random.randint(0,len(validMoves)-1)
            randomValidMove = validMoves[randomValidMoveNumber]
            self.move(randomValidMove)
            count = count + 1

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
            str_cur_state = ' '.join(str(piece) for line in current_state.__puzzleConfiguration for piece in line)
            visited.add(str_cur_state)

            if current_state.isSolved():
                print(f"Nodes created during search: {nodes_explored}")
                print(f"Solution length: {len(path)}")
                print("Move sequence:")
                for move in path:
                    print(f"move {move}")
                print(f"Effective Branching Factor: {self.findEffectiveBranchingFactor(nodes_explored, len(path))}")
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
                print(f"Effective Branching Factor: {self.findEffectiveBranchingFactor(nodes_explored, len(path))}")
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

    def stopStateTracking(self):
        self.__stateTracking = False

    def startStateTracking(self):
        self.__stateTracking = True
        
    def updateHistory(self):
        if(self.__stateTracking == False):
            raise ValueError("State Tracking is off")
        else:
            self.__stateHistory.add(self.hashConfiguration(self.__puzzleConfiguration))
            return
        
    def hashConfiguration(self, configuration):
        str_configuration = ' '.join(str(piece) for line in configuration for piece in line)
        return str_configuration

    def isUnexploredState(self) -> bool:
        if self.hashConfiguration(self.__puzzleConfiguration) in self.__stateHistory:
            return False
        else:
            return True    
        
    def printStateHistory(self):
        print(self.__stateHistory)

    def solveAStar(self, heuristic="manhattan", max_nodes=1000):
        
        start_state = self.copy()
        g_score = 0  # Initial cost (number of moves so far)

        # Choose the heuristic function based on the parameter
        if heuristic == "h2":
            h_score = start_state.heuristicManhattan()
        elif heuristic == "h1":
            h_score = start_state.heuristicNumMismatch()
        else:
            raise ValueError(f"Invalid heuristic: {heuristic}. Choose 'h1' or 'h2'.")

        f_score = g_score + h_score
        
        # Priority queue for A* (min-heap), stores (f, g, path, state)
        pq = [(f_score, g_score, [], start_state)]
        
        # Visited set to track explored states
        visited = set()
        
        # Convert the initial state into a hashable string representation
        initial_state_str = start_state.hashConfiguration(start_state.__puzzleConfiguration)
        visited.add(initial_state_str)
        
        nodes_explored = 0
        
        while pq and nodes_explored < max_nodes:
            # Pop the state with the lowest f_score (f = g + h)
            f, g, path, current_state = heapq.heappop(pq)
            nodes_explored += 1
            
            # Check if the current state is the goal (solved state)
            if current_state.isSolved():
                print(f"Solution found after exploring {nodes_explored} nodes")
                print(f"Solution path length: {len(path)}")
                print("Path:", path)
                print(f"Effective Branching Factor: {self.findEffectiveBranchingFactor(nodes_explored, len(path))}")
                return path
            
            # Explore all the valid moves from the current state
            for move in current_state.getValidMoves():
                new_state = current_state.copy()
                new_state.move(move)
                
                new_state_str = new_state.hashConfiguration(new_state.__puzzleConfiguration)
                
                # If the new state has not been visited, explore it
                if new_state_str not in visited:
                    new_g = g + 1  # find the g_score (cost) for the move

                    # Compute h_score based on the selected heuristic
                    if heuristic == "h2":
                        new_h = new_state.heuristicManhattan()
                    elif heuristic == "h1":
                        new_h = new_state.heuristicNumMismatch()

                    new_f = new_g + new_h  
                    
                    # Add the new state to the priority queue (only compare f and g)
                    heapq.heappush(pq, (new_f, new_g, path + [move], new_state))
                    
                    # Mark the new state as visited
                    visited.add(new_state_str)
        
        print(f"No solution found after exploring {nodes_explored} nodes.")
        return None
    
    def findEffectiveBranchingFactor(self, nodes_generated, depth, tolerance=1e-6):

        if depth == 0:
            return 0  #Base case

        # Start with an initial guess for b, we assume all nodes are distributed evenly
        b_star = (nodes_generated / depth) ** (1 / depth)

        for _ in range(depth - 1):
            # Calculate the number of nodes at the current level 
            current_level_nodes = b_star

            # Subtract the number of nodes from the total nodes remaining
            nodes_generated -= current_level_nodes

            # Recalculate b* using the remaining nodes and depth
            if nodes_generated > 0:
                b_star = (nodes_generated / (depth - 1)) ** (1 / (depth - 1))
        
        return b_star
       
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
        elif parts[0] == "solve":
            if parts[1] == "A*":
                if parts[2] == "h1":
                    max_nodes = int(parts[3]) if len(parts) > 3 else 1000
                    self.solveAStar("h1", max_nodes)
                elif parts[2] == "h2":
                    max_nodes = int(parts[3]) if len(parts) > 3 else 1000
                    self.solveAStar("h2", max_nodes)
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
                    # Skip empty lines 
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
    
class EightPuzzleTest:
    def testBranchingFactor(self, known_b_star, depth):
        """
        Test the `findEffectiveBranchingFactor` function with a tree that has
        a known branching factor and depth.
        """
        # Calculate the total number of nodes analytically using geometric series
        nodes_generated = self.calculateTotalNodes(known_b_star, depth)

        # Use the findEffectiveBranchingFactor function to estimate b*
        estimated_b_star = EightPuzzle().findEffectiveBranchingFactor(nodes_generated, depth)
        
        print(f"Known b*: {known_b_star}, Estimated b*: {estimated_b_star}, Nodes: {nodes_generated}")
        
    def calculateTotalNodes(self, b_star, depth):
        """
        Calculate the total number of nodes in a tree with branching factor `b_star` and depth `depth`
        using the geometric series formula.
        """
        if b_star == 1:
            return depth + 1  # Special case when b* = 1, it is a straight line tree
        
        return int((b_star**(depth + 1) - 1) / (b_star - 1))

def main():
    puzzle_test = EightPuzzleTest()

    # Test the algorithm with known values for branching factor and depth
    print("Running test cases for effective branching factor estimation...\n")
    
    puzzle_test.testBranchingFactor(2, 5)  # Known branching factor b* = 2, depth = 5
    puzzle_test.testBranchingFactor(3, 4)  # Known branching factor b* = 3, depth = 4
    puzzle_test.testBranchingFactor(4, 6)  # Known branching factor b* = 4, depth = 6
    puzzle_test.testBranchingFactor(2, 3)  # Known branching factor b* = 2, depth = 3

    print("\nTests completed.")

if __name__ == "__main__":
    main()
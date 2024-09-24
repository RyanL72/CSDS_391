import random
from collections import deque
import heapq
import math

class EightPuzzle:
    """ Implementation of an Eight Puzzle with built-in self solving solutions. """
    
    def __init__(self, puzzleConfiguration=[[0,1,2],[3,4,5],[6,7,8]]):
        """Initialize the puzzle with a given configuration."""
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
        """Set the puzzle to a new configuration."""
        self.checkConfiguration(newPuzzleConfiguration)
        self.__puzzleConfiguration = newPuzzleConfiguration
        self.updateZeroPosition()
        
    def printState(self):
        """Print the current puzzle state in a human-readable format."""
        for row in self.__puzzleConfiguration:
            formattedRow = [" " if element == 0 else str(element) for element in row]
            print(" ".join(formattedRow))

    def move(self, direction):
        """Move the empty tile (0) in the given direction if valid."""
        if self.__stateTracking == True:
            self.updateHistory()
        directionLowerCase = direction.lower()
        validMoves = self.getValidMoves()
        if directionLowerCase in validMoves:
            currentX = self.__x
            currentY = self.__y
            newState = [row[:] for row in self.__puzzleConfiguration] 
            if directionLowerCase == "right":
                swapPosition = currentX + 1
            elif directionLowerCase == "down":
                swapPosition = currentY + 1
            elif directionLowerCase == "left":
                swapPosition = currentX - 1
            elif directionLowerCase == "up":
                swapPosition = currentY - 1
            newState[currentY if directionLowerCase in ["left", "right"] else swapPosition]\
                [currentX if directionLowerCase in ["up", "down"] else swapPosition] =\
                newState[currentY][currentX]
            newState[currentY][currentX] = newState[currentY if directionLowerCase in ["left", "right"] else swapPosition]\
                [currentX if directionLowerCase in ["up", "down"] else swapPosition]
            self.setState(newState)
            return
        raise ValueError(f"Can't move {directionLowerCase}")

    def getValidMoves(self):
        """Return the list of valid moves based on the empty tile's position."""
        position = self.getZeroPosition()
        return {
            (0, 0): ["right", "down"],
            (1, 0): ["right", "down", "up"],
            (2, 0): ["right", "up"],
            (0, 1): ["right", "down", "left"],
            (1, 1): ["right", "down", "left", "up"],
            (2, 1): ["right", "left", "up"],
            (0, 2): ["down", "left"],
            (1, 2): ["down", "left", "up"],
            (2, 2): ["left", "up"],
        }[position]
        
    def scrambleState(self, n):
        """Scramble the puzzle state with n random valid moves."""
        self.setState([[0,1,2],[3,4,5],[6,7,8]])
        count = 0
        while count < n:
            validMoves = self.getValidMoves()
            randomValidMove = random.choice(validMoves)
            self.move(randomValidMove)
            count += 1

    def solveDFS(self, max_nodes=1000):
        """Solve the puzzle using Depth-First Search (DFS)."""
        stack = [(self.copy(), [])]
        nodes_explored = 0
        visited = set()
        while stack:
            current_state, path = stack.pop()
            nodes_explored += 1
            visited.add(self.hashConfiguration(current_state.__puzzleConfiguration))
            if current_state.isSolved():
                print("DFS results:")
                print(f"Nodes created during search: {nodes_explored}")
                print(f"Solution length: {len(path)}")
                # print("Move sequence:")
                # for move in path:
                #     print(f"move {move}")
                print(f"Effective Branching Factor: {self.findEffectiveBranchingFactor(nodes_explored, len(path))}")
                return path
            if nodes_explored >= max_nodes:
                return None
            for move in current_state.getValidMoves():
                new_state = current_state.copy()
                new_state.move(move)
                if self.hashConfiguration(new_state.__puzzleConfiguration) not in visited:
                    stack.append((new_state, path + [move]))
        return None

    def solveBFS(self, max_nodes=1000):
        """Solve the puzzle using Breadth-First Search (BFS)."""
        queue = deque([(self.copy(), [])])
        nodes_explored = 0
        visited = {self.hashConfiguration(self.__puzzleConfiguration)}
        while queue:
            current_state, path = queue.popleft()
            nodes_explored += 1
            if current_state.isSolved():
                print("BFS results:")
                print(f"Nodes created during search: {nodes_explored}")
                print(f"Solution length: {len(path)}")
                # print("Move sequence:")
                # for move in path:
                #     print(f"move {move}")
                print(f"Effective Branching Factor: {self.findEffectiveBranchingFactor(nodes_explored, len(path))}")
                return path
            if nodes_explored >= max_nodes:
                return None
            for move in current_state.getValidMoves():
                new_state = current_state.copy()
                new_state.move(move)
                if self.hashConfiguration(new_state.__puzzleConfiguration) not in visited:
                    visited.add(self.hashConfiguration(new_state.__puzzleConfiguration))
                    queue.append((new_state, path + [move]))
        return None

    def heuristicNumMismatch(self):
        """Calculate the heuristic based on the number of misplaced tiles."""
        solvedArray = [[0,1,2], [3,4,5],[6,7,8]]
        wrongCount = 0
        for i in range(len(self.__puzzleConfiguration)):
            for j in range(len(self.__puzzleConfiguration[i])):
                if self.__puzzleConfiguration[j][i] != 0 and \
                   self.__puzzleConfiguration[j][i] != solvedArray[j][i]:
                    wrongCount += 1
        return wrongCount

    def heuristicManhattan(self):
        """Calculate the heuristic based on the Manhattan distance of tiles."""
        manhattanTotal = 0
        for i in range(len(self.__puzzleConfiguration)):
            for j in range(len(self.__puzzleConfiguration[i])):
                value = self.__puzzleConfiguration[j][i]
                if value == 0:
                    continue
                goalPosition = self.goalPosition(value)
                manhattanTotal += abs(i - goalPosition[1]) + abs(j - goalPosition[0])
        return manhattanTotal

    def goalPosition(self, number):
        """Return the goal position of a given number in the puzzle."""
        return {
            0: (0,0), 1: (0,1), 2: (0,2),
            3: (1,0), 4: (1,1), 5: (1,2),
            6: (2,0), 7: (2,1), 8: (2,2),
        }[number]

    def stopStateTracking(self):
        """Stop tracking puzzle states."""
        self.__stateTracking = False

    def startStateTracking(self):
        """Start tracking puzzle states."""
        self.__stateTracking = True

    def updateHistory(self):
        """Update the history of visited states."""
        if self.__stateTracking:
            self.__stateHistory.add(self.hashConfiguration(self.__puzzleConfiguration))

    def hashConfiguration(self, configuration):
        """Hash the puzzle configuration for state tracking."""
        return ' '.join(str(piece) for row in configuration for piece in row)

    def isUnexploredState(self):
        """Check if the current state has been visited."""
        return self.hashConfiguration(self.__puzzleConfiguration) not in self.__stateHistory

    def solveAStar(self, heuristic="manhattan", max_nodes=1000):
        """Solve the puzzle using A* search with a specified heuristic."""
        start_state = self.copy()
        g_score = 0
        h_score = start_state.heuristicManhattan() if heuristic == "h2" else start_state.heuristicNumMismatch()
        pq = [(g_score + h_score, g_score, [], start_state)]
        visited = {start_state.hashConfiguration(start_state.__puzzleConfiguration)}
        nodes_explored = 0
        while pq and nodes_explored < max_nodes:
            f, g, path, current_state = heapq.heappop(pq)
            nodes_explored += 1
            if current_state.isSolved():
                print(f"Astar {heuristic} results:")
                print(f"Solution found after exploring {nodes_explored} nodes")
                print(f"Solution path length: {len(path)}")
                # print("Path:", path)
                print(f"Effective Branching Factor: {self.findEffectiveBranchingFactor(nodes_explored, len(path))}")
                return path
            for move in current_state.getValidMoves():
                new_state = current_state.copy()
                new_state.move(move)
                new_state_str = new_state.hashConfiguration(new_state.__puzzleConfiguration)
                if new_state_str not in visited:
                    new_g = g + 1
                    new_h = new_state.heuristicManhattan() if heuristic == "h2" else new_state.heuristicNumMismatch()
                    heapq.heappush(pq, (new_g + new_h, new_g, path + [move], new_state))
                    visited.add(new_state_str)
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
        """Execute a command string for puzzle operations."""
        command = command.strip()
        if not command or command.startswith('#') or command.startswith('//'):
            return  
        parts = command.split()
        if not parts:
            return
        if parts[0] == "setState":
            self.setState([list(map(int, parts[1:4])), list(map(int, parts[4:7])), list(map(int, parts[7:]))])
        elif parts[0] == "move":
            self.move(parts[1])
        elif parts[0] == "printState":
            self.printState()
        elif parts[0] == "scrambleState":
            self.scrambleState(int(parts[1]))
        elif parts[0] == "solveDFS":
            self.solveDFS(int(parts[1]) if len(parts) > 1 else 1000)
        elif parts[0] == "solveBFS":
            self.solveBFS(int(parts[1]) if len(parts) > 1 else 1000)
        elif parts[0] == "heuristics":
            if parts[1] == "h1":
                print(self.heuristicNumMismatch())
            elif parts[1] == "h2":
                print(self.heuristicManhattan())
        elif parts[0] == "solve" and parts[1] == "A*":
            self.solveAStar(parts[2], int(parts[3]) if len(parts) > 3 else 1000)

    def cmdfile(self, filename):
        """Execute commands from a file."""
        with open(filename, 'r') as file:
            for line in file:
                command = line.strip()
                if command:
                    self.cmd(command)

    def checkConfiguration(self, configuration):
        """Check if the puzzle configuration contains all required numbers."""
        requiredValues = set(range(9))
        flattenedConfiguration = {element for row in configuration for element in row}
        if flattenedConfiguration != requiredValues:
            raise ValueError("Invalid Puzzle Configuration")

    def updateZeroPosition(self):
        """Update the position of the empty tile (0) in the current configuration."""
        for i, row in enumerate(self.__puzzleConfiguration):
            for j, element in row:
                if element == 0:
                    self.__x = j
                    self.__y = i
                    return
        raise ValueError("No Zero Value")

    def getZeroPosition(self):
        """Return the position of the empty tile (0)."""
        return self.__y, self.__x

    def printPuzzleConfiguration(self):
        """Print the puzzle configuration."""
        for row in self.__puzzleConfiguration:
            print(" ".join(map(str, row)))

    def isSolved(self):
        """Check if the puzzle is in the solved state."""
        return self.__puzzleConfiguration == [[0,1,2], [3,4,5],[6,7,8]]
    
    def copy(self):
        """Create and return a copy of the current puzzle configuration."""
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

# sliding_puzzle

# Initialize global variables
side_length = 3
blank = "0"
up = "U"
down = "D"
left = "L"
right = "R"

# Stores grid as two-dimensional array
def storeInitialPuzzle():
    numberSequence = input().split()
    commandSequence = input().split()
    initialPuzzle = []

    for i in range(len(numberSequence)):
        if i == 0 or i == 3 or i == 6:
            initialPuzzle.append(numberSequence[i:i+3])

    return initialPuzzle, commandSequence

# Checks if indicies are in bounds for sliding puzzle
def inBounds(i, j):
    inBoundsIndicies = [0, 1, 2]
    if i not in inBoundsIndicies or j not in inBoundsIndicies:
        return False
    return True

# Applies given command sequence to given puzzle state
def applyCommands(puzzle, commandSequence):
    for command in commandSequence:
        movedAlready = False
        for i in range(side_length):
            for j in range(side_length):
                isBlank = puzzle[i][j] == blank
                if isBlank and inBounds(i, j + 1) and command == right and movedAlready == False:
                    puzzle[i][j] = puzzle[i][j + 1]
                    puzzle[i][j + 1] = blank
                    movedAlready = True
                elif isBlank and inBounds(i, j - 1) and command == left and movedAlready == False:
                    puzzle[i][j] = puzzle[i][j - 1]
                    puzzle[i][j - 1] = blank
                    movedAlready = True
                elif isBlank and inBounds(i - 1, j) and command == up and movedAlready == False:
                    puzzle[i][j] = puzzle[i - 1][j]
                    puzzle[i - 1][j] = blank
                    movedAlready = True
                elif isBlank and inBounds(i + 1, j) and command == down and movedAlready == False:
                    puzzle[i][j] = puzzle[i + 1][j]
                    puzzle[i + 1][j] = blank
                    movedAlready = True

    return puzzle

# If given puzzle state is solved return True otherwise return False
def solved(state):
    goalState = [["1", "2", "3"], ["4", "5", "6"], ["7", "8", "0"]]
    if state != goalState:
        return False
    return True

# Put it all together and print results
initialPuzzle, commandSequence = storeInitialPuzzle()
finalPuzzle = applyCommands(initialPuzzle, commandSequence)
if solved(finalPuzzle):
    print("Solution is good!")
else:
    print("Wrong solution!")

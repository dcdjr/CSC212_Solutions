# game_of_life

# Initialize global variables
alive = "*"
dead = "."
border = "#"

# Stores grid as two-dimensional array
def storeGrid():
    numRows, numCols, numGens = input().split()
    numRows = int(numRows)
    numCols = int(numCols)
    numGens = int(numGens)

    initialState = []

    for _ in range(numRows):
        row = input().split()
        initialState.append(row)
    
    return initialState, numRows, numCols, numGens

# Extends grid to ensure no index errors when evaluating number of neighbors for each cell
def extendGrid(state, numRows, numCols):
    emptyList = []
    for i in range(numCols + 2):
        emptyList.append(border)

    state.append(emptyList.copy())
    state.insert(0, emptyList.copy())

    for i in range(1, len(state) - 1):
        state[i].append(border)
        state[i].insert(0, border)
        
    return state, numRows + 2, numCols + 2

# Strips grid of outer layer to print grid
def stripGrid(state):
    state = state[1:-1]

    for i in range(len(state)):
        state[i] = state[i][1:-1]

    return state

# Prints grid
def printGrid(state):
    for i in range(len(state)):
        for j in range(len(state[i])):
            cell = state[i][j]

            if j == len(state[i]) - 1:
                print(cell)
            else:
                print(cell, end=" ")

# Gets the number of live neighbors for the current cell
def numNeighbors(state, i, j):
    cell = state[i][j]
    numLiveNeighbors = 0

    for h in range(i - 1, i + 2):
        for k in range(j - 1, j + 2):
            neighbor = state[h][k]
            
            if neighbor == alive: 
                numLiveNeighbors += 1

    if cell == alive:
        return numLiveNeighbors - 1
    elif cell == dead:
        return numLiveNeighbors

# Copies a given grid so as to not mutate the original
def copyGrid(numRows, numCols):
    gridCopy = []

    for _ in range(numRows - 2):
        row = []
        for _ in range(numCols - 2):
            row.append(border)
        gridCopy.append(row)

    return gridCopy

# Computes the next generation of a given state
def computeNextGeneration(state, numRows, numCols):
    gridCopy = copyGrid(numRows, numCols)
    for i in range(1, numRows - 1):
        for j in range(1, numCols - 1):
            cell = state[i][j]
            numLiveNeighbors = numNeighbors(state, i, j)
            
            if numLiveNeighbors < 2 and cell == alive:
                gridCopy[i - 1][j - 1] = dead
            elif numLiveNeighbors > 3 and cell == alive:
                gridCopy[i - 1][j - 1] = dead
            elif (numLiveNeighbors == 2 or numLiveNeighbors == 3) and cell == alive:
                gridCopy[i - 1][j - 1] = alive
            elif numLiveNeighbors == 3 and cell == dead:
                gridCopy[i - 1][j - 1] = alive
            else:
                gridCopy[i - 1][j - 1] = cell

    extendedGridCopy, _, _ = extendGrid(gridCopy, numRows - 2, numCols - 2)

    return extendedGridCopy

# Repeatedly computes next n generations of a given state
def computeNGenerations(initialState, numRows, numCols, n):
    nextState = initialState
    for _ in range(n):
        nextState = computeNextGeneration(nextState, numRows, numCols)
    
    return nextState

# Put it all together and print results
initialState, numRows, numCols, n = storeGrid()
initialStateExt, numRowsExt, numColsExt = extendGrid(initialState, numRows, numCols)
finalState = computeNGenerations(initialStateExt, numRowsExt, numColsExt, n)
strippedGrid = stripGrid(finalState)
printGrid(strippedGrid)
# game_of_life

# Stores grid as two-dimensional array
def storeGrid():
    parameters = input().split()
    numRows = int(parameters[0])
    numCols = int(parameters[1])
    numGens = int(parameters[2])

    initialState = []
    for i in range(numRows):
        row = input().split()
        initialState.append(row)
        
    return initialState, numRows, numCols, numGens

# Extends grid to ensure no index errors when evaluating number of neighbors for each cell
def extendGrid(state, numRows, numCols):
    emptyList1 = []
    for i in range(numCols + 2):
        emptyList1.append("#")

    state.insert(len(state), emptyList1)
    state.insert(0, emptyList1)


    for i in range(1, len(state)):
        state[i].insert(numCols, "#")
        state[i].insert(0, "#")

    numRows += 2
    numCols += 2
        
    return state, numRows, numCols

def stripGrid(state, numRows, numCols):


    del state[numRows - 1]
    del state[0]

    for i in range(numRows - 2):
        del state[i][numCols - 1]
        del state[i][0]

    return state

def printGrid(state):
    for i in range(len(state)):
        for j in range(len(state[i])):
            if j == len(state[i]) - 1:
                print(state[i][j])
            else:
                print(state[i][j], end=" ")
    


# Gets the number of live neighbors for the current cell
def numNeighbors(state, i, j):
    alive = state[i][j] == "*"
    dead = state[i][j] == "."


    numLiveNeighbors = 0
    for h in range(i - 1, i + 2):
        for k in range(j - 1, j + 2):
            if state[h][k] == "*": 
                numLiveNeighbors += 1

    if alive:
        return numLiveNeighbors - 1
    if dead:
        return numLiveNeighbors

def copyGrid(numRows, numCols):
    gridCopy = []
    for i in range(numRows - 2):
        row = []
        for j in range(numCols - 2):
            row.append("#")
        gridCopy.append(row)
        row = []

    return gridCopy

def computeNextGeneration(state, numRows, numCols):
    gridCopy = copyGrid(numRows, numCols)
    for i in range(1, numRows - 1):
        for j in range(1, numCols - 1):
            alive = state[i][j] == "*"
            dead = state[i][j] == "."
            numLiveNeighbors = numNeighbors(state, i, j)
            if numLiveNeighbors < 2 and alive:
                gridCopy[i - 1][j - 1] = "."
            elif numLiveNeighbors > 3 and alive:
                gridCopy[i - 1][j - 1] = "."
            elif (numLiveNeighbors == 2 or numLiveNeighbors == 3) and alive:
                gridCopy[i - 1][j - 1] = "*"
            elif numLiveNeighbors == 3 and dead:
                gridCopy[i - 1][j - 1] = "*"
            else:
                gridCopy[i - 1][j - 1] = state[i][j]

    extendedGridCopy, n, r = extendGrid(gridCopy, numRows - 2, numCols - 2)
    return extendedGridCopy

def computeNGenerations(initialState, numRows, numCols, numGens):
    nextState = initialState
    for i in range(numGens):
        nextState = computeNextGeneration(nextState, numRows, numCols)
    
    return nextState

initialState, numRows, numCols, numGens = storeGrid()
initialState, numRows, numCols = extendGrid(initialState, numRows, numCols)
grid = computeNGenerations(initialState, numRows, numCols, numGens)
strippedGrid = stripGrid(grid, numRows, numCols)
printGrid(strippedGrid)
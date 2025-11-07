# sudoku_checker c++

# Reads and stored puzzle as 2D array
def readAndStorePuzzle():
    storedPuzzle = []

    for _ in range(9):
        row = input().split()
        storedPuzzle.append(row)
        
    return storedPuzzle

# Checks the columns to ensure they don't have duplicate digits
def checkCols(storedPuzzle):
    length = len(storedPuzzle[0])
    seen = []
    for i in range(length):
        seen = []
        for j in range(length):
            if storedPuzzle[j][i] in seen:
                return False
            else:
                seen.append(storedPuzzle[j][i])
    return True

# Checks the rows to ensure they don't have duplicate digits
def checkRows(storedPuzzle):
    length = len(storedPuzzle[0])
    seen = []
    for i in range(length):
        seen = []
        for j in range(length):
            if storedPuzzle[i][j] in seen:
                return False
            else:
                seen.append(storedPuzzle[i][j])
    return True

# Checks the 9 boxes to ensure they don't have duplicate digits
def checkBoxes(storedPuzzle):
    length = len(storedPuzzle[0])
    for i in range(1, length, 3):
        for j in range(1, length, 3):
            seen = []
            for h in range(i - 1, i + 2):
                for k in range(j - 1, j + 2):
                    if storedPuzzle[h][k] in seen:
                        return False
                    else:
                        seen.append(storedPuzzle[h][k])
    return True

# Put it all together and print results
storedPuzzle = readAndStorePuzzle()
if checkCols(storedPuzzle) and checkRows(storedPuzzle) and checkBoxes(storedPuzzle):
    print("Solution is good!")
else:
    print("Wrong solution!")
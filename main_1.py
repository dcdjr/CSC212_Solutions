# sudoku_checker

def readAndStorePuzzle():
    storedPuzzle = []

    for i in range(9):
        row = input().split()
        storedPuzzle.append(row)
        
    return storedPuzzle

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

storedPuzzle = readAndStorePuzzle()
if checkCols(storedPuzzle) and checkRows(storedPuzzle) and checkBoxes(storedPuzzle):
    print("Solution is good!")
else:
    print("Wrong solution!")
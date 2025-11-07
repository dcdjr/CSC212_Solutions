# k_nearest_neighbors

# Read and store input
def readAndStoreInput():
    numPrecPoints, numNearestNeighbors = input().split()
    numPrecPoints = int(numPrecPoints)
    numNearestNeighbors = int(numNearestNeighbors)

    precPoints = []
    
    for _ in range(numPrecPoints):
        precPoints.append(input().split())

    classPoint = input().split()

    return numNearestNeighbors, precPoints, classPoint

# Calculate distances of nearest k neighbors and return a list with that point's distance and its classification
def calcDistancesOfNearestKNeighbors(k, precPoints, classPoint):
    distancesOfAllNeighbors = []
    x2 = float(classPoint[0])
    y2 = float(classPoint[1])

    for point in precPoints:
        x1 = float(point[0])
        y1 = float(point[1])
        classification = point[2]
        distance = ((y2 - y1) ** 2 + (x2 - x1) ** 2) ** 0.5
        distancesOfAllNeighbors.append([distance] + [classification])

    distancesOfAllNeighbors.sort()
    distancesOfNearestKNeighbors = distancesOfAllNeighbors[0:k]

    return distancesOfNearestKNeighbors

# Determine classification of point in interest
def calcClassification(distancesOfNearestKNeighbors):
    numR = 0
    numB = 0
    for neighbor in distancesOfNearestKNeighbors:
        if "R" in neighbor:
            numR += 1
        elif "B" in neighbor:
            numB += 1

    if numR > numB:
        return "R"
    return "B"

# Put it all together and print results
k, precPoints, classPoint = readAndStoreInput()
distancesOfNearestKNeighbors = calcDistancesOfNearestKNeighbors(k, precPoints, classPoint)
print(calcClassification(distancesOfNearestKNeighbors))



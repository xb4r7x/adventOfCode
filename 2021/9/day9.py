with open("test.txt", "r") as f:
    input = f.read().strip().split("\n")
    inputList = [list(map(int, list(row))) for row in input]

def main():
    global lowPoints
    lowPoints = []
    print("The solution for part 1 is: {0}".format(part1Solution(inputList)))
    print("The solution for part 2 is: {0}".format(part2Solution(inputList)))

def part1Solution(inputList):
    risk = []
    for i in range(len(inputList)):
        for j in range(len(inputList[0])):
            neighbors = getNeighbors(inputList, i, j)
            if inputList[i][j] < min(neighbors):
                risk.append(inputList[i][j] + 1)
                coords = (i,j)
                lowPoints.append(coords)
    return sum(risk)

def part2Solution(inputList):
    for point in lowPoints:
        print(getBasin(inputList,point))
    return 2

def getBasin(inputList,startPoint):
    sRow = startPoint[0]
    sCol = startPoint[1]
    basinSet = {startPoint}
    startLength = len(basinSet)
    while True:
        
        right = inputList[sRow][sCol+1]
        left = inputList[sRow][sCol-1]
        up = inputList[sRow-1][sCol]
        down = inputList[sRow+1][sCol]
        #Check to the right
        if inputList[sRow][sCol+1] < 9:
            basinSet.add() 
        #Check to the left

        #Check up

        #Check down

        if len(basinSet) == startLength:
            print("length is the same")
            break
        startLength = len(basinSet)
    return 0



#Make this return the position of the lowpoints 
def getNeighbors(inputList, rowIdx, numIdx):
    neighbors = []
    if rowIdx > 0:
        neighbors.append(inputList[rowIdx - 1][numIdx])
    if rowIdx < len(inputList) - 1:
        neighbors.append(inputList[rowIdx + 1][numIdx])
    if numIdx > 0:
        neighbors.append(inputList[rowIdx][numIdx - 1])
    if numIdx < len(inputList[0]) - 1:
        neighbors.append(inputList[rowIdx][numIdx + 1])
    return neighbors

if __name__ == "__main__":
    main()

with open('input.txt') as f:
    lines = [line.rstrip() for line in f]

# There's a shitload of copy/pasta in here... I was going to refactor it and make it pretty, but it was like 2am. Don't judge me.

def main():
    print("The solution for part 1 is: {0}".format(part1Solution(lines)))
    print("The solution for part 2 is: {0}".format(part2Solution(lines)))

def checkHeight(trees, rowIdx, colIdx):
    testTree=trees[rowIdx][colIdx]

    testUp = []
    for row in range(rowIdx):
        testUp.append(trees[row][colIdx])

    testDown = []
    for row in range(rowIdx+1,len(trees)):
        testDown.append(trees[row][colIdx])

    testLeft = []
    for col in range(0,colIdx):
        testLeft.append(trees[rowIdx][col])
        
    testRight = []
    for col in range(colIdx+1,len(trees[rowIdx])):
        testRight.append(trees[rowIdx][col])
    
    if testTree > max(testUp) or testTree > max(testDown) or testTree > max(testLeft) or testTree > max(testRight):
        return True
    return False

def calculateScore(trees, rowIdx, colIdx):
    testTree=trees[rowIdx][colIdx]

    testUp = []
    for row in range(rowIdx):
        testUp.append(trees[row][colIdx])

    testDown = []
    for row in range(rowIdx+1,len(trees)):
        testDown.append(trees[row][colIdx])

    testLeft = []
    for col in range(0,colIdx):
        testLeft.append(trees[rowIdx][col])
        
    testRight = []
    for col in range(colIdx+1,len(trees[rowIdx])):
        testRight.append(trees[rowIdx][col])

    #upDistance
    upDistance = 0
    for uptree in reversed(testUp):
        if testTree <= uptree:
            upDistance += 1
            break
        else:
            upDistance += 1

    downDistance = 0
    for downtree in testDown:
        if testTree <= downtree:
            downDistance+= 1
            break
        else:
            downDistance+= 1

    leftDistance = 0
    for lefttree in reversed(testLeft):
        if testTree <= lefttree:
            leftDistance += 1
            break
        else:
            leftDistance += 1

    rightDistance = 0
    for righttree in testRight:
        if testTree <= righttree:
            rightDistance += 1
            break
        else:
            rightDistance += 1

    return upDistance*leftDistance*rightDistance*downDistance

def part1Solution(lines):
    trees = []
    viscount = 0
    for line in lines:
        trees.append([*line])

    #Count all outside trees
    viscount = int((len(trees)-2)*2) + int(len(trees[0]) + int(len(trees[-1])))

    for i, row in enumerate(trees):
        if i == 0 or i == len(trees)-1:
            continue
        for x, tree in enumerate(row):
            if x == 0 or x == len(row)-1:
                continue
            if checkHeight(trees,i,x):
                viscount += 1
    return viscount

def part2Solution(lines):
    trees = []
    scenicScores = []
    for line in lines:
        trees.append([*line])

    for i, row in enumerate(trees):
        for x, tree in enumerate(row):
            scenicScores.append(calculateScore(trees,i,x))
            
    return max(scenicScores)

if __name__ == "__main__":
    main()

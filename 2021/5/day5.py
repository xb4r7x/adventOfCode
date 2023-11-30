import re
from bresenham import bresenham

with open('input.txt') as f:
    lines = [str(line.strip()) for line in f]

def main():
    global pointsDict
    pointsDict = {}
    print("The solution for part 1 is: {0}".format(part1Solution(lines)))
    pointsDict = {}
    print("The solution for part 2 is: {0}".format(part2Solution(lines)))

def part1Solution(lines):
    straightLines = scrubDiag(splitLines(lines))
    for coords in straightLines:
        x1, y1, x2, y2 = coords
        points = list(bresenham(int(x1), int(y1), int(x2), int(y2)))
        for point in points:
            countPoints(point[0],point[1])
    count = 0
    for point in pointsDict:
        if pointsDict[point] > 1:
            count+=1
    return count

def part2Solution(lines):
    allLines = splitLines(lines)
    for coords in allLines:
        x1, y1, x2, y2 = coords
        points = list(bresenham(int(x1), int(y1), int(x2), int(y2)))
        for point in points:
            countPoints(point[0],point[1])
    count = 0
    for point in pointsDict:
        if pointsDict[point] > 1:
            count+=1
    return count


def countPoints(x, y):
    if (x,y) not in pointsDict:
        pointsDict[(x,y)] = 1
    else:
        pointsDict[(x,y)] += 1

def scrubDiag(inputList):
    straightList = []
    for i in inputList:
        if i[0] == i[2] or i[1] == i[3]:
            straightList.append(i)
    return straightList

def splitLines(lines):
    splitList = []
    for line in lines:
        split = re.split(',|\s->\s', line)
        splitList.append(split)
    return splitList

if __name__ == "__main__":
    main()

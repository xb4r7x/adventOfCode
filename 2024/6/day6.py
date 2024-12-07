from aocd import get_data, submit
from itertools import cycle

useExample=True
submitA=False
submitB=False

if useExample == False:
    lines = get_data(day=6, year=2024).splitlines()
else:
    with open('ex_input.txt') as f:
        lines = [line.rstrip() for line in f]

def main():
    print("The solution for part 1 is: {0}".format(part1Solution(lines)))
    if submitA == True:
        print("Submitting solution A to AoC:")
        submit(part1Solution(lines), part="a", day=6, year=2024)
    print("The solution for part 2 is: {0}".format(part2Solution(lines)))
    if submitB == True:
        print("Submitting solution B to AoC:")
        submit(part2Solution(lines), part="b", day=6, year=2024)

def findGuardPos(grid, char="^"):
    for irow, row in enumerate(grid):
        for icol, pos in enumerate(row):
            if pos == char:
                return irow, icol
    return None

def moveGuardPos(grid, dir, nextDir, visitedLocs, char="^"):
    guardPos = findGuardPos(grid)
    newPos = (guardPos[0] + dir[0], guardPos[1] + dir[1])
    rightPos = (newPos[0] + nextDir[0], newPos[1] + nextDir[1])
    obsPos = False
    if grid[newPos[0]][newPos[1]] == "#":
        return grid, None, True, None
    
    if newPos in visitedLocs and rightPos in visitedLocs:
        print("Obstacle position found.")
        for line in grid:
            print(line)
        obsPos = True
        
    # print("The guard's current position is: " + str(guardPos))
    # print("We're moving like this: " + str(dir))
    
    moved = False
    for irow, row in enumerate(grid):
        for icol, pos in enumerate(row):
            if pos == char:
                if irow > 0:
                    # print(str(irow), str(icol) + "banana")
                    # print(irow + dir[0], icol + dir[1])
                    grid[irow][icol], grid[irow + dir[0]][icol + dir[1]] = grid[irow + dir[0]][icol + dir[1]], grid[irow][icol]
                    moved = True
            if moved:
                break
        if moved:
            break       
    
    newPos = findGuardPos(grid)
    # print("The guard's new position is: " + str(newPos))
    return grid, newPos, False, obsPos

def part1Solution(lines):
    grid = [list(line) for line in lines]
    startPos = findGuardPos(grid)
    visitedLocs = set()    
    visitedLocs.add(startPos)

    dirs = [
        (-1, 0), # up
        (0, 1), # right
        (1, 0), # down
        (0, -1), # left
    ]

    numObsPos = 0
    offGrid = False
    exceptionsCt=0
    while not offGrid:
        for i, dir in enumerate(dirs):
            nextDir = dirs[(i + 1) % len(dirs)]
            obstruction = False
            while True:
                try:
                    newGrid, newPos, obstruction, obsPos = moveGuardPos(grid, dir, nextDir, visitedLocs)
                    if obstruction:
                        break
                    if obsPos:
                        numObsPos+=1
                    visitedLocs.add(newPos)
                except(IndexError):
                    print("OOB OOB OOB")
                    exceptionsCt+=1
                    offGrid = True
                    break
            if offGrid:
                break

    print(exceptionsCt)
    print(grid)
    print(numObsPos)
    return len(visitedLocs)

def part2Solution(lines):
    # Ideas...
    # For every move, check if the destination is in the existing set of visited places.
    # Also check the position to the right of the direction of travel (the next index in the dirs)
    # If both spots are in the list, then the spot directly in front of the current spot (in the current direction of travel)
    # is the
    return 2

if __name__ == "__main__":
    main()

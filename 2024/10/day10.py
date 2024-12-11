from aocd import get_data, submit

useExample=True
submitA=False
submitB=False

if useExample == False:
    lines = get_data(day=10, year=2024).splitlines()
else:
    with open('ex_input.txt') as f:
        lines = [line.rstrip() for line in f]

def main():
    print("The solution for part 1 is: {0}".format(part1Solution(lines)))
    if submitA == True:
        print("Submitting solution A to AoC:")
        submit(part1Solution(lines), part="a", day=10, year=2024)
    print("The solution for part 2 is: {0}".format(part2Solution(lines)))
    if submitB == True:
        print("Submitting solution B to AoC:")
        submit(part2Solution(lines), part="b", day=10, year=2024)

def findStarts(grid):
    startList = []
    for i, _ in enumerate(grid):
        for y, _ in enumerate(grid[i]):
            if grid[i][y] == 0:
                startList.append((i,y))
    return startList

def getScore(grid, startPos, endVal=9):
    dirs = [
        (-1, 0), # up
        (1, 0), # down
        (0, -1), # left
        (0, 1), # right
    ]

    startVal = grid[startPos[0]][startPos[1]]
    
    print(startVal)
    
    return 0

def part1Solution(lines):
    grid = [list(map(int, line)) for line in lines]
    startList = findStarts(grid)
    for start in startList:
        getScore(grid, start)
    
    return 1

def part2Solution(lines):
    
    return 2

if __name__ == "__main__":
    main()

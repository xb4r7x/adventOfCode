from aocd import get_data, submit
from collections import defaultdict

useExample=True
submitA=False
submitB=False

if useExample == False:
    lines = get_data(day=12, year=2024).splitlines()
else:
    with open('ex_input.txt') as f:
        lines = [line.rstrip() for line in f]

def main():
    print("The solution for part 1 is: {0}".format(part1Solution(lines)))
    if submitA == True:
        print("Submitting solution A to AoC:")
        submit(part1Solution(lines), part="a", day=12, year=2024)
    print("The solution for part 2 is: {0}".format(part2Solution(lines)))
    if submitB == True:
        print("Submitting solution B to AoC:")
        submit(part2Solution(lines), part="b", day=12, year=2024)

def part1Solution(lines):
    grid = [list(map(str, line)) for line in lines]
    dirs = [
        (-1, 0), # up
        (0, 1), # right
        (1, 0), # down
        (0, -1), # left
    ]
    
    farmData = defaultdict(list)
    lastChar = ''
    curChar = ''
    area = 0
    perim = 0
    for i, row in enumerate(grid):
        for y, col in enumerate(row):
            curChar = grid[i][y]
            for ro, co in dirs:
                if grid[ro][co] == curChar:
                    area += 1
                else:
                    perim += 1
                
                    
                    # Need to flood fill check for letters, add to defaultdict which will use the letters for a key
                    # And the a list of tuples containing the areas and perimeters of each instance of that letter.

            

    return 1

def part2Solution(lines):
    
    return 2

if __name__ == "__main__":
    main()

from aocd import get_data, submit

useExample=False
submitA=False
submitB=True

if useExample == False:
    lines = get_data(day=4, year=2024).splitlines()
else:
    with open('ex_input.txt') as f:
        lines = [line.rstrip() for line in f]

def main():
    print("The solution for part 1 is: {0}".format(part1Solution(lines)))
    if submitA == True:
        print("Submitting solution A to AoC:")
        submit(part1Solution(lines), part="a", day=4, year=2024)
    print("The solution for part 2 is: {0}".format(part2Solution(lines)))
    if submitB == True:
        print("Submitting solution B to AoC:")
        submit(part2Solution(lines), part="b", day=4, year=2024)

def part1Solution(lines):
    total = 0
    searchString = "XMAS"
    searchStringLen = len(searchString)
    grid = [list(line) for line in lines]
    rowidx, colidx = len(grid), len(grid[0])

    dirs = [
        (-1, 0), # up
        (1, 0), # down
        (0, -1), # left
        (0, 1), # right
        (-1, -1), # up left
        (-1, 1), # up right
        (1, -1), # down left
        (1, 1)  # down right
    ]

    for row in range(rowidx):
        for col in range(colidx):
            for rowoff, coloff in dirs:
                if (0 <= row + (searchStringLen - 1) * rowoff < rowidx) and (0 <= col + (searchStringLen - 1) * coloff < colidx):
                    try:
                        rangeString = ""
                        rangeChars = []
                        for i in range(searchStringLen):
                            rangeChars.append(grid[row + i * rowoff][col + i * coloff])
                        
                        rangeString = ''.join(rangeChars)

                        if rangeString == searchString:
                            #print(f"Found '{rangeString}' at ({row}, {col}) in direction {rowoff},{coloff}")
                            total+=1
                    except IndexError:
                        pass
    return total

def part2Solution(lines):
    total = 0
    searchString = "MAS"
    searchStringLen = len(searchString)
    grid = [list(line) for line in lines]
    rowidx, colidx = len(grid), len(grid[0])

    dirs = [
        (-1, -1), # up left
        (-1, 1), # up right
        (1, -1), # down left
        (1, 1)  # down right
    ]

    centerPositions = []
    for row in range(rowidx):
        for col in range(colidx):
            for rowoff, coloff in dirs:
                if (0 <= row + (searchStringLen - 1) * rowoff < rowidx) and (0 <= col + (searchStringLen - 1) * coloff < colidx):
                    try:
                        rangeString = ""
                        rangeChars = []
                        centerPos = ()
                        for i in range(searchStringLen):
                            rangeChars.append(grid[row + i * rowoff][col + i * coloff])
                            if i == 1:
                                centerPos=((row + i * rowoff),(col + i * coloff))
                        
                        rangeString = ''.join(rangeChars)

                        if rangeString == searchString:
                            centerPositions.append(centerPos)

                    except IndexError:
                        pass
    
    count = {}
    for pos in centerPositions:
        if pos in count:
            count[pos] += 1
        else:
            count[pos] = 1
    
    print(count)
    return sum(1 for n in count.values() if n == 2)

if __name__ == "__main__":
    main()

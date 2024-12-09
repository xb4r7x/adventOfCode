from aocd import get_data, submit

useExample=False
submitA=True
submitB=False

if useExample == False:
    lines = get_data(day=9, year=2024).splitlines()
else:
    with open('ex_input.txt') as f:
        lines = [line.rstrip() for line in f]

def main():
    print("The solution for part 1 is: {0}".format(part1Solution(lines)))
    if submitA == True:
        print("Submitting solution A to AoC:")
        submit(part1Solution(lines), part="a", day=9, year=2024)
    print("The solution for part 2 is: {0}".format(part2Solution(lines)))
    if submitB == True:
        print("Submitting solution B to AoC:")
        submit(part2Solution(lines), part="b", day=9, year=2024)

def calcBlockList(line):
    blockList = []
    id = 0
    for i in range(0, len(line),2):
        pair = line[i:i+2]
        if len(pair) == 2:
            file, space = pair
        else:
            file = pair
        for x in range(int(file)):
            blockList.append(id)
        for y in range(int(space)):
            blockList.append(".")
        id+=1
    return blockList

def getLists(line):
    lineList = list(map(int, line))
    blockList = []
    spaceList = []
    id=0
    block = True
    for char in lineList:
        if block:
            for num in range(char):
                blockList.append(id)
            id+=1
        else:
            for num in range(char):
                idx = len(blockList)
                spaceList.append(idx)
                blockList.append(".")
        block = not block

    return blockList, spaceList

def part1Solution(lines):
    for line in lines: 
        blockList, freeSpace = getLists(line)

        for space in freeSpace:
            if space > len(blockList) - 1:
                break
            num = blockList.pop()
            blockList[space] = num
            while blockList[-1] == ".":
                blockList.pop()

        total = 0
        for i, num in enumerate(blockList):
            total += i * int(num)
    return total

# 6310675819476

def part2Solution(lines):
    
    return 2

if __name__ == "__main__":
    main()

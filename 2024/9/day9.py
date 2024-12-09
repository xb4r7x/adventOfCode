from aocd import get_data, submit
from itertools import groupby

useExample=False
submitA=False
submitB=True

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

def getLists(line):
    lineList = list(map(int, line))
    blockList = []
    spaceList = []
    id=0
    block = True
    for char in lineList:
        if block:
            for _ in range(char):
                blockList.append(id)
            id+=1
        else:
            for _ in range(char):
                idx = len(blockList)
                spaceList.append(idx)
                blockList.append(".")
        block = not block
    return blockList, spaceList

def getSpaces(blocklist):
    spaceSizes = []
    blockSizes = []
    idx = 0
    for key, group in groupby(blocklist):
        listGroup = list(group)
        length = len(listGroup)
        if key == '.':
            spaceSizes.append((idx, length))
        else:
            blockSizes.append((idx, length))
        idx+=length
    return spaceSizes, blockSizes

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



def part2Solution(lines):
    for line in lines:
        blockList, _ = getLists(line)
        spaceSizes, blockSizes = getSpaces(blockList)
        for bsize in reversed(blockSizes):
            for ssize in spaceSizes:
                if ssize[1] >= bsize[1] and ssize[0] < bsize[0]:
                    blockList[ssize[0]:ssize[0] + bsize[1]], blockList[bsize[0]:bsize[0] + bsize[1]] = blockList[bsize[0]:bsize[0] + bsize[1]], blockList[ssize[0]:ssize[0] + bsize[1]]
                    spaceSizes, _ = getSpaces(blockList)
                    break
                else:
                    continue
        total = 0
        for i, num in enumerate(blockList):
            if str(num).isdigit():
                total += i * int(num)
    return total

if __name__ == "__main__":
    main()

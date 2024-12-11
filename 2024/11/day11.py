from aocd import get_data, submit
from collections import defaultdict

useExample=False
submitA=False
submitB=True

if useExample == False:
    lines = get_data(day=11, year=2024).splitlines()
else:
    with open('ex_input.txt') as f:
        lines = [line.rstrip() for line in f]

def main():
    print("The solution for part 1 is: {0}".format(part1Solution(lines)))
    if submitA == True:
        print("Submitting solution A to AoC:")
        submit(part1Solution(lines), part="a", day=11, year=2024)
    print("The solution for part 2 is: {0}".format(part2Solution(lines)))
    if submitB == True:
        print("Submitting solution B to AoC:")
        submit(part2Solution(lines), part="b", day=11, year=2024)

def splitNum(num):
    strNum = str(num)
    mid = len(strNum) // 2
    left = int(strNum[:mid])
    right = int(strNum[mid:])
    return left, right

def ruleTransform(num):
    if num == 0:
        return [1]
    elif len(str(num)) % 2 == 0:
        listParts = []
        left, right = splitNum(num)
        listParts.append(left)
        listParts.append(right)
        return listParts
    else:
        return [num * 2024]

def part1Solution(lines):
    for line in lines:
        nums = list(map(int, line.split()))
        for _ in range(6):
            newList = []
            for num in nums:
                newList = newList + ruleTransform(num)
            nums = newList[:]
    return len(nums)

def part2Solution(lines):
    # Thanks for the hint, Tim!
    for line in lines:
        nums = list(map(int, line.split()))
        numDict = {num: 1 for num in nums}

        for _ in range(75):
            newDict = defaultdict(int)
            for num,y in numDict.items():
                if num == 0:
                    newDict[1] += y
                elif len(str(num)) % 2 == 0:
                    left, right = splitNum(num)
                    newDict[left] += y
                    newDict[right] += y
                else:
                    newDict[num * 2024] = y
            numDict = newDict
        print(numDict)
    return sum(numDict.values())

if __name__ == "__main__":
    main()

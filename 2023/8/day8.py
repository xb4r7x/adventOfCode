from aocd import get_data, submit
from math import lcm
import regex as re

useExample=False
submitA=False
submitB=True

if useExample == False:
    lines = get_data(day=8, year=2023).splitlines()
else:
    with open('ex_input.txt') as f:
        lines = [line.rstrip() for line in f]

def main():
    print("The solution for part 1 is: {0}".format(part1Solution(lines)))
    if submitA == True:
        print("Submitting solution A to AoC:")
        submit(part1Solution(lines), part="a", day=8, year=2023)
    print("The solution for part 2 is: {0}".format(part2Solution(lines)))
    if submitB == True:
        print("Submitting solution B to AoC:")
        submit(part2Solution(lines), part="b", day=8, year=2023)

def dictify(lines):
    movesDict={}
    for line in lines[2:]:
        pos, left, right = re.findall(r'\b[A-Za-z]+\b', line)
        movesDict[pos]=(left,right)
    return movesDict

def part1Solution(lines):
    instruction=lines[0]
    movesDict=dictify(lines)
    zReached=False
    
    steps=1
    while zReached==False:
        if steps == 1:
            nextElement="AAA"
        for direction in instruction:
            if direction == "L": idx=0
            elif direction == "R": idx=1
            nextElement=movesDict[nextElement][idx]
            if nextElement == "ZZZ":
                zReached=True    
            else:
                steps+=1
    return steps

def part2Solution(lines):
    instruction = lines[0]
    movesDict = dictify(lines)

    startingElements = [keys for keys in movesDict.keys() if keys[-1] == "A"]

    stepList = []
    for element in startingElements:
        steps=1
        zReached=False
        while zReached==False:
            if steps == 1:
                nextElement=element
            for direction in instruction:
                if direction == "L": idx=0
                elif direction == "R": idx=1
                nextElement=movesDict[nextElement][idx]
                if nextElement.endswith('Z'):
                    zReached=True
                else:
                    steps+=1
        stepList.append(steps)
    return lcm(*stepList)

if __name__ == "__main__":
    main()

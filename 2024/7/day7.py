from aocd import get_data, submit
from itertools import product
from functools import reduce

useExample=False
submitA=False
submitB=True

if useExample == False:
    lines = get_data(day=7, year=2024).splitlines()
else:
    with open('ex_input.txt') as f:
        lines = [line.rstrip() for line in f]

def main():
    print("The solution for part 1 is: {0}".format(part1Solution(lines)))
    if submitA == True:
        print("Submitting solution A to AoC:")
        submit(part1Solution(lines), part="a", day=7, year=2024)
    print("The solution for part 2 is: {0}".format(part2Solution(lines)))
    if submitB == True:
        print("Submitting solution B to AoC:")
        submit(part2Solution(lines), part="b", day=7, year=2024)


## I kind cheated on this one... I was struggling to figure out how to approach it,
## and I didn't want to spend my entire friday night goofing around, so I checked reddit for some hints
## Gave me the idea and rough outline for the reduce/lambda math.
## Got the answer faster than I should have, but I learned things, so I count it as a win.

def part1Solution(lines):
    total = 0
    for line in lines:
        answer, numbers = int(line.split(":")[0]), list(map(int, line.split(":")[1].strip().split()))

        repeats = len(numbers) - 1 
        
        for oper in product("*+", repeat=repeats):
            op = iter(oper)
            doMath = reduce(lambda a,b: a+b if next(op) == '+' else a*b, numbers)
            if doMath == answer:
                total = total + doMath
                break
    return total

def doThings(a, b, op):
    if op == "+":
        return a+b
    if op == "*":
        return a*b
    if op == "|":
        return int(str(a)+str(b))
    return None

def part2Solution(lines):
    total = 0
    for line in lines:
        answer, numbers = int(line.split(":")[0]), list(map(int, line.split(":")[1].strip().split()))

        repeats = len(numbers) - 1

        for oper in product("*+|", repeat=repeats):
            op = iter(oper)
            doMath = reduce(lambda a, b: doThings(a, b, next(op)) ,numbers)        
            if doMath == answer:
                total = total + doMath
                break
    return total

if __name__ == "__main__":
    main()

from aocd import get_data, submit
import regex as re

useExample=False
submitA=False
submitB=False

if useExample == False:
    lines = get_data(day=3, year=2024).splitlines()
else:
    with open('ex_input.txt') as f:
        lines = [line.rstrip() for line in f]

def main():
    print("The solution for part 1 is: {0}".format(part1Solution(lines)))
    if submitA == True:
        print("Submitting solution A to AoC:")
        submit(part1Solution(lines), part="a", day=3, year=2024)
    print("The solution for part 2 is: {0}".format(part2Solution(lines)))
    if submitB == True:
        print("Submitting solution B to AoC:")
        submit(part2Solution(lines), part="b", day=3, year=2024)

def multiply(string):
    pattern = r"mul\((\d+),(\d+)\)"
    matches = re.findall(pattern, string)
    products = [int(a) * int(b) for a, b in matches]
    return sum(products)

def part1Solution(lines):
    total = 0
    for line in lines:
        total = total + multiply(line)
    return total

def part2Solution(lines):
    total = 0
    stringLines = ''.join(lines)
    firstDont = r"^.*?(?=don't\(\))"
    firstSection = re.findall(firstDont, stringLines)
    total = total + multiply(firstSection[0])
        
    doDont = r"do\(\)(.*?)don't\(\)"
    doSections = re.findall(doDont, stringLines)

    for section in doSections: 
        total = total + multiply(section)
    return total

if __name__ == "__main__":
    main()

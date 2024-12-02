from aocd import get_data, submit

useExample=False
submitA=False
submitB=True

if useExample == False:
    lines = get_data(day=2, year=2024).splitlines()
else:
    with open('ex_input.txt') as f:
        lines = [line.rstrip() for line in f]

def main():
    print("The solution for part 1 is: {0}".format(part1Solution(lines)))
    if submitA == True:
        print("Submitting solution A to AoC:")
        submit(part1Solution(lines), part="a", day=2, year=2024)
    print("The solution for part 2 is: {0}".format(part2Solution(lines)))
    if submitB == True:
        print("Submitting solution B to AoC:")
        submit(part2Solution(lines), part="b", day=2, year=2024)

def safeReports(lineList):
    decreasing = all(1 <= int(j) - int(i) <= 3 for i, j in zip(lineList, lineList[1:]))
    increasing = all(1 <= int(i) - int(j) <= 3 for i, j in zip(lineList, lineList[1:]))
    return decreasing or increasing

def part1Solution(lines):
    safe = 0
     
    for line in lines:
        lineList=line.split()
        
        decreasing = all(1 <= int(j) - int(i) <= 3 for i, j in zip(lineList, lineList[1:]))
        increasing = all(1 <= int(i) - int(j) <= 3 for i, j in zip(lineList, lineList[1:]))
       
        if decreasing or increasing:
            safe += 1

    return safe

def part2Solution(lines):
    safe = 0
    for line in lines:
        lineList=line.split()
        if safeReports(lineList):
            safe += 1
            continue

        for i in range(len(lineList)):
            newList = lineList[:i] + lineList[i+1:]
            if safeReports(newList):
                safe += 1
                break
    return safe

if __name__ == "__main__":
    main()

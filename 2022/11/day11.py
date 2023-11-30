import math

with open('ex_input.txt') as f:
    lines = [line.rstrip() for line in f]

def main():
    print("The solution for part 1 is: {0}".format(part1Solution(lines)))
    print("The solution for part 2 is: {0}".format(part2Solution(lines)))

def processInput(lines, lnum):
    for i in range(6):
        lineStart = lines[lnum+i].split()
        if lineStart[0] == "Starting":
            #print("Starting Items {}:".format(lineStart[2:]))
            startingItems = []
            for item in lineStart[2:]:
                item = item.replace(',','')
                startingItems.append(int(item))
        elif lineStart[0] == "Operation:":
            #print("Operation is {}".format(lineStart))
            if lineStart[5].isdigit():
                lineStart[5] = int(lineStart[5])
            operation = [lineStart[4], lineStart[5]]
        elif lineStart[0] == "Test:":
            #print("Test is {}".format(lineStart))
            divisibleBy = int(lineStart[3])
        elif lineStart[0] == "If":
            #print("If is {}".format(lineStart[1]))
            if lineStart[1] == "true:":
                trueMove = int(lineStart[5])
            if lineStart[1] == "false:":
                falseMove = int(lineStart[5])
        activityCount = 0
    return startingItems, operation, divisibleBy, trueMove, falseMove, activityCount

def processMonkeyMoves(monkeys):
    for x, monk in enumerate(monkeys):
        print(monkeys)
        print("MONKEY {}".format(x))
        ###I made a tactical error here... this entire logic doesn't take into account the fact that the lenth of the list is constantly changing... 
        ###Going to revisit in the morning, but perhaps a thing where we pop the element from the list immiediately, perform the maths on it, and then put it where it goes... and just do that until the list is empty?
        ###Regardless... as good as all of the below is, it doesn't work. 
        for idx in range(len(monk[0])):
            if len(monk[0]) > 0:
                currentWorryLevel = monk[0].pop(0)
                if monk[1][0] == "*":
                    if monk[1][1] == "old":
                        monk[1][1] = currentWorryLevel
                    currentWorryLevel *= monk[1][1]
                    currentWorryLevel /= 3
                    currentWorryLevel = math.floor(currentWorryLevel)
                elif monk [1][0] == "+":
                    if monk[1][1] == "old":
                        monk[1][1] = currentWorryLevel
                    currentWorryLevel += monk[1][1]
                    currentWorryLevel /= 3
                    currentWorryLevel = math.floor(currentWorryLevel)
                if currentWorryLevel % monk[2] == 0:
                    print("Evaluated TRUE. Popping {} from {} and inserting into {}".format(currentWorryLevel, x, monkeys[monk[3]][0]))
                    monkeys[monk[3]][0].insert(len(monkeys[monk[3]][0]),currentWorryLevel)
                    print(currentWorryLevel)
                    print(monkeys[monk[3]][0])
                else:
                    print("Evaluated FALSE. Popping {} from {} and inserting into {}".format(currentWorryLevel, x, monkeys[monk[4]][0]))
                    monkeys[monk[4]][0].insert(len(monkeys[monk[4]][0]),currentWorryLevel)
                    print(currentWorryLevel)
                    print(monkeys[monk[4]][0])

            monk[5] += 1
    return

def part1Solution(lines):
    monkeys = []
    for idx, line in enumerate(lines):
        if line and line[0] == "M":
            monkey = []
            monkey.extend(processInput(lines, idx))
            monkeys.append(monkey)
    for round in range(20):
        print("ROUND {}".format(round))
        processMonkeyMoves(monkeys)
    print(monkeys)
    return monkeys

def part2Solution(lines):
    
    return 2

if __name__ == "__main__":
    main()

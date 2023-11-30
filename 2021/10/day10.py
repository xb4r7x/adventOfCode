with open('test.txt') as f:
    lines = f.readlines()

openList = ["[","{","(","<"]
closedList = ["]","}",")",">"]

def main():
    print("The solution for part 1 is: {0}".format(part1Solution(lines)))
    print("The solution for part 2 is: {0}".format(part2Solution(lines)))

def part1Solution(lines):
    scores = []
    for line in lines:
        score = getScore(line)
        if score > 0:
            scores.append(score)
    return sum(scores)

def part2Solution(lines):
    for line in lines:
        score = getCompletionScore(line)
        print(score)
    return 2

def getScore(line):
    stack = []
    points = 0
    for i in line:
        if i in openList:
            stack.append(i)
        elif i in closedList:
            pos = closedList.index(i)
            if ((len(stack) > 0) and (openList[pos] == stack[len(stack)-1])):
                stack.pop()
            else:
                if i == ")":
                    points = 3
                elif i == "]":
                    points = 57
                elif i == "}":
                    points = 1197
                elif i == ">":
                    points = 25137
                break
    return points


def getCompletionScore(line):
    stack = []
    points = 0
    for i in line:
        if i in openList:
            stack.append(i)
        elif i in closedList:
            pos = closedList.index(i)
            if ((len(stack) > 0) and (openList[pos] == stack[len(stack)-1])):
                #stack.pop()
                num = openList.index(stack[len(stack)-1])
                expected = closedList[num]
                print(expected)
            else:
                if i == ")":
                    points = 3
                elif i == "]":
                    points = 57
                elif i == "}":
                    points = 1197
                elif i == ">":
                    points = 25137
                break
    return points


if __name__ == "__main__":
    main()

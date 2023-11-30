with open('input.txt') as f:
    lines = [line.rstrip() for line in f]

def main():
    print("The solution for part 1 is: {0}".format(part1Solution(lines)))
    print("The solution for part 2 is: {0}".format(part2Solution(lines)))

def getScore1(_split):
    if _split[0] == "A":
        if _split[1] == "X":
            score = 4
        if _split[1] == "Y":
            score = 8
        if _split[1] == "Z":
            score = 3
    if _split[0] == "B": 
        if _split[1] == "X":
            score = 1
        if _split[1] == "Y":
            score = 5
        if _split[1] == "Z":
            score = 9
    if _split[0] == "C":
        if _split[1] == "X":
            score = 7
        if _split[1] == "Y":
            score = 2
        if _split[1] == "Z":
            score = 6
    return score

def getScore2(_split):
    if _split[1] == "X":
        if _split[0] == "A":
            score = 3
        if _split[0] == "B":
            score = 1
        if _split[0] == "C":
            score = 2
    if _split[1] == "Y": 
        if _split[0] == "A":
            score = 4
        if _split[0] == "B":
            score = 5
        if _split[0] == "C":
            score = 6
    if _split[1] == "Z":
        if _split[0] == "A":
            score = 8
        if _split[0] == "B":
            score = 9
        if _split[0] == "C":
            score = 7
    return score

def part1Solution(lines):
    outcome = []
    for line in lines: 
        split = line.split()
        outcome.append(getScore1(split))
    return sum(outcome)

def part2Solution(lines):
    outcome = []
    for line in lines: 
        split = line.split()
        outcome.append(getScore2(split))
    return sum(outcome)


if __name__ == "__main__":
    main()
from collections import Counter

with open('input.txt') as f:
        lines = f.read()

def main():
    print("The solution for part 1 is: {0}".format(part1Solution(lines)))
    print("The solution for part 2 is: {0}".format(part2Solution(lines)))

def part1Solution(lines):
    inputList = splitLines(lines)
    count = []
    for line in inputList:
        output = line[1].split(" ")
        for word in output:
            length = len(word)
            count.append(length)
    counter = Counter(count)
    count = [counter[2],counter[4],counter[3],counter[7]]
    return sum(count)

def part2Solution(lines):
    inputList = splitLines(lines)
    count = []
    for line in inputList:
        output = line[1].split(" ")
        for word in output:
            chars = list(word)
            print(chars)

    return 2

def splitLines(input):
    res = []
    for line in input.split('\n'):
        out = line.split(' | ')
        res.append(out)
    return res

if __name__ == "__main__":
    main()

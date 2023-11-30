with open('input.txt') as f:
    lines = [line.rstrip() for line in f]

def main():
    print("The solution for part 1 is: {0}".format(part1Solution(lines)))
    print("The solution for part 2 is: {0}".format(part2Solution(lines)))

def part1Solution(lines):
    subset = []
    fattestelf = 0
    for line in lines:
        if not line:
            elfcal = sum(subset)
            if elfcal > fattestelf:
                fattestelf = elfcal
            subset.clear()
        else:
            subset.append(int(line))
    return fattestelf

def part2Solution(lines):
    subset = []
    fattestelves = []
    for line in lines:
        if not line:
            fattestelves.append(sum(subset))
            subset.clear()
        else:
            subset.append(int(line))
    fattestelves.append(sum(subset))
    fattestelves.sort()
    return sum(fattestelves[-3:])

if __name__ == "__main__":
    main()

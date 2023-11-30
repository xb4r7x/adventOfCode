with open('input.txt') as f:
    input = [int(x) for x in f.readline().strip().split(',')]

def main():
    print("The solution for part 1 is: {0}".format(part1Solution(input)))
    print("The solution for part 2 is: {0}".format(part2Solution(input)))

def part1Solution(input):
    lowest = float('inf')
    for pos in input:
        cost = 0
        for dest in input:
            distance = abs(dest - pos)
            cost += distance
        if cost < lowest:
            lowest = cost
    return lowest

def part2Solution(input):
    lowest = float('inf')
    for pos in input:
        cost = 0
        for dest in input:
            distance = abs(dest - pos)
            for i in range(distance+1):
                cost += i
        if cost < lowest:
            lowest = cost
    return lowest

if __name__ == "__main__":
    main()

from aocd import get_data, submit

useExample=False
submitA=False
submitB=True

if useExample == False:
    lines = get_data(day=3, year=2025).splitlines()
else:
    with open('ex_input.txt') as f:
        lines = [line.rstrip() for line in f]

def main():
    print("The solution for part 1 is: {0}".format(part1Solution(lines)))
    if submitA == True:
        print("Submitting solution A to AoC:")
        submit(part1Solution(lines), part="a", day=3, year=2025)
    print("The solution for part 2 is: {0}".format(part2Solution(lines)))
    if submitB == True:
        print("Submitting solution B to AoC:")
        submit(part2Solution(lines), part="b", day=3, year=2025)

# Brute force -- I'm going to regret this.
def largest_two_digit(line):
    largest=0
    for i in range(len(line)):
        for j in range(i+1, len(line)):
            number=int(line[i]+line[j])
            if number > largest:
                largest=number
    return largest

# That's less dumb...
def largest_twelve_digits(line):
    digits=12
    start=0
    results=[]
    for i in range(digits):
        remaining = digits - i - 1
        end = len(line) - remaining
        best = max(range(start,end), key=lambda idx: line[idx])
        results.append(line[best])
        start = best + 1
    return "".join(results)

def part1Solution(lines):
    total = 0
    for line in lines:
        largest=largest_two_digit(line)
        total+=int(largest)
    return total

def part2Solution(lines):
    total = 0
    for line in lines:
        largest=largest_twelve_digits(line)
        total+=int(largest)
    return total

if __name__ == "__main__":
    main()

from aocd import get_data, submit

useExample=False
submitA=False
submitB=False

if useExample == False:
    lines = get_data(day=8, year=2024).splitlines()
else:
    with open('ex_input.txt') as f:
        lines = [line.rstrip() for line in f]

def main():
    print("The solution for part 1 is: {0}".format(part1Solution(lines)))
    if submitA == True:
        print("Submitting solution A to AoC:")
        submit(part1Solution(lines), part="a", day=8, year=2024)
    print("The solution for part 2 is: {0}".format(part2Solution(lines)))
    if submitB == True:
        print("Submitting solution B to AoC:")
        submit(part2Solution(lines), part="b", day=8, year=2024)

def part1Solution(lines):
    
    return 1

def part2Solution(lines):
    
    return 2

if __name__ == "__main__":
    main()

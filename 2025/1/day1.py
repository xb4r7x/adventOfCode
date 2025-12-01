from aocd import get_data, submit

useExample=False
submitA=False
submitB=True

if useExample == False:
    lines = get_data(day=1, year=2025).splitlines()
else:
    with open('ex_input.txt') as f:
        lines = [line.rstrip() for line in f]

def main():
    print("The solution for part 1 is: {0}".format(part1Solution(lines)))
    if submitA == True:
        print("Submitting solution A to AoC:")
        submit(part1Solution(lines), part="a", day=1, year=2025)
    print("The solution for part 2 is: {0}".format(part2Solution(lines)))
    if submitB == True:
        print("Submitting solution B to AoC:")
        submit(part2Solution(lines), part="b", day=1, year=2025)

def getPosition(dial, start, count):
    final_index = (start + count) % len(dial)
    return dial[final_index]

def part1Solution(lines):
    count=0
    num=50
    dial = list(range(100))
    for line in lines:
        number=int(line[1:])
        if line[0] == "L":
            number = -number
        value = getPosition(dial, start=num, count=number)
        num=value
        if value == 0:
            count+=1
    return count

def part2Solution(lines):
    count=0
    num=50
    for line in lines:
        direction=line[0]
        number=int(line[1:])
        if direction == "L":
            dir = -1
        else:
            dir = 1
        for _ in range(number):
            num = (num + dir) % 100
            if num == 0:
                count+=1
    return count

if __name__ == "__main__":
    main()

from aocd import get_data, submit

useExample=False
submitA=False
submitB=True

if useExample == False:
    lines = get_data(day=2, year=2025).splitlines()
else:
    with open('ex_input.txt') as f:
        lines = [line.rstrip() for line in f]

def main():
    print("The solution for part 1 is: {0}".format(part1Solution(lines)))
    if submitA == True:
        print("Submitting solution A to AoC:")
        submit(part1Solution(lines), part="a", day=2, year=2025)
    print("The solution for part 2 is: {0}".format(part2Solution(lines)))
    if submitB == True:
        print("Submitting solution B to AoC:")
        submit(part2Solution(lines), part="b", day=2, year=2025)

def repeats_at_least_twice(strNum):
    strLen = len(strNum)
    for size in range(1, strLen // 2 + 1):
        if strLen % size != 0:
            continue
        unit = strNum[:size]
        repeats = strLen // size
        if repeats >= 2 and unit * repeats == strNum:
            return True
    return False

def part1Solution(lines):
    total = 0
    for line in lines:
        ranges = line.split(',')

    for _range in ranges:
        nums = _range.split('-')
        begin = int(nums[0])
        finish = int(nums[1])
        for num in range(begin,finish+1):
            strNum=str(num)
            if len(strNum) % 2 != 0:
                continue
            half = len(strNum) // 2
            firstHalf=strNum[:half]
            secondHalf=strNum[-half:]
            if firstHalf == secondHalf:
                total+=num
    return total

def part2Solution(lines):
    total = 0
    for line in lines:
        ranges = line.split(',')

    for _range in ranges:
        nums = _range.split('-')
        begin = int(nums[0])
        finish = int(nums[1])
        for num in range(begin,finish+1):
            strNum=str(num)
            if repeats_at_least_twice(strNum):
                total+=num
    return total

if __name__ == "__main__":
    main()

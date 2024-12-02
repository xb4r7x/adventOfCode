from aocd import get_data, submit

useExample=False
submitA=False
submitB=True

if useExample == False:
    lines = get_data(day=1, year=2024).splitlines()
else:
    with open('ex_input.txt') as f:
        lines = [line.rstrip() for line in f]

def main():
    print("The solution for part 1 is: {0}".format(part1Solution(lines)))
    if submitA == True:
        print("Submitting solution A to AoC:")
        submit(part1Solution(lines), part="a", day=1, year=2023)
    print("The solution for part 2 is: {0}".format(part2Solution(lines)))
    if submitB == True:
        print("Submitting solution B to AoC:")
        submit(part2Solution(lines), part="b", day=1, year=2023)

def part1Solution(lines):
    list1 = []
    list2 = []
    sum_list = []
    for line in lines:
        num1, num2 = map(int, line.split())
        list1.append(num1)
        list2.append(num2)
    
    list1.sort()
    list2.sort()

    for a, b in zip(list1, list2):
        sum_list.append(abs(a - b))

    return sum(sum_list)

def part2Solution(lines):
    list1 = []
    list2 = []
    count_list = []
    for line in lines: 
        num1, num2 = map(int, line.split())
        list1.append(num1)
        list2.append(num2)

    for num in list1:
        count = list2.count(num)
        total = num * count
        count_list.append(total)

    return sum(count_list)

if __name__ == "__main__":
    main()

with open('input.txt') as f:
    lines = [line.rstrip() for line in f]

def main():
    print("The solution for part 1 is: {0}".format(part1Solution(lines)))
    print("The solution for part 2 is: {0}".format(part2Solution(lines)))

def part1Solution(lines):
    priorities = []
    for line in lines:
        compartment1, compartment2 = line[:len(line)//2], line[len(line)//2:]
        commonItem = list(set(compartment1)&set(compartment2))
        for item in commonItem:
            if item.isupper():
                priorities.append(ord(item)-38)
            else:
                priorities.append(ord(item)-96)
    return sum(priorities)

def part2Solution(lines):
    priorities = []
    elfgroup = []
    count = 0
    for line in lines:
        elfgroup.append(line)
        count += 1
        if count == 3:
            commonItem = list(set(elfgroup[0])&set(elfgroup[1])&set(elfgroup[2]))
            for item in commonItem:
                if item.isupper():
                    priorities.append(ord(item)-38)
                else:
                    priorities.append(ord(item)-96)
            count = 0
            elfgroup.clear()
    return sum(priorities)

if __name__ == "__main__":
    main()

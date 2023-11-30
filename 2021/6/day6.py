from collections import Counter

with open('test.txt') as f:
    input = [int(x) for x in f.readline().strip().split(',')]

def main():
    print("The solution for part 1 is: {0}".format(part1Solution(input)))
    print("The solution for part 2 is: {0}".format(part2Solution(input)))

def part1Solution(input):
    fishes = input.copy()
    newFish = 0
    for i in range(80):
        for j,fish in enumerate(fishes):
            fishes[j] -= 1
            if fish == 0:
                fishes[j] = 6
                newFish += 1
        for x in range(newFish):
            fishes.append(8)
            newFish = 0
    solution=len(fishes)
    return solution

def part2Solution(input):
    count = Counter(input)
    for i in range(256): 
        tempCount = Counter()
        for num in count:
            if num == 0:
                tempCount[6] += count[0]
                tempCount[8] += count[0]
            else: 
                tempCount[num-1] += count[num]
        count = tempCount
        solution = sum(count.values())
    return solution

if __name__ == "__main__":
    main()

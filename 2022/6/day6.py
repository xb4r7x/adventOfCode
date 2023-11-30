from collections import deque

with open('input.txt') as f:
    lines = f.readline()

def main():
    print("The solution for part 1 is: {0}".format(Solution(lines, 4)))
    print("The solution for part 2 is: {0}".format(Solution(lines, 14)))

def Solution(lines, length):
    testSet = deque()
    for i, c in enumerate(lines):
        if len(testSet) == length:
            uniq = set(testSet)
            if len(uniq) == length:
                return i
            testSet.popleft()
        testSet.append(c)

if __name__ == "__main__":
    main()
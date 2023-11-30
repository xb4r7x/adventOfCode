import numpy as np

with open('ex_input.txt') as f:
    lines = [line.rstrip() for line in f]

def main():
    print("The solution for part 1 is: {0}".format(part1Solution(lines)))
    print("The solution for part 2 is: {0}".format(part2Solution(lines)))

def getCoords(lines):
    x=np.zeros(len(lines), dtype=int)
    y=np.zeros(len(lines), dtype=int)
    lastDir = ""
    for i, line in enumerate(lines):
        direction, distance = line.split()
        distance = int(distance)
        
        if lastDir:
            if lastDir in "LR" and direction in "LR":
                print("Same Direction")            
            elif lastDir in "UD" and direction in "UD":
                print("Same Direction")
            else:
                print("New direction")

        if direction == "R":
            x[i] = x[i - 1] + distance
            y[i] = y[i - 1]
        elif direction == "L":
            x[i] = x[i - 1] - distance
            y[i] = y[i - 1]
        elif direction == "U":
            x[i] = x[i - 1]
            y[i] = y[i - 1] + distance
        elif direction == "D":
            x[i] = x[i - 1]
            y[i] = y[i - 1] - distance
        lastDir = direction
    return list(zip(x,y))

def part1Solution(lines):
    hcoords = getCoords(lines)
    return 1

def part2Solution(lines):
    
    return 2

if __name__ == "__main__":
    main()

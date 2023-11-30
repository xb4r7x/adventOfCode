with open('input.txt') as f:
    lines = [line.rstrip() for line in f]

def main():
    print("The solution for part 1 is: {0}".format(part1Solution(lines)))
    print("The solution for part 2 is: {0}".format(part2Solution(lines)))

def part1Solution(lines):
    countOverlaps = 0
    for line in lines:
        strRange1, strRange2 = line.split(",")
        #got fancier than necessary here - could have just compared the numbers without making them ranges... was trying to anticpate part 2
        range1 = range(int(strRange1.split("-")[0]),int(strRange1.split("-")[1]))
        range2 = range(int(strRange2.split("-")[0]),int(strRange2.split("-")[1]))

        if range1.start <= range2.start and range1.stop >= range2.stop:
            countOverlaps += 1
            continue
        if range1.start >= range2.start and range1.stop <= range2.stop:
            countOverlaps += 1
            continue
    return countOverlaps

def part2Solution(lines):
    countOverlaps = 0
    for line in lines:
        strRange1, strRange2 = line.split(",")
        range1 = range(int(strRange1.split("-")[0]),int(strRange1.split("-")[1])+1)
        range2 = range(int(strRange2.split("-")[0]),int(strRange2.split("-")[1])+1)

        if max(range1.start,range2.start) < min(range1.stop,range2.stop):
            countOverlaps += 1
    return countOverlaps

if __name__ == "__main__":
    main()
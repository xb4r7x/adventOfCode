from aocd import get_data, submit

useExample=False
submitA=False
submitB=False

if useExample == False:
    lines = get_data(day=6, year=2023).splitlines()
else:
    with open('ex_input.txt') as f:
        lines = [line.rstrip() for line in f]

def main():
    print("The solution for part 1 is: {0}".format(part1Solution(lines)))
    if submitA == True:
        print("Submitting solution A to AoC:")
        submit(part1Solution(lines), part="a", day=6, year=2023)
    print("The solution for part 2 is: {0}".format(part2Solution(lines)))
    if submitB == True:
        print("Submitting solution B to AoC:")
        submit(part2Solution(lines), part="b", day=6, year=2023)

def multiplyList(aList):
    result = 1
    for x in aList: result*= x
    return result

def solveIt(races):
    total = 0
    wins = []
    for time,distance in races:
        winCount=0
        remainingTime=time
        for speed in range(time):
            totDist=speed*remainingTime
            if totDist > distance:
                winCount+=1
            remainingTime-=1 
        wins.append(winCount)
    return multiplyList(wins)

def part1Solution(lines):
    races=zip([int(time) for time in lines[0].split()[1:]], [int(dist) for dist in lines[1].split()[1:]])
    return solveIt(races)

def part2Solution(lines):
    races=[(int("".join(lines[0].split()[1:])),int("".join(lines[1].split()[1:])))]
    return solveIt(races) 

if __name__ == "__main__":
    main()

from aocd import get_data, submit

useExample=True
submitA=False
submitB=False

if useExample == False:
    lines = get_data(day=4, year=2023).splitlines()
else:
    with open('ex_input.txt') as f:
        lines = [line.rstrip() for line in f]

def main():
    print("The solution for part 1 is: {0}".format(part1Solution(lines)))
    if submitA == True:
        print("Submitting solution A to AoC:")
        submit(part1Solution(lines), part="a", day=4, year=2023)
    print("The solution for part 2 is: {0}".format(part2Solution(lines)))
    if submitB == True:
        print("Submitting solution B to AoC:")
        submit(part2Solution(lines), part="b", day=4, year=2023)

def part1Solution(lines):
    total=0
    score=1
    for line in lines: 
        winningNums, gameNums = line.split(":")[1].split("|")
        winningList = [i for i in winningNums.strip().split(" ") if i]
        gameList = [i for i in gameNums.strip().split(" ") if i]
        commonNums = [num for num in gameList if num in winningList]
        
        score=1
        if len(commonNums)==0:
            score=0
        for _ in range(len(commonNums)-1):
            if len(commonNums) == 0:
                continue
            score*=2
        total+=score
    return total

def part2Solution(lines):
    total=0
    cardCounts={index+1: 0 for index in range(len(lines))}
    for i, line in enumerate(lines):
        winningNums, gameNums = line.split(":")[1].split("|")
        winningList = [i for i in winningNums.strip().split(" ") if i]
        gameList = [i for i in gameNums.strip().split(" ") if i]
        commonNums = [num for num in gameList if num in winningList]
        
        cardNum=i+1        
        numWins=len(commonNums)
        
        #Add orignal card to count.
        cardCounts[cardNum]+=1

        for x in range(numWins):
            for y in range(cardCounts[cardNum]):
                cardCounts[cardNum+x+1]+=1

    total=sum(cardCounts.values())
 
    return total

if __name__ == "__main__":
    main()

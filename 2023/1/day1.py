from aocd import get_data
from aocd import submit
import regex as re

stringData = get_data(day=1, year=2023)
lines = stringData.splitlines()

#with open('ex_input.txt') as f:
#    lines = [line.rstrip() for line in f]

submitA=False
submitB=False

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
    total=0
    for line in lines:
         nums=re.findall(r'\d', line)
         number=nums[0]+nums[-1]
         total=total+int(number)     
    return total

def part2Solution(lines):
    total=0
    for line in lines:
        print(line)
        nums=re.findall(r'\d|one|two|three|four|five|six|seven|eight|nine', line, overlapped=True)
        wordNums = {'one': "1",
                    'two': "2",
                    'three': "3",
                    'four': "4",
                    'five': "5",
                    'six': "6",
                    'seven': "7",
                    'eight': "8",
                    'nine': "9",
                   }
 
        if nums[0] in wordNums:
            firstNum=wordNums[nums[0]]
        else:
            firstNum=nums[0]

        if nums[-1] in wordNums:
            lastNum=wordNums[nums[-1]]
        else:
            lastNum=nums[-1]

        firstLast=firstNum+lastNum

        total=total+int(firstLast)
        
    return total

if __name__ == "__main__":
    main()

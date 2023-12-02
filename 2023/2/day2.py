from aocd import get_data, submit
import regex as re

useExample=False
submitA=False
submitB=False

if useExample == False:
    lines = get_data(day=2, year=2023).splitlines()
else:
    with open('ex_input.txt') as f:
        lines = [line.rstrip() for line in f]

def main():
    print("The solution for part 1 is: {0}".format(part1Solution(lines)))
    if submitA == True:
        print("Submitting solution A to AoC:")
        submit(part1Solution(lines), part="a", day=2, year=2023)
    print("The solution for part 2 is: {0}".format(part2Solution(lines)))
    if submitB == True:
        print("Submitting solution B to AoC:")
        submit(part2Solution(lines), part="b", day=2, year=2023)

def part1Solution(lines):
    maxR=12
    maxG=13
    maxB=14
    total=0
    for game in lines:
        possible=True
        spl=game.split(':')
        gameNumber=int(re.findall(r'\d+', spl[0])[0])
        shows=spl[1].split(';')
        for show in shows:
            colors=show.split(',')
            for color in colors:
                if "red" in color:
                    if int(re.findall(r'\d+', color)[0]) > maxR:
                        possible=False
                if "green" in color:
                    if int(re.findall(r'\d+', color)[0]) > maxG:
                        possible=False
                if "blue" in color:
                    if int(re.findall(r'\d+', color)[0]) > maxB:
                        possible=False
       
        if possible == True:
            total+=gameNumber

    return total

def part2Solution(lines):
    total=0
    for game in lines:
        redMin=0
        blueMin=0
        greenMin=0
        spl=game.split(':')
        gameNumber=int(re.findall(r'\d+', spl[0])[0])
        shows=spl[1].split(';')
        for show in shows:
            colors=show.split(',')
            for color in colors:
                if "red" in color:
                    redNum=int(re.findall(r'\d+', color)[0])
                    if redNum > redMin:
                        redMin=redNum
                if "green" in color:
                    greenNum=int(re.findall(r'\d+', color)[0])
                    if greenNum > greenMin:
                        greenMin=greenNum
                if "blue" in color:
                    blueNum=int(re.findall(r'\d+', color)[0])
                    if blueNum > blueMin:
                        blueMin=blueNum

        power=redMin*blueMin*greenMin
        total+=power
    return total

if __name__ == "__main__":
    main()

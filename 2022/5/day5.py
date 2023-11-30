import re

with open('input.txt') as f:
    lines = [line.rstrip() for line in f]

#This one is ugly. Really dislike it.
#This is why you don't exceed Ballmer's Peak... https://xkcd.com/323/

def main():
    global stacks 
    #stacks = [["N","Z"], ["D","C","M"], ["P"]]
    stacks = [["B","S","J","Z","V","D","G"], ["P","V","G","M","S","Z"], ["F","Q","T","W","S","B","L","C"], ["Q","V","R","M","W","G","J","H"], ["D","M","F","N","S","K","C"], ["D","C","G","R"], ["Q","S","D","J","R","T","G","H"], ["V","F","P"], ["J","T","S","R","D"]]
    print("The solution for part 1 is: {0}".format(part1Solution(lines)))
    #stacks = [["N","Z"], ["D","C","M"], ["P"]]
    stacks = [["B","S","J","Z","V","D","G"], ["P","V","G","M","S","Z"], ["F","Q","T","W","S","B","L","C"], ["Q","V","R","M","W","G","J","H"], ["D","M","F","N","S","K","C"], ["D","C","G","R"], ["Q","S","D","J","R","T","G","H"], ["V","F","P"], ["J","T","S","R","D"]]
    print("The solution for part 2 is: {0}".format(part2Solution(lines)))

def part1Solution(lines):
    for line in lines:
        if line.startswith("move"):
            moves = re.findall(r'\d+',line)
            for x in range(int(moves[0])):
                stacks[int(moves[2])-1].insert(0,stacks[int(moves[1])-1].pop(0))
    string = ""
    for stack in stacks:
        string = string + stack[0]
    return string

def part2Solution(lines):
    for line in lines:
        if line.startswith("move"):
            moves = re.findall(r'\d+',line)
            for x in reversed(range(int(moves[0]))):
                stacks[int(moves[2])-1].insert(0,stacks[int(moves[1])-1].pop(x))
    string = ""
    for stack in stacks:
        string = string + stack[0]
    return string

if __name__ == "__main__":
    main()

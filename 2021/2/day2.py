import re

with open('input.txt') as f:
    lines = f.readlines()

def main():
    part1 = part1Solution(lines)
    part2 = part2Solution(lines)
    print(part1)
    print(part2)

def part1Solution(lines):
    horiz = 0
    depth = 0
    for line in lines:
        search = re.search("(\w+)\s(\d+)", line)
        command = search.group(1)
        movement = int(search.group(2))
        if command == "forward":
            horiz = horiz + movement
        if command == "up":
            depth = depth - movement
        if command == "down":
            depth = depth + movement

    solution = horiz * depth 
    return solution

def part2Solution(lines):
    horiz = 0
    depth = 0
    aim = 0
    for line in lines:
        search = re.search("(\w+)\s(\d+)", line)
        command = search.group(1)
        movement = int(search.group(2))
        if command == "forward":
            horiz = horiz + movement
            multiply = movement * aim
            depth = depth + multiply
        if command == "up":
            aim = aim - movement
        if command == "down":
            aim = aim + movement

    solution = horiz * depth 
    return solution

if __name__ == "__main__":
    main()

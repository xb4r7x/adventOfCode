#!/bin/bash

if [ $# -eq 0 ]; then
    day=$(date -v+1d +%-d)
    echo "No arguments provided. Assuming today: $day."
else
    day=$1
fi

echo "Ensuring folder for $day doesn't already exist."
if [ -d ./$day ]; then
    echo "The directory for $day already exists. Exiting to prevent overwritting things."
    exit 1
fi

year=2025
mkdir "./$day"
touch "./$day/ex_input.txt"
scriptPath="./$day/day$day.py"

cat <<- EOF > $scriptPath
from aocd import get_data, submit

useExample=False
submitA=False
submitB=False

if useExample == False:
    lines = get_data(day=$day, year=$year).splitlines()
else:
    with open('ex_input.txt') as f:
        lines = [line.rstrip() for line in f]

def main():
    print("The solution for part 1 is: {0}".format(part1Solution(lines)))
    if submitA == True:
        print("Submitting solution A to AoC:")
        submit(part1Solution(lines), part="a", day=$day, year=$year)
    print("The solution for part 2 is: {0}".format(part2Solution(lines)))
    if submitB == True:
        print("Submitting solution B to AoC:")
        submit(part2Solution(lines), part="b", day=$day, year=$year)

def part1Solution(lines):

    return 1

def part2Solution(lines):

    return 2

if __name__ == "__main__":
    main()
EOF

echo "Activate python venv"
source ./venv/bin/activate

echo "Created directory: ./$day"
echo "Created script skeleton: $scriptPath"

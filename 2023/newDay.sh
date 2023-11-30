#!/bin/bash

day=$1
year=2023
mkdir "./$1"
touch "./$1/ex_input.txt"
scriptPath="./$1/day$1.py"

cat <<- EOF > $scriptPath
from aocd import get_data
from aocd import submit

stringData = get_data(day=$1, year=$year)
lines = stringData.splitlines()

submitA=False
submitB=False

def main():
    print("The solution for part 1 is: {0}".format(part1Solution(lines)))
    if submitA == True:
        print("Submitting solution A to AoC:")
        submit(part1Solution(lines), part="a", day=$1, year=$year)
    print("The solution for part 2 is: {0}".format(part2Solution(lines)))
    if submitB == True:
        print("Submitting solution B to AoC:")
        sumbit(part2Solution(lines), part="b", day=$1, year=$year)

def part1Solution(lines):
    
    return 1

def part2Solution(lines):
    
    return 2

if __name__ == "__main__":
    main()
EOF

echo "Activate python venv"
source ./venv/bin/activate

echo "Created directory: ./$1"
echo "Created script skeleton: $scriptPath"

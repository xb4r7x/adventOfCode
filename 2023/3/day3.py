from aocd import get_data, submit
from itertools import product

useExample=False
submitA=False
submitB=False

if useExample == False:
    lines = get_data(day=3, year=2023).splitlines()
else:
    with open('ex_input.txt') as f:
        lines = [line.rstrip() for line in f]

def main():
    print("The solution for part 1 is: {0}".format(part1Solution(lines)))
    if submitA == True:
        print("Submitting solution A to AoC:")
        submit(part1Solution(lines), part="a", day=3, year=2023)
    print("The solution for part 2 is: {0}".format(part2Solution(lines)))
    if submitB == True:
        print("Submitting solution B to AoC:")
        submit(part2Solution(lines), part="b", day=3, year=2023)

def neighbors(arr, *coordinate, part2=False):
    x, y=coordinate[0], coordinate[1]
    #Get row indicies
    row=[i for i in range(x-1,x+2) if 0<=i<len(arr)]
    #Get col indicies
    col=[i for i in range(y-1,y+2) if 0<=i<len(arr[0])]
    #Get cartesian product of possible indicies (do not include our referenced coords)
    neighbors= set(product(row,col))-{(x,y)}
    if part2==True:
        return neighbors
    else:
        #Return a list of array contents at the the give points from our cartesian product
        return [arr[val[0]][val[1]] for val in neighbors]

def getNumbers(arr, neighbors):
    numbers=set()
    
    for pos in neighbors:
        if arr[pos[0]][pos[1]].isdigit():
            strNum=arr[pos[0]][pos[1]]
            #Search forward
            i = pos[1]+1
            while i < len(arr[pos[0]]):
                if arr[pos[0]][i].isdigit():
                    strNum+=arr[pos[0]][i]
                    i+=1
                else:
                    break

            #Search backward
            i = pos[1]-1
            while i >= 0:
                if arr[pos[0]][i].isdigit():
                    strNum=arr[pos[0]][i]+strNum
                    i-=1
                else:
                    break 
            numbers.add(strNum)
    return numbers    
 
def part1Solution(lines):

    matrix = [[char for char in line] for line in lines]

    symbols='#$%&*+-/=@'
    total=0
    isValid=False
    numStr=''
    for i, row in enumerate(matrix):
        if isValid==True:
            total+=int(numStr)
            isValid=False
        numStr=''
        for y, char in enumerate(row):
            if char.isdigit():
                numStr+=char
                if any(spec in symbols for spec in neighbors(matrix,i,y)):
                    isValid=True
            else:
                if isValid==True:
                    total+=int(numStr)
                    isValid=False
                isValid=False
                numStr=''
    return total

def part2Solution(lines):
    matrix=[]
    for line in lines:
        chars=[]
        for char in line:
            chars.append(char)
        matrix.append(chars)     
    total=0
    for i, row in enumerate(matrix):
        for y, char in enumerate(row):
            if char == '*':
                nums=getNumbers(matrix, neighbors(matrix,i,y,part2=True))
                
                if len(nums)==2:
                    prod=1
                    for num in nums:
                        prod = prod * int(num)
                    total+=prod         
    return total

if __name__ == "__main__":
    main()

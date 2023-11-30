from io import StringIO
import numpy as np

####### WIP - Does not function yet ########

with open('./input.txt') as f:
    lines = f.readlines()

def main():
    print("The solution for part 1 is: {0}".format(part1Solution(lines)))
    print("The solution for part 2 is: {0}".format(part2Solution(lines)))

def part1Solution(lines):
    bingoBalls = lines[0].split(",")
    bingoBoards = lines
    bingoBoards.pop(0)

    boardsList = getBoards(bingoBoards)
    for ball in bingoBalls:    #Loop through all balls
        for i in range(len(boardsList)):    #Loop through all boards
            for j in range(len(boardsList[i])):   #Loop through each row in each board
                for x in range(len(boardsList[i][j])):   #Loop through each number in each row.
                    print("checking board row %s" % (boardsList[i][j]))
                    if ball == boardsList[i][j][x]:
                        boardsList[i][j][x] = "X"
                    if checkWinner(boardsList[i]):
                        print("Winnter detected! %s" % (boardsList[i]))
                        sum = 0
                        for items in boardsList[i]:
                            for item in items:
                                if item != "X":
                                    sum = sum + int(item)
                        print(sum * int(ball))                                    
                        exit(0)
                        
                        

                        #print("winner detected! %s" % (boardsList[i]))
                #answer = sum(boardsList[i]) * int(ball)
            

#    print(boardsList)

    return 0

def part2Solution(lines):

    return lines

def checkWinner(board):
    winner = False
    for row in board:
        winner = all(element == "X" for element in row)
        if winner:
            break
    if not winner:
        col = []
        for i, line in enumerate(board):
            for j, number in enumerate(line):
                col.append(line[j])
                winner = all(element == "X" for element in col)  
        col = []
    return winner

def getBoards(bingoBoards):
    bingoBoards.pop(0)
    boards = []
    board = []
    for line in bingoBoards:
        if len(line) == 1:
            boards.append(board)
            board = []
            continue
        row = line.split()
        board.append(row)       
    return boards

if __name__ == "__main__":
    main()

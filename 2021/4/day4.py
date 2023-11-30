with open('test.txt', 'r') as f:
    balls, *boards = f.read().split('\n\n')
    f.close()

ballsList = list(map(int, balls.split(',')))
boardsList = [[[int(i) for i in x.split()] for x in r.split('\n') if x] for r in boards]

def main():
    print("The solution for part 1 is: {0}".format(part1Solution()))
    #print("The solution for part 2 is: {0}".format(part2Solution(lines)))

def part1Solution():
    for num in ballsList:
        for i, board in enumerate(boardsList):
            boards[i] = markTheSpot(board, num)
        for i, board in enumerate(boardsList):
            for row in board:
                if set(row) == {'X'}:
                    sum = sumWinner(board)
                    score = num * sum
                    return score
            columns = [[row[i] for row in board] for i in range(5)]
            for column in columns:
                if set(column) == {'X'}:
                    sum = sumWinner(board)
                    score = num * sum
                    return board
    return 1

def part2Solution(lines):
    
    return 2

def markTheSpot(board, n):
 #   assert len(board) == 5
    for i in range(5):
        for x in board[i]:
            print(x)
            print(n)
            if x == n:
                board[i] = 'X'
                print(board[i])
                
    return board

def sumWinner(board):
    sum = 0
    for row in board:
        for x in row:
            if x != 'X':
                sum += x
    return sum

if __name__ == "__main__":
    main()

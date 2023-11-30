import numpy as np

with open('ex_input.txt') as f:
    lines = [line.rstrip() for line in f]

def main():
    print("The solution for part 1 is: {0}".format(part1Solution(lines)))
    print("The solution for part 2 is: {0}".format(part2Solution(lines)))

# def getCoords(lines):
#     x=np.zeros(len(lines), dtype=int)
#     y=np.zeros(len(lines), dtype=int)
#     for i, line in enumerate(lines):
#         direction, distance = line.split()
#         distance = int(distance)

#         if direction == "R":
#             x[i] = x[i - 1] + distance
#             y[i] = y[i - 1]
#         elif direction == "L":
#             x[i] = x[i - 1] - distance
#             y[i] = y[i - 1]
#         elif direction == "U":
#             x[i] = x[i - 1]
#             y[i] = y[i - 1] + distance
#         elif direction == "D":
#             x[i] = x[i - 1]
#             y[i] = y[i - 1] - distance
#     return list(zip(x,y))

def part1Solution(lines):
    tpositions = [[0,0]]
    lastDirection = ""
    for i, line in enumerate(lines):
        currentDirection = ""
        direction, distance  = line.split()
        distance = int(distance)
        for _ in range(distance-1):
            if direction == "R":
                currentDirection = direction
                _x = tpositions[-1][0]+1 #Add logic in each of these to detect a direction change and add/subtract values as appropriate. 
                tpositions.append([_x,tpositions[-1][1]])
                print(currentDirection, lastDirection)
                lastDirection = direction
            if direction == "L":
                currentDirection = direction
                _x = tpositions[-1][0]-1
                tpositions.append([_x,tpositions[-1][1]])
                print(currentDirection, lastDirection)
                lastDirection = direction
            if direction == "U":
                currentDirection = direction
                _y = tpositions[-1][1]+1
                tpositions.append([_y,tpositions[-1][0]])
                print(currentDirection, lastDirection)
                lastDirection = direction
            if direction == "D":
                currentDirection = direction
                _y = tpositions[-1][1]-1
                tpositions.append([_y,tpositions[-1][0]])
                print(currentDirection, lastDirection)
                lastDirection = direction
            
    print(tpositions)


    # hcoords = getCoords(lines)
    # tcoords = []
    # for i, line in enumerate(lines):
    #     direction, distance  = line.split()
    #     distance = int(distance)
    #     offset = {'R': (0, 1),'L': (0, -1),'U': (-1, 0), 'D': (1, 0)} #Access with offset[direction]
    # for x in range(distance):
    #     for point in hcoords[i]:
    #         tpcoord = []
    #         for opoint in offset[direction]:
    #             tpoint = int(point) - int(opoint)
    #             tpcoord.append(tpoint)
    #             tcoords.append(tpcoord)
    # print(hcoords)
    # print(tcoords)
            
    return 1

def part2Solution(lines):
    
    return 2

if __name__ == "__main__":
    main()

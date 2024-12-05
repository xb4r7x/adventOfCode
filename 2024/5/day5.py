from aocd import get_data, submit

useExample=False
submitA=False
submitB=False

if useExample == False:
    lines = get_data(day=5, year=2024)#.splitlines()
else:
    with open('ex_input.txt') as f:
        lines = f.read()#[line.rstrip() for line in f]

def main():
    print("The solution for part 1 is: {0}".format(part1Solution(lines)))
    if submitA == True:
        print("Submitting solution A to AoC:")
        submit(part1Solution(lines), part="a", day=5, year=2024)
    print("The solution for part 2 is: {0}".format(part2Solution(lines)))
    if submitB == True:
        print("Submitting solution B to AoC:")
        submit(part2Solution(lines), part="b", day=5, year=2024)

def checkAll(dictionary, key, testList):
    allexist = True
    try:
        allexist = all(item in dictionary[key] for item in testList)
    except(KeyError):
        print("KeyError")
        allexist = False
    return allexist

def checkValid(beforeDict, afterDict, update):
    isValid = True

    for i, page in enumerate(update):
        numsBefore = update[:i]
        numsAfter = update[i + 1:]
                
        if numsBefore:
            isValid = checkAll(afterDict, page, numsBefore)
            if not isValid:
                break
        if numsAfter:
            isValid = checkAll(beforeDict, page, numsAfter)
            if not isValid:
                break

    return isValid

def reorder(update, beforeDict, afterDict):
    newList = update[:]
    
    for i, num in enumerate(newList):
        numsBefore = newList[:i]
        
        if numsBefore:
            y = i
            isValid = checkAll(afterDict, num, numsBefore)
            while not isValid:
                if y > 0:
                    newList[y], newList[y - 1] = newList[y - 1], newList[y]
                    y-=1
                else: 
                    break
                isValid = checkValid(beforeDict, afterDict, newList)
                print(newList)

    print(newList)
    for i, num in enumerate(newList):
        numsAfter = newList[i + 1:]
        if numsAfter:
            x = i
            isValid = checkAll(beforeDict, num, numsAfter)
            while not isValid:
                if x < len(newList) -1:
                    newList[x], newList[x + 1] = newList[x + 1], newList[x]
                    x+=1
                else:
                    break
                isValid = checkValid(beforeDict, afterDict, newList)

    print("")
    return newList

def part1Solution(lines):
    rulesRaw, updatePageRaw = lines.split('\n\n')
    rules = [line.split('|') for line in rulesRaw.splitlines()]
    updatePage = [line.split(',') for line in updatePageRaw.splitlines()]

    beforeDict = {}
    afterDict = {}
    for rule in rules:
        beforeDict.setdefault(rule[0], []).append(rule[1]) # lists of numbers that come after the rule
        afterDict.setdefault(rule[1], []).append(rule[0]) # lists of numbers that come before the rule

    total = 0
    centerNums = []
    for update in updatePage:
        isValid = True
        centerNum = 0
        for i, page in enumerate(update):
            numsBefore = update[:i]
            numsAfter = update[i + 1:]
            
            centerNum = update[len(update) // 2]
           
            if numsBefore:
                isValid = checkAll(afterDict, page, numsBefore)
                if not isValid:
                    break
            if numsAfter:
                isValid = checkAll(beforeDict, page, numsAfter)
                if not isValid:
                    break
        if isValid:
            centerNums.append(centerNum)

    return sum(map(int, centerNums))

def part2Solution(lines):
    rulesRaw, updatePageRaw = lines.split('\n\n')
    rules = [line.split('|') for line in rulesRaw.splitlines()]
    updatePage = [line.split(',') for line in updatePageRaw.splitlines()]
    
    beforeDict = {}
    afterDict = {}
    for rule in rules:
        beforeDict.setdefault(rule[0], []).append(rule[1]) # lists of numbers that come after the rule
        afterDict.setdefault(rule[1], []).append(rule[0]) # lists of numbers that come before the rule
    
    validList = []
    failList = []
    centerNums = []
    print(str(len(updatePage)))
    for update in updatePage:
        if checkValid(beforeDict, afterDict, update):
            validList.append(update)
            continue
        else:
            failList.append(update)
            newList = reorder(update, beforeDict, afterDict)

            centerNum = newList[len(newList) // 2]
            centerNums.append(centerNum)

        # print("Old list " + str(update))
        # print("New List " + str(newList))
        # print("")    

    

    return sum(map(int, centerNums))

if __name__ == "__main__":
    main()

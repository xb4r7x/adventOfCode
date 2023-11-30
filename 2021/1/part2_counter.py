def main():
    lines = openFile()
    total = count(lines)
    print(total)

def count(lines):
    toSum = []
    oldSum = 0
    newSum = 0
    count = 0
    for line in lines:
        if len(toSum) < 3:
            toSum.append(int(line))
            continue
        if len(toSum) == 3:
            newSum = sum(toSum)
            if newSum > oldSum:
                count+=1
            oldSum = newSum
            toSum.pop(0)
            toSum.append(int(line))
    return count

def openFile():
    with open('input.txt') as f:
        lines = f.readlines()
    return lines
    
if __name__ == "__main__":
    main()

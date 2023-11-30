def main():
    lines = openFile()
    total = count(lines)
    print(total)

def count(lines):
    count = 0
    lastLine = 0
    for line in lines:
        if int(line) > lastLine and lastLine != 0:
            count+=1
        lastLine = int(line)
    return count

def openFile():
    with open('input.txt') as f:
        lines = f.readlines()
    return lines
    
if __name__ == "__main__":
    main()

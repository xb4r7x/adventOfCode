import ast

with open('ex_input.txt') as f:
    lines = [line for line in f]

def main():
    print("The solution for part 1 is: {0}".format(part1Solution(lines)))
    print("The solution for part 2 is: {0}".format(part2Solution(lines)))

def compareLists(l,r):
        print(l,r)
        for i in range(max(len(l),len(r))):
            print(type(l[i]), type(r[i]))
            try:
                if all(isinstance(x, int) for x in (l[i],r[i])):
                    compareint = compareInts(l[i],r[i])
                    ltype = type(l[i])
                    rtype = type(r[i])
                    print("Comparing {} {} ints {} and {}. Result is: {}".format(ltype, rtype, l[i], r[i], compareint))
                    if compareint == 0:
                        continue
                    elif compareint == False:
                        continue
                    else:
                        return compareint
                elif all(isinstance(y, list) for y in (l[i],r[i])):
                    ltype = type(l[i])
                    rtype = type(r[i])
                    print("Comparing {} {} lists {} and {}. Result is:".format(ltype, rtype, l[i], r[i]))
                    comparelist = compareInts(l[i],r[i])
                    print(comparelist)
                    return comparelist
                elif not all(isinstance(z, list) for z in (l[i],r[i])):
                    if isinstance(l[i], int):
                        l[i] = [l[i]]
                        compareLists(l[i],r[i])
                    elif isinstance(r[i], int):
                        r[i] = [r[i]]
                        compareLists(l[i],r[i])
                    else:
                        return 0
                    
            except:
                if len(l) < len(r):
                    return True
                if len(l) > len(r):
                    return False


def compareInts(l,r):
    if l < r:
        return True
    elif l > r:
        return False
    else:
        return 0
    


def evalPairs(pair):
    l = pair[0]
    r = pair[1]
    try:
        for i in range(max(len(l),len(r))):
            return compareLists(l,r)
    except:
        print("OOR")

def part1Solution(lines):
    pair = []
    pairs = []
    rightPairs = []
    for line in lines:
        if not line == "\n":
            pair.append(ast.literal_eval(line.strip()))
        else:
            pair.clear()
        if len(pair) == 2:
            pairs.append(pair.copy())
    for i, pair in enumerate(pairs):
        if evalPairs(pair):
            rightPairs.append(i)

    print(rightPairs)            
    return sum(rightPairs)

def part2Solution(lines):
    
    return 2

if __name__ == "__main__":
    main()

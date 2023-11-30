#It worked, okay. Maybe I'll refactor it later.

with open('input.txt') as f:
    lines = [str(line.strip()) for line in f]

linelen=len(lines[0])

def main():
    print("The solution for part 1 is: {0}".format(part1Solution(lines)))
    print("The solution for part 2 is: {0}".format(part2Solution(lines)))

def part1Solution(binary_list):
    gamma = [] 
    epsilon = [] 
    zero_count = 0
    one_count = 0
    index = 0
    for x in range(linelen):
        for line in binary_list:
            if int(line[index]) == 0:
                zero_count+=1
            if int(line[index]) == 1:
                one_count+=1
        index+=1
        if zero_count > one_count:
            gamma.append("0")
        elif one_count > zero_count:
            gamma.append("1")
        if zero_count < one_count:
            epsilon.append("0")
        elif one_count < zero_count:
            epsilon.append("1")
        zero_count = 0
        one_count = 0

    gammaint = int(''.join(map(str, gamma)),2)
    epsilonint = int(''.join(map(str, epsilon)),2)
    solution = gammaint * epsilonint
    return solution

def part2Solution(binary_list):
    new_bin_list = binary_list
    o2 = 0
    co2 = 0
    one_count = 0
    zero_count = 0
    keeper = 0
    for i in range(linelen+1):
        tempList = []
        if len(new_bin_list) == 1:
            o2 = new_bin_list[0]
            break
        counterList = getCounterList(new_bin_list, i)
        for num in counterList:
            if int(num) == 1:
                one_count+=1
            if int(num) == 0:
                zero_count+=1
        if one_count >= zero_count:
            keeper = 1
        elif zero_count >= one_count:
            keeper = 0

        for bins in new_bin_list:
            if int(bins[i]) == keeper:
                tempList.append(bins)

        new_bin_list = tempList
        one_count = 0
        zero_count = 0
    
    #kill me please I just wanna go to bed
    new_bin_list = binary_list
    one_count = 0
    zero_count = 0
    keeper = 0
    for i in range(linelen+1):
        tempList = []
        if len(new_bin_list) == 1:
            co2 = new_bin_list[0]
            break
        counterList = getCounterList(new_bin_list, i)
        for num in counterList:
            if int(num) == 1:
                one_count+=1
            if int(num) == 0:
                zero_count+=1
        if one_count >= zero_count:
            keeper = 0
        elif zero_count >= one_count:
            keeper = 1

        for bins in new_bin_list:
            if int(bins[i]) == keeper:
                tempList.append(bins)

        new_bin_list = tempList
        one_count = 0
        zero_count = 0

    o2int = int(''.join(map(str, o2)),2)
    co2int = int(''.join(map(str, co2)),2)

    solution = o2int*co2int
    return solution

def getCounterList(bits, index):
    count_list = []
    for item in bits:
        count_list.append(item[index])
    return count_list

if __name__ == "__main__":
    main()

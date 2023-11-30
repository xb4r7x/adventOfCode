with open('input.txt') as f:
    lines = [line.rstrip() for line in f]

global sizes
sizes = {}

#######
# This one is incomplete - doesn't work - has bugs somewhere. Works with example input, not with real data.
# It's also super ugly after I've been wrenching on it for too many hours and getting nowhere. 
#######

def main():
    print("The solution for part 1 is: {0}".format(part1Solution(lines)))
    print("The solution for part 2 is: {0}".format(part2Solution(lines)))

from typing import List

#Shamelessly stole this class from Stackoverflow: https://stackoverflow.com/questions/39818669/dynamically-accessing-nested-dictionary-keys
class DynamicAccessNestedDict:
    """Dynamically get/set nested dictionary keys of 'data' dict"""
    def __init__(self, data: dict):
        self.data = data

    def getval(self, keys: List):
        data = self.data
        for k in keys:
            data = data[k]
        return data

    def addval(self, keys: List, newkey, val) -> None:
        data = self.data
        lastkey = keys[-1]
        for k in keys[:-1]:
            data = data[k]
        data[lastkey][newkey] = val

    def setval(self, keys: List, val) -> None:
        data = self.data
        lastkey = keys[-1]
        for k in keys[:-1]:  # when assigning drill down to *second* last key
            data = data[k]
        data[lastkey] = val

def getDepth(mydict):
    if isinstance(mydict, dict):
        return 1 + (max(map(getDepth, mydict.values()))
                                    if mydict else 0)
    return 0


def part1Solution(lines):
    pathDict = {}
    d = DynamicAccessNestedDict(pathDict)
    pathList = []
    for line in lines:
        if line[0] == "$":
            if line[2] == "c":
                if line[5:] == "/":
                    pathList.append("/")
                    d.setval(pathList,{})
                elif line[5:] == "..":
                    pathList.pop()
                else:
                    pathList.append(line[5:])
                    d.setval(pathList,{})
        if line[0].isdigit():
            size, filename = line.split()
            if pathList[-1] == "/":
                d.addval(pathList,filename,size)
            else:
                d.addval(pathList,filename,size)

    for x, y in get_all_keys(pathDict):
        continue

    for x, y in get_all_keys(pathDict, False):
        fileList = find_key(pathDict,y)
        if fileList:
            print(fileList)
            for idx in range(len(fileList)-1):
                filesize = int(nested_get(pathDict,fileList))
                filepath = sizes[fileList[idx]]
                print("Adding {} to {} for {}".format(filesize, filepath, fileList[idx]))
                sizes[fileList[idx]] = int(filepath) + filesize

    answerList = []
    for k, v in sizes.items():
        if v <= 100000:
            print("{} is less than 100000".format(v))
            answerList.append(v)

    return sum(answerList)

def nested_get(input_dict, nested_key):
    internal_dict_value = input_dict
    for k in nested_key:
        internal_dict_value = internal_dict_value.get(k, None)
        if internal_dict_value is None:
            return None
    return internal_dict_value

def find_key(d, value):
    for k,v in d.items():
        if isinstance(v, dict):
            p = find_key(v, value)
            if p:
                return [k] + p
        elif v == value:
            return [k]

def get_all_keys(d,isFirst=True):
    for key, value in d.items():
        yield key, value
        if isinstance(value, dict):
            if isFirst:
                sizes.update({key:0})
            yield from get_all_keys(value)

def part2Solution(lines):
    
    return 2

if __name__ == "__main__":
    main()

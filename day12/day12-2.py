# 96852
# total up all the integers found in the json input
# but only if the object does not have a property set to "red"
# https://adventofcode.com/2015/day/12

import sys
import json

filename = sys.argv[1]
with open(filename, 'r') as inputFile:
    jsonString = inputFile.read()

jsonObj = json.loads(jsonString)

def countNumbers(dictionary):
    total = 0
    # items in the dictionary are dict (object), list (array), int (integer), str (string)
    for child in dictionary.values():
        if type(child) is dict:
            # find out if it has an property with value "red"
            if not 'red' in child.values():
                total += countNumbers(child)
        elif type(child) is list:
            total += countNumbersinList(child)
        elif type(child) is int:
            total += int(child)
        elif type(child) is str:
            pass

    return total

def countNumbersinList(aList):
    total = 0
    for item in aList:
        if type(item) is dict:
            # find out if it has an property with value "red"
            if not 'red' in item.values():
                total += countNumbers(item)
        elif type(item) is list:
            total += countNumbersinList(item)
        elif type(item) is int:
            total += int(item)
        elif type(item) is str:
            pass

    return total

print(countNumbersinList(jsonObj))


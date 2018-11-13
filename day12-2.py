# 96852
# total up all the integers found in the json input
# but only if the object does not have a property set to "red"
# https://adventofcode.com/2015/day/12

import sys
import re
import json
import pprint

filename = sys.argv[1]
with open(filename, 'r') as inputFile:
    jsonString = inputFile.read()

jsonObj = json.loads(jsonString)

reds = 0

def countNumbers(dictionary):
    global reds
    total = 0
    # items in the dictionary are dict (object), list (array), int (integer), unicode (string)
    for child in dictionary.values():
        if type(child) is dict:
            hasNoRed = True
            # find out if it has an property with value "red"
            for property in child.values():
                if (type(property) is unicode) and (property == "red"):
                    reds += 1
                    hasNoRed = False

            if hasNoRed:
                total += countNumbers(child)

        elif type(child) is list:
            total += countNumbersinList(child)

        elif type(child) is int:
            total += int(child)

        elif type(child) is unicode:
            pass

    return total

def countNumbersinList(aList):
    global reds
    total = 0
    for item in aList:
        #print type(item)
        if type(item) is dict:
            #total += countNumbers(item)
            hasNoRed = True
            # find out if it has an property with value "red"
            for property in item.values():
                if (type(property) is unicode) and (property == "red"):
                    reds += 1
                    hasNoRed = False

            if hasNoRed:
                total += countNumbers(item)

        elif type(item) is list:
            total += countNumbersinList(item)
        elif type(item) is int:
            total += int(item)
        elif type(item) is unicode:
            pass

    return total

print countNumbersinList(jsonObj)


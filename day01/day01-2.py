# 1795
# find first location where floor = -1
# first char in input is location = 1

import sys

filename = sys.argv[1]
with open(filename, 'r') as inputFile:
    content = inputFile.read()

directions = list(content)

floor = 0
finalStep = 0
for index in range(0, len(directions)) :
    if (directions[index] == "(") :
        floor += 1
    else:
        floor -= 1

    if (floor < 0) :
        finalStep = index + 1
        break

print finalStep

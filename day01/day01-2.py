# 1795
# find first location where floor = -1
# first char in input is location = 1

import sys

directions = list(open(sys.argv[1], 'r').read())

floor = 0
index = 0
for step in directions :
    floor += 1 if step == '(' else -1

    if (floor < 0) :
        break

    index += 1

print(index + 1)

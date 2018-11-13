# 3 compartments -> 11846773891
# 4 compartments -> 80393059
# there is no day 2 file, just change divisor on thirdWeight.
# https://adventofcode.com/2015/day/24

import sys
import itertools
import pprint

filename = sys.argv[1]
with open(filename, 'r') as inputFile:
    lines = inputFile.readlines()

boxes = map(lambda x : int(x), lines)

# look for one box, then two, the three, etc, boxes
# until you get a group that is 1/3 of the total weight
found = False
count = 1
totalWeight = sum(boxes)
thirdWeight = totalWeight / 3
thirdGroups = []
while not found:
    thirdGroups = []
    groups = itertools.combinations(boxes, count)
    glist = list(groups)
    for g in glist:
        if sum(g) == thirdWeight:
            thirdGroups.append(g)
            found = True
    count += 1

# now you have the third groups
# find the one with the lowest product
lowestProduct = thirdWeight ** count
lowestGroup = []
for tg in thirdGroups:
    product = reduce(lambda x, y : x * y, tg)
    if product < lowestProduct:
        lowestProduct = product
        lowestGroup = tg

print lowestProduct, lowestGroup


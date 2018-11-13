# 4372
# find all combinations of containers that add up to 150
# https://adventofcode.com/2015/day/17

import sys
import pprint
import itertools

filename = sys.argv[1]

with open(filename, 'r') as inputFile:
    lines = inputFile.readlines()

sizes = list(map(lambda x : int(x), lines))

count = 0
for length in range(0, len(sizes)):
    containerSets = itertools.combinations(sizes, length)
    for oneSet in containerSets:
        capacity = sum(oneSet)
        if capacity == 150:
            #pprint.pprint(oneSet)
            count += 1

print count

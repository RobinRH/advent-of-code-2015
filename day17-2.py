# minimum number:  4
# number of sets:  4
# [(47, 31, 36, 36), (47, 31, 46, 26), (32, 36, 36, 46), (36, 32, 36, 46)]
# find the minimum number of containers to hold 150
# how many different ways to get that minimum
# https://adventofcode.com/2015/day/17

import sys
import pprint
import itertools

filename = sys.argv[1]

with open(filename, 'r') as inputFile:
    lines = inputFile.readlines()

sizes = list(map(lambda x : int(x), lines))

count = 0
minimum = len(sizes) + 1
minimumSets = []
for length in range(0, len(sizes)):
    containerSets = itertools.combinations(sizes, length)
    for oneSet in containerSets:
        capacity = sum(oneSet)
        if capacity == 150:
            count += 1
            if len(oneSet) < minimum:
                minimum = len(oneSet)
                minimumSets = [oneSet]
            elif len(oneSet) == minimum:
                minimumSets.append(oneSet)

print count
print "minimum number: ", minimum
print "number of sets: ", len(minimumSets)
pprint.pprint(minimumSets)

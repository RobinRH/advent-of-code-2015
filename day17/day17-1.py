# part 1: 4372
# part 2: 4
# find all combinations of containers that add up to 150
# https://adventofcode.com/2015/day/17

import sys
import itertools

filename = sys.argv[1]
with open(filename, 'r') as inputFile:
    sizes = [int(line) for line in inputFile.readlines()]

count = 0
for length in range(0, len(sizes)):
    containerSets = itertools.combinations(sizes, length)
    count += len([1 for oneset in containerSets if sum(oneset) == 150])

print('part 1: ', count)


# find all the set where capacity = 150
allSets = []
for length in range(0, len(sizes)):
    containerSets = itertools.combinations(sizes, length)
    allSets.extend([oneset for oneset in containerSets if sum(oneset) == 150])

minLength = min([len(x) for x in allSets])
minNumber = len([x for x in allSets if len(x) == 4])
print('part 2: ', minNumber)

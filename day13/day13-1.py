# 709
# https://adventofcode.com/2015/day/13

import sys
import itertools

# Alice would gain 54 happiness units by sitting next to Bob.
# Mallory gain 40 Eric
filename = sys.argv[1]
with open(filename, 'r') as inputFile:
    lines = [line.strip().replace('would ', '').replace('happiness units by sitting next to ', '').replace('.', '').split(' ') for line in inputFile.readlines()]

rules = {}
names = set()

for name1, gainLose, units, name2 in lines:
    rules[(name1, name2)] = int(units) if gainLose == 'gain' else -int(units)
    names = names.union(set([name1, name2]))

# create all possible seatings
# they're in an array, but we will treat it as a circular array
allSeatings = [list(s) for s in itertools.permutations(names)]

# find the total happiness for each possible seating
results = []
for seating in allSeatings:
    pairs = list(zip(seating, seating[1:] + [seating[0]]))
    happiness = sum([rules[(name1, name2)] + rules[(name2, name1)] for name1, name2 in pairs])
    results.append(happiness)

print(max(results))


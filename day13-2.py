# 668
# add self to the seating, all happiness 0
# https://adventofcode.com/2015/day/13

import sys
import pprint
import re
import itertools

filename = sys.argv[1]

with open(filename, 'r') as inputFile:
    lines = inputFile.readlines()

#Alice would gain 54 happiness units by sitting next to Bob.
#Alice would lose 81 happiness units by sitting next to Carol.
ruleExpr = re.compile('(?P<name1>.+) would (?P<gainLose>gain|lose) (?P<units>\d+) happiness units by sitting next to (?P<name2>.+)\.')
rules = {}
names = set()

# create a rule for each line in the input file
for line in lines:
    match = ruleExpr.match(line)
    if match:
        name1 = match.group('name1')
        name2 = match.group('name2')
        gainLose = match.group('gainLose')
        units = match.group('units')
        units = int(units)
        if gainLose == "lose":
            units = -units
        rules[(name1, name2)] = units
        names.add(name1)
        names.add(name2)

# add self to the rules (before adding self to names, or else you end up with rules of self-to-self)
for name in names:
    rules[(name, "self")] = 0
    rules[("self", name)] = 0

# add self to the names
names.add("self")

#pprint.pprint(lines)
#pprint.pprint(rules)
#pprint.pprint(names)

# create all possible seatings
# there in an array, but we will treat it as a circular array
allSeatings = list(itertools.permutations(names))

# find the total happiness for each possible seating
results = []
for seating in allSeatings:
    happiness = 0
    for index in range(0, len(seating)):
        name1 = seating[index]
        name2 = ""
        if index == len(seating) - 1:
            name2 = seating[0]
        else:
            name2 = seating[index+1]
        happiness += rules[(name1, name2)]  # A likes to sit by B
        happiness += rules[(name2, name1)]  # but maybe B doesn't like to sit by A
    results.append(happiness)

print max(results)


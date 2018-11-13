# 241
# the cats and trees readings indicates that there are greater than that many
# the pomeranians and goldfish readings indicate that there are fewer than that many
# https://adventofcode.com/2015/day/16


import sys
import pprint
import re

clues = {
    "children" : 3,
    "cats" : 7,
    "samoyeds" : 2,
    "pomeranians" : 3,
    "akitas" : 0,
    "vizslas" : 0,
    "goldfish" : 5,
    "trees" : 3,
    "cars" : 2,
    "perfumes" : 1,
}


filename = sys.argv[1]

with open(filename, 'r') as inputFile:
    lines = inputFile.readlines()

#Sue 1: goldfish: 9, cars: 0, samoyeds: 9
ruleExpr = re.compile('Sue (?P<id>\d+): (?P<name1>.+): (?P<number1>\d+), (?P<name2>.+): (?P<number2>\d+), (?P<name3>.+): (?P<number3>\d+)')

sues = {}
for line in lines:
    match = ruleExpr.match(line)
    if match:
        sueDict = {}
        sueDict[match.group('name1')] = int(match.group('number1'))
        sueDict[match.group('name2')] = int(match.group('number2'))
        sueDict[match.group('name3')] = int(match.group('number3'))
        sues[int(match.group('id'))] = sueDict


# look at each clue
# if a sue has that clue, but the number is not a match, eliminate that sue
for clue in clues.keys():
    # you can't modify a iterable in the loop (I don't think), so add a marker to ignore
    for sue in sues.keys():
        sueDict = sues[sue]
        if "skip" in sueDict.keys():
            continue

        number = clues[clue]

        # clue is a string like "goldfish"
        if clue == "cats" or clue == "trees":
            # the cats and trees readings indicates that there are greater than that many
            if clue in sueDict.keys() and sueDict[clue] <= number:
                sueDict["skip"] = 0
        elif clue == "pomeranians" or clue == "goldfish":
            # the pomeranians and goldfish readings indicate that there are fewer than that many
            if clue in sueDict.keys() and sueDict[clue] >= number:
                sueDict["skip"] = 0    
        else:
            if clue in sueDict.keys() and sueDict[clue] <> number:
                sueDict["skip"] = 0

# see what's left
for sue in sues.keys():
    sueDict = sues[sue]
    if "skip" in sueDict.keys():
        continue

    # only one should print out
    print(sue)





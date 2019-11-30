# 40
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

for clue, value in clues.items():
    sues = {id:s for id, s in sues.items() if (clue in s.keys() and s[clue] == value) or not clue in s.keys()}

print(list(sues.keys())[0])


# 2660
# 2503 seconds
# https://adventofcode.com/2015/day/14

import sys
import pprint
import re
import itertools

filename = sys.argv[1]
time = int(sys.argv[2])

with open(filename, 'r') as inputFile:
    lines = inputFile.readlines()

# Vixen can fly 19 km/s for 7 seconds, but then must rest for 124 seconds.
ruleExpr = re.compile('(?P<name>.+) can fly (?P<speed>\d+) km/s for (?P<move>\d+) seconds, but then must rest for (?P<rest>\d+) seconds\.')
rules = {}

# create a rule for each reindeer
for line in lines:
    match = ruleExpr.match(line)
    if match:
        name = match.group('name')
        speed = int(match.group('speed'))
        move = int(match.group('move'))
        rest = int(match.group('rest'))
        rules[name] = (speed, move, rest)

# run a counter for each second
distances = {}
for name in rules.keys():
    speed = rules[name][0]
    move = rules[name][1]
    rest = rules[name][2]
    # print name, speed, move, rest

    distance = 0
    moving = True
    resting = False
    moveCount = 0
    restCount = 0
    for tick in range(0,time):
        if moving:
            distance += speed
            moveCount += 1
            if moveCount == move:
                moveCount = 0
                resting = True
                restCount = 0
                moving = False
        else:
            restCount += 1
            if restCount == rest:
                restCount = 0
                moveCount = 0
                resting = False
                moving = True
    
    distances[name] = distance

pprint.pprint(distances)
print max(distances.values())
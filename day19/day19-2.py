# 195, might have to run it several times
# https://adventofcode.com/2015/day/19

import sys
import re
import pprint
import random

rulesFilename = sys.argv[1]
with open(rulesFilename, 'r') as inputFile:
    lines = inputFile.readlines()

# Al => ThF
# Al => ThRnFAr

replacements = {}
ruleExpr = re.compile('(?P<in>.+) => (?P<out>.+)')
for line in lines:
    if line == "":
        break
    match = ruleExpr.match(line)
    if match:
        replacements[match.group('out')] = match.group('in')


input = lines[-1]

sortedRules = sorted(replacements.keys())

srules = sorted(replacements.keys() , key = len, reverse = True)

keysShuffled = list(replacements.keys())

random.shuffle(keysShuffled)

current = input
found = False
while not found:
    current = input
    count = 0
    mutations = 0
    random.shuffle(keysShuffled)
    while input != 'e':
        for s in keysShuffled:
            mutations += current.count(s)
            current = current.replace(s, replacements[s])
        count += 1
        if count > 20:
            # print('might need to rerun several times to get answers, uses randomization')
            # print(current)
            break
        if current == 'e':
            found = True
            # pprint.pprint(keysShuffled)
            # print(mutations)
            break

print(mutations)


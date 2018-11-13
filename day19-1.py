# 509
# https://adventofcode.com/2015/day/19

import sys
import re
import pprint

rulesFilename = sys.argv[1]
with open(rulesFilename, 'r') as inputFile:
    lines = inputFile.readlines()

#stringFilename = sys.argv[2]
#with open(stringFilename, 'r') as stringFile:
#    input = stringFile.read()

# Al => ThF
# Al => ThRnFAr

replacements = []
ruleExpr = re.compile('(?P<in>.+) => (?P<out>.+)')
for line in lines:
    if line == "":
        break
    match = ruleExpr.match(line)
    if match:
        replacements.append((match.group('in'), match.group('out')))

input = lines[-1]

words = set()
# only replace one at a time
for repl in replacements:

    starts = []
    for match in re.finditer(repl[0], input):
        starts.append(match.start())

    for start in starts:
        # get string before start
        part1 = input[:start]
        # get second part of string
        part2 = input[start + len(repl[0]):]
        word = "".join((part1, repl[1], part2))
        #print word 
        words.add(word)

print len(words)



# 509
# https://adventofcode.com/2015/day/19

import sys
import re
import pprint

# Al => ThRnFAr
rulesFilename = sys.argv[1]
with open(rulesFilename, 'r') as inputFile:
    lines = [line.strip().replace('=> ', '').split(' ') for line in inputFile.readlines()]

replacements = [(a, b) for a, b in lines[0:len(lines)-2]]
input = lines[-1][0]

words = set()
# only replace one at a time
for repl in replacements:
    starts = [match.start() for match in re.finditer(repl[0], input)]
    length = len(repl[0])
    additions = [input[:start] + repl[1] + input[start + length:] for start in starts]
    words.update(additions)

print(len(words))



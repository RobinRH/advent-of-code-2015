# 156366
# total up all the integers found in the json input
# https://adventofcode.com/2015/day/12

import sys
import re

filename = sys.argv[1]
with open(filename, 'r') as inputFile:
    json = inputFile.read()

# use regex to find all the integers
numbers = re.findall('-?\d+', json)

# map strings to ints
numbers = [int(x) for x in numbers]

# sum
print(sum(numbers))

# 1350
# Disregarding the whitespace in the file, 
# what is the number of characters of code for string literals 
# minus the number of characters in memory for the values of the strings in total for the entire file?

import sys

filename = sys.argv[1]
with open(filename, 'r') as inputFile:
    lines = [line.strip() for line in inputFile.readlines()]

totalOutside = 0
totalInside = 0
for line in lines:
    totalOutside += len(line)
    bline = bytes(line, encoding='utf-8')
    totalInside += len(bytes(bline.decode('unicode_escape'), 'latin1')) - 2

print(totalOutside - totalInside)

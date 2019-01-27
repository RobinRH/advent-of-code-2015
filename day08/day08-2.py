# 2085
# Disregarding the whitespace in the file, 
# what is the number of characters of code for string literals 
# minus the number of characters in memory for the values of the strings in total for the entire file?

import sys

filename = sys.argv[1]
with open(filename, 'r') as inputFile:
    lines = inputFile.readlines()

lines = list(map(lambda s: s.strip(), lines))

totalOutside = 0
totalInside = 0
totalEscaped = 0
for line in lines:
    totalOutside += len(line)
    # take off the opening and closing quote
    shortLine = line[1:-1]
    escapeBack = shortLine.replace("\\", "*").replace("*", "\\\\")
    escapeQuote = escapeBack.replace("\"","\\\"")
    quoted = "\"\\\"" + escapeQuote + "\"\\\""
    #print line
    #print escapeQuote
    #print quoted
    totalEscaped += len(quoted)


print totalEscaped - totalOutside
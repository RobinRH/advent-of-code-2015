# 74 = 3537 - 3463

import sys

filename = sys.argv[1]
with open(filename, 'r') as inputFile:
    content = inputFile.read()

directions = list(content)

# ( is up one floor
# ) is down one floor
# destination = numberUp - numberDown

numberUp = len(list(filter(lambda s : s == "(", directions)))
numberDown = len(list(filter(lambda s : s == ")", directions)))
print numberUp - numberDown

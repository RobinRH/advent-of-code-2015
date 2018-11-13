# 69
# It contains a pair of any two letters that appears at least twice in the string without overlapping, 
# like xyxy (xy) or aabcdefgaa (aa), but not like aaa (aa, but it overlaps).
# It contains at least one letter which repeats with exactly one letter between them, 
# like xyx, abcdefeghi (efe), or even aaa.

import sys
import string
import re

filename = sys.argv[1]
with open(filename, 'r') as inputFile:
    words = inputFile.readlines()

alphabet = list(string.ascii_lowercase)
def hasLetterRepeat(word):
    for letter in alphabet:
        p = re.compile('.*' + letter + '.' + letter)
        m = p.match(word)
        if m:
            return True

    return False

def hasTwoRepeat(word):
    # make list of all the pairs
    pairs = set()
    chars = list(word)
    for index in range(0, len(word) - 1):
        pairs.add(chars[index] + chars[index+1])

    for pr in pairs:
        expr = ".*" + pr + ".*" + pr
        p = re.compile(expr)
        m = p.match(word)        
        if m:
            return True
        
    return False

nice = 0
for word in words:
    word = word.strip()
    if not hasLetterRepeat(word):
        continue

    if not hasTwoRepeat(word):
        continue

    print word
    nice += 1


print(nice)


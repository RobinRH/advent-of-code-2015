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

words = [word.strip() for word in words]

alphabet = list(string.ascii_lowercase)
def hasLetterRepeat(word):
    for letter in alphabet:
        p = re.compile('.*' + letter + '.' + letter)
        m = p.match(word)
        if m:
            return True

    return False

def hasTwoRepeat(word):
    for index in range(0, len(word) - 4+ 1):
        if (word[index:index+2] in word[index+2:]):
            return True
    
    return False

nice = sum([hasLetterRepeat(word) and hasTwoRepeat(word) for word in words])

print(nice)


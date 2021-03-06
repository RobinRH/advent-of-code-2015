# 238
# It contains at least three vowels (aeiou only), like aei, xazegov, or aeiouaeiouaeiou.
# It contains at least one letter that appears twice in a row, like xx, abcdde (dd), or aabbccdd (aa, bb, cc, or dd).
# It does not contain the strings ab, cd, pq, or xy, even if they are part of one of the other requirements.

import sys

filename = sys.argv[1]
with open(filename, 'r') as inputFile:
    words = inputFile.readlines()

def hasDouble(string):
    chars = list(string)
    for index in range(0, len(chars)-1):
        if chars[index] == chars[index+1]:
            return True
    
    return False

nice = 0
for word in words:

    vowelCount = sum([word.count(vowel) for vowel in list('aeiou')])
    if vowelCount < 3:
        continue

    if not hasDouble(word):
        continue

    if "ab" in word:
        continue

    if "cd" in word:
        continue

    if "pq" in word:
        continue

    if "xy" in word:
        continue

    nice += 1


print(nice)



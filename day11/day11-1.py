# next: cqjxxyzz
# next: cqkaabcc
# input: cqjxjnds
# test input: abcdefgh output: abcdffaa
# test input: ghijklmn output: ghjaabcc
# https://adventofcode.com/2015/day/11

# ord (returns number) and chr (returns letter)

import sys
import string

input = sys.argv[1]

def incrementByPlace(password, place):

    if place < 0:
        print("error")
        return

    if password[place] != 'z':
        # increment the place
        index = ord(password[place])
        newChar = chr(index+1)
        newPassword = password[0:place] + newChar + password[place + 1:]
        return newPassword
    else:
        # set place equal to a and increment next place
        newPassword = password[0:place] + "a" + password[place + 1:]
        newPassword = incrementByPlace(newPassword, place - 1)
        return newPassword

# Passwords must include one increasing straight of at least three letters, 
# like abc, bcd, cde, and so on, up to xyz. They cannot skip letters; abd doesn't count.
def containsStraight(password):
    for index in range(len(password) - 3):
        i1, i2, i3 = [ord(x) for x in password[index:index+3]]
        if (i2 == i1 + 1) and (i3 == i1 + 2):
            return True

    return False

# Passwords may not contain the letters i, o, or l, 
# as these letters can be mistaken for other characters and are therefore confusing.
def noIOL(password):
    if 'i' in password:
        return False

    if 'o' in password:
        return False

    if 'l' in password:
        return False

    #print "no iol: ", password
    return True

# Passwords must contain at least two different, non-overlapping pairs of letters, like aa, bb, or zz.
# create all the pairs
pairs = [c + c for c in string.ascii_lowercase]

def hasPairs(password):
    number = sum([password.count(p) for p in pairs])
    return number >= 2

total = 0
while total < 2:
    input = incrementByPlace(input, len(input) - 1)
    if noIOL(input) and containsStraight(input) and hasPairs(input):
        print(input)
        total += 1

# 74 = 3537 - 3463

import sys

directions = list(open(sys.argv[1], 'r').read())

# ( is up one floor
# ) is down one floor
# destination = numberUp - numberDown

numberUp = directions.count('(')
numberDown = directions.count(')')
print(numberUp - numberDown)

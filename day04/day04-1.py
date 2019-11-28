# 282749
# find lowest start+integer, such that MD4 hex digest starts with "00000"

import hashlib

start = 'yzbqklnj'
count = 0

for count in range(0, 2000000):
    string = start + str(count)
    m = hashlib.md5()
    m.update(string.encode('utf-8'))
    digest = m.hexdigest()
    if str(digest).startswith("00000"):
        print(count, digest)
        break

# 9962624 (takes 3 minutes or so)
# find lowest start+integer, such that MD4 hex digest starts with "000000"

import hashlib

start = 'yzbqklnj'
count = 0

found = False
while not found:
    string = start + str(count)
    m = hashlib.md5()
    m.update(string.encode('utf-8'))
    digest = m.hexdigest()
    if str(digest).startswith("000000"):
        print(count, digest)
        break
    count += 1

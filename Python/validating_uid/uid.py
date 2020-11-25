'''
For teach test case T, print "valid" or "invalid" if T is a valid
UID or not on separate lines.The qualifications for validity
are in the description.
'''

import re

filter = re.compile(r'(?!.*(.).*\1)(?=.*\d.*\d.*\d)(?=.*[A-Z].*[A-Z])[A-Za-z0-9]{10}')

t = int(input())

for _ in range(t):
    uid = input()
    if filter.match(uid):
        print('Valid')
    else:
        print('Invalid')

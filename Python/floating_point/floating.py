'''
Given string N determine whether N is a floating point number.
'''

import re

for _ in range(int(input())):
    print(bool(re.match("^[\+-]?\d*\.\d+$", input())))

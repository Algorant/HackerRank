'''
Given a string S, find the indices of the start and end of
string k in S.
'''

import re

S, k = input(), input()

m = re.search(k, S)
pattern = re.compile(k)
if not m: print("(-1, -1)")
while m:
    print("({0}, {1})".format(m.start(), m.end() -1 ))
    m = pattern.search(S, m.start() + 1)

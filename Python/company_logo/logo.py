'''
Given a string S, find the 3 most common characters and print
their occurences on a separate line.

If they are the same, sort in alphabetical order.
'''

from collections import Counter, OrderedDict

chars = Counter(input()).items()

for char, n in sorted(chars, key=lambda c: (-c[1], c[0]))[:3]:
    print(char, n)

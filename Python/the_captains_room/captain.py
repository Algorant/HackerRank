'''
In an unordered list of integers, find the one that does
not repeat.
'''

from collections import Counter

n = int(input())
rooms = [int(x) for x in input().split()]
count = Counter(rooms)

for k, v in count.items():
    if v == 1:
        print(k)
        break

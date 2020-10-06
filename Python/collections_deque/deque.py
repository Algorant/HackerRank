'''
Given empty double ended queue, perform various operations
on it and then return the space separated result of the
queue.
'''

from collections import deque

d = deque()

for _ in range(int(input())):
    method, *n = input().split()
    getattr(d, method)(*n)

print(*d)

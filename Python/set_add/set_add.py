'''
Given an integer and a list of items as input,
use set.add function to count the number
of unique items in the set.
'''

n = int(input())
s = set()
for i in range(n):
    s.add(input())
print(len(s))

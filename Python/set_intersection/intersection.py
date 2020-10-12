'''
Given integers n and b, and two lists of that size
that denote students with English and French newspaper subscriptions,
output the number of students that have both subscriptions.
'''

_, a = input(), set(input().split())
_, b = input(), set(input().split())

print(len(a.intersection(b)))

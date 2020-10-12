'''
Given integers n and b, and two lists of that size
that denote students with English and French newspaper subscriptions,
output the number of students that subscribe to English paper only.
'''

_, a = input(), set(input().split())
_, b = input(), set(input().split())

print(len(a.difference(b)))

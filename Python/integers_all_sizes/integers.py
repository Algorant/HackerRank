'''
Given 4 integers as inputs:
a b c d, return a ^ b + c ^ d
'''


a, b, c, d = (int(input()) for _ in range(4))

print((a**b) + (c**d))

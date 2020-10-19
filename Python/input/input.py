'''
Given x, k, and a polynomial P, verify P(x) = k.
'''

x, k = map(int, input().split())
print(k==eval(input()))

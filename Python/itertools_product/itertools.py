'''
Given two lists A and B, find the cartesian product of A and B.
'''


from itertools import product

a = list(map(int, input().split()))

b = list(map(int, input().split()))

print(*list(product(a,b))) # asterisk unpacks both lists, product finds product

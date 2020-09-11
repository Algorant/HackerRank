'''
Given string S and integer k, find all permutations within S of size k.
'''


from itertools import permutations

S, k = input().split(" ")
permutations = list(permutations(S, int(k)))
permutations.sort()

for i in permutations:
    print("".join(i))

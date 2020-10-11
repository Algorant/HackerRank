'''
Given a list l of characters of length n,
return the probability of permutations of the list
containing the letter 'a' given a permutation
length of integer k.
'''

from itertools import combinations

n = int(input())
l = input().split()
k = int(input())

C = list(combinations(l, k))
f = filter(lambda c: 'a' in c, C)
print("{0:.3}".format(len(list(f))/len(C)))

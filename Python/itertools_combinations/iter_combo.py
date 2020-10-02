'''
Given string S and number of combinations k, use itertools.combinations
module to find all permutations of string S of size k in sorted order.
'''


from itertools import combinations


S, k = input().split()

for i in range(int(k)):
    print(*map("".join, combinations(sorted(S), i + 1)), sep='\n')

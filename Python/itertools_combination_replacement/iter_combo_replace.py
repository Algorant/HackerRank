'''
Given string S, print all possible k replacement
combinations in lexigraphical sorted order. Output
on separate lines.
'''

from itertools import combinations_with_replacement as combo

S, k = input().split()

for c in combo(sorted(S), int(k)):
    print("".join(c))

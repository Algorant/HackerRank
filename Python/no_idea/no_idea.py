'''
Given various inputs.

Find the "happiness" of the inputs given
that integers in A increase happiness by 1,
and integers in B decrease happiness by 1.
'''




_ = input()

sc_ar = input().split()


A = set(input().split())

B = set(input().split())

print(sum([(i in A) - (i in B) for i in sc_ar]))

'''
Given two arrays A and B, find the inner and outer product and
print them.
'''

import numpy as np

A = np.array(input().split(), int)
B = np.array(input().split(), int)

print(np.inner(A,B), np.outer(A,B), sep="\n")

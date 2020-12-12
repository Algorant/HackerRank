'''
Given a 1-D array A, print the floor, ceiling, and rint of all
elements of A.
'''

import numpy as np

# must be in code for it to work
np.set_printoptions(legacy = '1.13')

A = np.array(input().split(), float)

print(np.floor(A), np.ceil(A), np.rint(A), sep="\n")

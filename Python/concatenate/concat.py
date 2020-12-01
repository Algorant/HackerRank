'''
Given two arrays of size NxP and MxP (N, M rows and P column) your task is to
concatenate the arrays along axis 0.
'''

import numpy as np

N, M, P = map(int, input().split())

a = np.array([input().split() for i in range(N)], int)
b = np.array([input().split() for i in range(M)], int)

print(np.concatenate((a, b), axis=0))

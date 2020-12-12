'''
Given a square matrix A with dimensions N x N, find the determinant.
'''

import numpy as np
# This line is needed due to HackerRank np being legacy
np.set_printoptions(legacy='1.13')

N = int(input())
A = np.array([input().split() for _ in range(N)], float)

print(np.linalg.det(A))

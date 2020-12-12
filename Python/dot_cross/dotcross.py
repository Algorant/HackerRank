'''
Given two arrays A and B of dimension N x N, print the matrix
multiplication of A and B.
'''

import numpy as np

N = int(input())

A = np.array([input().split() for _ in range(N)], int)
B = np.array([input().split() for _ in range(N)], int)

print(np.matmul(A, B))

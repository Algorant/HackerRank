'''
Given an N x M integer array matrix with space separated elements,
print the transpose and flatten results.
'''

import numpy as np

N, M = list(map(int, input().split()))

a = np.array([input().split() for _ in range(N)], int)

print(a.T, a.flatten(), sep='\n')

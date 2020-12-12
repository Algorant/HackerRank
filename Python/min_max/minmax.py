'''
Given a 2-D array with dimensions N x M, perform the min function
over axis 1 and find the max of that.
'''

import numpy as np

N, M = map(int, input().split())

arr = np.array([input().split() for _ in range(N)], int)

print(np.max(np.min(arr, axis=1), axis=0))

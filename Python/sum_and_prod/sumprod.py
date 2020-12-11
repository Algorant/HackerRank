'''
Given a 2-D array with dimensions NxM, preform the sum axis 0 and
then find the prduct of that result.
'''

import numpy as np

N, M = map(int, input().split())

array = np.array([input().split() for _ in range(N)], int)

print(np.prod(np.sum(array, axis=0), axis=0))

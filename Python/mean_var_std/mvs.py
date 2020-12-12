'''
Given a 2D array of size NxM, find the mean along axis 1, the var along axis 0,
the std along axis None.
'''

# Warning: There is an error in the submitting of this on HackerRank. It uses
# an old version of Numpy and therefore the answer is correct, but formatting
# makes it show as incorrect.

import numpy as np

# this line is needed for formatting
np.set_printoptions(legacy='1.13')

N, M = map(int, input().split())

arr = np.array([input().split() for _ in range(N)], int])

print(np.mean(arr, axis=1),
      np.var(arr, axis=0),
      np.std(arr), sep="\n")

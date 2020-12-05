'''
Given the shape of an array in the form of space separated integers, use numpy
functions zeros and ones to print an array of the given shape
'''

import numpy as np

dimensions = tuple(map(int, (input().strip().split()))

zeros = np.zeros(dimensions, dtype=np.int)

ones = np.ones(dimensions, dtype=np.int)

print(zeroes)
print(ones)

'''
Convert a list of 9 space separated integers into a 3x3 numpy array.
'''

import numpy as np

array = np.array(list(map(int, input().split())))

print(np.reshape(array,(3,3)))

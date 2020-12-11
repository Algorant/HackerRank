'''
Print an array of size N x M with its main diagonal elements as 1s, and 0s everywhere else.
'''

import numpy as np

# must add this line for formatting
np.set_printoptions(legacy='1.13')

print(np.eye(*map(int, input().split())))

'''
Given a space separated list of numbers, print a reversed NumPy array with
element type float.
'''


# # How I would do it
#
# import numpy as np
#
# a = np.array(arr([::-1], float)
#
# print(a)

# How the coding example makes you do it

import numpy

def arrays(arr):
   return numpy.array(arr[::-1], float)

arr = input().strip().split(' ')
result = arrays(arr)
print(result)

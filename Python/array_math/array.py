'''
Given two integer arrays A and B, of dimensions NxM, perform the
following operations:

Add
Subtract
Multiply
Integer Division
Mod
Power

Print the result
'''

import numpy as np

N, M = map(int, input().split())

A = np.array([input().split() for _ in range(N)], int)
B = np.array([input().split() for _ in range(N)], int)

print(np.add(A,B),
      np.subtract(A,B),
      np.multiply(A,B,),
      np.floor_divide(A,B),
      np.mod(A,B),
      np.power(A,B), sep = "\n")

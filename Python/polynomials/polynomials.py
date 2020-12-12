'''
Given the coefficients of a polynomial P, find the value of P at
point x.
'''

import numpy as np

coeffs = list(map(float, input().split()))

x = input()

print(np.polyval(coeff, int(x)))

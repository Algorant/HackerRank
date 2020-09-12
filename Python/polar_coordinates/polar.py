'''
Given complex number r as input, calculate the polar coorndinates
of r using cmath module.
'''

import cmath

r = complex(input().strip())

print(cmath.polar(r)[0])
print(cmath.polar(r)[1])

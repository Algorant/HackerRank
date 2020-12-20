"""
A left rotation shifts each element in the array 1 unit to the left.

Given an array of a of n integers, and a number d, perform d left rotations
on the array. Return the updated array printed as single line of space-separated
integers.
"""

import math
import os
import random
import re
import sys

# Complete the rotLeft function below.
def rotLeft(a, d):
    for i in range(d):
        a.append(a.pop(0))
    return a

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    nd = input().split()

    n = int(nd[0])

    d = int(nd[1])

    a = list(map(int, input().rstrip().split()))

    result = rotLeft(a, d)

    fptr.write(' '.join(map(str, result)))
    fptr.write('\n')

    fptr.close()

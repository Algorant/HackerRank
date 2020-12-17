'''
Given some starter code, complete the function such that n number of socks
within an array ar are paired to each other.

Return the total number of matching pairs of sucks that can be sold.
'''

import math
import os
import random
import re
import sys

# Complete the sockMerchant function below.
def sockMerchant(n, ar):
    pairs = 0
    d = {}
    for i in range(n):
        if ar[i] in d:
            d.pop(ar[i])
            pairs += 1
        else:
            d[ar[i]] = 1
    return pairs

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    ar = list(map(int, input().rstrip().split()))

    result = sockMerchant(n, ar)

    fptr.write(str(result) + '\n')

    fptr.close()

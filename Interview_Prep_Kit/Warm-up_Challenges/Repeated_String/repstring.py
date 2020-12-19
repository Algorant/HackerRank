'''
Given string s of lowercase letters that is repeated infinitely many times,
find the number of occurrences of the letter 'a' within the string of given
length n.
'''

import math
import os
import random
import re
import sys

# Complete the repeatedString function below.
def repeatedString(s, n):
    a_count = s.count('a')
    length = n // len(s)
    if n % len(s) == 0:
        a_count = a_count * length
    else:
        tail = n % len(s)
        a_count = a_count * length + s[:tail].count('a')
    return a_count
    
    # repetitions needed = n // len(s)
    # iterate through that length of string
    # if char == a, count += 1


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    n = int(input())

    result = repeatedString(s, n)

    fptr.write(str(result) + '\n')

    fptr.close()

'''
For each game, you will get an array of clouds numbered if they are safe or
if they must be avoided.

Complete the jumpingOnClouds function in the editor below.

Determine the minimum number of jumps it will take to jump from the starting
postion to the last cloud. It is always possible to win the game.

Print the minimum number of jumps needed to win the game.
'''

import math
import os
import random
import re
import sys

# Complete the jumpingOnClouds function below.
def jumpingOnClouds(c):
    i = jumps = 0
    length = len(c)
    while i < length - 1:
        if i < length - 2 and c[i + 2] == 0:
            i += 2
        else:
            i += 1
        jumps += 1

    return jumps



if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    c = list(map(int, input().rstrip().split()))

    result = jumpingOnClouds(c)

    fptr.write(str(result) + '\n')

    fptr.close()

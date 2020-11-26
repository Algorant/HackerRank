'''
Decode the script given according to the instructions to be able to decipher
the words between the characters. Print the decoded message.
'''


# Most of this code is already given in the problem

import math
import os
import random
import re
import sys




first_multiple_input = input().rstrip().split()

n = int(first_multiple_input[0])

m = int(first_multiple_input[1])

matrix = []

for _ in range(n):
    matrix_item = input()
    matrix.append(matrix_item)

li = ''

for i in range(m):
    for item in matrix:
        li += item[i]

print(re.sub(r'(?<=[\w])[\W\s]+(?=[\w])', ' ' , li) )

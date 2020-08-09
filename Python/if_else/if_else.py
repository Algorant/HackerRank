# if n is odd print Weird
# if n is even and between 2-5 inclusive, Not Weird
# if n is even and 6-20 inclusive, Weird
# if n is even and greater than 20, Not Weird

import math
import os
import random
import re
import sys


# Instantiate file with input

if __name__ == '__main__':
    n = int(input())

# Logic for solution
if n % 2 == 0:
  if n in range(2,6):
    print("Not Weird")

  elif n in range(6,21):
    print("Weird")

  elif n > 20:
    print("Not Weird")

else:
  print("Weird")

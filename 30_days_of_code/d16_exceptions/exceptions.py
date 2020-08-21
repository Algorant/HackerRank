#!/bin/python3

import sys

# Read a string, , and print its integer value; if cannot be converted
# to an integer, print Bad String.

S = input().strip()

try: print(int(S))
except: print("Bad String")

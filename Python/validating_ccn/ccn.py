'''
Print "Valid" if a credit card number is valid, otherwise print "Invalid".
The characteristics for what count validity are given in the instructions.
'''

import re

filter = re.compile(
    r"^"
    r"(?!.*(\d)(-?\1){3})"
    r"[456]"
    r"\d{3}"
    r"(?:-?\d{4}){3}"
    r"$")

for _ in range(int(input().strip())):
    print("Valid" if filter.search(input().strip()) else "Invalid")

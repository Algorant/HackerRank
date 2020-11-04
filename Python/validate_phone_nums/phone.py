'''
For every string listed, print YES if it is a valid phone number,
and NO if it is not on separate lines.
'''

import re

for _ in range(int(input())):
    str = input()

    if re.match(r"^[789]{1}\d{9}$", str):
        print("YES")

    else:
        print("NO")

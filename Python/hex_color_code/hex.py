'''
Given N lines of CSS code, print all valid Hex Color codes,
in order of occurrence from top to bottom.
'''

import re

for i in range(int(input())):
    match = re.findall(r':?.(#[0-9a-fA-F]{6}|#[0-9a-fA-F]{3})', input())

    if match:
        print(*match, sep='\n')

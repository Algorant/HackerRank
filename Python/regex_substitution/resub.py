'''
Given a text of N lines, which contain && and || symbols,
modify the symbols to be && > and and || > or.

Both && and || should have a space "" on both sides.
'''

import re

for _ in range(int(input())):
    print(re.sub(r'(?<= )(\&\&|\|\|)(?= )', (lambda m: 'and' \

    if m.group(1) == '&&' \

    else 'or'), input()))

'''
Verify if a given regex string is valid or not,
prints True or False for each string.
'''


import re

def val_regex(regex):
    try:
        re.compile(regex)

    except re.error:
        return False

    return True

for i in range(int(input())):
    print(val_regex(input()))

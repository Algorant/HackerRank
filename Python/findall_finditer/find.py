'''
Given a string S, consisting of alphanumeric characters, spaces, and
symbols, find all the substrings of S that contain 2 or more vowels.

The substrings should lie between 2 consonants and should contain
vowels only.
'''

import re

vowels = 'aeiou'
consonants = 'bcdfghjklmnpqrstvwxyz'
regex = '(?<=[' + consonants + '])([' + vowels + ']{2,})[' + consonants + ']'

match = re.findall(regex, input(), re.IGNORECASE)

if match:
    print(*match, sep='\n')
else:
    print('-1')

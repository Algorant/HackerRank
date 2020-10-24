'''
Given a string s, use regex module split to split all of
the , and . symbols in s.
'''

# Most of this code is given in example problem.

regex_pattern = r"\D+"	# Do not delete 'r'.

import re
print("\n".join(re.split(regex_pattern, input())))

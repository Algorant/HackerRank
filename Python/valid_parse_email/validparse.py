'''
Given n pairs of names and email addresses as input, print each name and
email address pair having a valid email address on a new line.
'''

import email.utils
import re

N = input()
for _ in range(int(N)):
    email_inpt = email.utils.parseaddr(input())

    if bool(re.match('[a-zA-Z](\w|-|\.)*@[a-zA-Z]*\.[a-zA-Z]{0,3}$', email_inpt[1])):
        print(email.utils.formataddr(email_inpt))

'''
Given a list of first name and emails, create a function
that returns the first name of the entries with emails
ending in '@gmail.com'
'''

import re
import sys

if __name__ == '__main__':
    names = []
    N = int(input())

    for N_itr in range(N):
        firstNameEmailID = input().split()

        firstName = firstNameEmailID[0]

        emailID = firstNameEmailID[1]

        # use regex to search for gmails, take name and append to list
        if re.search(r"@gmail.com$", emailID):
            names.append(firstName)

    print(*sorted(names),sep='\n') #print names separated by newline

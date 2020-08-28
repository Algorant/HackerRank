'''
Given string s capitalize first letter of every
space-separated word in the string.
'''

s = str(input())


def solve(s):
    s = s.split(" ")
    return(" ".join(i.capitalize() for i in s))


# print(solve(s)) # not used on site, just for testing

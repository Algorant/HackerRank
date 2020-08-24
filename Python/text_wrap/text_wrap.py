'''
Given string S and width w: wrap the string into a paragraph of width w
'''

import textwrap #textwrap module does all work here, is imported in exercise

def wrap(string, max_width):
    return textwrap.fill(string,max_width)

if __name__ == '__main__':
    string, max_width = input(), int(input())
    result = wrap(string, max_width)
    print(result)

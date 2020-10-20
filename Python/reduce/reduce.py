'''
Given list of n pairs of rational numbers,
use reduce to return the product of each pair
of numbers as numerator/denominator fraction
by every fraction in list n.
'''

# some of this code is supplied to user

from fractions import Fraction
from functools import reduce

def product(fracs):
    t = reduce(lambda x, y: x * y, fracs)
    return t.numerator, t.denominator

if __name__ == '__main__':
    fracs = []
    for _ in range(int(input())):
        fracs.append(Fraction(*map(int, input().split())))
    result = product(fracs)
    print(*result)

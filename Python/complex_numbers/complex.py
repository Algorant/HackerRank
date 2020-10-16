'''
Given two complex numbers, find the result of their addition, subtraction,
multiplication, division, and modulus operations.
'''

import math

class Complex(object):
    def __init__(self, real, imag):
        self.real = real
        self.imag = imag

    def __add__(self, n):
        comp = n + complex(self.real, self.imag)
        return Complex(comp.real, comp.imag)

    def __sub__(self, n):
        comp = n - complex(self.real, self.imag)
        return Complex(comp.real, comp.imag)

    def __mul__(self, n):
        comp = n * complex(self.real, self.imag)
        return Complex(comp.real, comp.imag)

    def __truediv__(self, n):
        comp = n / complex(self.real, self.imag)
        return Complex(comp.real, comp.imag)

    def mod(self):
        comp = complex(math.sqrt(self.real**2 + self.imag**2))
        return Complex(comp.real, comp.imag)

    def __str__(self):
        if self.imag == 0:
            result = "{:.2f}+0.00i".format(self.real)

        elif self.real == 0:
            if self.imag >= 0:
                result = "0.00+{:.2f}i".format(self.imag)
            else:
                result = "0.00-{:.2f}i".format(abs(self.imag))

        elif self.imag > 0:
            result = "{:.2f}+{:.2f}i".format(self.real, self.imag)
            
        else:
            result = "{:.2f}-{:.2f}i".format(self.real, abs(self.imag))

        return result

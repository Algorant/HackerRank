'''
Given an integer input: print the phrase "I implemented: AdvancedArithmetic"
and on the next line give the sum of all the divisors of the integer.
'''

class AdvancedArithmetic(object):
    def divisorSum(n):
        raise NotImplementedError

class Calculator(AdvancedArithmetic):
    def divisorSum(self, n):
        # begin with 0
        sum = 0
        for i in range(1,n+1):
            if n % i == 0: # determine if its factor
                sum += i # append to sum
        return sum


n = int(input())
my_calculator = Calculator()
s = my_calculator.divisorSum(n)
print("I implemented: " + type(my_calculator).__bases__[0].__name__)
print(s)

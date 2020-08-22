# Write a Calculator class with a single method: int power(int,int).
# The power method takes two integers, and , as parameters and returns the
# integer result of . If either or is negative, then the method must throw an
# exception with the message: n and p should be non-negative.

class Calculator:

    def power(self, n, p):
        self.n = n
        self.p = p
        if n < 0 or p < 0:
            raise Exception('n and p should be non-negative')
        else:
            return n ** p

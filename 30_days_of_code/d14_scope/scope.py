# Complete Difference class by writing:
# a class constructor that takes integers as a param and saves to
# elements variable, and a computeDifference method which finds maximum
# absolute difference between any 2 numbers and N.


class Difference:
    def __init__(self, a):
        self.__elements = a
        self.maximumDifference=abs(max(a) - min(a)) #add variable
    def computeDifference(self): # return the difference
        return self.maximumDifference

'''
Given array of length n find the average of the values
in the set of the array.
'''

def average(array):
    return sum(set(array)) / len(set(array))

'''
Bubble sorting algorithm that given integer n and array a, returns
the number of swaps, the first element, and the last element in an array
a of length n.
'''

import sys

n = int(input().strip())
a = list(map(int, input().strip().split(' ')))

def bub_sort(arr):
    swaps = 0 # count number of swaps
    for num in range(len(arr) -1, 0, -1):
        for i in range(num):
            if arr[i] > arr[i+1]: # do the swap if next number is larger
                arr[i], arr[i+1] = arr[i+1], arr[i]
                swaps = +=1
    return swaps

print("Array is sorted in {} swaps".format(bub_sort(a)))
print("First Element:", (a[0]))
print("Last Element:", a[-1]))

'''
Given X number of shoes,
a list of all shoe sizes,
number of customers N,
the value of shoe size and its price per customer:

Calculate the amount of money earned.
'''

import collections

num_shoes = int(input())
shoe_sizes = collections.Counter(map(int, input().split()))

revenue = 0

for _ in range(int(input())):
    size, price = map(int, input().split())
    if shoe_sizes[size]:
        revenue += price
        shoe_sizes[size] -= 1

print(revenue)

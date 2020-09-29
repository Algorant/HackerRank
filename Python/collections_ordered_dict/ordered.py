'''
Given a list of items with its name and price separated by a
space, print the item name and net price in order of its first
occurrence as output.
'''

from collections import OrderedDict

market_items = OrderedDict()

num_items = int(input())

for _ in range(num_items):
    *item, price = input().split()
    try:
        market_items[' '.join(item)] += int(price)
    except KeyError:
        market_items[' '.join(item)] = int(price)

for item in market_items:
    print(item, market_items[item])

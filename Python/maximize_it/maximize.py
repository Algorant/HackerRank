'''
Given various integer lists and a function given, find the
maximum value possible from the integers in each list.
'''

import itertools


k, m = map(int, input().split())

print(max(sum(j) % m for j in itertools.product(*((int(i) ** 2 \
      for i in input().split()[1:]) for _ in range(k)))))

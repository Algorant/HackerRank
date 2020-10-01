'''
Given 2 sets of integers: M and N, print their symmetric
difference in asending order. This means values that exist
in either M or N, but do not exist in both.
'''

M, m = input(), set(list(map(int, input().split())))
N, n = input(), set(list(map(int, input().split())))

s = sorted(list(m.difference(n)) + list(n.difference(m)))

for i in s:
    print(i)

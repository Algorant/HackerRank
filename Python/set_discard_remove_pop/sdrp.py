'''
Given integer n, set s, integer N, and various commands,
return the sum of the set after all commands have been input
as a single line.
'''


n = int(input())
s = set(map(int, input().split()))

for i in range(int(input())):
    eval('s.{0}({1})'.format(*input().split()+['']))

print(sum(s))

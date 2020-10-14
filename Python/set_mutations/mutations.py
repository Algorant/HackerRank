'''
Perform specific mutation operations on set A an N number
of other sets.  Perform the operations and print the sum
of elements from set A.
'''

input()

L = set(input().split())

for _ in range (int(input())):
    command, *args = input().split()
    getattr(L, command)(set(input().split()))

print(sum(map(int, L)))

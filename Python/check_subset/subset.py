'''
Check if a test set of integers is a subset of two other sets:
A and B.
'''


for i in range(int(input())):
    _, a = input(), set(map(int, input().split()))
    _, b = input(), set(map(int, input().split()))
    print(a.issubset(b))

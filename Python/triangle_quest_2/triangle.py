'''
Without using strings or 1 > for statements, return a palindromic
triangle of size positive integer N, which is given.
'''


for i in range(1, int(input()) + 1):
    print((10 ** i // 9) ** 2)

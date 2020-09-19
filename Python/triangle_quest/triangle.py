'''
Given integer n, create number triangle of size n-1
so if n = 5, return:

1
22
333
4444
'''


n = 5


for i in range(1, n):
    print(i * (10**i -1)//9)

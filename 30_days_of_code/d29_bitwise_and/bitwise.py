'''
Given set S from 1-N, find two integers A and B
from S such that A&B (bitwise and) is max possible,
but also less than given integer K
'''

# if __name__ == '__main__':
#     t = int(input())
#
#     for t_itr in range(t):
#         nk = input().split()
#
#         n = int(nk[0])
#
#         k = int(nk[1])


for i in range(int(input())):

    n,k=map(int,input().split())

    s=max(set(((k-1)&j)for j in range(1,n+1) if j!=k-1))

    print(s)

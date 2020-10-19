'''
Given N atheletes with M attributes and integer K,
sort the data by the Kth attribute.
'''

N, M = map(int, input().split())

rows = [input() for _ in range(N)]

K = int(input())

for row in sorted(rows, key=lambda row: int(row.split()[K])):
    print(row)

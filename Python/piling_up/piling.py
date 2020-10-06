'''
Given list of cubes of size n, denoted by length
as space separated integers, return whether
the cubes can be stacked on top of each other
such that the bottom cube is always larger than
the one stacked on top.
'''

from collections import deque


for _ in range(int(input())):
    _, queue = input(), deque(map(int, input().split()))

    for cube in reversed(sorted(queue)):
        if queue[-1] == cube:
            queue.pop()

        elif queue[0] == cube:
            queue.popleft()

        else:
            print('No')
            break

    else:
        print('Yes')

'''
Use the defaultdict container in Collections module
to find occurrences of words in two lists of given
length n and m.
'''

from collections import defaultdict

# Inputs

n, m = map(int, input().split(' '))

# Groups as lists

list1 = list()
for i in range(n):
    list1.append(input())

occurrences = list()
for i in range(m):
    occurrences.append(input())

# Calculate Output

def_dict = defaultdict(list)

# Fill with Inputs

for i in range(n):
    def_dict[list1[i]].append(i + 1)

# Print out answer

for i in occurrences:
    if i in def_dict:
        print(*def_dict[i])
    else:
        print(-1)

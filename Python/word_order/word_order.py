'''
Given a list of words, some that repeat
and some that don't, as output show the
number of distinct words as well as their
number of occurrences.
'''


from collections import Counter


n = int(input())

words = [input().strip() for _ in range(n)]

counts = Counter(words)

print(len(counts))
print(*counts.values())

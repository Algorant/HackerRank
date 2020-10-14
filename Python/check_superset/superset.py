'''
Check if a test set of integers is a strit superset of two other sets:
A and B.
'''

s, n, answer = [set(input().split()), int(input()), True]

for i in range(n):
    s1 = input().split()
    if not s.issuperset(s1):
        answer = False
        break

print(answer)

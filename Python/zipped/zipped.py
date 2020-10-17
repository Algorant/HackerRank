'''
Given grades for N students in X subjects, find the
average scores of each student.
'''

x, y = map(int, input().split())

scores = [map(float, input().split()) for _ in range(y)]

[print(sum(student) / y) for student in zip(*scores)]

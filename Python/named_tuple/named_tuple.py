'''
Given an input of:
-number of students
-an array with various columns including "marks" and student names:

Find the average of the marks column.
'''

from collections import namedtuple

n, Student = int(input()), namedtuple('Student', input())
print("{:2f}".format(sum([int(Student(*input().split()).MARKS) for _ in range(n)]) / n))

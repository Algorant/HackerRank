# This challenge takes n students and makes
# a dictionary of their names plus scores for grades
# and asks for the average of those grades for given
# name of student, to 2 decimal places.

if __name__ == '__main__':
    n = int(input())
    student_marks = {}
    for _ in range(n):
        name, *line = input().split()
        scores = list(map(float, line))
        student_marks[name] = scores
    query_name = input()

# structure query to return the scores and divide by 3
def avg(query_name):
    return (sum(student_marks[query_name]) / 3)

# Return average to 2 decimal places
print("%.2f" % (avg(query_name)))

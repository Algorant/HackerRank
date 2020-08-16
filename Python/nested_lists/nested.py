# Take inputs to create name, grade dictionary and return name of person
# with second lowest grade. If multiple people, return them separated on
# one line each.

if __name__ == '__main__':
    # empty dict
    grades = []
    # take inputs
    for _ in range(int(input())):
        name = input()
        score = float(input())
        # create grades, names dict
        grades.append([score, name])

    # sort by lowest score first
    grades.sort()

    # filter out first entry
    grade_filter = [i for i in grades if i[0] != grades[0][0]]

    # trim down to only this score and include duplicates
    answer = [j for j in grade_filter if j[0] == grade_filter[0][0]]

    # order alphabetically using lambda

    answer.sort(key=lambda x: x[1])

    # print on separate lines if multiple names

    for i in range(len(answer)):
        print(answer[i][1])

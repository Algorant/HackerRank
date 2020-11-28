'''
Output N names on separate lines in the format described in
ascending order of age.
'''


# Most of this code is given

import operator

def person_lister(f):
    def inner(people):
        return [f(i) for i in sorted(people, key=lambda x:int(x[2]))]

    return inner

@person_lister
def name_format(person):
    return ("Mr. " if person[3] == "M" else "Ms. ") + person[0] + " " + person[1]

if __name__ == '__main__':
    people = [input().split() for i in range(int(input()))]
    print(*name_format(people), sep='\n')

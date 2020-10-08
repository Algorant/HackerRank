'''
Take a string S and find occurences of character c in it.
Return as output number of occurences for each character c
as (#_occurences, c) for each value.
'''


from itertools import groupby

S = str(input())

values = []

for k, g in groupby(S):
    print("({}, {})".format(len(list(g)), k), end=" ")

'''
Sort a string S according to predetermined rules:

lowercase > uppercase > odd digits > even digits
'''

S = str(input())

print(*sorted(S, key=lambda c:
                    (c.isdigit() - c.islower(), c in '02468', c)), sep='')

'''
Given three integers a b and m, return the result of pow(a,b) and the
result of pow(a,b,m) on separate lines.
'''


a, b, m = [int(input()) for _ in '123']

print(pow(a,b), pow(a,b,m), sep='\n')

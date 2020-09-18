'''
Given two integers, try to print a / b. Use try/except to catch errors.
'''

for i in range(int(input())):

    try:
        a,b = map(int,input().split())
        print(a//b)

    except Exception as e:
        print("Error Code:", e)

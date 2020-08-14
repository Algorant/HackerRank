# Take in input n

n = int(input())


# Simple factorial function

def factorial(n):
    start = 1
    if int(n) >= 1:
        for i in range(1, (n+1)):
            start = start * i
    return start

# Prints answer
print(factorial(n))

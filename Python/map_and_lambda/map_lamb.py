'''
Given integer input N:

Make a lambda function to calculate fibbonacci and then use map()
to find the cube of all of the values from 0-N.
'''


# some of this code is pre-given

cube = lambda x: x**3

def fibbonacci(n):
    result = [0,1]
    [result.append(result[i-2] + result[i-1]) for i in range(2,n)]
    return result[0:n]

if __name__ == '__main__':
    n = int(input())
    print(list(map(cube, fibonacci(n))))

# This will take a number, and return a list of integers squared
# up until that number.

if __name__ == '__main__':
    n = int(input())

    def squares(n):
        for i in range(0,n):
            print(i**2)

    squares(n)

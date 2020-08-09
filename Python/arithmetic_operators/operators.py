# This function takes two inputs, and returns
# addition, subtraction, and multiplication on
# them, in that order.

if __name__ == '__main__':
    a = int(input())
    b = int(input())

    def arith(a,b):
        print(a + b),
        print(a - b),
        print(a * b)

    arith(a,b)

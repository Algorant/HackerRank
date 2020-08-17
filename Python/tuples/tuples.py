# For given integer n, and n-space separated integers,
# create a tuple and then hash that tuple.

if __name__ == '__main__':
    # inputs
    n = int(input())
    integer_list = map(int, input().split())
    #create tuple
    tup = tuple(integer_list)

# hash the tuple (tuple is a builtin function)
print(hash(tup))

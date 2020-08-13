

if __name__ == '__main__':
    """Accepts n integer input and arr as array"""
    n = int(input())

    arr = list(map(int, input().rstrip().split()))

# Unpacks the array, reversed, and prints the numbers
print(*reversed(arr))

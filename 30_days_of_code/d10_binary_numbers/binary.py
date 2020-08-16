# Given an integer in base 10, convert it to binary,
# then print the number of consecutive 1's.

# Take an input
n = int(input())

def bin_count(n):
    # convert to binary
    binary = bin(n).replace("0b","")
    for num in binary:
        # iterate and return max number of 1s that occur using 0 as separator
        return len(max(binary.replace('0',' ').split(), key=len))

print(bin_count(n))

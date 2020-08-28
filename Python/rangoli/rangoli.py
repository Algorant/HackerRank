import string

# the lowercase alphabet in a string
alphabet = string.ascii_lowercase



def print_rangoli(size):
    # this prints first half
    for i in range(size -1, 0, -1):
        row = ["-"] * (size * 2 -1) # prints the dashes
        for j in range(0, size - i):
            row[size - 1 - j] = alphabet[j + i]
            row[size - 1 + j] = alphabet[j + i]
        print("-".join(row))
    # this prints second half
    for i in range(0, size):
        row = ["-"] * (size * 2 -1)
        for j in range(0, size - i):
            row[size - 1 - j] = alphabet[j + i]
            row[size - 1 + j] = alphabet[j + i]
        print("-".join(row))

print_rangoli(7)

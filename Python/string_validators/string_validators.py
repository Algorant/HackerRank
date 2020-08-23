# You are given a string . Your task is to find out if the string contains:
# alphanumeric characters, alphabetical characters, digits, lowercase
# and uppercase characters.

if __name__ == '__main__':
    s = input()

# any() checks for anything true, will iterate through all tests


# Check for alphanumerics
print(any(c.isalnum() for c in s))

# Check for alphabet characters
print(any(c.isalpha() for c in s))

# Check for digits
print(any(c.isdigit() for c in s))

# Check for lowercase
print(any(c.islower() for c in s))

# Check for uppercase
print(any(c.isupper() for c in s))

# Given input of first name and last name, return the statement
# with the persons name in it.

def print_full_name(a, b):
    print("Hello {} {}! You just delved into python.".format(a, b))

if __name__ == '__main__':
    first_name = input()
    last_name = input()
    print_full_name(first_name, last_name)

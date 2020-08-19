# Given a string, split using a " " and join using a -

def split_and_join(line):
    a = line.split(" ") # converted to list with spaces
    b = "-".join(a) # join by hyphen "-"
    return b

if __name__ == '__main__':
    line = input()
    result = split_and_join(line)
    print(result)

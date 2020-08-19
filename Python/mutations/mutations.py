# Given a string, an integer, and a character:
# return the string with the character replaced at position of integer

def mutate_string(string, position, character):
    return string[:(position)] + character + string[(position + 1):]

if __name__ == '__main__':
    s = input()
    i, c = input().split()
    s_new = mutate_string(s, int(i), c)
    print(s_new)

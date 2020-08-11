# This challenge asks to split an input string
# by its even and odd characters, separated
# by a space on the same line.


# take an input
# word = int(input())



def eo_split(word):
    # Separate each character
    split_word = list(word)
    # Begin with empty even and odd lists
    evens = []
    odds = []
    # split them and reconstitute
    for item, char in enumerate(split_word):
        if item % 2 == 0:
            evens.append(char)
        else:
            odds.append(char)
    print(''.join(evens), ''.join(odds))


if __name__ == '__main__':
    n = int(input()) # number of strings
    for i in range(n): # iterate for each input
        eo_split(input())

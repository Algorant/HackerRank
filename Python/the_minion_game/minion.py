'''
The Minion Game:

Given a string S, 2 players (Stuard and Kevin in example) attempt
to find most substrings in S. Each substring is worth 1 point for
each time it appears in S. One player can only begin substrings
with vowels, the other with consonants.
'''

S = str(input())

def game(string):
    vowel = ["A", "E", "I", "O", "U"] # define vowels
    S = 0 # stuart starts at 0
    K = 0 # kevin starts at 0

    # logic for determining points
    for i in range(len(string)):
        if string[i] in vowel:
            K+= len(string) -i

        else:
            S+=len(string) -i

    # logic for determining winner
    if S > K:
        print("Stuart"+" "+ "%d" % S)

    elif K > S:
        print("Kevin"+" "+ "%d" % K)
    else:
        print("Draw")

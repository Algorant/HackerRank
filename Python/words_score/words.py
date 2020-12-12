'''
Fix the given code so that it gives the correct scoring for words:
Words with an even number of vowels get 2 points, odd number get 1 point.
Vowels are: a, e, i, o, u, and y
'''

# Given code below

# in line 25, previously there was an error that showed "++score", not correct
# syntax for python, changed to "score += 1"

def is_vowel(letter):
    return letter in ['a', 'e', 'i', 'o', 'u', 'y']

def score_words(words):
    score = 0
    for word in words:
        num_vowels = 0
        for letter in word:
            if is_vowel(letter):
                num_vowels += 1
        if num_vowels % 2 == 0:
            score += 2
        else:
            score += 1
    return score


n = int(input())
words = input().split()
print(score_words(words))
